from graph.weighted.basic import EdgeWeightedGraph
from graph.weighted.basic import EdgeWeightedDigraph
from graph.weighted.mst import PrimLazyMST
from graph.weighted.mst import KruskalMST
from dequeue.priority_queue import MinIndexPriorityQueue
from graph.weighted.sp import DijkstraSP
from graph.weighted.sp import DijkstraMonoSP
from graph.weighted.sp import BellmanFordSP
from graph.weighted.negative_circle import NegativeCircle
from graph.topological_order import TopologicalOrder
from graph.basic import Digraph
from graph.weighted.flow.basic import FlowNetwork
from graph.weighted.flow.ford_fulkerson import FordFulkerson
from sort.lsd import LSD
from sort.msd import MSD
from sort.three_way_quick_sort import ThreeWayQuickSort
from tree.tries.tst import TST
from strings.kmp import KMP

from binary.bitreader import BitReader
from binary.bitwriter import BitWriter
import sys
import os


def main():
    w = BitWriter(sys.stdout.buffer)
    # r = BitReader(sys.stdin.buffer)
    # while True:
    #     c = r.read_char()
    #     if r.is_empty():
    #         break
    #     w.write_char(c, 7)
    #

    for i in range(100):
        w.write_bits(255, 8)
    w.flush()
    sys.stdout.close()


    # with open('test.dat', 'wb') as outfile:
    #     with BitWriter(outfile) as w:
    #         w.write_bits(8, 5)
    #         w.write_bits(11, 4)
    #         w.write_bits(2019, 12)
    #
    # with open('test.dat', 'rb') as infile:
    #     with BitReader(infile) as r:
    #         day = r.read_bits(5)
    #         month = r.read_bits(4)
    #         year = r.read_bits(12)
    #         print(day, month, year)

    # data = ['wsd', 'abc', 'aav', 'bda', 'cadd', 'ba']
    # print(data)
    # MSD.sort(data)
    # print(data)


    # data = ['wsd', 'abc', 'aav', 'bda', 'cadd', 'ba']
    # print(data)
    # ThreeWayQuickSort.sort(data)
    # print(data)


    # fn = FlowNetwork(open("../data/tinyFlow.txt", "r"))
    # # print(repr(fn))
    #
    # ff = FordFulkerson(fn, 0, 7)
    # print(ff.flow())

    # dsp = DijkstraMonoSP(ewg, 0)
    # for v in range(ewg.v()):
    #     print("Has path to {}: {} dist: {} path: {}".format(v, dsp.has_path_to(v), dsp.dist_to(v), ", ".join([str(e) for e in dsp.path_to(v)])))
    #
    # dsp = BellmanFordSP(ewg, 0)
    # for v in range(ewg.v()):
    #     print("Has path to {}: {} dist: {} path: {}".format(v, dsp.has_path_to(v), dsp.dist_to(v), ", ".join([str(e) for e in dsp.path_to(v)])))





if __name__ == "__main__":
    main()
