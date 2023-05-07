#!/bin/bash

echo -e "Digite uma interface de rede:\n"

read interface

echo -e "\nEndereço IP da interface $interface:\n"

result=$(ifconfig $interface | grep "inet" | head -n1)

echo $result | cut -d' ' -f2