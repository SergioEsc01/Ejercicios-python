# #1) Cargar los datos de los alumnos en un Manejador de Alumnos, implementado usando un arreglo Numpy.
import numpy as np
import csv

class Alumno:
    # Variable de clase para almacenar el arreglo NumPy
    alumnos_np = np.empty((0, 5), dtype=object)

    # def __init__(self, archivo_csv):
    #     # Cargar los datos de los alumnos desde un archivo CSV en un arreglo numpy
    #     self.alumnos_np = np.genfromtxt(archivo_csv, delimiter=',', dtype=str)


    def __init__(self, dni, apellido, nombre, carrera, anio_cursado):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.carrera = carrera
        self.anio_cursado = anio_cursado

    def __lt__(self, other):
        if self.anio != other.anio:
            return self.anio < other.anio
        else:
            return self.apellido + ' ' + self.nombre < other.apellido + ' ' + other.nombre


    # #sobrecarga lt
    # def __lt__(self, otro_alumno):
    #     if self.anio_cursado != otro_alumno.anio_cursado:
    #         return self.anio_cursado < otro_alumno.anio_cursado
    #     else:
    #         if self.apellido != otro_alumno.apellido:
    #             return self.apellido < otro_alumno.apellido
    #         else:
    #             return self.nombre < otro_alumno.nombre  

    # Métodos get y set
    def getDni(self):
        return self.__dni

    def getApellido(self):
        return self.__apellido

    def getNombre(self):
        return self.__nombre

    def getCarrera(self):
        return self.__carrera

    def getAnio(self):
        return self.__anio

    # def obtener_datos_alumno(self, dni):
    #     indice = np.where(self.alumnos_np == dni)[0][0]

    #     datos_alumno = self.alumnos_np[indice, 1:]
    #     return datos_alumno


