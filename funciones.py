#Elaborado por: Derian Segura y Juan Gonzalez
#Fecha de creacion: 16/05/2026 19:00
#Ultima modificacion: 
#Version 3.14.3

#importaciones
import re
import pickle
import tkinter as tk
from datetime import datetime

#funciones
#validaciones para datos cargados
def validarNombreCompletoBD(pNombre):
    if isinstance(pNombre, list) and len(pNombre) == 3:
        if isinstance(pNombre[0], str) and isinstance(pNombre[1], str) and isinstance(pNombre[2], str):
            nombre = pNombre[0]+" "+pNombre[1]+" "+pNombre[2]
            nombre = nombre.title()
            if re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]+$", nombre):
                return True
    return False
def validarCedulaBD(pCedula):
    if isinstance(pCedula, str):
        if re.match("^[1-7]{1}-\\d{4}-\\d{4}$", pCedula):
            return True
    return False
def validarTSangreBD(pSangre):
    if pSangre in [1,2,3,4,5,6,7,8]:
        return True
    return False
def validarSexoBD(pSexo):
    if isinstance(pSexo, bool):
        return True
    return False
def validarEdad(pFecha):
    fecha1 = datetime(pFecha[2], pFecha[1], pFecha[0])
    fecha2 = datetime.now()
    edad = fecha2.year - fecha1.year
    if (fecha2.month, fecha2.day) < (fecha1.month, fecha1.day):
        edad -= 1
    if edad >= 18 and edad < 65:
        return True
    return False
def formatoFechaBD(diaNac,mesNac,annoNac):
    if isinstance(diaNac, int) and isinstance(mesNac, int) and isinstance(annoNac, int):
        if diaNac < 10:
            dia = f"0{diaNac}"
        else:
            dia = f"{diaNac}"
        if mesNac < 10:
            mes = f"0{mesNac}"
        else:
            mes = f"{mesNac}"
        anno = f"{annoNac}"
    elif isinstance(diaNac, str) and isinstance(mesNac, str) and isinstance(annoNac, str):
        if len(diaNac) == 1:
            dia = f"0{diaNac}"
        else:
            dia = f"{diaNac}"
        if len(mesNac) == 1:
            mes = f"0{mesNac}"
        else:
            mes = f"{mesNac}"
        anno = f"{annoNac}"
    else:
        return False
    return f"{dia}/{mes}/{anno}",dia,mes,anno
def validarFechaNacBD(pFechaNac):
    if isinstance(pFechaNac, tuple):
        diaNac = pFechaNac[0]
        mesNac = pFechaNac[1]
        annoNac = pFechaNac[2]
        fechaNac,dia,mes,anno = formatoFechaBD(diaNac,mesNac,annoNac)
        if not re.match("^\\d{2}/\\d{2}/\\d{4}$", fechaNac):
            return False
        if mes in ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]:
            diaNacInt = int(dia)
            mesNacInt = int(mes)
            annoNacInt = int(anno)
            fechaNacInt = (diaNacInt,mesNacInt,annoNacInt)
            estado = False
            if mes in ["01", "03", "05", "07", "08", "10", "12"]:
                if diaNacInt <= 31 and diaNacInt >= 1:
                    estado = validarEdad(fechaNacInt)
            elif mes in ["04", "06", "09", "11"]:
                if diaNacInt <= 30 and diaNacInt >= 1:
                    estado = validarEdad(fechaNacInt)
            elif mes == "02":
                esBisiesto = (annoNacInt % 4 == 0 and annoNacInt % 100 != 0) or (annoNacInt % 400 == 0)
                if esBisiesto == True and 1 <= diaNacInt and diaNacInt <= 29:
                    estado = validarEdad(fechaNacInt)
                elif esBisiesto == False and 1 <= diaNacInt and diaNacInt <= 28:
                    estado = validarEdad(fechaNacInt)
            if estado:
                return True
        return False
def validarPesoBD(pPeso):
    if isinstance(pPeso, float):
        if pPeso > 50 and pPeso < 120:
            return True
    return False
def validarCorreoBD(pCorreo):
    if isinstance(pCorreo, str):
        patron = r"^[a-zA-Z0-9._%+-]+@(costarricense\.cr|racsa\.go\.cr|ccss\.sa\.cr|gmail+\.com)$"
        if re.match(patron, pCorreo):
            return True
    return False
def validarTelBD(pTel):
    if isinstance(pTel, str):
        patron = r"^\d{4}-\d{4}$"
        if re.match(patron, pTel) and pTel[0] not in "0135":
            return True
    return False
def validarEstadoBD(pEstado):
    if pEstado in [0,1]:
        return True
    return False
def validarJustificacionBD(pJust):
    if pJust in [0,1,2,3,4,5,6,7]:
        return True
    return False
def validarBD(bdDonadores):
    if isinstance(bdDonadores, list):
        validos = 0
        invalidos = 0
        temp = []
        for donador in bdDonadores:
            if isinstance(donador, list) and len(donador) == 10:
                if validarNombreCompletoBD(donador[0]) and validarCedulaBD(donador[1]) and validarTSangreBD(donador[2]) and validarSexoBD(donador[3]) and validarFechaNacBD(donador[4]):
                    if validarPesoBD(donador[5]) and validarCorreoBD(donador[6]) and validarTelBD(donador[7]) and validarEstadoBD(donador[8]) and validarJustificacionBD(donador[9]):
                        fecha = donador[4]
                        fecha = (f"{fecha[0]}",f"{fecha[1]}",f"{fecha[2]}")
                        datos = [donador[0],donador[1],donador[2],donador[3],fecha,donador[5],donador[6],donador[7],donador[8],donador[9]]
                        temp.append(datos)
                        validos += 1
                    else:
                        invalidos += 1
                else:
                    invalidos += 1
            else:
                invalidos += 1
        print(f"Válidos: {validos} - Invalidos: {invalidos}")
        bdDonadores = temp
        return bdDonadores
    return False
#Cargar base de datos
def cargarDonadores():
    try:
        with open("bdDonadores.txt", "rb") as f:
            bdDonadores = pickle.load(f)
            print("Base de datos cargada")
            # print(bdDonadores)
            print()
            print("Base de datos limpiada")
            bdDonadores = validarBD(bdDonadores)
        return bdDonadores
    except:
        print("Se ha inicializado la base de datos")
        return [[]]
#Guardar base de datos
def guardarDonadores(bdDonadores):
    with open("bdDonadores.txt", "wb") as f:
        pickle.dump(bdDonadores, f)
        print("Base de datos guardada")
        # print(bdDonadores)
    return
#Ventana de Menu
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
    # MesNacInt = int(MesNac)
    annoNacInt = int(annoNac)
    if MesNac in ["01","02","03","04","05","06","07","08","09","10","11","12"]:
        if MesNac in ["01","03","05","07","08","10","12"]:
            if diaNacInt <= 31 and diaNacInt >= 1:
                mensFechaNacValidacion.config(text="Fecha valida",
                                              foreground="green")
        elif MesNac in ["04","06","09","11"]:
            if diaNacInt <= 30 and diaNacInt >= 1:
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
            mensFechaNacValidacion.config(text="Fecha invalida. Verifique que su fecha de nacimiento este escrita de forma correcta",
                                              foreground="red")