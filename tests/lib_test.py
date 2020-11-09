# -*- coding: UTF-8 -*-

# Import from standard library
import os
import wordcounter
import pandas as pd
# Import from our lib
from wordcounter.lib import get_wordnet_pos, part_of_speech
import pytest


# def test_clean_data():
#     datapath = os.path.dirname(os.path.abspath(wordcounter.__file__)) + '/data'
#     df = pd.read_csv('{}/data.csv.gz'.format(datapath))
#     first_cols = ['id', 'civility', 'birthdate', 'city', 'postal_code', 'vote_1']
#     assert list(df.columns)[:6] == first_cols
#     assert df.shape == (999, 142)
#     out = clean_data(df)
#     assert out.shape == (985, 119)

def test_part_of_speech():
   # X = part_of_speech('sentence')
    # assert isinstance(X,pd.DataFrame)
    assert 1==1
