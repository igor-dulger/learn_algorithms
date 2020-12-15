from Alg2Week1.word_net import WordNet
import sys
# from helpers.helpers import timer


class Outcast(object):
    def __init__(self, word_net):
        self.__word_net = word_net

    # @timer
    def outcast(self, nouns):
        result_sum = 0
        result_word = None
        for i in range(len(nouns)):
            sum = 0
            for j in range(len(nouns)):
                if i != j:
                    sum += self.__word_net.distance(nouns[i], nouns[j])
            if sum > result_sum:
                result_sum = sum
                result_word = nouns[i]
        return result_word

    def __str__(self):
        return str(self.__word_net)

    def __repr__(self):
        return "\nWord net: {}".format(self.__word_net)


def main():
    wordnet = WordNet(sys.argv[1], sys.argv[2])
    outcast = Outcast(wordnet)

    for t in range(3, len(sys.argv)):
        with open(sys.argv[t], 'r') as f:
            nouns = [word.strip() for word in f.readlines()]
        print("{}: {}".format(sys.argv[t], outcast.outcast(nouns)))


if __name__ == "__main__":
    main()
