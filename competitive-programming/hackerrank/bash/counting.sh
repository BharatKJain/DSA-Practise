n=0
while [ $n -lt 100 ]
do
    echo $n
    echo
    expr $n + 1 | $n
done