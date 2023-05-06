from manejadorAlumnos import Alumno
class Materias:
    __dni= 0
    __nombre=''
    __fecha=''
    __nota=''
    __aprobado=''

    def __init__(self,dni,nombre,fecha,nota,apr):

        self.__dni=int (dni)
        self.__nombre=nombre
        self.__fecha=fecha
        self.__nota=nota
        self.__aprobado=apr

        print("Documento: {}".format(self.__dni))
        print("Nombre: {}".format(self.__nombre))
        print("Fecha: {}".format(self.__fecha))
        print("Nota: {}".format(self.__nota))
        print("Aprobado: {}".format(self.__aprobado))

    def getDocumento(self):
        return self.__dni

    def getMateria(self):
        return self.__nombre
    
    def getNota(self):
        return self.__nota
    
    def getAprobado(self):
        return self.__aprobado

    def getFecha(self):
        return self.__fecha
    