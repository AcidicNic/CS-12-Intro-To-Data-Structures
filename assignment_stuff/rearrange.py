from sys import argv
from random import randrange


def rearrange(words_list):
    # this list is the same length as words_list, but full of None objects.
    rearranged = [None] * len(words_list)
    for word in words_list:
        # find a random empty space in our
        rand_index = randrange(len(rearranged))
        while rearranged[rand_index] is not None:
            rand_index = randrange(len(rearranged))
        rearranged[rand_index] = word
    return " ".join(rearranged)


def reverse_sentences(sentence):
    """ Stretch Challenge: reverses the words in a sentence"""
    sentence.reverse()
    return " ".join(sentence)


def reverse_words(words):
    """ Stretch Challenge: reverses the characters in a string"""
    for i in range(len(words)):
        words[i] = words[i][::-1]
    return " ".join(words)


if __name__ == '__main__':
    if len(argv) > 1:
        print(rearrange(argv[1:]))
    else:
        pls = 'Please enter words for me to rearrange!'
        print(pls)
        print(rearrange(pls.split()))
