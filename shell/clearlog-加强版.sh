#!/bin/sh
logpath="/data/logs/"
size=0
echo "please input zhe number(Ҫɾ��������֮ǰ����־):"
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

echo "��ɾ��$n��֮ǰ����־"
echo "�����$size �ֽڿռ�"
