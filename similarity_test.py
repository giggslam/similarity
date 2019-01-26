# -*- coding: utf-8 -*-
"""
test run for Similarity class, 2019-01-27
"""

from SimilarityClass import Similarity

def main():

    """ main function to create Similarity class instance and get use of it """

    sim = Similarity()

    print(sim.euclidean_distance([0,3,4,5],[7,6,3,-1]))
    print(sim.jaccard_similarity([0,1,2,5,6],[0,2,3,5,7,9]))
    print(sim.cosine_similarity([3, 45, 7, 2], [2, 54, 13, 15]))
    print(sim.manhattan_distance([10,20,10],[10,20,20]))
    print(sim.minkowski_distance([0,3,4,5],[7,6,3,-1],3))

if __name__ == "__main__":
    main()