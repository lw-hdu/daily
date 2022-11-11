'''
Descripttion: 
Author: Liuwen
Date: 2022-08-25 09:57:52
LastEditTime: 2022-11-11 15:59:42
图片识别
'''


from aip import AipOcr
from selenium import webdriver
import time

# driver = webdriver.Chrome()
# driver.get('http://t.zoukankan.com/loren880898-p-15117298.html')
# driver.maximize_window()
# time.sleep(2)
# js_height = "return document.body.clientHeight"
# k = 1
# height = driver.execute_script(js_height)
# while 1:
#     if k*500 < height:
#         js_move = "window.scrollTo(0,{})".format(k * 500)
#         driver.execute_script(js_move)
#         time.sleep(0.2)
#         height = driver.execute_script(js_height)
#         k += 1
#     else:
#         break

# width = driver.execute_script("return document.body.scrollWidth")
# height = driver.execute_script("return document.body.scrollHeight")
# driver.set_window_size(width, height)
# time.sleep(1)
# png_file = f'D:/1.png'
# driver.save_screenshot(png_file)
# time.sleep(0.5)
# driver.close()
#百度ai的应用信息
APP_ID = '27152241'
API_KEY='7lrQbc2zDkt65epWVrMm7cv0'
SECRET_KEY='zvRCDGZKe5FT06qSztOwHwIr8s1QzrnK'
#实例化对象
client = AipOcr(APP_ID,API_KEY,SECRET_KEY)
def get_img(file):
    with open(file,'rb') as f:
        return f.read()
img = get_img(r'D:\liuwen10\Desktop\ly.png')
# options = {}
# options["result_type"] = "json"
# res_image = client.tableRecognition(img, options)
# print(res_image)
result = client.basicGeneral(img)
# print(result)
for item in result['words_result']:
    # with open('file.txt','a+',encoding='utf-8') as fw:
    #     fw.write(item['words'])
    print(item['words'])