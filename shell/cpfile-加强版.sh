#!/bin/sh
file_path="/vmdata/icms/upload/hzv5"
echo -e "please input the start:\c"
read start
echo -e "please input the end:\c"
read end 

cd $file_path

while [ "$start" -le "$end" ]

do 
   cp -rf 222.ts ./3gp_$start.ts
   let start+=1
   
done

echo "文件复制完成"






#while [ $i -lt $1 ]
#do
#       cp -f $filename 3gp_$i.ts
#        echo "cp $filename 3gp_$i.ts"
#       i=`expr $i + 1`
#done
