if __name__ == '__main__':
    
    import csv
    import sys 
    from claseviajeroooo import ViajeroFrecuente as claseViajero
    
    lista = []
    archivo = open('C:\\Users\\juana manso\\Desktop\\Ejercicios python\\Ejercicio 2\\infoViajeros.csv')
    reader = csv.reader(archivo, delimiter=';')
    
    for i in reader:
        nuevoObjeto = claseViajero(int(i[0]), i[1], i[2], i[3], int(i[4]))
        lista.append(nuevoObjeto)
        
    num = int(input("Ingresa el numero de viajero para el que quieres realizar una operacion: "))
    
    for k in range(len(lista)):
        if  lista[k].numero() == num:
            buscado = lista[k]
            print("Se ha encontrado al viajero ")
            print("1: Consultar cantidad de millas ")
            print("2: Acumular millas ")
            print("3: Canjear Millas")
            print("0: salir")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                print(f"La cantidad de millas son: {buscado.cantidadTotalMillas()}")
            elif opcion == 2:
                acummm = int(input("Ingrese la cantidad de millas a acumular"))
                buscado.acumularMillas(acummm)
            elif opcion == 3:
                masmillas = int(input("ingrese la cantidad de millas a canjear "))
                buscado.canjearMillas(masmillas)
            elif opcion == 0:
                exit()
            else: print("ERROR, ingresaste mal el numero")
    k=0
    while k < len(lista):
        print(f"El objeto de el viajero {lista[k].numero()} llamado {lista[k].nombree()} ocupa {sys.getsizeof(lista[k])} bytes de memoria")
        k+=1
    
        
    

    
    
    