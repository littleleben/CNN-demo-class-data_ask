# -*- coding: utf-8 -*-
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def my_function():
    news = open('E:\\text-cnn-master\\data\\tx1.txt', 'r')
    model = Word2Vec(LineSentence(news), sg=1,size=100, window=10, min_count=2, workers=10)
    model.save('E:\\text-cnn-master\\data\\D100.txt')

if __name__ == '__main__':
    my_function()
