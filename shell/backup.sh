#!/bin/bash

find /data/mysql-backups/ -mtime +5 -type f -print -exec rm -rf {} \;

mysqldump -uroot -pmysql cloudpc | gzip > /data/mysql-backups/cloudpc_$(date +%Y%m%d_%H%M%S).sql.gz
mysqldump -uroot -pmysql ApolloConfigDB | gzip > /data/mysql-backups/ApolloConfigDB_$(date +%Y%m%d_%H%M%S).sql.gz
mysqldump -uroot -pmysql ApolloPortalDB | gzip > /data/mysql-backups/ApolloPortalDB_$(date +%Y%m%d_%H%M%S).sql.gz

scp -r /data/mysql-backups root@10.221.122.120:/data/
