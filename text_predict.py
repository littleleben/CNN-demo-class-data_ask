#encoding:utf-8
from text_model import *
import  tensorflow as tf
import tensorflow.keras as kr
import os
import numpy as np
import jieba
import re
import heapq
import codecs



def predict(sentences):
    config = TextConfig()
    config.pre_trianing = get_training_word2vec_vectors(config.vector_word_npz)
    model = TextCNN(config)
    save_dir = 'E:\\text-cnn-master\\checkpoints\\textcnn'
    save_path = os.path.join(save_dir, 'best_validation')

    _,word_to_id=read_vocab(config.vocab_filename)
    input_x= process_file(sentences,word_to_id,max_length=config.seq_length)
    labels ={0: 'Thigh pain', 1: 'Walking disability', 2: 'Flatulence/wind', 3: 'Vertigo', 4: 'Severe pain', 5: 'Hip pain', 6: 'Unable to think clearly', 7: 'Unable to walk', 8: 'Constant pain', 9: 'Lipitor', 10: 'Myalgia', 11: 'Numbness of hand', 12: 'Pain in upper limb', 13: 'Weakness of limb', 14: 'Headache', 15: 'Influenza-like illness', 16: 'Difficulty sleeping', 17: 'Muscle fatigue', 18: 'Serum cholesterol raised', 19: 'Dizziness', 20: 'Pain', 21: 'Rash', 22: 'Excessive upper gastrointestinal gas', 23: 'Pain provoked by movement', 24: 'Stomach cramps', 25: 'Loss of hair', 26: 'Pain in calf', 27: 'Charleyhorse', 28: 'Excruciating pain', 29: 'Loss of motivation', 30: 'Arthritis', 31: 'Stomach ache', 32: 'Itching', 33: 'Muscle atrophy', 34: 'Depression', 35: 'Upset stomach', 36: 'Pain in lower limb', 37: 'Tired', 38: 'Asthenia', 39: 'Lack of energy', 40: 'Memory impairment', 41: 'Myocardial infarction', 42: 'Visual disturbance', 43: 'Tremor', 44: 'Burning sensation', 45: 'Unable to concentrate', 46: 'Tinnitus', 47: 'Feeling irritable', 48: 'Malaise', 49: 'Cramp in calf', 50: 'Nausea', 51: 'Fatigue', 52: 'Backache', 53: 'Cramp in foot', 54: 'Myalgia/myositis - lower leg', 55: 'Hypersomnia', 56: 'Impairment of balance', 57: 'Hand pain', 58: 'Lightheadedness', 59: 'Myopathy', 60: 'Knee pain', 61: 'Poor short-term memory', 62: 'Cramp in lower limb', 63: 'Finding of increased blood pressure', 64: 'ascorbic acid', 65: 'ubidecarenone', 66: 'Generalised aches and pains', 67: 'Shoulder pain', 68: 'Foot pain', 69: 'Mentally dull', 70: 'Chest pain', 71: 'Insomnia', 72: 'Arthralgia', 73: 'Bleeding', 74: 'Blurred vision - hazy', 75: 'Diarrhoea', 76: 'Muscle cramp', 77: 'Muscle twitch', 78: 'Neck pain', 79: 'Serum creatinine raised', 80: 'Pins and needles', 81: 'Reduced libido', 82: 'Low back pain', 83: 'Ankle pain', 84: 'Arthrotec', 85: 'Muscle weakness', 86: 'Heart disease', 87: 'Cannot sleep at all'}

    feed_dict = {
        model.input_x: input_x,
        model.keep_prob: 1,
    }
    session = tf.Session()
    session.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.restore(sess=session, save_path=save_path)
    y_prob=session.run(model.prob, feed_dict=feed_dict)
    y_prob=y_prob.tolist()
    cat=[]
    cat_dict={}
    cat_dict_onlyname={}
    p_num=-1
    for prob in y_prob:
        p_num=p_num+1
        top2= list(map(prob.index, heapq.nlargest(10, prob)))
        print(top2)
        cat.append(labels[top2[0]])
        for t in top2:
            print(t)
            cat_dict[p_num]='top1='+labels[top2[0]],'top2='+labels[top2[1]],'top3='+labels[top2[2]],'top4='+labels[top2[3]],'top5='+labels[top2[4]],'top6='+labels[top2[5]],'top7='+labels[top2[6]],'top8='+labels[top2[7]],'top9='+labels[top2[8]],'top10='+labels[top2[9]],
            cat_dict_onlyname[p_num]=labels[top2[0]],labels[top2[1]],labels[top2[2]],labels[top2[3]],labels[top2[4]],labels[top2[5]],labels[top2[6]],labels[top2[7]],labels[top2[8]],labels[top2[9]],
    tf.reset_default_graph()
    print(cat)
    print(cat_dict[0])
    return  cat,cat_dict,cat_dict_onlyname

def sentence_cut(sentences):
    """
    Args:
        sentence: a list of text need to segment
    Returns:
        seglist:  a list of sentence cut by jieba 

    """
    re_han = re.compile(u"([\u4E00-\u9FD5a-zA-Z0-9+#&\._%]+)")  # the method of cutting text by punctuation
    seglist=[]
    for sentence in sentences:
        words=[]
        blocks = re_han.split(sentence)
        for blk in blocks:
            if re_han.match(blk):
                words.extend(jieba.lcut(blk))
        seglist.append(words)
    return  seglist


def process_file(sentences,word_to_id,max_length=600):
    """
    Args:
        sentence: a text need to predict
        word_to_id:get from def read_vocab()
        max_length:allow max length of sentence 
    Returns:
        x_pad: sequence data from  preprocessing sentence 

    """
    data_id=[]
    seglist=sentence_cut(sentences)
    for i in range(len(seglist)):
        data_id.append([word_to_id[x] for x in seglist[i] if x in word_to_id])
    x_pad=kr.preprocessing.sequence.pad_sequences(data_id,max_length)
    return x_pad


def read_vocab(vocab_dir):
    """
    Args:
        filename:path of vocab_filename
    Returns:
        words: a list of vocab
        word_to_id: a dict of word to id

    """
    words = codecs.open(vocab_dir, 'r', encoding='utf-8').read().strip().split('\n')
    word_to_id = dict(zip(words, range(len(words))))
    return words, word_to_id

def get_training_word2vec_vectors(filename):
    """
    Args:
        filename:numpy file
    Returns:
        data["embeddings"]: a matrix of vocab vector
    """
    with np.load(filename) as data:
        return data["embeddings"]

def toprank_evaluate():
    if str(labels[i]) in cat_list[0]:
        A.append(str(labels[i]))
        # print(A)
    if str(labels[i]) in cat_list[0:4]:
        B.append(str(labels[i]))
        # print(B)
    if str(labels[i]) in cat_list[0:9]:
        C.append(str(labels[i]))

if __name__ == '__main__':
    print('predict random five samples in test data.... ')
    import random
    sentences=[]
    labels=[]
    A=[]
    B=[]
    C=[]
    ALL_jb=[]
    with codecs.open('./data/cnews.test.txt','r',encoding='utf-8') as f:
        sample=random.sample(f.readlines(),3000)####随机
        # sample =f.readlines()###总的
        for line in sample:
            print(line)
            try:
                line=line.rstrip().split('    ')
                assert len(line)==2
                sentences.append(line[1])
                labels.append(line[0])
                print(sentences)
            except:
                pass
    cat,cat_dict,cat_dict_onlyname=predict(sentences)
    # print(cat)
    for i,sentence in enumerate(sentences,0):

        print(i)
        print ('----------------------the text-------------------------')
        # print (sentence[:50]+'....')
        print('the orginal label:%s'%labels[i])
        print('the predict label:%s'%cat[i])
        print('the predict top10 label:'+str(cat_dict[i]))
        print('the predict top10 label:' + str(cat_dict_onlyname[i]))
        cat_dict_onlyname_replacekh=str(cat_dict_onlyname[i]).replace('(','[').replace(')',']')
        print(cat_dict_onlyname_replacekh)
        cat_list=eval(cat_dict_onlyname_replacekh)
        toprank_evaluate()
        ALL_jb.append(i)###用来计算测试的总数
    A_accuracy=len(A)/len(ALL_jb)
    B_accuracy=len(B)/len(ALL_jb)
    C_accuracy=len(C)/len(ALL_jb)


    print('the top1 accuracy:%s'%A_accuracy)
    print('the top5 accuracy:%s'%B_accuracy)
    print('the top10 accuracy:%s'%C_accuracy)
