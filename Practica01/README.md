# Práctica 1

## Ejercicio 1
Partiremos de un archivo binario de 1024 bits, todos ellos con valor 0. Para hacer refencia al mismo voy a supone que se llama input.bin.

### Creación de input.bin

Necesitamos pasar los bits a bytes, una vez lo tenemos usaremos dd para crear el fichero binario.

1024 bits / 8 = 128 bytes
dd if=/dev/zero of=input.bin count=1 bs=128

![Ejercicio 1](img/ejercicio1.png)

## Ejercicio 2
Creamos un archivo binario de 1024 bits, todos ellos con valor 0 y en los primeros 40 bits debe haber un 1. Para hacer refencia al mismo voy a supone que se llama input1.bin.

### Creación de input1.bin

Necesitamos pasar los bits a bytes, una vez lo tenemos usaremos dd para crear el fichero binario.

1024 bits / 8 = 128 bytes
dd if=/dev/zero of=input1.bin count=1 bs=128

Ahora lo editamos con gHex para añadir el 1, en mi caso lo añadiré en el 2 byte.

![Ejercicio 2](img/ejercicio2.png)

## Ejercicio 3
Cifrad input.bin con DES en modos ECB, CBC, Y OFB, usando como claves una debil y otra semidebil, con vector de inicialización a vuestra elección, explicad los resultados.

Clave debil: 0x0101010101010101
Clave semidebil: 0x01FE01FE01FE01FE

### DES-ECB input.bin

#### DES-ECB input.bin debil
Debemos pasar la clave como parametro en la llamada a openssl, debido a que si no realizará la función hash de la clave introducida.

        openssl enc -des-ecb -in ./input.bin -out ./input.bin.des.ecb.debil -K 0101010101010101

![Ejercicio 3](img/ejercicio3_des_ecb_debil.png)

Se puede observar, que se repite en mismo patron desde 0x0 hasta 0x7f.


#### DES-ECB input.bin semidebil

        openssl enc -des-ecb -in ./input.bin -out ./input.bin.des.ecb.semidebil -K 01FE01FE01FE01FE

![Ejercicio 3](img/ejercicio3_des_ecb_semidebil.png)

En este caso tambien se repite el mismo patrón, desde el offset 0x0 hasta 0x7f


### DES-CBC input.bin
#### DES-CBC input.bin debil
Vector de inicialización: 0000000000000000

        openssl enc -des-cbc -in ./input.bin -out ./input.bin.des.cbc.debil -K 0101010101010101 -iv 0000000000000000

![Ejercicio 3](img/ejercicio3_des_cbc_debil.png)

Se puede apreciar, que se repite la misma estructura, pero en este caso en dos bloques distintos de longitud 16 bytes, lo unico que no se repite es de 0x80 a 0x87. En el 2 bloque, vemos que es casi identico a la entrada.


#### DES-CBC input.bin semidebil

Vector de inicialización: 0000000000000000

        openssl enc -des-cbc -in ./input.bin -out ./input.bin.des.cbc.semidebil -K 01FE01FE01FE01F -iv 0000000000000000

![Ejercicio 3](img/ejercicio3_des_cbc_semidebil.png)

No se observan patrones o repeticiones aparentes.


### DES-OFB input.bin
