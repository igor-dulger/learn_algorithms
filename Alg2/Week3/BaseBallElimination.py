from graph.weighted.flow.ford_fulkerson import FordFulkerson
from graph.weighted.flow.basic import FlowNetwork
from graph.weighted.flow.basic import FlowEdge
import math
from helpers.basic import timer


class BaseballElimination(object):
    class Team(object):
        def __init__(self, name, w, l, r):
            self.__name = name
            self.__wins = int(w)
            self.__losses = int(l)
            self.__remains = int(r)
            self.__remaining = []

        def name(self):
            return self.__name

        def wins(self):
            return self.__wins

        def losses(self):
            return self.__losses

        def remaining(self):
            return self.__remains

        def set_remaining(self, games):
            for to_play in games:
                self.__remaining.append(int(to_play))

        def get_remaining(self, team_id):
            return self.__remaining[team_id]

        def __str__(self):
            return self.__repr__()

        def __repr__(self):
            return "{} \t w:{} l:{} r:{} with {}".format(
                self.__name,
                self.__wins,
                self.__losses,
                self.remaining(),
                " ".join([str(i)+":"+str(v) for i, v in enumerate(self.__remaining)])
            )

    @timer
    def __init__(self, path):
        self.__teams = []
        self.__team_names = {}

        self.__load_from_file(open(path, "r"))
        self.__max_wins = self.__max_wins_team()

        self.__eliminated = [False] * len(self.__teams)
        self.__certificate = [None] * len(self.__teams)

        for team in self.__teams:
            self.__eliminated[self.__team_names[team.name()]] = self.__check_elimination(team.name())

    def __max_wins_team(self):
        result = self.__teams[0]
        max_wins = self.__teams[0].wins()
        for team in self.__teams:
            if max_wins < team.wins():
                result = team
                max_wins = team.wins()
        return result

    def __load_from_file(self, file):
        for line in [i.strip().split() for i in file]:
            if len(line) > 1:
                team = self.Team(line[0], line[1], line[2], line[3])
                team.set_remaining(line[4:])
                self.__teams.append(team)
                self.__team_names[line[0]] = len(self.__teams) - 1
                # print(team)
        file.close()

    def __check_elimination(self, name):
        to_check = self.__teams[self.__team_names[name]]
        if to_check.wins() + to_check.remaining() < self.__max_wins.wins():
            self.__certificate[self.__team_names[name]] = [self.__max_wins.name()]
            return True

        to_check_max = to_check.wins() + to_check.remaining()
        teams = len(self.teams())
        fn = FlowNetwork(teams + teams*teams + 2)
        s = fn.v() - 2
        t = fn.v() - 1

        for i, team in enumerate(self.__teams):
            if team.name() != name:
                fn.add_edge(FlowEdge(i, t, to_check_max - team.wins()))
                for g in range(i+1, teams):
                    game_index = len(self.__teams) + i*len(self.__teams) + g
                    remain = team.get_remaining(g)
                    if g != self.__team_names[name] and remain:
                        fn.add_edge(FlowEdge(game_index, i, math.inf))
                        fn.add_edge(FlowEdge(game_index, g, math.inf))
                        fn.add_edge(FlowEdge(s, game_index, remain))
        # print(repr(self))

        ff = FordFulkerson(fn, s, t)
        # print(repr(fn))
        # print(repr(ff))

        for edge in fn.adj(s):
            if edge.flow() != edge.capacity():
                self.__certificate[self.__team_names[name]] = self.__get__certificate(ff)
                return True

        return False

    def __get__certificate(self, network):
        result = []
        for i in range(len(self.__teams)):
            if network.in_cut(i):
                result.append(self.__teams[i].name())
        return result

    def number_of_teams(self):
        return len(self.__teams)

    def teams(self):
        return [x.name() for x in self.__teams]

    def wins(self, team):
            return self.__teams[self.__team_names[team]].wins()

    def losses(self, team):
        return self.__teams[self.__team_names[team]].losses()

    def remaining(self, team):
        return self.__teams[self.__team_names[team]].remaining()

    def against(self, team1, team2):
        return self.__teams[self.__team_names[team1]].get_remaining_with(team2)

    def is_eliminated(self, team):
        return self.__eliminated[self.__team_names[team]]

    def certificate_of_elimination(self, team):
        return self.__certificate[self.__team_names[team]]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Teams: {}\nNames:{}\nEliminated:{}\nCertificate:{}\nMaxWins{}\n".format(
            self.__teams,
            self.__team_names,
            self.__certificate,
            self.__eliminated,
            self.__max_wins
        )


def main():
    division = BaseballElimination("../../data/baseball/teams42.txt")
    for team in division.teams():
        if division.is_eliminated(team):
            print("{} is eliminated by the subset R = {}".format(team, [x for x in division.certificate_of_elimination(team)]))
        else:
            print(team + " is not eliminated")


if __name__ == "__main__":
    main()
