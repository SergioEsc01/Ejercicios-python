class Email:
    idCuenta = ""
    dominio = ""
    tipoDominio = ""
    contraseña = ""
    
    def __init__(self, id, dom, tipodom, contraseña = "contraseña"):
        self.idCuenta = id
        self.dominio = dom
        self.tipoDominio = tipodom
        self.contraseña = contraseña

    def retornaEmail(self):     
        return self.idCuenta + "@" + self.dominio + "." + self.tipoDominio
    def getDominio(self):
        return self.dominio
        
    def crearCuenta(self, emailnuevo):
        cadena1 = emailnuevo.split("@")
        id = cadena1[0]
        cadena2 = cadena1[1].split(".")
        dominio = cadena2[0]
        tipodom = cadena2 [1]
        nuevoObjeto = Email(id, dominio, tipodom)
        return nuevoObjeto
    
    
    def mostrarDatos(self):
        print('id: {} \n dominio: {} \n tipo del dominio: {} \n contraseña: {}' .format(self.idCuenta, self.dominio, self.tipoDominio, self.contraseña))
    
    def cambioContraseña(self, contra):
        if (self.contraseña == contra):
            self.contraseña = input("Ingrese la nueva contraseña ")
            print("Se realizo correctamente el cambio")
        else:
            print("Error, las contraseñas no coinciden")
            
    def verificarCorreo(self, correo):
        if '@' in correo and '.' in correo:
            r = 1
        else:
            r = 0
        return r
            
            
               



    