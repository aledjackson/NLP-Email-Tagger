import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import brown
from nltk.corpus.reader import WordListCorpusReader
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
import re
from os import listdir
from os.path import isfile, join

wnl = WordNetLemmatizer()
stemmer = PorterStemmer()

tagged_data_filepath = "/Users/aledjackson/Documents/University/Second Year/Modules/Natural Language Processing/Assignments/assignment1/training"
untagged_data_filepath = "/Users/aledjackson/Documents/University/Second Year/Modules/Natural Language Processing/Assignments/assignment1/seminar_testdata/test_untagged"
general_data_filepath = "/Users/aledjackson/Documents/University/Second Year/Modules/Natural Language Processing/Assignments/assignment1/Data"

l_names = WordListCorpusReader(general_data_filepath, ["names.family"]).words()

file_names = [f for f in listdir(untagged_data_filepath) if isfile(join(untagged_data_filepath, f))]
file_names = file_names[1:]

reader = WordListCorpusReader(untagged_data_filepath, [file_names[0]])

corpus = reader.raw()
words = reader.words()

def get_tags_by_name(corpus, name):
    return re.findall(r"<" + name + r">.+</" + name  + r">", corpus)

def tokenise(corpus):
    return re.findall("([^\s<>]+)[\s\n<>]",corpus)

def get_name_of_poster(corpus):
    return re.findall()

def names_in_file(corpus):
    output = []
    for name in l_names:
        found_names = re.findall(name + r"\W", corpus)
        if (len(found_names) != 0):
            for found_name in found_names:
                output.append(found_name)
    return output

print('hello')
print(names_in_file(corpus))