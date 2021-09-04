import os
import tqdm
import time
########跑完以后像'    ,','直接空行'等问题需要手动修改############

basepath= "E:\实验备份\疾病gather"##主文件夹

path_basewrite='F:\\疾病语料\\'###写入的文本


path_wf=os.path.join(basepath,'万方加百度筛选后的疾病')##万方疾病
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
    num=0
    for file in files:  # 遍历文件夹

        num = num + 1
        # print(num)
        f = os.path.basename(file)
        name = f.replace('.txt','')##取出每个疾病的名字，用于后面的拼接
        print(name)
        name_label=name+'    '
    # print(name)

        single_jb= os.path.join(path_wf,name+'.txt')

        with open(single_jb,'r',encoding='utf-8')as fr:
            waitClasue=fr.read()

            Clause_list = waitClasue.split('。')
            for i in Clause_list:

                # print(i)
                # print(name_label)
                i_new=replace_dealing_bd(i)


                content_str=name_label+i_new###每句label+content
                content_str_new=content_str.replace('    ,','    ').replace('    ，','    ').replace('    ,','    ')##去除一些处理后错误的字符

                content.append(content_str)
                # print(str(content))
                # print(type(content_str))
        if num%750==0:

            path_write=path_basewrite + 'raw' + str(num/750)+'.txt'
            print(len(content))
            with open(path_write, 'a', encoding='utf-8')as fw:
                for j in content:
                    fw.write(j+'\n')
        if num % 1000 == 0:
            content.clear()
        # print(str(content))
        # print(single_jb)








if __name__ == '__main__':
    print('begin clausing...')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    readClause(files_wf)
    print('over clausing...')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

