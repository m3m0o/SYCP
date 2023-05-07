#!/bin/bash

echo -e "Digite (r) para Routes e (i) para Interfaces de Rede:\n"

read option

if [ "$option" == "r" ]
then
echo -e "\nRotas:\n"
route -n
elif [ "$option" == "i" ]
then
echo -e "\nDigite uma interface de rede:\n"

read interface

echo -e "\nEndereço IP da interface $interface:\n"

result=$(ifconfig $interface | grep "inet" | head -n1)

echo $result | cut -d' ' -f2
else
echo -e "\nOpção inválida."
fi