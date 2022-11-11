#!/bin/sh
root_path="/opt/hjcip/hjcip/webapps/hjcip/modules/"
class_file_path="/home/class/file/"
stime=$(date "+%Y%m%d%H%M%S")
while read path
do
  file_path=${path%/*}
  file_name=${path##*/}
  dst_file_path=$root_path$file_path
  dst_file_name=$root_path$path
  org_file_name=$class_file_path$file_name
  file_rename=$file_name$stime
#  echo -e $file_rename
  if [ -f $dst_file_name ];then 
    cd $dst_file_path
    mv $file_name $file_rename
    cp $org_file_name .
  else 
    mkdir -p $dst_file_path
    cd $dst_file_path
    cp $org_file_name .
  fi


done </home/class/path/path.txt
