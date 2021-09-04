# -*- coding: utf-8 -*-
import codecs
import numpy
import gensim
import numpy as np
import os
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import random
import re








def url_open(url_random):
    url_random_new='https://'+url_random
    # print(url_random_new)
    headers = {

        'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',

    }
    request = urllib.request.Request(url=url_random_new, headers=headers)
    response_stop = urllib.request.urlopen(request)
    content = response_stop.read().decode('gbk')
    soup = BeautifulSoup(content, 'lxml')
    # title_url = soup.findAll('div', class_="pb20 article_detail")
    title_url = soup.findAll('p', class_="dis-obj")

    for i in title_url:
        i_txt=i.get_text()
        # print(i_txt)
        compare_list.append(i_txt)
    # compare_list_str=str(compare_list)
    # return compare_list_str
    # print(title_url.get_text())



def hdf_urlsearch(jbms):
    query_jbms = urllib.parse.quote(jbms)
    # print(query_jbms)
    url_jb = 'https://so.haodf.com/index/search?kw=' + query_jbms

    headers = {

        'User-Agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',

    }
    request = urllib.request.Request(url=url_jb, headers=headers)
    response_stop = urllib.request.urlopen(request)
    content = response_stop.read().decode()
    soup=BeautifulSoup(content,'lxml')
    title_url=soup.findAll('a',class_="a-title sc-i-title-a")
    re_url=re.compile(' href="//(.*?)"',re.S)
    title_url_re=re_url.findall(str(title_url))
    # random_url=random.sample(title_url_re,1)####随机选择两个网址
    for i in title_url_re:
        # print(i)
        url_open(i)
        print(i)

    # print(soup)



def list_deal(list_str):
    remove_1_i_txt=list_str.replace(' ','')###去掉所有的空格
    # print(remove_blank_i_txt)
    remove_2_i_txt = str(remove_1_i_txt).replace('\n', '')  ###去掉所有的空格
    remove_3_i_txt = str(remove_2_i_txt).replace('\xa0', '')
    return remove_3_i_txt

path_needsearch='F:\\2000分类\\SELECT.txt'
path_writesearch='F:\\2000分类\\search_HDF.txt'

fw=open(path_writesearch,'a',encoding='utf-8')

with open(path_needsearch,'r',encoding='utf-8')as f:
    needcontent=f.read()
    path_needsearch=eval(needcontent)
# print(type(path_needsearch))

if __name__ == '__main__':
    ALL=[]
    compare={}


    # jbms=input('请输入要查找的疾病名称：')###自行输入的时候
    # JBMS=jbms.split(' ')

    JBMS=path_needsearch####导入列表的时候
    for jb in JBMS:
        compare_list = []

        # print('               ')
        hdf_urlsearch(jb)
        compare_list_str = str(compare_list)
        print(compare_list_str)
        label_content=jb+'    '+compare_list_str
        if compare_list_str =='[]':
            continue
        else:
            fw.write(label_content+'\n')
            # ALL.append(compare_list_str)
            print(label_content)









path_jib = "E:\\疾病gather\\万方加百度筛选后的疾病"
files= os.listdir(path_jib)
















if __name__ == '__main__':
    model = gensim.models.Word2Vec.load('E:\\gensim\\data\\word医文词向量\\jb_use_300.word2vec')
    compare={}
    p1_keywords = './data/P11_keywords.txt'
    p2_keywords = './data/P12_keywords.txt'
    p1_keywords_new = './data/P11_keywords_new.txt'

    jbms=input('请输入要查找的疾病名称：')
    JBMS=jbms.split(' ')
    # getKeywords(p2, p2_keywords)
    # p1_vec=word2vec(p1_keywords,model)
    # p2_vec=word2vec(p2_keywords,model)
    for jb in JBMS:
        compare_list = []
        try:
            print('               ')
            pvec_list = []
            hdf_urlsearch(jb)#￥￥￥￥￥￥不需要下载时注释
            compare_list_str = str(compare_list)#￥￥￥￥￥￥不需要下载时注释
            p1 = 'E:\\疾病gather\\好大夫搜索测试600\\'+jb+'.txt'
            for i in compare_list:
                with open(p1,'a',encoding='utf-8')as fi:
                    fi.write(str(i).replace('\xa0','').replace('0xb0',''))
                    fi.close()
            getKeywords(p1, p1_keywords)
            with open(p1_keywords, 'r',encoding='utf-8')as fi:
                key_word=fi.readlines()
                for j in key_word:
                    p1_keywords_newkey=j.replace('\\n','')
                    pvec_list.append(j)
            with open(p1_keywords_new,'w')as fp:
                pvec_list_str=str(pvec_list).replace('\\n','').replace("'",'').replace(',','').replace('[','').replace(']','').replace('    ','').replace('   ','').replace('  ','').replace(' ','',1)

                fp.write(pvec_list_str)
            with open(p1_keywords_new, 'r')as fp:
                com1=fp.read()
                        # print(com1)
            for file in files:  # 遍历文件夹
                f = os.path.basename(file)
                name_s = f.replace('.txt', '')

                    # print(name)
                p2 = path_jib + '\\' + f
                with open(p2, 'rb')as fr:
                    sum_step = 0
                    k = 0
                    com2 = fr.read()
                        # print(com2)
                    step1=get_input_data(com1,com2,model)
                        # print(step1)
                    step2=cnn_folding(step1)
                    step3=cnn_pooling(step2)
                    # print(step3)

                    for j in step3:
                        for math_i in j:
                            k=k+1
                            sum_step=sum_step+math_i
                            avange_step=sum_step/k
                        # print(avange_step-0.5)
                    sim= avange_step
                        # compare[name_s] = sim
                    sim_4 = round(sim, 4)
                    compare[name_s] = sim_4
            n = 10
                        ########################################################################
            L = sorted(compare.items(), key=lambda item: item[1], reverse=True)
            L = L[:n]
            print(jb)
            print(L)
            with open("C:\\Users\\雷神\\Desktop\\CNN补充.txt",'a')as ft:
                ft.write(jb)
                ft.write(str(L))

        except:
            print(jb)
            print('报错报错报错**********')
            continue