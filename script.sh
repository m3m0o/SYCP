#!/bin/bash

echo -e "Digite uma interface de rede:\n"

read interface

echo -e "Informações da interface de rede $interface:\n"

ifconfig $interface