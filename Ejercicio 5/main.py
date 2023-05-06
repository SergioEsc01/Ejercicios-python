import csv
from listacons import listaVehiculos
if __name__=='__main__':
    archivo=open('C:\\Users\\juana manso\\Desktop\\Ejercicios python\\Ejercicio 5\\planes.csv')
    reader=csv.reader(archivo,delimiter=";")
    newLista=listaVehiculos()
    for fila in reader:
        cod=int(fila[0])
        mod=fila[1]
        ver=fila[2]
        pre=float(fila[3])
        cc=int(fila[4])
        ccap=int(fila[5])
        newLista.carga(cod,mod,ver,pre,cc,ccap)
    archivo.close()
    menu=int(input("Ingrese el valor correspondiente:\n1-Para modificar el valor del vehiculo de cada plan de ahorro\n2-Ingresando un valor se mostraran los planes que tengan un valor menos al ingresado\n3-Se muestra el valor de lo que se debe haber pagado para licitar el vehiculo\n4-Ingresando el codigo del plan se modifican la cantidad de cuotas a licitar\n"))
    if menu==1:
        newLista.muestra()
    elif menu==2:
        valor=float(input("Ingrese el valor\n"))
        newLista.muestrainferior(valor)
    elif menu==3:
            newLista.muestracuotaslic()
    elif menu==4:
        num=int(input("Ingrese el codigo del plan para modificar las cuotas a licitar\n"))
        newLista.cambiavalor(num)
    else:
        print("El numero ingresado no es correcto")