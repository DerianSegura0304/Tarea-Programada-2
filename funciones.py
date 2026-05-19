#Elaborado por: Derian Segura y Juan Gonzalez
#Fecha de creacion: 16/05/2026 19:00
#Ultima modificacion: 
#Version 3.14.3

#importaciones
import re
import tkinter as tk

#funciones

def volverMenu(ventanaActual, ventanaMenu):
    ventanaActual.destroy()
    ventanaMenu.deiconify()

def insertarDonador(ventanaMenu, anchoVentana, altoVentana, posicionX, posicionY):
    ventanaMenu.withdraw()
    ventanaIngresarDon = tk.Toplevel()
    ventanaIngresarDon.title("Sistema de Banco de Sangre")
    ventanaIngresarDon.geometry(f"{anchoVentana}x{altoVentana}+{posicionX}+{posicionY}")

    mensIngresarDonador = tk.Label(ventanaIngresarDon,
                                      text="Insertar Donador",
                                      font=("Arial", 12))
    mensIngresarDonador.place(x=340, y=30)







    mensCedula = tk.Label(ventanaIngresarDon,
                          text="Digite su cedula de la siguiente manera: #-####-####:")
    mensCedula.place(x=98, y=70)

    mensCedulaValidacion = tk.Label(ventanaIngresarDon, 
                            text="", 
                            font=("Arial", 10))
    mensCedulaValidacion.place(x=265, y=90)






    mensNombre = tk.Label(ventanaIngresarDon,
                             text="Digite su nombre:")
    mensNombre.place(x=98, y=118)

    mensNombreValidacion = tk.Label(ventanaIngresarDon, 
                            text="", 
                            font=("Arial", 10))
    mensNombreValidacion.place(x=265, y=138)





    mensFechaNacimiento = tk.Label(ventanaIngresarDon,
                             text="Digite fecha de nacimiento de la siguiente manera: DD/MM/AAAA:")
    mensFechaNacimiento.place(x=98, y=168)

    mensFechaNacValidacion = tk.Label(ventanaIngresarDon, 
                            text="", 
                            font=("Arial", 10))
    mensFechaNacValidacion.place(x=265, y=188)







    cedula = ingresarCedula(ventanaIngresarDon, mensCedulaValidacion)
    nombreDon = ingresarNombre(ventanaIngresarDon, mensNombreValidacion)
    fechaNamiento = ingresarFechaNac(ventanaIngresarDon, mensFechaNacValidacion)









def ingresarCedula(ventanaIngresarDon, mensCedulaValidacion):
    cedulaDonador = tk.Entry(ventanaIngresarDon,
                         font=("Arial", 11))
    cedulaDonador.place(x=100, y=92)
    cedulaDonador.bind("<KeyRelease>", lambda cedula: validarCedula(cedula, mensCedulaValidacion))
    return cedulaDonador

def validarCedula(cedula, mensCedulaValidacion):
    cedula = cedula.widget.get()
    if re.match("^[1-7]{1}-\\d{4}-\\d{4}$", cedula):
        mensCedulaValidacion.config(text="Cedula valida",
                                    foreground="green")
    else:
        mensCedulaValidacion.config(text="Cedula invalida. debe estar escrita como en el ejemplo y solo datos caracteres numericos",
                                    foreground="red")





def ingresarNombre(ventanaIngresarDon, mensNombreValidacion):
    nombreDonador = tk.Entry(ventanaIngresarDon,
                         font=("Arial", 11))
    nombreDonador.place(x=100, y=140)
    nombreDonador.bind("<KeyRelease>", lambda nombre: validarNombre(nombre, mensNombreValidacion))
    return nombreDonador

def validarNombre(nombre, mensNombreValidacion):
    nombre = nombre.widget.get()
    nombre = nombre.title()
    if re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]+$", nombre):
        mensNombreValidacion.config(text="Nombre valido",
                                    foreground="green")
    else:
        mensNombreValidacion.config(text="Nombre invalido. Su nombre debe estar conformado solo por letras",
                                    foreground="red")





def ingresarFechaNac(ventanaIngresarDon, mensFechaNacValidacion):
    fechaNacDonador = tk.Entry(ventanaIngresarDon,
                         font=("Arial", 11))
    fechaNacDonador.place(x=100, y=190)
    fechaNacDonador.bind("<KeyRelease>", lambda fechaNac: validarFechaNac(fechaNac, mensFechaNacValidacion))
    return fechaNacDonador

def validarFechaNac(fechaNac, mensFechaNacValidacion):
    fechaNac = fechaNac.widget.get()

    if not re.match("^\\d{2}/\\d{2}/\\d{4}$", fechaNac):
        mensFechaNacValidacion.config(text="Fecha invalida. el formato debe ser DD/MM/AAAA",
                                      foreground="red")
        return None
    fechaNac = fechaNac.split("/")
    diaNac = fechaNac[0]
    MesNac = fechaNac[1]
    annoNac = fechaNac[2]
    diaNacInt = int(diaNac)
    MesNacInt = int(MesNac)
    annoNacInt = int(annoNac)

    if MesNacInt <= 12 and MesNacInt >= 1:
        if MesNac in "01030507081012":
            if diaNacInt <= 31 and diaNacInt >= 1:
                mensFechaNacValidacion.config(text="Fecha valida",
                                              foreground="green")
        elif MesNac == "02":
            esBisiesto = (annoNacInt % 4 == 0 and annoNacInt % 100 != 0) or (annoNacInt % 400 == 0)
            if esBisiesto == True and 1 <= diaNacInt and diaNacInt <= 29:
                mensFechaNacValidacion.config(text="Fecha valida",
                                              foreground="green")
                
            elif esBisiesto == False and 1 <= diaNacInt and diaNacInt <= 28:
                mensFechaNacValidacion.config(text="Fecha valida",
                                              foreground="green")
            else:
                mensFechaNacValidacion.config(text="Fecha invalida. Verifique que su fecha de nacimiento este escrita de forma correcta",
                                              foreground="red")
    else:
        if diaNacInt <= 30 and diaNacInt >= 1:
            mensFechaNacValidacion.config(text="Fecha valida",
                                              foreground="green")
        else:
            mensFechaNacValidacion.config(text="Fecha invalida. Verifique que su fecha de nacimiento este escrita de forma correcta",
                                              foreground="red")