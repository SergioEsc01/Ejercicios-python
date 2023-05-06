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
    menu=int(input("Ingrese 1- Para comprobar si un viajero tiene mas millas que el otro\n2- Para mostrar las millas acumuladas\n3-Para ingresar un numero de viajero y restar millas\n"))
    if menu==1:
        newl.muestravmayor()
    elif menu==2:
        newl.acummillas()
    elif menu==3:
        n=int(input("Ingrese el codigo de viajero\n"))
        m2=int(input("Ingrese la cantidad de millas a restar\n"))
        newl.restamillas(m2,n)
    else:
        print("EL numero ingresado no es correcto")

