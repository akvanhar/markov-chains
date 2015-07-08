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
    #tuple_list = []
    #next two lines adds the last two items to a list and creates an empty value
    last_key = (corpus_list[-2], corpus_list[-1])
    corpus_dict[last_key] = []

    for i in range(len(corpus_list)-2):
        key = (corpus_list[i], corpus_list[i+1])
        if key not in corpus_dict:# and corpus_list[i+1] in corpus_list:
            corpus_dict[key] = [corpus_list[i+2]]
        else:# corpus_list[i+1]:# and corpus_list[i+1] in corpus_list:
            corpus_dict[key].append(corpus_list[i+2])
    
    #append values into dictionary keys
    # for x in range(len(corpus_list) -2):
    #     list_tuple = (corpus_list[x], corpus_list[x+1])
    #     corpus_dict[list_tuple].append(corpus_list[x+2])
    
    #to print a test dictionary, uncomment the two lines bellow        
    # for key, value in corpus_dict.items():
    #      print key, value   

    return corpus_dict


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    output_text = ""
    random_key = random.choice(chains.keys())

    #populate the first tuple and make sure it's not empty
    if chains[random_key] != []:
        random_word = random.choice(chains[random_key])
        key_word_tuple = (random_key[0], random_key[1], random_word)
        output_text = "%s %s %s" %( key_word_tuple[0], key_word_tuple[1], key_word_tuple[2])
    else:
        output_text = "%s %s" %(random_key[0], random_key[1])
        return output_text

    #until the tuple is empty, keep re-populating the three-word tuple
    while True:
        new_key = (key_word_tuple[1], key_word_tuple[2])
        if chains[new_key] != []: #need to pick a better type of variable for "chains "
            random_word = random.choice(chains[new_key])
            key_word_tuple = (new_key[0], new_key[1], random_word)
            output_text = "%s %s" %(output_text, random_word)
        else:
            break

    return output_text

# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = "hello there world hello there joel hello there katie"

# Get a Markov chain
#chain_dict = make_chains(input_text)

# Produce random text
#random_text = make_text(chain_dict)

magic_dict_super_de_duper = make_chains("test.txt")
print make_text(magic_dict_super_de_duper)
