#!/bin/sh
file_path="/data/cqicms/local"

echo -e "please input the number:\c"
read n 

cd $file_path

for ((i=1;i<=$n;i++))

do 
   cp -rf new2.ts test_$i.ts
done

echo "文件复制完成"
