'''
Descripttion: 
Author: Liuwen
Date: 2022-02-28 08:42:59
LastEditTime: 2022-02-28 10:05:38
'''
with open('D:\\liuwen10\\Desktop\\file.txt',encoding='utf-8') as f:
    file = f.readlines()
    for i in file:
        id = i.split(',')[0]
        name = i.split(',')[1]
        t = i.split(',')[2]
        phone = i.split(',')[3]
        sql = f'insert  into mon_customer(id,company_name,create_time,user_phone) values ({id},\'{name}\',{t},\'{phone}\');\n'
        with open('D:\\liuwen10\\Desktop\\sql.txt','a',encoding='utf-8') as s:
            s.writelines(sql)