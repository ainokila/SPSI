# Práctica 2

## Ejercicio 1
Generad, cadad uno de vosotros, una clave RSA de 768 bits, para referirnos a ella supondre que se llama nombreRSAkey.pem.
No es necesario que este protegida por contraseña.

        openssl genrsa -out cristianRSAkey.pem 768

## Ejercicio 2
Extraed la clave privada contenida en nombreRSAkey.pem a otro archivo llamado nombreRSApriv.pem, este debe estar protegido por contraseña cifrado con AES-128.

Contraseña: 0123456789

El fichero cristianRSAkey.pem ya contiene la clave privada, por lo que no es necesario extraerlo, solo nos queda protegerlo.

        openssl rsa -in cristianRSAkey.pem -out cristianRSApriv.pem -aes128

![Ejercicio 2](img/ejercicio2.png)

## Ejercicio 3 
Extraer la clave pública contenida en nombreRSAkey.pem y llamarla nombreRSApub.pem, evidentemente esta clave no debe estar cifrada, mostrar sus valores.

        openssl rsa -in cristianRSAkey.pem -out cristianRSApub.pem

![Ejercicio 3](img/ejercicio3.png)

## Ejercicio 4

Reutilizando el fichero input.bin de 1024 bits, todos a 0 de la practica anterior, intenta cifrarlo con la clave pública anteriormente generada.

Para cifrarlo realizariamos:

        openssl rsautl -in input.bin -out input.bin.cifrado -inkey cristianRSApub.pem -pubin 

Pero este fichero es demasiado grande para cifrarlo mediante RSA, por lo que nos genera un error que nos informa.

![Ejercicio 4](img/ejercicio4.png)

## Ejercicio 5 

Diseñad un sistema hibrido, con RSA como sistema de cifrado Asimetrico.


















