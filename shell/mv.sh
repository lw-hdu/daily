#!/bin/bash
#stime=$(date "+%Y-%m-%d" )
time='2019-09-05'
find /data/result/MetaDataResult/ ! -name '*.xml'>>/home/SHELL/tmp.list
while read path
do
  houzhui=.xml
  file_name=${path##*/}
  rename=$file_name$houzhui
  times=$(stat $path |grep '最近更改' |awk -F ' ' {'print$1'}  |awk -F '：' {'print $2'}) 
#  echo -e $times
if [ -f $path ];then
	if [ $times > $time ];then
         cd /data/result/MetaDataResult
	     mv $file_name $rename
    fi
fi

done </home/SHELL/tmp.list