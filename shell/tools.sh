#!/bin/bash

USDL_catalinash="/opt/onewave/usdl/tomcat/bin/catalina.sh"
USDL_serverxml="/opt/onewave/usdl/tomcat/conf/server.xml"
logFilePath="/opt/onewave/usdl/tomcat/logs"
CatalinaLogPath="/opt/onewave/usdl/tomcat/logs"
DATABASE_PATH="/opt/onewave/usdl/tomcat/webapps/usdl/WEB-INF/conf"
line="------------------------------"
yyyy=`date +%Y`
colour=`echo -e "\033[31;40m"`
form=`tput sgr0`
bold=`tput bold`

function viewPort()
{

	UsdlPort=`grep "Connector port" $USDL_serverxml | head -1 | awk -F\" '{print $2}'`
	UsdlDebugPort=`grep "JPDA_ADDRESS=" $USDL_catalinash | awk -F\" '{print $2}'`

	echo -e "UsdlPort:$colour$bold$UsdlPort$form
UsdlDebugPort:$colour$bold$UsdlDebugPort$form"
}

function clearLog()
{

	if [ "$#" != "1" ];then
        	echo "usage:6_clearLog.sh clear_day"
        	exit 1
	fi

	logFileList=`find $logFilePath -name "*.log" -ctime +$1`
	countSize=0

	for i in $logFileList
	do
        	fileSize=`ls -l $i | awk '{print $5}'`
        	#echo $fileSize
        	countSize=`expr $countSize + $fileSize`
        	rm -fr $i
        	echo "$i 文件已清理"
	done

	countSize=`expr $countSize / 1048576`
	echo "成功清理$colour$bold$1$form天之前的日志,释放空间$colour$bold${countSize}${form}MB"
}

function viewStartUpTime()
{
	echo "please input date(yyyy-mm-dd)?"
	read date

	if [ "$date" = "" ];then
        	date=`date +%Y-%m-%d`
	fi

	echo -e "\n\n\n$date"

	startUpTime=`grep "org.apache.catalina.startup.Catalina start" $CatalinaLogPath/catalina.$date.log 2>> startUpTime.log | awk '{print $1,$2}'`
	startUpTimeCount=`echo $startUpTime | grep -o "$yyyy" | wc -l`
	#echo $startUpTime
	#echo $startUpTimeCount

	echo -e "$line\n启动时间：\n$colour$startUpTime$form"
	echo -e "\n\n启动次数：\n$colour$startUpTimeCount$form\n$line"
}

function viewDatabase()
{
	URL=`grep "^/spring/config.properties|jdbc.url=" $DATABASE_PATH/config.properties | awk -F@ '{print $2}'`
	USERNAME=`grep "^/spring/config.properties|jdbc.username=" $DATABASE_PATH/config.properties | awk -F= '{print $2}'`
	PASSWORD=`grep "^/spring/config.properties|jdbc.password=" $DATABASE_PATH/config.properties | awk -F= '{print $2}'`

	echo -e "url: $colour$URL$form\nusername: $colour$USERNAME$form\npassword: $colour$PASSWORD$form"
}

echo "Please choose the number?"

while :
do
select var in "View Port" "Clean Log(default 10 days ago)" "View StartUp Time" "View Database" "Quit"
do
	case $var in
	"View Port")
		viewPort
		break;;
	"Clean Log(default 10 days ago)")
		clearLog 10
		break;;
	"View StartUp Time")
		viewStartUpTime
		break;;
	"View Database")
		viewDatabase
		break;;
	"Quit")
		exit 1
		;;
	esac	
	
done
done
