if __name__=='__main__':
    from claseEmail import Email
    import csv
    nombre = input("Ingrese su nombre: ")
    id = input("Ingrese el ID de su Email: ")
    dominio = input("Ingrese el dominio de su Email: ")
    tipodom = input("Ingrese el tipo de dominio de su Email: ")
    contra = input("Ingrese su contraseña: ")
    objeto = Email (id, dominio, tipodom, contra)
    print('Estimado {} te enviaremos tus mensajes a la direccion {}' .format(nombre, objeto.retornaEmail()))
    listaObjetos = []
    listaObjetos.append(objeto)
    contraseña1 = input("Ingrese su contraseña para poder cambiarla: ")
    objeto.cambioContraseña(contraseña1)
    newCorreo = input("ingrese la direccion de correo al que le desea crear un objeto: ")
    listaObjetos.append(listaObjetos[0].crearCuenta(newCorreo))
    
    archivo = open('C:\\Users\\juana manso\\Desktop\\Ejercicios python\\Ejercicio 1\\correos.csv')
    reader = csv.reader(archivo,delimiter=',')
    
    for correooo in reader:
        i=0
        while i <= 9:
            if objeto.verificarCorreo(correooo[i]) == 1:    
                listaObjetos.append(listaObjetos[0].crearCuenta(correooo[i]))
            else:
                print(f"Error, el correo: {correooo[i]} invalido ")
            i += 1
    for i in range(len(listaObjetos)):
        print(f"OBJETO CORREO {i+1}:")
        listaObjetos[i].mostrarDatos()
        
    domi = input("Ingrese el dominio a buscar: ")
    contador = 0
    for k in range(len(listaObjetos)):
        if listaObjetos[k].getDominio() == domi:
            contador += 1
    print(f"La cantidad de dominios iguales a {domi} es de: {contador}")