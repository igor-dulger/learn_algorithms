from graph.digraph import Digraph
from graph.cyclic import Cyclic
from Alg2Week1.sap import Sap
from helpers.helpers import timer


class WordNet(object):
    #    // constructor takes the name of the two input files
    @timer
    def __init__(self,  synsets, hypernyms):
        if synsets is None or hypernyms is None:
            raise ValueError("Argument can't be None")

        # self.__synsets = []
        self.__nouns = {}
        self.__root = None

        fd = open(synsets, "r")
        count = 0
        for line in [i.strip().split(sep=",") for i in fd]:
            if line:
                nouns = line[1].split()
                # self.__synsets.append({
                #     "nouns": nouns,
                #     "desc": line[2]
                # })
                count += 1
                for noun in nouns:
                    if noun in self.__nouns:
                        self.__nouns[noun].append(int(line[0]))
                    else:
                        self.__nouns[noun] = [int(line[0])]
        fd.close()

        self.__rdag = Digraph(count)

        fd = open(hypernyms, "r")
        for line in [i.strip().split(sep=",") for i in fd]:
            if line:
                for w in line[1:]:
                    self.__rdag.add_edge(int(line[0]), int(w))
        fd.close()

        if not self.__check_root():
            raise ValueError("Input digraph isn't rooted")

        cyclic = Cyclic(self.__rdag)
        if cyclic.is_cyclic():
            raise ValueError("Input digraph isn't acyclic")

    def __check_root(self):
        result = 0
        for v in range(self.__rdag.v()):
            if self.__rdag.outdegree(v) == 0:
                self.__root = v
                result += 1
        if result == 1:
            return True
        return False

    #    // returns all WordNet nouns
    def nouns(self):
        for noun, synset in self.__nouns.items():
            yield noun

    #    // is the word a WordNet noun?
    def is_noun(self, word):
        if word is None:
            raise ValueError("Argument can't be None")
        return word in self.__nouns

    #    // distance between nounA and nounB (defined below)
    def distance(self, nounA, nounB):
        if nounA is None or nounB is None:
            raise ValueError("Argument can't be None")
        if not self.is_noun(nounA) or not self.is_noun(nounB):
            raise ValueError("Argument isn't WordNet noun")
        sap = Sap(self.__rdag)
        return sap.length(self.__nouns[nounA], self.__nouns[nounB])

    #    // a synset (second field of synsets.txt) that is the common ancestor of nounA and nounB
    #    // in a shortest ancestral path (defined below)
    def sap(self, nounA, nounB):
        if nounA is None or nounB is None:
            raise ValueError("Argument can't be None")
        if not self.is_noun(nounA) or not self.is_noun(nounB):
            raise ValueError("Argument isn't WordNet noun")
        sap = Sap(self.__rdag)
        return sap.ancestor(self.__nouns[nounA], self.__nouns[nounB])

    def __repr__(self):
        return "Root: {}\nNouns: {}".format(self.__root, self.__nouns)


def main():

    list = [
            # ["synsets3.txt", "hypernyms3InvalidCycle.txt"],
            # ["synsets3.txt", "hypernyms3InvalidTwoRoots.txt"],
            # ["synsets6.txt", "hypernyms6InvalidCycle+Path.txt"],
            # ["synsets6.txt", "hypernyms6InvalidCycle.txt"],
            # ["synsets6.txt", "hypernyms6InvalidTwoRoots.txt"],
            ["synsets6.txt", "hypernyms6TwoAncestors.txt"],
            # ["synsets8.txt", "hypernyms8ManyAncestors.txt"],
            # ["synsets8.txt", "hypernyms8WrongBFS.txt"],
            # ["synsets11.txt", "hypernyms11AmbiguousAncestor.txt"],
            # ["synsets11.txt", "hypernyms11ManyPathsOneAncestor.txt"],
            # ["synsets15.txt", "hypernyms15Tree.txt"],
            # ["synsets100-subgraph.txt", "hypernyms100-subgraph.txt"]
    ]

    for file in list:
        try:
            wn = WordNet("../data/word_net/" + file[0], "../data/word_net/" + file[1])
        except ValueError as e:
            print(file, e)

    print(repr(wn))
    print(wn.sap("c", "f"), wn.distance("c", "f"))


if __name__ == "__main__":
    main()
