
import numpy as np
import csv

class Alumno:
    # Variable de clase para almacenar el arreglo NumPy
    alumnos_np = np.empty((0, 5), dtype=object)



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

 


