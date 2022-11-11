cp /opt/cloudpc.eurekaserver/nohup.out /data/log/eurekaserver`date -d yesterday +%Y%m%d`.out;
cat /dev/null > /opt/cloudpc.eurekaserver/nohup.out

cp /opt/cloudpc.gateway/north_nohup.out /data/log/north_gateway`date -d yesterday +%Y%m%d`.out;
cat /dev/null > /opt/cloudpc.gateway/north_nohup.out

cp /opt/cloudpc.gateway/south_nohup.out /data/log/south_gateway`date -d yesterday +%Y%m%d`.out;
cat /dev/null > /opt/cloudpc.gateway/south_nohup.out

cp /opt/cloudpc.gateway/dns_nohup.out /data/log/dns_gateway`date -d yesterday +%Y%m%d`.out;
cat /dev/null > /opt/cloudpc.gateway/dns_nohup.out