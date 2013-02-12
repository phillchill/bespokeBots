"""
ngrams.py
Class for NGram models of arbitrary N
(first test version, not yet calculating ngrams frequencies)

Created by Philo van Kemenade on 2013-02-06.
Copyright (c) 2013. All rights reserved.
"""

import sys
import os
import nltk
from nltk.corpus import gutenberg
from nltk import FreqDist

class NGrams(object):
    """N-gram model that reads in corpus file and calculates ngrams for 
    varying n"""
    def __init__(self):
        super(NGrams, self).__init__()
        print "... initiating NGrams()"
    
    def read_corpus(self, path):
        """read in corpus (.txt) from specified path"""
        pass
    
    def load_corpus(self):
        """load in a corpus from the NLTK gutenberg collection"""
        print gutenberg.fileids()
        textName = raw_input("Please input filename of text to load \n\
        (choose from the above)\n>>> ")
        self.corpus = gutenberg.words(textName)
        
    def calc_freq_dist(self):
        """calculate freq dist of words in corpus"""
        if self.corpus:
            self.fd = FreqDist()
            for word in self.corpus:
                self.fd.inc(word)
        else:
            print "No corpus found. Please load in corpus first."
            return False
    
    def print_freq_dist_info(self):
        """show some basic info from the freq dist"""
        print "Number of tokens: ", self.fd.N()
        print "Number of unique tokens: ", self.fd.B()
        topN = 10
        print "Top ", topN, " most frequent tokens:\n"
        for word in self.fd.keys()[:topN]:
            print word, self.fd[word]
    
    def calc_grams(self, n):
        """calculate Ngram counts for N is n"""
        pass
    



def main():
	nGramModel = NGrams()
	nGramModel.load_corpus()
	nGramModel.calc_freq_dist()
	nGramModel.print_freq_dist_info()


if __name__ == '__main__':
	main()

