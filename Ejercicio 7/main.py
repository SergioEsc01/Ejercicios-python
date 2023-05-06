import csv
from listaviajero import listaV 
if __name__=='__main__':
    archivo=open('C:\\Users\\juana manso\\Desktop\\Ejercicios python\\Ejercicio 6\\viajeros.csv')
    reader=csv.reader(archivo,delimiter=",")
    newl=listaV()
    for fila in reader:
        id=int(fila[0])
        dni=fila[1]
        nom=fila[2]
        ap=fila[3]
        millas=int(fila[4])
        newl.carga(id,dni,nom,ap,millas)
    archivo.close()
    menu=int(input("Ingrese 1-Para ingresar un numero y comparar si es igual a la cantidaad de millas del viajero\n2-Para mostrar la cantidad de millas acumuladas\n3-Para ingresar el numero de viajero y restar la cantidad de millas\n"))
    if menu==1:
        n=int(input("Ingrese un valor\n"))
        print("----Sobrecarga normal----")
        newl.compara(n)
        print("----Sobrecarga por derecha____")
        n2=int(input("Ingrese un valor\n"))
        newl.compara2(n2)
    elif menu==2:
        newl.acummillas()
    elif menu==3:
        n=int(input("ingrese el numero de viajero\n"))
        m2=int(input("Ingrese la cantidad de millas a restar\n"))
        newl.restamillas(m2,n)
    else:
        print("El numero ingresado no es correcto")