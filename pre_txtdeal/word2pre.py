# -*- coding: utf-8 -*-
from gensim.corpora import WikiCorpus
import jieba
from word2langconv import *
import os

def my_function():
    space = ' '
    i = 0
    l = []
    path_jib = "F:\\2000分类"
    files = os.listdir(path_jib)
    for file in files:  # 遍历文件夹
        f = os.path.basename(file)
        # name_s = f.replace('.txt', '')
        # print(name)
        paths = path_jib + '\\'+f
    # jb_name = 'C:\\Users\\雷神\\Desktop\\好问康训练\\hwkwk.txt'
    # f = open('C:\\Users\\雷神\\Desktop\\gensim\\reduce.txt', 'w',encoding='utf-8')
        with open(paths,'r',encoding='utf-8')as fs:
            text=fs.readlines()
            # print(text)
            for temp_sentence in text:
                temp_sentence = Converter('zh-hans').convert(temp_sentence)
                seg_list = list(jieba.cut(temp_sentence))
                for temp_term in seg_list:
                    l.append(temp_term)
                with open('F:\\2000分类\\raw_2000.txt', 'a',encoding='utf-8')as f:
                    f.write(space.join(l) + '\n')
                    l = []
                    i = i + 1
                if (i %1000 == 0):
                    print('Saved ' + str(i) + ' articles')
                    f.close()
        print(file +'have done')

if __name__ == '__main__':
    my_function()
