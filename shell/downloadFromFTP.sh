#!/bin/bash

FILE_USER="testfile"
FILE_PASS="viewt00!QAZ"
FILE_URL="192.168.2.11"
FILE_PATH="$1"
FILE_NAME="$2"
PUT_PATH="$3"

if [ "$#" != "3" ]
   then echo "use:FILE_PATH FILE_NAME PUT_PATH"
   exit 0
fi

ftp -n <<!
open $FILE_URL
user $FILE_USER $FILE_PASS
binary
cd $FILE_PATH
get $FILE_NAME
close
bye
!

mv -f ./$FILE_NAME $PUT_PATH/$FILE_NAME
echo "文件$FILE_NAME已成功下载到$PUT_PATH"
