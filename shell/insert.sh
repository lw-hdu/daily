#!/bin/bash
IFS=','
while read name phone
do
echo "insert into temp(name,phone) values('$name','$phone');" >> /opt/shell/insert.sql
done</opt/shell/name.csv






csv 文件多个列之间用,分隔
CREATE TABLE `temp` (
  `name` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4