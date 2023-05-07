#!/bin/bash
# This script uses the NMAP tool to perform a TCP ACK scan on all possible hosts on a given network and returns those that are identified as up

if [ -z "$1" ]
    then
        echo -e "\nPlease enter a network interface.\n"
else
    ip_range=$(ifconfig $1 | grep "inet" | head -n1 | cut -d "." -f1,2,3 | sed 's/inet //' | sed 's/$/./')

    for i in {0..255}
        do
            if [[ $(sudo nmap -sn -PA $ip_range$i | grep "Host is up") ]]
                then
                    echo $ip_range$i is up.
            fi
        done
fi