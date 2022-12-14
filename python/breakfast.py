'''
Descripttion: 
Author: Liuwen
Date: 2022-11-07 10:20:23
LastEditTime: 2022-12-05 08:50:21
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
    all_food = []
    all_price = []

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
        8、煎饼果子
        9、肉卷
        10、菜盒(外)
        11、包子(外)
        12、手抓饼
*************************************
            ''')
        item = {'鸡蛋':1,'烤肠':3,'油条':0.8,'水煎包':0.5,'牛肉饼':5,'菜盒':1.3,'油饼':1,'煎饼果子':3.5,'肉卷':2.5,'菜盒(外)':3,'包子(外)':1.5,'手抓饼':2.5}
        
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
        elif b == '8':
            all_food.append(f'{n}个煎饼果子')
            all_price.append(item['煎饼果子']*n)
        elif b == '9':
            all_food.append(f'{n}个肉卷')
            all_price.append(item['肉卷']*n)
        elif b == '10':
            all_food.append(f'{n}个菜盒(外)')
            all_price.append(item['菜盒(外)']*n)
        elif b == '11':
            all_food.append(f'{n}个包子(外)')
            all_price.append(item['包子(外)']*n)
        elif b == '12':
            all_food.append(f'{n}个手抓饼')
            all_price.append(item['手抓饼']*n)
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