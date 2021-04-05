"""
Takes a group of CSVs in the directory 'path' and creates on csv out of them
TO DO.
1. Error warning if the files aren't there 
2. Pass it a file variable instead of hard coding it
3. RE to remove commas from the csv !!!
"""
import csv
import os
import sys
import re
import glob

import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.text import Text
from nltk import bigrams, trigrams
from nltk import FreqDist

from nltk import word_tokenize

#Path of the folder where all the files are stored.
#I added the folder munged so that you'd know which ones were altered
path = 'csvs/'
p = re.compile(r'<.*?>')

def getPos():
  # get all the files in the path
  #for filename in glob.glob(os.path.join(path, '*.csv')):
    filename = "csvs/test-bioshock.csv"
    f = open(filename, 'rt')
    reader = csv.reader(f)
    print(filename, reader)
    for row in reader:
      #remove all the html
      temp_string=' '.join(row)
      reged = p.sub('', temp_string)
      #use the nltk tokenize library to break up the text without the html into tokens
      text = word_tokenize(reged)
      #now turn the tokens into tagged parts of speech
      pos_tagged = nltk.pos_tag(text)
      #pos_tag returns an array of words with the part of speech tagged
      #take each word pos_tag and see what's inside
      for pos in pos_tagged:
          thisword = pos
          #look for any words tagged as adjectives or adverbs
          if thisword[1] == 'JJ' or thisword[1] == 'RB':
            nextword=pos_tagged[pos_tagged.index(pos)-len(pos_tagged)+1]
            if nextword[1] == 'NN':
              print(thisword[0], nextword[0])
    return 'done'
