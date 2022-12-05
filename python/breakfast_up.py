'''
Descripttion: 
Author: Liuwen
Date: 2022-12-05 08:57:16
LastEditTime: 2022-12-05 10:09:00
'''
import csv,os,datetime
from time import sleep

now = datetime.datetime.now().strftime("%Y%m%d")

def main():
    while True:
        print('''
*************************************************************
        欢迎来到外带早餐系统：
        1、代餐记录
        2、计算总价 注意：计算总价操作后即开启新一轮记录
*************************************************************
        ''')
        global name
        result = input('请输入序号开始使用，q退出：')
        if result == '1' or result == '2':
            name = input('请输入工号：')
        if result == '1':
            order_food()
        elif result == '2':
            sum_order()
        elif result == 'q':
            break
        else:
            print('输入错误，请重新输入')
            sleep(1)

def order_food():
    print('早餐餐品：')
    with open('food.csv','r',encoding='UTF-8',newline='') as f:
        read_csv = csv.reader(f)
        for i in read_csv:
            print(i[0],i[1])

    all_food = []
    all_price = []

    while True:
        b = input('请输入序号选择您需要的餐品，选择完毕输入q退出：')
        if b != 'q':
            n = int(input('请输入餐品数量：'))
            with open('food.csv','r',encoding='UTF-8',newline='') as f1:
                read_csv1 = csv.reader(f1)
                for j in read_csv1:  
                    if b == j[0]:
                        all_food.append(f'{n}个{j[1]}')
                        all_price.append('{:.2f}'.format(float(j[2])*n))
        elif b == 'q':
            break
    #数据写入csv文件
    row = [
        all_food,all_price
    ]
    with open(f'{name}_food.csv','a',newline='',encoding='utf-8') as file:
        write_csv = csv.writer(file)
        write_csv.writerows(row)

def sum_order():
    sum = 0 
    try:
        with open(f'{name}_food.csv','r',newline='',encoding='utf-8') as file:
            read_csv = csv.reader(file)
            result = list(read_csv)
            for food in range(0,len(result),2):
                print(f'代餐记录：{result[food]}')
            for i in range(1,len(result),2):
                #获取价格行的数
                # print(result[i])
                for j in result[i]:
                #     print(j)
                    sum += float(j)
            print(f'早餐总价：{sum}')
        os.rename(f'{name}_food.csv',f'{name}_food.csv_{now}')
    except FileNotFoundError:
        print('\n该员工还未记录，请先记录')
        sleep(1)


# 调用主菜单函数
if __name__ == '__main__':
    main()
    
    
