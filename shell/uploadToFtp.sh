#!/bin/bash

FTP_USER="testfile"
FTP_PASSWORD="viewt00!QAZ"
FTP_URL="192.168.2.11"
FILE_PATH="$1"
FILE_NAME="$2"

if [ "$#" != "2" ];then
        echo "UASGE：uploadToFtp FILE_PATH FILE_NAME"
        exit 1
fi

ftp -n <<!
open ${FTP_URL}
user ${FTP_USER} ${FTP_PASSWORD}
binary
cd ${FILE_PATH}
put ${FILE_NAME}
close
bye
!

echo "${FILE_NAME}已上传到${FILE_PATH}目录下"
