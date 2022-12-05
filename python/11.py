'''
Descripttion: 
Author: Liuwen
Date: 2022-12-05 09:44:05
LastEditTime: 2022-12-05 09:54:48
'''
import csv
with open('food.csv','r',encoding='UTF-8',newline='') as f:
    read_csv = csv.reader(f)
    for i in read_csv:
        print(i[0])
        # print(i[1])
        # print(i[2])