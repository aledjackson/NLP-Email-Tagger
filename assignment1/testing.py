import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import brown
from nltk.corpus.reader import WordListCorpusReader
from nltk.stem.porter import *
from nltk.stem import WordNetLemmatizer
import re
from os import listdir
from os.path import isfile, join

tagged_data_filepath = "/Users/aledjackson/Documents/University/Second Year/Modules/Natural Language Processing/Assignments/assignment1/seminar_testdata/test_tagged"
untagged_data_filepath = "/Users/aledjackson/Documents/University/Second Year/Modules/Natural Language Processing/Assignments/assignment1/seminar_testdata/test_untagged"
general_data_filepath = "/Users/aledjackson/Documents/University/Second Year/Modules/Natural Language Processing/Assignments/assignment1/Data"

l_names = WordListCorpusReader(general_data_filepath, ["names.family"]).words()

file_names = [f for f in listdir(tagged_data_filepath) if isfile(join(tagged_data_filepath, f))]
file_names = file_names[1:]

print("running on file: " + file_names[0])

reader = WordListCorpusReader(tagged_data_filepath, [file_names[0]])

corpus = reader.raw()
words = reader.words()

# gets a set of all the tags in a corpus
def get_all_tags(corpus):
    return set(re.findall(r"<([^<>/]+)>",corpus)[1:])

# joins a list of strings together
def join_string_list(l):
    output = ""
    for string in l:
        output = output + string
    return output

# returns the contents of all tags with a the argument name
def get_tag_contents(corpus, name):
    return re.findall(r"<" + name + r">(.+)</" + name  + r">", corpus)

# removes all the tags within a corpus
def remove_tags(corpus):
    return re.sub(r"<[^<>]*>","",corpus)

class Test_Individual:
    def __init__(self,output_corpus,validation_corpus):
        self.output_corpus = output_corpus
        self.validation_corpus = validation_corpus
        self.fp = 0
        self.tp = 0
        self.fn = 0

    # tests one corpus against another
    def test_whole(self):

        validation_tags = get_all_tags(self.validation_corpus)
        output_tags = get_all_tags(self.output_corpus)

        for v_tag in validation_tags:
            self.test_tag(v_tag)

        print("tp " + str(self.tp))
        print("fp " + str(self.fp))
        print("fn " + str(self.fn))

    # tests if a tag was identified correctly each time by the text
    # returns a dictionary of {tp:Int,fp:Int,fn:Int}
    def test_tag(self,tag):
        print(tag)

        # gets all the text marked by the tag
        v_corpora_tagged = get_tag_contents(self.validation_corpus, tag)
        o_corpora_tagged = get_tag_contents(self.output_corpus, tag)

        o_corpora = []
        v_corpora = []
        # removes all the inner tags
        for inner in v_corpora_tagged:
            v_corpora.append(remove_tags(inner))

        for inner in o_corpora_tagged:
            o_corpora.append(remove_tags(inner))

        if(len(v_corpora) - len(o_corpora)) > 0:
            self.fp += len(v_corpora) - len(o_corpora)

        # print(v_corpora)
        # print(o_corpora)


        for v_corpus in v_corpora:
            found = False
            for i, o_corpus in enumerate(o_corpora):
                if v_corpus == o_corpus:
                    # print("found :" + o_corpus)
                    found = True
                    self.tp += 1
                    # print(o_corpora)
                    del o_corpora[i]
                    # print(o_corpora)
                    break
            if not found:
                self.fn += 1
                print("didn't find " + v_corpus)

        self.fp += len(o_corpora)
        print("incorrectly labeled: " + str(o_corpora))



t = Test_Individual(corpus + "<location>find me</location>",corpus )
t.test_whole()

