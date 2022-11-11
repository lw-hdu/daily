#!/bin/sh
logpath="/data/logs/"
size=0
echo "please input zhe number(要删除多少天之前的日志):"
read n
if [ "$n" = "" ]
   then n=5
fi

find $logpath -mtime +$n -name  "*.log"|xargs du -s |awk '{print $1}'>size.txt

for i in `cat size.txt`
do
   size=$(($size+$i))
done

find $logpath -mtime +$n -name  "*.log" -exec rm -rfv {} \;

echo "已删除$n天之前的日志"
echo "清理出$size 字节空间"
