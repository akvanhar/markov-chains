import sys
import random

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    
    #clean  up the text
    corpus_file = open(corpus).read()
    clean_corpus = corpus_file.replace("\n", " ")

    #create dictionary keys
    corpus_list = clean_corpus.split(" ")
    corpus_dict = {}
    for i in range(len(corpus_list)-1):
        key = (corpus_list[i], corpus_list[i+1])
        corpus_dict[key] = None   
        print key

    return {}


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = "Some text"

# Get a Markov chain
#chain_dict = make_chains(input_text)

# Produce random text
#random_text = make_text(chain_dict)

#print random_text


make_chains("green-eggs.txt")