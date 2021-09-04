import os
import tqdm
import time
########跑完以后像'    ,','直接空行'等问题需要手动修改############

basepath= "F:\\"##主文件夹

path_allwrite='F:\\tr_te_val\\2000.txt'###写入的文本


path_wf=os.path.join(basepath,'万方_ 百度_2000')##万方疾病
##path_xx=

files_wf= os.listdir(path_wf)
##files=


content=[]##记录
def replace_dealing_bd(i):####去除一些处理中不必要的字符
    i_new=i.replace('[','').replace(']','').replace('"','').replace(' ','')\
        .replace('(1)','').replace('(2)','').replace('(3)','').replace('(4)','').replace('(5)','').replace('(6)','').replace('(7)','').replace('(8)','').replace('(9)','').replace('(10)','')\
        .replace('1．','').replace('2．','').replace('3．','').replace('4．','').replace('5．','').replace('6．','').replace('7．','').replace('8．','').replace('9．','').replace('10．','')\
        .replace('（1）','').replace('（2）','').replace('（3）','').replace('（4）','').replace('（5）','').replace('（6）','').replace('（7）','').replace('（8）','').replace('（9）','').replace('（10）','')\
        .replace('1.','').replace('2.','').replace('3.','').replace('4.','').replace('5.','').replace('6.','').replace('7.','').replace('8.','').replace('9.','').replace('10.','')\
        .replace('1）','').replace('2）','').replace('3）','').replace('4）','').replace('5）','').replace('6）','').replace('7）','').replace('8）','').replace('9）','').replace('10）','')\
        .replace('1)','').replace('2)','').replace('3)','').replace('4)','').replace('5)','').replace('6)','').replace('7)','').replace('8)','').replace('9)','').replace('10)','')
    return i_new


def readClause(files):
    for file in files:  # 遍历文件夹
        f = os.path.basename(file)
        name = f.replace('.txt','')##取出每个疾病的名字，用于后面的拼接
        name_label=name+'    '
    # print(name)
        num=0
        single_jb= os.path.join(path_wf,name+'.txt')

        with open(single_jb,'r',encoding='utf-8')as fr:
            waitClasue=fr.read()

            Clause_list = waitClasue.split('。')
            for i in Clause_list:
                # num=num+1
                # print(i)
                # print(name_label)
                i_new=replace_dealing_bd(i)


                content_str=name_label+i_new###每句label+content
                content_str_new=content_str.replace('    ,','    ').replace('    ，','    ').replace('    ,','    ')##去除一些处理后错误的字符

                content.append(content_str)
                # print(content_str)
                if content_str==name_label:
                    print(content_str)
                    content.remove(content_str)
                # print(type(content_str))


    with open(path_allwrite, 'a', encoding='utf-8')as fw:

        for j in content:
            fw.write(j+'\n')
        # print(single_jb)








if __name__ == '__main__':
    print('begin clausing...')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    readClause(files_wf)
    print('over clausing...')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

