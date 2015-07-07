import sys
import random

def make_chains(corpus):
    """Takes input text as string; returns dictionary of markov chains."""
    
    #clean  up the text
    corpus_file = open(corpus).read().rstrip()
    clean_corpus = corpus_file.replace("\n", " ")
    
    #create dictionary keys
    corpus_list = clean_corpus.split(" ")
    corpus_dict = {}
    tuple_list = []

    for i in range(len(corpus_list)-1):
        key = (corpus_list[i], corpus_list[i+1])
        tuple_list.append(key)
        corpus_dict[key] = [] 
    
    #append values into dictionary keys
    for x in range(len(corpus_list) -1):
        list_tuple = (corpus_list[x], corpus_list[x+1])
        for tup in corpus_dict.keys():
            if tup == list_tuple and x <= (len(corpus_list)-3):
                corpus_dict[tup].append(corpus_list[x+2])

    #to print a test dictionary, uncomment the two lines bellow        
    #for key, value in corpus_dict.items():
    #   print key, value   

    return corpus_dict


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    output_text = ""
    random_key = random.choice(chains.keys())
    random_word = random.choice(chains[random_key])
    key_string = "%s %s" %(random_key[0], random_key[1])
    print key_string
    output_text += "%s %s" %(key_string, random_word)
    print output_text

    # while chains[random_key] != []:
    #     #string_key = random_key[0] + " " + random_key[1] + random_word

    #     random_key = random.choice(chains.keys())
    #     random_word = random.choice(chains[random_key])
    # print random_key, random_word
    # return "Here's some random text."


magic_dict_super_de_duper = make_chains("green-eggs.txt")
make_text(magic_dict_super_de_duper)
# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = "Some text"

# Get a Markov chain
#chain_dict = make_chains(input_text)

# Produce random text
#random_text = make_text(chain_dict)

#print random_text

