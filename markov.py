from sys import argv
import random

def make_list(filename):
    """Opens a file, strips end-of-line whitespace, and splits into a list on spaces."""
    #open the file as a string and strip whitespace off the end.
    corpus_file = open(filename).read().rstrip()
    #remove end-of-line characters
    clean_corpus = corpus_file.replace("\n", " ")
    
    #create a list
    corpus_list = clean_corpus.split(" ")

    return corpus_list



def make_chains(corpus_list):
    """Takes input text as a list; returns dictionary of markov chains."""
    
    corpus_dict = {}

    #define the end case (2nd to last, last)
    last_key = (corpus_list[-2], corpus_list[-1])
    corpus_dict[last_key] = [corpus_list[0]]

    #define the wraparound case (end to beginning)
    last_first_key = (corpus_list[-1], corpus_list[0])
    corpus_dict[last_first_key] = [corpus_list[1]]

    for i in range(len(corpus_list)-2):
        key = (corpus_list[i], corpus_list[i+1])
        if key not in corpus_dict:
            corpus_dict[key] = [corpus_list[i+2]]
        else:
            corpus_dict[key].append(corpus_list[i+2])
    
    #to print a test dictionary, uncomment the two lines bellow        
    # for key, value in corpus_dict.items():
    #     print key, value   

    return corpus_dict


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    output_text = ""
    random_key = random.choice(chains.keys())

    #populate the first tuple and make sure it's not empty
    random_word = random.choice(chains[random_key])
    key_word_tuple = (random_key[0], random_key[1], random_word)
    output_text = "%s %s %s" %( key_word_tuple[0].title(), key_word_tuple[1], key_word_tuple[2])

    #until the tuple is empty, keep re-populating the three-word tuple
    while len(output_text) < 140:
        new_key = (key_word_tuple[1], key_word_tuple[2])
        random_word = random.choice(chains[new_key])
        key_word_tuple = (new_key[0], new_key[1], random_word)
        output_text = "%s %s" %(output_text, random_word)



    return output_text

def end_at_punct(markov_text):
    output_text = markov_text

    output_text = output_text.rstrip('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,')
    print
    return output_text

input_list_one = make_list("test.txt")
input_list_two = make_list("green-eggs.txt")
combined_list = []

combined_list.extend(input_list_two)
combined_list.extend(input_list_one)

combined_dict = make_chains(combined_list)
print combined_dict

final_string = make_text(combined_dict)

print end_at_punct(final_string)
