class ViajeroFrecuente:
    __num_viajero = 00
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas_acum = 00
    
    def __init__(self, numeroviajero, dniviajero, nombreviajero, apellidoviajero, millasacumviajero = 0):
        self.__num_viajero = numeroviajero
        self.__dni = dniviajero
        self.__nombre = nombreviajero
        self.__apellido = apellidoviajero
        self.__millas_acum = millasacumviajero
        
    def numero(self):
        return self.__num_viajero
    
    def nombree(self):
        return self.__nombre
    
    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    def acumularMillas(self, nuevasmillas):
        self.__millas_acum += nuevasmillas
        return self.__millas_acum
    
    def canjearMillas (self, millasAcanjear):
        if self.__millas_acum >= millasAcanjear:
            self.__millas_acum -= millasAcanjear
        else:
            print("Error, no tiene suficientes millas")
        return self.__millas_acum
