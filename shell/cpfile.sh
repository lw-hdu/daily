#!/bin/sh
file_path="/data/Image/sihuatest"

echo -e "please input the number:\c"
read n 

cd $file_path

for ((i = 1; i <= $n; i++ ))

do 
   cp 1.ts $i.ts
done

echo "文件复制完成"
