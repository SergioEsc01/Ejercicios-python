import csv
import numpy as np
from manejadorMaterias import Manejador
from manejadorAlumnos import Alumno
from materias import Materias

if __name__=='__main__':

    print("EJERCICIO 1")
    print("Arreglo numpy")
    archivo = open('C:\\Users\\juana manso\\Desktop\\Ejercicios python\\tp integrador2\\alumnos.csv')
    reader = csv.reader(archivo,delimiter=";")
    bandera=True
    alumnos=[]
    
    for fila in reader:
        if bandera:
            bandera=False
        else:
            dni= int(fila[0])
            apellido=fila[1]
            nombre=fila[2]
            carrera=fila[3]
            anio=fila[4]

            alumnos.append([dni, apellido, nombre, carrera, anio])

    archivo.close()

    alumnos_np = np.array(alumnos)

   
    print(alumnos_np)
    print("----------------------------------------------------------------")
    print("EJERCICIO 2")
    print("Lista con las materias")
    archivo=open('C:\\Users\\juana manso\\Desktop\\Ejercicios python\\tp integrador2\\materiasAprobadas.csv')
    reader = csv.reader(archivo,delimiter=';')
    bandera=True
    newLista= Manejador()
    for fila in reader:
        if bandera:
            bandera=False
        else:
             print("\n")
             print("Datos del archivo cargado")
             dni=int(fila[0])
             materia=fila[1]
             fecha=fila[2]
             nota=int(fila[3])
             aprobacion=fila[4]
             print("\n")
             newLista.cargarMateria(dni,materia,fecha,nota,aprobacion)
    archivo.close()   
    print("----------------------------------------------------------------")
    menu=(input("Elegir opcion: \n a-Ingresar DNI para calcular promedio con y sin aplazo \n b- Ingresar nombre de una materia \n c- Obtener un listado de alumnos ordenado\n"))
    while menu != "z":
        if menu =="a":
   
            print("EJERCICIO 3")
            print("Inicio APARTADO A")
            print("\n")

            xdni= int(input("Ingresar un numero de DNI: "))

            indices = np.where(alumnos_np[:,0] == str(xdni))

            if indices[0].size==0:
                print("No se encontro el DNI buscado")
            else:
                i = indices[0][0]
                alumno_encontrado = alumnos_np[i]

               
                print("Datos del alumno encontrado:")
                print(f"DNI: {alumno_encontrado[0]}")
                print(f"Apellido: {alumno_encontrado[1]}")
                print(f"Nombre: {alumno_encontrado[2]}")
                print(f"Carrera: {alumno_encontrado[3]}")
                print(f"Año de carrera: {alumno_encontrado[4]}") 

            newLista.busqueda(xdni)



        elif menu == "b":
            print("EJERCICIO 3")
            print("Inicio APARTADO B")
            print("\n")
        
            materia = input("Ingresar nombre de una materia: ")
            dni_aprobado = newLista.aprobadoDni(materia)
            nota_aprobado = newLista.aprobadoNota(materia)
            fecha_aprobado = newLista.aprobadoFecha(materia)
            

            indices = np.where(alumnos_np[:,0] == str(dni_aprobado))
            if indices[0].size==0:
                print("No se encontro el DNI buscado")
            else:
                i = indices[0][0]
                alumno_encontrado = alumnos_np[i]
                ap=(alumno_encontrado[1])
                nom=(alumno_encontrado[2])
                anio=(alumno_encontrado[4])
            


            print("Dni | Apellido | Nombre | Fecha| Nota | Año que cursa")
            print("{} {} {} {} {} {}".format(dni_aprobado,ap,nom,fecha_aprobado,nota_aprobado,anio))
            print("\n")

        elif menu =="c":
            indices = np.lexsort((np.char.add(alumnos_np[:, 1], alumnos_np[:, 2]), alumnos_np[:, 4].astype(int)))

            alumnos_ordenados = alumnos_np[indices]

            for i in indices:
                print(f"{alumnos_np[i, 1]} {alumnos_np[i, 2]} - {alumnos_np[i, 3]} {alumnos_np[i, 4]}")


        else: 
            print("Opcion incorrecta, presione z para salir")
            print("\n")
        menu=(input("Elegir opcion: \n a-Ingresar DNI para calcular promedio con y sin aplazo \n b- Ingresar nombre de una materia \n c- Obtener un listado de alumnos ordenado\n"))
    



