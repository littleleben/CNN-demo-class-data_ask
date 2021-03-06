import os
import random

annotation_path = "F:\\text-cnn-ENG\\data\\RESULT_raw.txt"
train_path = "F:\\text-cnn-ENG\\data\\cnews.train.txt"
val_path = "F:\\text-cnn-ENG\\data\\cnews.val.txt"
test_path ="F:\\text-cnn-ENG\\data\\cnews.test.txt"
train_file = open(train_path, "a+",encoding='utf-8')
val_file = open(val_path, "a+",encoding='utf-8')
test_file = open(test_path, "a+",encoding='utf-8')
anno = open(annotation_path, 'r',encoding='utf-8')
result = []
my_dict = {}
cnt = 0
for line in anno:
    my_dict[cnt] = line
    cnt += 1
totalnum = cnt
test_num = totalnum * 0.1
val_num = totalnum * 0.2
train_num = totalnum * 0.7

test_set = set()
val_set = set()
train_set = set()

while (len(test_set) < test_num):
    x = random.randint(0, totalnum)
    if x not in test_set:
        test_set.add(x)

while (len(val_set) < val_num):
    x = random.randint(0, totalnum)
    if x in test_set:
        continue
    if x not in val_set:
        val_set.add(x)

for x in range(totalnum):
    if x in test_set or x in val_set:
        continue
    else:
        train_set.add(x)

index = 0
for i in range(cnt):
    strs =my_dict[i]
    if i in train_set:
        train_file.write(strs)
    elif i in val_set:
        val_file.write(strs)
    else:
        test_file.write(strs)
    index += 1

train_file.close
val_file.close
test_file.close