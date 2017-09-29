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


