Para que el programa funcione correctamente, dentro de la carpeta donde estemos corriendo el mismo debemos crear un archivo llamado "db.txt".
Esto solo si es la primera vez que se ejecuta el programa, dado que este lo primero que hace es asignarle a un diccionario vacio todos los datos 
de user-pass que se encuentren alamcenados en el txt, por lo que si no esta creado el archivo, dara error. Esto lo hice para que cuando se corra 
el programa se recuperen los usuarios y contraseñas alamcenados en una previa ejecucion del programa(en caso de no haber almacenado nada, como
es en la primera ejecucion, el diccionario seguira vacio).
