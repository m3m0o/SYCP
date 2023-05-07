#!/bin/bash
# This script downloads an HTML page from a valid address and looks for comments in the document

if [ -z $1 ]
    then
        echo -e "\nPlease enter an URL.\n"
else
    wget $1 -O temp.html 2>/dev/null
    
    if [[ $(wc -c temp.html | cut -d " " -f1 ) == 0 ]]
        then
            echo "Incorrect URL."
    else
        cat temp.html | grep -n "<!--"
    fi

    rm temp.html
fi