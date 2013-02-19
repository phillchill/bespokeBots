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
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
import pprint


class NGrams(object):
    """N-gram model that reads in corpus file and calculates ngrams for 
    varying n"""
    def __init__(self,n):
        super(NGrams, self).__init__()
        self.n = n
        self.ngrams = dict()
        print "... initialised NGrams Model with N = ", n
    
    def read_text(self, path = "prompt"):
        """read in corpus (.txt) from specified path"""
        if path == "prompt":
            path = raw_input("please input path to .txt corpus")
        elif ".txt" in path:
            # read txt file
            print "... now reading: ", path
            try:
                self.text = open(path)
            except:
                print "please specify correct path to .txt file"
        else:
            exit("please specify path to .txt file")
        pass
    
    def load_corpus(self):
        """load in a corpus from the NLTK gutenberg collection"""
        print gutenberg.fileids()
        textName = raw_input("Please input filename of text to load \n\
        (choose from the above)\n>>> ")
        self.corpus = gutenberg.words(textName)
    
    def get_ngrams(self):
        """return ngrams"""
        return self.ngrams
        
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
    
    def calc_grams(self):
        """calculate Ngram counts for N is n"""
        # for now, supose self.text
        if self.text:
            for line in self.text:
                tokens = wordpunct_tokenize(line)
                for i in range(len(tokens) - self.n + 1):
                    gram = tuple(tokens[i:i+self.n])
                    if gram in self.ngrams:
                        self.ngrams[gram] += 1
                    else:
                        self.ngrams[gram] = 1
            print "... added ", len(self.ngrams), "grams to model"
        else:
            print "No text found. Please read in text first."
            return False
    



def main():
    # nGramModel.load_corpus()
	oneGrams = NGrams(2)
	oneGrams.read_text("../data/corpora/testcorpus.txt")
	oneGrams.calc_grams()
	ngrams = oneGrams.get_ngrams()
	print "asdf"
	for k in ngrams:
	    if ngrams[k] > 10:
	        print k, ngrams[k]
    # oneGrams.calc_freq_dist()
    # oneGrams.print_freq_dist_info()


if __name__ == '__main__':
	main()

