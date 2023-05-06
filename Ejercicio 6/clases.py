class Viajero:
    __numeroviajero=0
    __dni=""
    __nombre=""
    __apellido=""
    __millasacum=0

    def __init__(self,num,dni,nom,ap,millas):
        self.__numeroviajero=num
        self.__dni=dni
        self.__nombre=nom
        self.__apellido=ap
        self.__millasacum=millas
    def getnum(self):
        return self.__numeroviajero
    def getdoc(self):
        return self.__dni
    def getnom(self):
        return self.__nombre
    def getap(self):
        return self.__apellido
    def getmillas(self):
        return self.__millasacum
    def __gt__(self,otro):
        print("millas viajero actual{}  millas viajero siguiente{}".format(self.__millasacum,otro.getmillas()))
        if self.__millasacum > otro.getmillas():  
            r=True
        else:
            r=False
        return r
    def __add__(self,otro):
        return Viajero(self.__numeroviajero,self.__dni,self.__nombre,self.__apellido,self.__millasacum + otro)
    def __sub__(self,otro):
        return Viajero(self.__numeroviajero,self.__dni,self.__nombre,self.__apellido,self.__millasacum - otro)
