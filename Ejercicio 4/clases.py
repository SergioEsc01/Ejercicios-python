class Ventana:
    __titulo=""
    __ejexsi=0
    __ejeysi=0
    __ejexid=500
    __ejeyid=500
    def __init__(self,tit,exsi=0,eysi=0,exid=500,eyid=500):
        if exsi < exid and eysi < eyid:
            self.__titulo=tit
            self.__ejexsi=exsi
            self.__ejeysi=eysi
            self.__ejexid=exid
            self.__ejeyid=eyid
        else:
            print("Datos erroneos")
    def getTitulo(self):
        return self.__titulo
    def getejexsi(self):
        return self.__ejexsi
    def getejeysi(self):
        return self.__ejeysi
    def getejexid(self):
        return self.__ejexid
    def getejeyid(self):
        return self.__ejeyid
    def mostrar(self):
        print("Titulo: {}\nEjex sup izq: {}\nEje y sup izq: {}\nEje x inf der:{}\nEje y inf der: {}".format(self.__titulo,self.__ejexsi,self.__ejeysi,self.__ejexid,self.__ejeyid))
    def alto(self):
        return self.__ejexid-self.__ejexsi
    def ancho(self):
        return self.__ejeyid-self.__ejeysi
    def moverDerecha(self,cant=1):
        if self.__ejexid+cant<=500:
            self.__ejexsi+=cant
            self.__ejexid+=cant
        else:
            print("No se puede mover {} {} a la derecha".format(self.__titulo,cant))
    def moverIzquierda(self,cant=1):
        if self.__ejexid-cant>=0:
            self.__ejexsi-=cant
            self.__ejexid-=cant
        else:
            print("No se puede mover {} {} a la izquierda".format(self.__titulo,cant))
    def bajar(self,cant=1):
        if self.__ejeyid+cant<=500:
            self.__ejeysi+=cant
            self.__ejeyid+=cant
        else:
            print("La ventana {} no se puede bajar {}".format(self.__titulo,cant))
    def subir(self,cant=1):
        if self.__ejeyid-cant>=500:
            self.__ejeysi-=cant
            self.__ejeyid-=cant
        else:
            print("La ventana {} no se puede subir {}".format(self.__titulo,cant))
