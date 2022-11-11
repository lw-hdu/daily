'''
Descripttion: 
Author: Liuwen
Date: 2022-11-07 10:20:23
LastEditTime: 2022-11-11 13:51:12
'''
import csv,os,datetime
from time import sleep

now = datetime.datetime.now().strftime("%Y%m%d")
all_food = []
all_price = []

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
        # elif result == '2':
        #     order_look()
        elif result == '2':
            sum_order()
        elif result == 'q':
            break
        else:
            print('输入错误，请重新输入')
            sleep(1)


def order_food():

    while True:
        print('''
*************************************
        请选择要外带的早餐：
        1、鸡蛋
        2、烤肠
        3、油条
        4、水煎包
        5、牛肉饼
        6、菜盒
        7、油饼
*************************************
            ''')
        item = {'鸡蛋':1,'烤肠':3,'油条':0.8,'水煎包':0.5,'牛肉饼':5,'菜盒':1.3,'油饼':1}
        
        b = input('请输入序号选择您需要的餐品，选择完毕输入q退出：')
        if b != 'q':
            n = int(input('请输入餐品数量：'))
        if b == '1':
            all_food.append(f'{n}个鸡蛋')
            all_price.append(item['鸡蛋']*n)
        elif b == '2':
            all_food.append(f'{n}个烤肠')
            all_price.append(item['烤肠']*n)
        elif b == '3':
            all_food.append(f'{n}个油条')
            all_price.append('{:.2f}'.format(item['油条']*n))
        elif b == '4':
            all_food.append(f'{n}个水煎包')
            all_price.append(item['水煎包']*n)
        elif b == '5':
            all_food.append(f'{n}个牛肉饼')
            all_price.append(item['牛肉饼']*n)
        elif b == '6':
            all_food.append(f'{n}个菜盒')
            all_price.append('{:.2f}'.format(item['菜盒']*n))
        elif b == '7':
            all_food.append(f'{n}个油饼')
            all_price.append(item['油饼']*n)
        elif b == 'q':
            print('选择完毕，退出咯')
            break

    #数据写入csv文件
    row = [
        all_food,all_price
    ]
    with open(f'{name}_food.csv','a',newline='',encoding='utf-8') as file:
        write_csv = csv.writer(file)
        write_csv.writerows(row)
    
# def order_look():

#     try:
#         with open(f'{name}_food.csv','r',newline='',encoding='utf-8') as file:
#             read_csv = csv.reader(file)
#             for i in read_csv:
#                 print(i)
#     except FileNotFoundError:
#         print('\n该员工还未记录，请先记录')
#         sleep(1)

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