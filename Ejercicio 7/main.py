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
    n=int(input("Ingrese un valor\n"))
    print("----Sobrecarga normal----")
    newl.compara(n)
    print("----Sobrecarga por derecha____")
    n2=int(input("Ingrese un valor\n"))
    newl.compara2(n2)
    m1=int(input("Ingrese las millas a sumar\n"))
    newl.acummillas(m1)
    m2=int(input("Ingrese la cantidad de millas a restar\n"))
    newl.restamillas(m2)