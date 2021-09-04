
path='F:\\text-cnn-ENG\\data\\cnews.train.txt'
with open(path,'r',encoding='utf-8')as f:
    num = -1
    label_dict={}
    label_list=[]
    lines=f.readlines()
    for i in lines:

        _,label,content=i.split('\t')
        label_list.append(label)

    label_new=list(set(label_list))
    for i in label_new:

        num=num+1
        label_dict[num] = i
    print(str(label_new))
    print(len(label_new))
    print(str(label_dict))
    for i,j in label_dict.items():
        print(i)
        print(j)

