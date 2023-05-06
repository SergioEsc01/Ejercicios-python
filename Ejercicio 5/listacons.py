from clases import planAhorro
class listaVehiculos:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def carga(self,cod,mod,ver,pre,cc,ccap):
        newplan=planAhorro(int(cod),mod,ver,float(pre),int(cc),int(ccap))
        self.__lista.append(newplan)
    def muestra(self):
        for vehiculo in self.__lista:
            cod=vehiculo.getcod()
            mod=vehiculo.getmod()
            ver=vehiculo.getver()
            print("Codigo del plan:{}\nModelo del vehiculo:{}\nVersion del vehiculo:{}".format(cod,mod,ver))
            valor=float(input("Ingrese el valor del vehiculo para poder modificarlo\n"))
            vehiculo.modvalor(valor)
    def muestrainferior(self,valorx):
        for vehiculo in self.__lista:
            impcuota=float(vehiculo.valorcuota(vehiculo.getpre()))
            if impcuota < valorx:
                cod=vehiculo.getcod()
                mod=vehiculo.getmod()
                ver=vehiculo.getver()
                print("Plan con valor de cuota inferior al ingresado:\nCodigo del plan:{}\nModelo del vehiculo:{}\nVersion del vehiculo:{}\n".format(cod,mod,ver))
            else:
                print("No hay ningun plan con un valor de la cuota sea inferior al ingresado\n")
    def muestracuotaslic(self):
        for vehiculo in self.__lista:
            cod=vehiculo.getcod()
            mod=vehiculo.getmod()
            ver=vehiculo.getver()
            print("Codigo del plan:{}\nModelo del vehiculo:{}\nVersion del vehiculo:{}".format(cod,mod,ver))
            tot=vehiculo.cantlicitar(vehiculo.getpre())
            print("El monto que se debe haber pagado para licitar el vehiculo es de:{}\n".format(tot))
    def cambiavalor(self,cod):
        for vehiculo in self.__lista:
            if cod==vehiculo.getcod():
                 num=int(input("Ingrese el valor a modificar\n"))
                 print("Valor antes de modificar: {}".format(vehiculo.getccap()))
                 
                 vehiculo.modclic(num)
                 print("Valor despues de modificar: {}".format(vehiculo.getccap()))
        