import os
path_test='F:\\万方_ 百度_2000'###我用来做为疾病标注的两千多个疾病
path_biecheng='E:\\实验备份\\疾病gather\\疾病_百度有别称的'###用来找这两千多个里面有别称的文件夹
path_wirteSELECT='F:\\2000分类\\SELECT.txt'

files_test=os.listdir(path_test)
files_biecheng=os.listdir(path_biecheng)

Name_test=[]
Name_biecheng=[]
SELECT=[]

for file_test in files_test:  # 遍历文件夹
    f = os.path.basename(file_test)
    name_test = f.replace('.txt', '')
    Name_test.append(name_test)
for file_biecheng in files_biecheng:
    f = os.path.basename(file_biecheng)
    name_biecheng = f.replace('.txt', '')
    Name_biecheng.append(name_biecheng)

for i_test in Name_test:
    if i_test in Name_biecheng:
        SELECT.append(i_test)
    print(SELECT)
    print('all of biecheng is %s'%len(SELECT))
with open(path_wirteSELECT,'w',encoding='utf-8')as f:
    f.write(str(SELECT))


