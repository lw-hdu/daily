while read path
do 
cd /opt/monitor-server
if [ -d $path ];then
    cd $path
    touch 111.txt
    ./stop.sh ;./start.sh
else
    echo $path"目录不存在"
fi
done</opt/shell/path2.txt