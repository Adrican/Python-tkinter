'''
Created on 31 oct. 2016

@author: Adri
'''
'''
print ("Hola Mundo Python")
print ("La suma de 2+5 es ", 2+5)
print ("5 elevado a 3 es ", 5**3)
print ("7 entre 2 es ", 7%2) 
print (3*4/2-2*5)
print ("AA"+"BB"+"CC")
print ("ABC,"*5+"DEF")
print (1, 8==5)
print (2, 8==8)
print (3, 8==8 and 4==2)
print (5, not(8==8 and 4==2))
print (5, not(8==8 or 4==2))
print (6, 'a'==('a' or 'b'))


num1=50.75
num2=100
num3=num1*num2
print(num3)

cadena1="Adrian"
cadena2="Canas"
cadena3=cadena1+cadena2
print (cadena3)

nombre = input("Digame su nombre ")
print ("Esta bien", nombre ,"puede pasar")
'''
'''
num = input ("Dame un numero decimal")
print (num)
num1 = float(input("Dame un numero decimal"))
print (num1)
'''
'''
num3 = float(input("Dame un número decimal "))
print(num3)
num4 = int(input("Dame un numero entero "))
print (num4)
print ("El num3 es del tipo ", type(num3))
print ("El num4 es del tipo ", type(num4))
num5 = (input("Dame un dato "))
print (num5)
print ("El num5 es del tipo ", type(num5))
'''

'''

print (mitupla)
print (mitupla[1:4]) #del 1 al 4, el 4 sin incluir
print (len(mitupla))
print (mitupla[:3])
print (mitupla[:])
print (mitupla.index("Hola"))
print (mitupla.count)
'''
'''
mitupla = (25,"Hola",6.9,"Universidad")
print (mitupla.count("Hola")) #A las tuplas no se les puede añadir nada con el metodo append

milista = [25,"Hola",6.9,"Universidad"]
print(milista)
milista.append("HOLA")
print(milista)

milista.remove(6.9)
print(milista)

var = milista.pop()  #Elimina elementos por el final y lo añade a la variable en este caso "var"
print (milista)

'''

'''
milista = [25,"Hola",6.9,"Universidad"]
var = milista.pop(2)
print (milista)
print (var)
milista.clear()
print (milista)


milista = [25,"Hola",6.9,"Universidad"]
print(milista)
milista[0] = 25
milista[1] = 6.9
milista[2] = 1
milista[3] = 10
print(milista)

milista.sort()
print(milista)

milista = [25,"Hola",6.9,"Universidad"]
milista.reverse()
print(milista)

del milista[1]
print(milista)


lista2 = milista.copy();
print(lista2)
'''
'''
procesos = [1, 2, 3, 4];
procesos.append(10);
procesos.append(11);
procesos.append(12);
print (procesos);
procesos.pop();
print (procesos);
procesos.pop();
print (procesos);
procesos.pop();
print (procesos);
'''

'''
procesos = [1, 2, 3, 4];
c=0;
procesos.append(5)
procesos.append(6)
procesos.append(7)
while c<3:
        procesos.pop(0); #Eliminara la primera posicion
        c=c+1;
print (procesos);

n=0;
while n <11:
    print(n);
    n+=1;
'''    

'''    
while True:
    nombre = input("Dame tu nombre...");
    print(nombre);
    if nombre:
        break;
'''    

'''    
numeros = [2,4,10,5,22];
longitud = 0;
suma = 0;
long = len(numeros)
while longitud < long:
    suma = numeros.pop() + suma;
    longitud +=1;
    
print(suma);
'''

'''
fin_prog="";
while fin_prog!="s":
    print("Estas dentro del while")
    fin_prog=input("pulsa la letra s para salir del while")
'''

'''
semaforo=input("De que color esta el semaforo? ")
if semaforo == "verde":
   print ("Prosiga")
elif semaforo == "rojo":
   print ("no pases")
elif semaforo == "ambar" or semaforo == "amarillo":
   print ("date prisa")
else:
    print ("Este color no es un color de semaforo")
    
'''

'''
lista = ["montaña", "valle", "laguna", "meseta", "nieve"]

for i in lista:
    print(i);

for i,x in enumerate(lista):
    print("lista[",i,"] = ", x);

for i in range(len(lista)):
    print("El valor de la posicion es: ", lista[i]);
    
lista.append("agua")
lista.append("charco")
lista.append("manantial")

for i in range(3, len(lista)):
    print("El valor de la posicion es: ", lista[i]);
    
    
listanum = (2,5,8,9,2,3);
suma = 0;
for i in listanum:
    suma+= i;
    
print(suma)
'''

listanum2 = [2,5,8,9,2,3,9];
listanum2.sort();
aux = 0;
for i in listanum2:
        if aux == i:
            print("Se ha encontrado " , aux)
        aux = i;