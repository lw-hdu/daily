#!/bin/sh
echo "<-----------------------------------------"
date
echo "查看内存"
free -m
echo "查看IO"
vmstat 2 5
echo  -e "查看进程总数: \c"
ps -ef | wc -l
echo  -e "查看进程的线程数 \c"
mspid=`ps -ef|grep cloudpc.biling.jar|grep -v "grep"|awk '{print $2}'`
ps -hH -p $mspid | wc -l
echo "biling 占用内存 "
ps -aux | grep biling
echo -e "查看系统打开句柄最大数量: \c"
more /proc/sys/fs/file-max
echo -e "查看打开句柄总数: \c"
lsof|awk '{print $2}'|wc -l
echo "----------------------------------------->"


