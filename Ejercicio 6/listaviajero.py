from clases import Viajero
class listaV:
    __lista=[]

    def __init__(self):
        self.__lista=[]
    def carga(self,id,dni,nom,ap,millas):
        newV=Viajero(id,dni,nom,ap,millas)
        self.__lista.append(newV)
    def muestravmayor(self):
        c=0
        while c < len(self.__lista):
            if c==(len(self.__lista)-1) and self.__lista[c].getmillas() > self.__lista[0].getmillas():
                print("El viajero {} tiene mas millas que el viajero incial {}".format(self.__lista[c].getnum(),self.__lista[0].getnum()))
                c+=1
            elif self.__lista[c].getmillas() > self.__lista[c+1].getmillas():
                print("El viajero {} tiene mas millas que el viajero {}".format(self.__lista[c].getnum(),self.__lista[c+1].getnum()))
                c+=1
            else:
                print("El viajero {} no tiene ms mills que el viajero {}".format(self.__lista[c].getnum(),self.__lista[c+1].getnum()))
                c +=1
    def acummillas(self,valor2):
        c=0
        while c < len(self.__lista):
            id=self.__lista[c].getnum()
            doc=self.__lista[c].getdoc()
            nom=self.__lista[c].getnom()
            ap=self.__lista[c].getap()
            valor=self.__lista[c].getmillas()
            v=Viajero(id,doc,nom,ap,valor)
            v= v + valor2
            c+=1
            print("Instancia de la clase Viajero id:{}\ndni{}\nnombre{}\napellido{}\nmillas{}\n".format(v.getnum(),v.getdoc(),v.getnom(),v.getap(),v.getmillas()))
    def restamillas(self,valor2):
        c=0
        while c < len(self.__lista):
            id=self.__lista[c].getnum()
            doc=self.__lista[c].getdoc()
            nom=self.__lista[c].getnom()
            ap=self.__lista[c].getap()
            valor=self.__lista[c].getmillas()
            v=Viajero(id,doc,nom,ap,valor)
            v= v - valor2
            c+=1
            print("Instancia de la clase Viajero id:{}\ndni{}\nnombre{}\napellido{}\nmillas{}\n".format(v.getnum(),v.getdoc(),v.getnom(),v.getap(),v.getmillas()))