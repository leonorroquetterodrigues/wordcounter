# -*- coding: UTF-8 -*-
# Copyright (C) 2018 Jean Bizot <jean@styckr.io>
""" Main lib for wordcounter Project
"""
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('nps_chat')
nltk.download('universal_tagset')
nltk.download('averaged_perceptron_tagger')
#from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import WordNetLemmatizer
#nltk.download('nps_chat')
from nltk.corpus import nps_chat
#nltk.download('wordnet')
# Lemmatize with POS Tag
from nltk.corpus import wordnet
import pandas as pd

def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


def part_of_speech(sentence):
    chat_tagged = nps_chat.tagged_words(tagset="universal")
    tuple_list = chat_tagged
    word = []
    category = []
    for a_tuple in tuple_list:
        word.append(a_tuple[0])
    for a_tuple in tuple_list:
        category.append(a_tuple[1])
    df = pd.DataFrame(zip(word,category),columns=['word', 'category'])
    df_unique = df.drop_duplicates(subset=['word'])# subset=['word'] -> if we want to get the first  category for each word
    lemmatizer = WordNetLemmatizer()
    aux = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in nltk.word_tokenize(sentence.lower())]
    aux_1 = pd.DataFrame(aux,columns=['word'])
    aux_2 = pd.DataFrame(aux_1.word.value_counts().index,columns=['word'])
    return pd.merge(df_unique, aux_2, on=['word'],how='inner', validate='1:1')


if __name__ == '__main__':
   print('this are my functions get_wordnet_pos and part_of_speech')


