import csv
from materias import Materias
from manejadorAlumnos import Alumno

class Manejador:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def cargarMateria(self,doc,nombre,fecha,nota,apr):
 
        newMateria = Materias(doc,nombre,fecha,nota,apr)
        self.__lista.append(newMateria)


    def busqueda(self, xdoc):
        sacum = 0  # acumulador sin aplazo mayor o igual a 4
        scont = 0  # contador sin aplazo
        cacum = 0  # acumulador con aplazo
        ccont = 0  # contador con aplazo
        
        for materia in self.__lista:
            if materia.getDocumento() == int(xdoc):
                if materia.getNota() >= 4:
                    sacum += materia.getNota()
                    scont += 1
                else:
                    cacum += materia.getNota()
                    ccont += 1

        if scont > 0:
            sprom = sacum / scont 
            if ccont > 0:
                cprom = (sacum + cacum) / (scont + ccont)
                print("El promedio sin aplazo es: {}".format(sprom))
                print("El promedio con aplazos es: {}".format(cprom))
            else:
                print("El promedio sin aplazo es: {}".format(sprom))
                print("El estudiante no tiene notas con aplazo.")
        else:
            print("No se encontró al estudiante con el DNI {}".format(xdoc))

    
    def aprobadoDni(self,xnombre):
        i=0
        encontrado = False
        DniLista = 0
        while i < len(self.__lista) and not encontrado:
            if self.__lista[i].getMateria() == xnombre:
                print("El nombre de la materia coincide")
                if self.__lista[i].getAprobado() == "P" and self.__lista[i].getNota() >= 7:
                    DniLista = self.__lista[i].getDocumento()
                encontrado=True
            else:

                i+=1

        return DniLista

    #Hacer el mismo codigo aprobado asi retorno la nota 
    def aprobadoNota(self,xnombre):
        i=0
        encontrado = False
        NotaLista = 0
        while i < len(self.__lista) and not encontrado:
            if self.__lista[i].getMateria() == xnombre:
                if self.__lista[i].getAprobado() == "P" and self.__lista[i].getNota() >= 7:
                    NotaLista = self.__lista[i].getNota()
                encontrado=True
            else:
                i+=1

        return NotaLista


    #Hacer el mismo codigo aprobado asi retorno la fecha
    def aprobadoFecha(self,xnombre):
        i=0
        encontrado = False
        FechaLista = 0
        while i < len(self.__lista) and not encontrado:
            if self.__lista[i].getMateria() == xnombre:
                if self.__lista[i].getAprobado() == "P" and self.__lista[i].getNota() >= 7:
                    FechaLista = self.__lista[i].getFecha()
                encontrado=True
            else:
                i+=1

        return FechaLista

