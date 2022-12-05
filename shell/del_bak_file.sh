while read path
do 
echo $path
cd $path
ls -t | sed -n '4,$p' | xargs -I {} rm -rf {}
done</opt/shell/path.txt