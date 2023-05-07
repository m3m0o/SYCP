#!/bin/bash

if [ "$1" == "r" ]
then
    echo -e "\nRotas:\n"
    route -n
elif [ "$1" == "i" ]
then
    echo -e "\nEndereço IP da interface $2:\n"

    result=$(ifconfig $2 | grep "inet" | head -n1)

    echo $result | cut -d' ' -f2
else
    echo -e "\nUsage: ./script.sh r|i interface"
fi