class planAhorro:
    #creo que son variables de clase
    __cantcuotas=70
    __cantcuolic=10

    def __init__(self,cod,mod,ver,pre,cc,ccap):
        self.__codplan=cod
        self.__mod=mod
        self.__version=ver
        self.__precio=pre
        #print("{}{}{}{}{}{}".format(self.__codplan,self.__mod,self.__version,self.__precio,self.__cantcuotas,self.__cantcuolic))
    def getcod(self):
        return self.__codplan
    def getmod(self):
        return self.__mod
    def getver(self):
        return self.__version
    def getpre(self):
        return self.__precio
    @classmethod
    def getcc(cls):
        return cls.__cantcuotas
    @classmethod
    def getccap(cls):
        return cls.__cantcuolic
    def modvalor(self,valor):
        self.__precio=valor
    @classmethod
    def valorcuota(cls,pre):
        total=(pre / cls.__cantcuotas) + pre * 0.10
        return total
    @classmethod
    def cantlicitar(cls,valor):
        tot= cls.__cantcuolic * cls.valorcuota(valor)
        return tot
    @classmethod
    def modclic(cls,valor):
        cls.__cantcuolic=valor