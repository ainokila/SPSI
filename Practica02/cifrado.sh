#!/bin/bash

#. /cifrado.sh enc -aes128 publica.pem holi.txt 

if [ "$1" == "enc" ]
then

    #Genero la clave aleatoria para cifra simetrica
    openssl rand -base64 48 -out sessionkey
    echo $2 >> sessionkey

    #Cifro el documento de manera simetrica
    openssl enc $2 -pass file:sessionkey -in $4 -out $4.encrypted

    #Cifro el fichero con la clave random y el tipo de cifrado
    openssl rsautl -encrypt -in sessionkey -out sessionkey.cifrado -inkey $3 -pubin



else

    #. /cifrado.sh dec sessionkey.cifrado privada.pem clave holi.txt.encrypted
   if [ "$1" == "dec" ]
    then


        #Descifro el fichero donde esta contenida la clave aleatoria y el metodo de cifrado
        openssl rsautl -decrypt -inkey $3 -in $2 -out sessionkey -passin pass:$4

        cifrado=$(tail sessionkey -n 1 )
        clave=$(head -n1 sessionkey)
        name=$5
        new_name=${name::-10}


        #Descifro el fichero importante usando la clave y metodo anterior
        openssl enc -d $cifrado -in $5 -pass pass:$clave -out $new_name


        
    else
        echo "Use: ./cifrado.sh enc -type public.pem file"
        echo "Use: ./cifrado.sh dec sessionkey.cifrado private.pem key_private file.encrypted"
fi
fi






