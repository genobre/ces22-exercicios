import sys
import string

def cleanword(word):
    l = list(word)
    t = ''
    for k in l:
        if str.isalpha(k):
            t = t + k
    return t

def has_dashdash(word):
    l = list(word)
    result = False
    for k in l:
        if k == '-':
            result = True
    return result

def extract_words(sentence):
    l = list(sentence)
    t = ''
    f = list([])
    for k in l:
        if k is not ' ' and k is not '-':
            if str.isalpha(k):
                t = t + k
        else:
            if t is not '':
                p = str.lower(t)
                f.append(p)
                t = ''
    if t is not '':
        p = str.lower(t)
        f.append(p)
    return f

def wordcount(word,word_list):
    count = 0
    for k in word_list:
        if k == word:
            count += 1
    return count

def wordset(word_list):
    f = list([])
    for k in word_list:
        it_is = False
        for p in f:
            if k == p:
                it_is = True
        if not it_is:
            f.append(k)
    return f

def longestword(word_list):
    max = 0
    for k in word_list:
        aux = len(k)
        if aux > max:
            max = aux
    return max
