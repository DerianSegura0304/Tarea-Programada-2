#Elaborado por: Derian Segura y Juan Gonzalez
#Fecha de creacion: 16/05/2026 19:00
#Ultima modificacion: 
#Version 3.14.3

#importaciones
import re
import pickle
import random
import tkinter as tk
from tkinter.ttk import *
from datetime import datetime
from tkinter import messagebox

#funciones
def actualizarBotones(opcActualizarDatosDonador, opcEliminarDonador, opcReportes):
        try: 
            with open("bdDonadores.txt", "rb") as archivo:
                contenido = archivo.read()
            if len(contenido.strip()) == 0:
                opcActualizarDatosDonador.config(state = "disabled")
                opcEliminarDonador.config(state = "disabled")
                opcReportes.config(state = "disabled")
            else:
                opcActualizarDatosDonador.config(state = "normal")
                opcEliminarDonador.config(state = "normal")
                opcReportes.config(state = "normal")
        except:
            opcActualizarDatosDonador.config(state = "disabled")
            opcEliminarDonador.config(state = "disabled")
            opcReportes.config(state = "disabled")

def dimensionarVentana(ventanaMenu):
    anchoPantalla = ventanaMenu.winfo_screenwidth()
    altoPantalla = ventanaMenu.winfo_screenheight()
    anchoVentana = 800
    altoVentana = 600
    posicionX = round((anchoPantalla / 2) - (anchoVentana / 2))
    posicionY = round((altoPantalla / 2) - (altoVentana / 2))
    ventanaMenu.geometry(f"{anchoVentana}x{altoVentana}+{posicionX}+{posicionY}")
    return anchoVentana, altoVentana, posicionX, posicionY
def asignarProvinciasHospitales(provinciaNac):
    diccHospi = {"1":["El Banco Nacional de Sangre","Hospital Mëxico","Hospital San Juan de Dios"],
                "2":["Hospital San Rafael de Alajuela","Hospital de San Ramón","Hospital del Cantón Norteño"],
                "3":["Hospital Max Peralta"],
                "4":["Hospital San Vicente de Paúl"],
                "5":["Hospital La Anexión en Nicoya","Hospital Enrique Baltodano de Liberia"],
                "6":["Hospital Monseñor Sanabria"],
                "7":["Hospital Tony Facio","Hospital de Guápiles"],
                "8":["El Banco Nacional de Sangre","Hospital Mëxico","Hospital San Juan de Dios"],
                "9":["El Banco Nacional de Sangre","Hospital Mëxico","Hospital San Juan de Dios"]}
    diccProv = {"1":"San José", "2":"Alajuela", "3":"Cartago",
                "4":"Heredia", "5":"Guanacaste", "6":"Puntarenas",
                "7":"Limón", "8": "Nacionalizado", "9": "Nacido en el extranjero"}
    prov = diccProv[provinciaNac] 
    hospi = diccHospi[provinciaNac]
    return prov, hospi

justificaciones = {0:"N/A",1:"Enfermedades Infecciosas/Crónicas", 3:"Conductas de Riesgo",4:"Factores de Salud Física",
                   5:"Procedimientos Médicos",6:"Uso de medicamentos",7:"Situaciones Específicas"}

def mostrarInformacionSangre(tipoSangreInt):
    infoTipoSangre = {1: "O-: Se les recomienda donar glóbulos rojos dobles y sangre entera",
                      2: "O+: Se les recomienda donar glóbulos rojos dobles y sangre entera.",
                      3: "A-: Se les recomienda que donen sangre entera y glóbulos rojos dobles.",
                      4: "A+: Se les recomienda que donen sangre entera y plaquetas.",
                      5: "B-: Se les recomienda que donen sangre entera o plaquetas.",
                      6: "B+: Se les recomienda que donen sangre entera y de glóbulos rojos dobles.",
                      7: "AB-: Se les recomienda donar plaquetas y plasma.",
                      8: "AB+: Se les recomienda hacer donaciones de plaquetas y de plasma."}
    infoSangreDonador = infoTipoSangre[tipoSangreInt]
    return infoSangreDonador
    
def registrarDonador(ventanaIngresarDon, anchoVentana, altoVentana, posicionX, posicionY, cedulaStr, nombreLista, fechaNacTupla, tipoSangreInt, sexoBool, pesoFloat, telefonoStr, correoStr, bdDonadores, ventanaMenu, opcActualizarDatosDonador, opcEliminarDonador, opcReportes):
    ventanaIngresarDon.withdraw()
    ventanaResultadoRegistarDon = tk.Toplevel()
    ventanaResultadoRegistarDon.title("Sistema de Banco de Sangre")
    ventanaResultadoRegistarDon.geometry(f"{anchoVentana}x{altoVentana}+{posicionX}+{posicionY}")
    sexoBool = sexoBool.get()
    if sexoBool == "Masculino":
        sexoBool = True
    else:
        sexoBool = False
    botRegresar = tk.Button(ventanaResultadoRegistarDon,
                                   cursor="Hand2",
                                   text="Regresar",
                                   relief="groove",
                                   font=("Arial", 11),
                                   command=lambda: volverMenu(ventanaResultadoRegistarDon, ventanaMenu))
    botRegresar.place(x=370, y=500)

    if validarFechaNacBD(fechaNacTupla):
        mensFechaResultado = tk.Label(ventanaResultadoRegistarDon,
                                    text="Dado su fecha de nacimiento usted ya puede ser donador",
                                    font=("Arial", 12))
        mensFechaResultado.place(x=98, y=70)
        if pesoFloat > 50:
            if pesoFloat < 120:
                mensPesoResultado = tk.Label(ventanaResultadoRegistarDon,
                                    text="Y usted posee un peso adecuado, correcto para ser donador de sangre.",
                                    font=("Arial", 12))
                mensPesoResultado.place(x=98, y=110)
                provinciaNac = cedulaStr[0]
                prov, listaHospi = asignarProvinciasHospitales(provinciaNac)
                if len(listaHospi) == 1:
                    hospi = listaHospi[0]
                elif len(listaHospi) == 2:
                    hospi = " y ".join(listaHospi)
                else:
                    hospi = ", ".join(listaHospi[:-1]) + " y " + listaHospi[-1]
                if provinciaNac in ["1","2","3","4","5","6","7"]:
                    mensLugarDonacion = tk.Label(ventanaResultadoRegistarDon,
                                                text=f"Dado que usted nacio en la provincia de {prov},\nusted podria donar en:\n{hospi}.",
                                                font=("Arial", 12),
                                                justify="left")
                    mensLugarDonacion.place(x=98, y=150)
                else:
                    mensEspecial = tk.Label(ventanaResultadoRegistarDon,
                                                text=f"Dado que usted es {prov},\nusted podria donar en: {hospi}",
                                                font=("Arial", 12),
                                                justify="left")
                    mensEspecial.place(x=98, y=150)

                infoSangreDonador = mostrarInformacionSangre(tipoSangreInt)
                mensConozcaSuSangre = tk.Label(ventanaResultadoRegistarDon,
                                                text=f"{infoSangreDonador}",
                                                font=("Arial", 11))
                mensConozcaSuSangre.place(x=98, y=225)

                if tipoSangreInt in [3,4]:
                    mensLugarDonacion = tk.Label(ventanaResultadoRegistarDon,
                                                text="Como su tipo de sangre es A, le recomendamos ver el video:\nParticularidades de la sangre tipo A: Responde diferente al estrés según la ciencia.\nLink: SE NECESITA INVESTIGAR CUAL ES",
                                                font=("Arial", 11),
                                                justify="left")
                    mensLugarDonacion.place(x=98, y=250)

                bdDonadores[cedulaStr] = [nombreLista, tipoSangreInt, sexoBool, fechaNacTupla, pesoFloat, correoStr, telefonoStr, 1, 0]
                guardarDonadores(bdDonadores)
                actualizarBotones(opcActualizarDatosDonador, opcEliminarDonador, opcReportes)
                print(bdDonadores)

            
            else:
                mensPesoResultado = tk.Label(ventanaResultadoRegistarDon,
                                    text="Pero, dado su sobre peso, no es posible donar sangre.",
                                    font=("Arial", 12))
                mensPesoResultado.place(x=98, y=110)
        else:
            mensPesoResultado = tk.Label(ventanaResultadoRegistarDon,
                                    text="Pero, usted debe pesar mas de 50 kgms para poder ser donador.",
                                    font=("Arial", 12))
            mensPesoResultado.place(x=98, y=110)
    else:
        mensFechaResultado = tk.Label(ventanaResultadoRegistarDon,
                                text="Dado su fecha de nacimiento usted aun no puede ser donador.",
                                font=("Arial", 12))
        mensFechaResultado.place(x=98, y=70)



def eliminarDonadorAux(ventanaMenu, anchoVentana, altoVentana, posicionX, posicionY, bdDonadores):
    ventanaMenu.withdraw()
    ventanaEliminarDonador = tk.Toplevel()
    ventanaEliminarDonador.title("Sistema de Banco de Sangre")
    ventanaEliminarDonador.geometry(f"{anchoVentana}x{altoVentana}+{posicionX}+{posicionY}")
    mensCedula = tk.Label(ventanaEliminarDonador,
                          text="Digite su cedula de la siguiente manera: Ej: 1-2345-6789: ")
    mensCedula.place(x=98, y=70)
    mensCedulaValidacion = tk.Label(ventanaEliminarDonador, 
                            text="", 
                            font=("Arial", 10))
    mensCedulaValidacion.place(x=265, y=90)
    cedula = ingresarCedula(ventanaEliminarDonador, mensCedulaValidacion)
    

    botBuscarCedula = tk.Button(ventanaEliminarDonador,
                                   cursor="Hand2",
                                   text="Buscar Cedula",
                                   relief="groove",
                                   font=("Arial", 11),
                                   command=lambda: buscarCedulaEliminar(cedula, bdDonadores, ventanaEliminarDonador, botBuscarCedula))
    botBuscarCedula.place(x=270, y=500)

    botRegresar = tk.Button(ventanaEliminarDonador,
                            cursor="Hand2",
                            text="Regresar",
                            relief="groove",
                            font=("Arial", 11),
                            command=lambda: volverMenu(ventanaEliminarDonador, ventanaMenu))
    botRegresar.place(x=410, y=500)


def definirJustificacion(justificacionStr):
    diccJustificaciones = {"Enfermedades Infecciosas/Crónicas": 1 ,
                           "Conductas de Riesgo": 2,
                           "Factores de Salud Física": 3,
                           "Procedimientos Médicos": 4,
                           "Uso de Medicamentos": 5,
                           "Estilo de Vida y Viajes": 6,
                           "Situaciones Específicas": 7}
    numJustificacion = diccJustificaciones[justificacionStr]
    return numJustificacion


def buscarCedulaEliminar(cedula, bdDonadores, ventanaEliminarDonador, botEliminarDonador):
    cedulaStr = cedula.get()
    cedulaValidada = validarExistenciaCedula(cedulaStr, bdDonadores)
    if cedulaValidada != 1:
        if cedulaValidada !=2:
            mensCedulaEncontrada = tk.Label(ventanaEliminarDonador,
                                text="Se encontro la cedula en el sistema\nSeleccione la justificacion de la eliminacion",
                                justify="left")
            mensCedulaEncontrada.place(x=98, y=120)
            comboBoxJustificacion = Combobox(ventanaEliminarDonador)
            comboBoxJustificacion['values'] = ("Enfermedades Infecciosas/Crónicas","Conductas de Riesgo","Factores de Salud Física","Procedimientos Médicos","Uso de Medicamentos","Estilo de Vida y Viajes","Situaciones Específicas")
            comboBoxJustificacion.place(x=98, y=160)


            botEliminarDonador.config(text="Confirmar Borrado",
                                      command=lambda: confirmarEliminacion(cedulaStr, comboBoxJustificacion, bdDonadores, ventanaEliminarDonador))
        else:
            messagebox.showerror("Cedula inexistente", f"La persona con el número de cédula: {cedulaStr}\nno está registrado en la base de datos del Banco de Sangre aún.")
            return
    else:
        messagebox.showerror("Cedula Invalida", "Verifique que esta escrita de la siguiente manera: Ej: 1-2345-6789.")
        return
    

def confirmarEliminacion(cedulaStr, comboBoxJustificacion, bdDonadores, ventanaEliminarDonador):
    justificacionSeleccionada = comboBoxJustificacion.get()
    if justificacionSeleccionada == "":
        messagebox.showerror("Faltan Datos", "No puede dejar datos en blanco")
        return
            
    respuesta = messagebox.askokcancel("Confirmar Acción", "¿Está seguro de que desea realizar esta acción?")
    if respuesta:  
        bdDonadores = eliminarDonador(cedulaStr, bdDonadores)
        mensCedula = tk.Label(ventanaEliminarDonador,
                        text="Donador eliminado satisfactoriamente")
        mensCedula.place(x=98, y=186)
        numJustificacion = definirJustificacion(justificacionSeleccionada)
        bdDonadores = asignarJustificacion(cedulaStr, bdDonadores, numJustificacion)
        print(bdDonadores)
        return bdDonadores
    else:
        mensCedula = tk.Label(ventanaEliminarDonador,
                                text="Donador NO eliminado")
        mensCedula.place(x=98, y=186)


def asignarJustificacion(cedulaStr, bdDonadores, numJustificacion):
    datos = bdDonadores[cedulaStr]
    datos[-1] = numJustificacion
    bdDonadores[cedulaStr] = datos
    return bdDonadores

def eliminarDonador(cedulaStr, bdDonadores):
    datos = bdDonadores[cedulaStr]
    datos[-2] = 0
    bdDonadores[cedulaStr] = datos
    return bdDonadores

def validarExistenciaCedula(cedulaStr, bdDonadores):
    while True:
        if not validarCedulaBD(cedulaStr):
            return 1
        if cedulaStr not in bdDonadores:
            return 2
        print("Cedula existente.")
        return cedulaStr

def formatoFechaNacIngresarDon(fechaNac):
    if not re.match("^\\d{2}/\\d{2}/\\d{4}$", fechaNac):
        return False
    return True

def registrarDonadorAux(ventanaIngresarDon, anchoVentana, altoVentana, posicionX, posicionY, cedula, nombre, fechaNac, tipoSangre, sexoBool, peso, telefono, correo, bdDonadores, ventanaMenu, opcActualizarDatosDonador, opcEliminarDonador, opcReportes):
    cedulaStr = cedula.get()
    nombreStr = nombre.get()
    tipoSangreStr = tipoSangre.get()
    telefonoStr = telefono.get()
    correoStr = correo.get()
    dicTipoSangre = {"O-": 1, "O+": 2,
                     "A-": 3, "A+": 4,
                     "B-": 5, "B+": 6,
                     "AB-": 7, "AB+": 8}
    tipoSangreInt = dicTipoSangre.get(tipoSangreStr)
    nombreLista = nombreStr.strip().split(" ")
    fechaNacStr = fechaNac.get()
    partesFechaNacStr = fechaNacStr.split("/")
    fechaNacTupla = tuple(partesFechaNacStr)
    if cedulaStr == "" or nombreStr == "" or tipoSangreStr == "" or telefonoStr == "" or correoStr == "" or fechaNacStr == "":
        messagebox.showerror("Faltan Datos", "No puede dejar datos en blanco")
        return
    try:
        pesoFloat = float(peso.get())
    except:
        messagebox.showerror("Peso Invalido", "Debe ser unicamente un numero flotante")
        return
    if validarCedulaBD(cedulaStr):
        if validarNombreCompletoBD(nombreLista):
            if formatoFechaNacIngresarDon(fechaNacStr):
                if validarTelBD(telefonoStr):
                    if validarCorreoBD(correoStr):
                        return registrarDonador(ventanaIngresarDon, anchoVentana, altoVentana, posicionX, posicionY, cedulaStr, nombreLista, fechaNacTupla, tipoSangreInt, sexoBool, pesoFloat, telefonoStr, correoStr, bdDonadores, ventanaMenu, opcActualizarDatosDonador, opcEliminarDonador, opcReportes)
                    else:
                        messagebox.showerror("Correo Invalido", "Verifique que este escrito como se solicita.")
                        return
                else:
                    messagebox.showerror("Telefono Invalido", "Verifique que este escrito como se solicita.")
                    return
            else:
                messagebox.showerror("Fecha de nacimiento Invalida", "Verifique que haya escrito de manera correcta el formato de fecha")
                return
        else:
            messagebox.showerror("Nombre Invalido", "Escriba su nombre y sus dos apellidos unicamente con letras")
            return
    else:
        messagebox.showerror("Cedula Invalida", "Deben estar escrito con 9 digitos separados por '-'. Ej: 1-2345-6789")
        return

#validaciones para datos cargados
def ingresarNombre(ventanaIngresarDon, mensNombreValidacion):
    nombreDonador = tk.Entry(ventanaIngresarDon,
                         font=("Arial", 11))
    nombreDonador.place(x=100, y=140)
    nombreDonador.bind("<KeyRelease>", lambda nombre: validarNombreAux(nombre, mensNombreValidacion))
    return nombreDonador
def validarNombreCompletoBD(pNombre):
    if isinstance(pNombre, list) and len(pNombre) == 3:
        if isinstance(pNombre[0], str) and isinstance(pNombre[1], str) and isinstance(pNombre[2], str):
            nombre = pNombre[0]+" "+pNombre[1]+" "+pNombre[2]
            nombre = nombre.title()
            if re.match("^[a-zA-ZáéíóúÁÉÍÓÚñÑ\\s]+$", nombre):
                return True
    return False
def validarNombreAux(nombre, mensNombreValidacion):
    nombre = nombre.widget.get()
    nombre = nombre.strip().split(" ")
    if validarNombreCompletoBD(nombre):
        mensNombreValidacion.config(text="Nombre valido",
                                    foreground="green")
    else:
        mensNombreValidacion.config(text="Nombre invalido. Su nombre debe estar conformado solo por letras",
                                    foreground="red")
def ingresarCedula(ventanaIngresarDon, mensCedulaValidacion):
    cedulaDonador = tk.Entry(ventanaIngresarDon,
                         font=("Arial", 11))
    cedulaDonador.place(x=100, y=92)
    cedulaDonador.bind("<KeyRelease>", lambda cedula: validarCedulaAux(cedula, mensCedulaValidacion))
    return cedulaDonador
def validarCedulaBD(pCedula):
    if isinstance(pCedula, str):
        if re.match("^[1-9]{1}-\\d{4}-\\d{4}$", pCedula):
            return True
    return False
def validarCedulaAux(cedula, mensCedulaValidacion):
    cedula = cedula.widget.get()
    if validarCedulaBD(cedula):
        mensCedulaValidacion.config(text="Cedula valida",
                                    foreground="green")
    else:
        mensCedulaValidacion.config(text="Cedula invalida. Debe estar escrita como en el ejemplo y solo datos caracteres numericos",
                                    foreground="red")
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
        formatoCorrecto = formatoFechaNacIngresarDon(fechaNac)
        if not formatoCorrecto:
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
def ingresarCorreo(ventanaIngresarDon, mensCorreoValidacion):
    correoDonador = tk.Entry(ventanaIngresarDon,
                         font=("Arial", 11))
    correoDonador.place(x=100, y=445)
    correoDonador.bind("<KeyRelease>", lambda correo: validarCorreoAux(correo, mensCorreoValidacion))
    return correoDonador
def validarCorreoBD(pCorreo):
    if isinstance(pCorreo, str):
        patron = r"^[a-zA-Z0-9._%+-]+@(costarricense\.cr|racsa\.go\.cr|ccss\.sa\.cr|gmail\.com)$"
        if re.match(patron, pCorreo):
            return True
def validarCorreoAux(correo, mensCorreoValidacion):
    correo = correo.widget.get()
    if validarCorreoBD(correo):
        mensCorreoValidacion.config(text="Correo valido",
                                    foreground="green")
    else:
        mensCorreoValidacion.config(text="Correo invalido. su creo debe de terminar en:\n@costarricense.cr, @racsa.go.cr, @ccss.sa.cr, @gmail.com",
                                    foreground="red")
    return False
def ingresarTelefono(ventanaIngresarDon, mensTelefonoValidacion):
    telefonoDonador = tk.Entry(ventanaIngresarDon,
                         font=("Arial", 11))
    telefonoDonador.place(x=100, y=398)
    telefonoDonador.bind("<KeyRelease>", lambda telefono: validarTelefonoAux(telefono, mensTelefonoValidacion))
    return telefonoDonador
def validarTelBD(pTel):
    if isinstance(pTel, str):
        patron = r"^\d{4}-\d{4}$"
        if re.match(patron, pTel) and pTel[0] not in "0135":
            return True
    return False
def validarTelefonoAux(telefono, mensTelefonoValidacion):
    telefono = telefono.widget.get()
    if validarTelBD(telefono):
        mensTelefonoValidacion.config(text="telefono valido",
                                    foreground="green")
    else:
        mensTelefonoValidacion.config(text="telefono invalido. El primer digito no puede ser 0, 1, 3, 5",
                                    foreground="red")
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
        temp = {}
        for donador in bdDonadores:
            if isinstance(donador, list) and len(donador) == 10:
                if validarNombreCompletoBD(donador[0]) and validarCedulaBD(donador[1]) and validarTSangreBD(donador[2]) and validarSexoBD(donador[3]) and validarFechaNacBD(donador[4]):
                    if validarPesoBD(donador[5]) and validarCorreoBD(donador[6]) and validarTelBD(donador[7]) and validarEstadoBD(donador[8]) and validarJustificacionBD(donador[9]):
                        fecha = donador[4]
                        fecha = (f"{fecha[0]}",f"{fecha[1]}",f"{fecha[2]}")
                        datos = [donador[0],donador[2],donador[3],fecha,donador[5],donador[6],donador[7],donador[8],donador[9]]
                        temp[donador[1]] = datos
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
        return {}
#Guardar base de datos
def guardarDonadores(bdDonadores):
    llaves = list(bdDonadores.keys())
    matriz = []
    for cedula in llaves:
        datos = bdDonadores[cedula]
        temp = []
        for i in range(len(datos)):
            temp.append(datos[i])
        temp.insert(1,cedula)
        matriz.append(temp)
    print(matriz)
    with open("bdDonadores.txt", "wb") as f:
        pickle.dump(matriz, f)
        print("Base de datos guardada")
        # print(bdDonadores)
    return
def limpiarEntradas(cedula, nombre, fechaNac, comboBoxTipoSangre, sexoDonador, peso, telefono, correo, mensCedulaValidacion, mensNombreValidacion, mensFechaNacValidacion, mensTelefonoValidacion, mensCorreoValidacion):
    cedula.delete(0, tk.END)
    nombre.delete(0, tk.END)
    fechaNac.delete(0, tk.END)
    comboBoxTipoSangre.set("")
    sexoDonador.set("Masculino")
    peso.delete(0, tk.END)
    telefono.delete(0, tk.END)
    correo.delete(0, tk.END)
    mensCedulaValidacion.config(text="")
    mensNombreValidacion.config(text="")
    mensFechaNacValidacion.config(text="")
    mensTelefonoValidacion.config(text="")
    mensCorreoValidacion.config(text="")
#Ventana de Menu
def volverMenu(ventanaActual, ventanaMenu):
    ventanaActual.destroy()
    ventanaMenu.deiconify()
def insertarDonador(ventanaMenu, anchoVentana, altoVentana, posicionX, posicionY, bdDonadores, opcActualizarDatosDonador, opcEliminarDonador, opcReportes):
    ventanaMenu.withdraw()
    ventanaIngresarDon = tk.Toplevel()
    ventanaIngresarDon.title("Sistema de Banco de Sangre")
    ventanaIngresarDon.geometry(f"{anchoVentana}x{altoVentana}+{posicionX}+{posicionY}")
    mensIngresarDonador = tk.Label(ventanaIngresarDon,
                                      text="Insertar Donador",
                                      font=("Arial", 12))
    mensIngresarDonador.place(x=340, y=30)
    mensCedula = tk.Label(ventanaIngresarDon,
                          text="Digite su cedula de la siguiente manera: Ej: 1-2345-6789: ")
    mensCedula.place(x=98, y=70)
    mensCedulaValidacion = tk.Label(ventanaIngresarDon, 
                            text="", 
                            font=("Arial", 10))
    mensCedulaValidacion.place(x=265, y=90)
    mensNombre = tk.Label(ventanaIngresarDon,
                             text="Digite su nombre completo:")
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
    mensTipoSangre = tk.Label(ventanaIngresarDon,
                              text="Seleccione su tipo de sangre:")
    mensTipoSangre.place(x=98, y=218)
    comboBoxTipoSangre = Combobox(ventanaIngresarDon)
    comboBoxTipoSangre['values'] = ("O+","O-","A+","A-","B+","B-","AB+","AB-")
    comboBoxTipoSangre.place(x=98, y=238)
    mensSexo = tk.Label(ventanaIngresarDon,
                              text="Seleccione su sexo:")
    mensSexo.place(x=98, y=265)
    sexoBool = tk.StringVar(value="Masculino")
    seleccionMascu = tk.Radiobutton(ventanaIngresarDon,
                                        text="Masculino",
                                        variable=sexoBool,
                                        value="Masculino")
    seleccionMascu.place(x=98, y=282)
    seleccionFemen = tk.Radiobutton(ventanaIngresarDon,
                                        text="Femenino",
                                        variable=sexoBool,
                                        value="Femenino")
    seleccionFemen.place(x=98, y=305)
    mensPeso = tk.Label(ventanaIngresarDon,
                          text="Digite su peso en KG:")
    mensPeso.place(x=98, y=330)
    mensPesoValidacion = tk.Label(ventanaIngresarDon, 
                            text="", 
                            font=("Arial", 10))
    mensPesoValidacion.place(x=265, y=348)
    mensTelefono = tk.Label(ventanaIngresarDon,
                          text="Digite su numero de telefono de la siguiente manera: Ej: 2233-4455:")
    mensTelefono.place(x=98, y=378)
    mensTelefonoValidacion = tk.Label(ventanaIngresarDon, 
                            text="", 
                            font=("Arial", 10))
    mensTelefonoValidacion.place(x=265, y=396)
    mensCorreo = tk.Label(ventanaIngresarDon,
                          text="Digite su correo:")
    mensCorreo.place(x=98, y=424)
    mensCorreoValidacion = tk.Label(ventanaIngresarDon, 
                            text="", 
                            font=("Arial", 10))
    mensCorreoValidacion.place(x=265, y=443)

    cedula = ingresarCedula(ventanaIngresarDon, mensCedulaValidacion)
    nombre = ingresarNombre(ventanaIngresarDon, mensNombreValidacion)
    tipoSangre = comboBoxTipoSangre
    #sexoBool
    fechaNac = ingresarFechaNac(ventanaIngresarDon)
    peso = ingresarPeso(ventanaIngresarDon)
    correo = ingresarCorreo(ventanaIngresarDon, mensCorreoValidacion)
    telefono = ingresarTelefono(ventanaIngresarDon, mensTelefonoValidacion)


    botRegistrar = tk.Button(ventanaIngresarDon,
                                   cursor="Hand2",
                                   text="Registrar",
                                   relief="groove",
                                   font=("Arial", 11),
                                   command=lambda: registrarDonadorAux(ventanaIngresarDon, anchoVentana, altoVentana, posicionX, posicionY, cedula, nombre, fechaNac, tipoSangre, sexoBool, peso, telefono, correo, bdDonadores, ventanaMenu, opcActualizarDatosDonador, opcEliminarDonador, opcReportes))
    botRegistrar.place(x=280, y=500)
    botLimpiar = tk.Button(ventanaIngresarDon,
                                   cursor="Hand2",
                                   text="Limpiar",
                                   relief="groove",
                                   font=("Arial", 11),
                                   command=lambda: limpiarEntradas(cedula, nombre, fechaNac, comboBoxTipoSangre, sexoBool, peso, telefono, correo, mensCedulaValidacion, mensNombreValidacion, mensFechaNacValidacion, mensTelefonoValidacion, mensCorreoValidacion))
    botLimpiar.place(x=370, y=500)
    botRegresar = tk.Button(ventanaIngresarDon,
                                   cursor="Hand2",
                                   text="Regresar",
                                   relief="groove",
                                   font=("Arial", 11),
                                   command=lambda: volverMenu(ventanaIngresarDon, ventanaMenu))
    botRegresar.place(x=450, y=500)

def ingresarFechaNac(ventanaIngresarDon): 
    fechaNacDonador = tk.Entry(ventanaIngresarDon,
                         font=("Arial", 11))
    fechaNacDonador.place(x=100, y=190)
    return fechaNacDonador

def ingresarPeso(ventanaIngresarDon): 
    pesoDonador = tk.Entry(ventanaIngresarDon,
                         font=("Arial", 11))
    pesoDonador.place(x=100, y=352)
    return pesoDonador

#Generar Donadores
def revisarCedulaRep(cedula, bdPersonas):
    if cedula in bdPersonas:
        return True
    return False
def generarCedula(cedula, bdPersonas):
    estado = True
    while estado:
        provincia = str(random.randint(1, 9))
        tomo = str(random.randint(1000, 9999))
        asiento = str(random.randint(1000, 9999))
        cedula = provincia + "-" + tomo + "-" + asiento
        estado = revisarCedulaRep(cedula, bdPersonas)
    return cedula
def generarNombre():
    nombres = [
        "Aaron", "Abigail", "Adam", "Adrian", "Aiden", "Alex", "Alice", "Amanda", "Andrew", "Ashley",
        "Barbara", "Benjamin", "Bethany", "Blake", "Brandon", "Brian", "Brianna", "Brittany", "Brooke", "Bryan",
        "Caleb", "Cameron", "Carl", "Caroline", "Carter", "Charles", "Charlotte", "Chloe", "Christian", "Christopher",
        "Dakota", "Daniel", "Danielle", "David", "Deborah", "Dennis", "Derek", "Diana", "Dominic", "Donna",
        "Edward", "Eleanor", "Elijah", "Elizabeth", "Ella", "Emily", "Emma", "Eric", "Ethan", "Evelyn",
        "Faith", "Felicia", "Fernando", "Finn", "Fiona", "Francis", "Frank", "Fred", "Freya", "Floyd",
        "Gabriel", "Gavin", "George", "Georgia", "Gianna", "Grace", "Graham", "Grant", "Gregory", "Gwen",
        "Hailey", "Hannah", "Harold", "Harry", "Hazel", "Heather", "Helen", "Henry", "Holly", "Hunter",
        "Ian", "Irene", "Isaac", "Isabel", "Isabella", "Ivan", "Ivy", "Iris", "India", "Imogen",
        "Jack", "Jackson", "Jacob", "Jade", "James", "Jamie", "Jane", "Jasmine", "Jason", "Julia",
        "Karen", "Katherine", "Kayla", "Keith", "Kelly", "Kenneth", "Kevin", "Kimberly", "Kyle", "Kylie",
        "Larry", "Laura", "Lauren", "Layla", "Leah", "Leo", "Liam", "Lillian", "Logan", "Lucas",
        "Madeline", "Madison", "Marcus", "Margaret", "Maria", "Mark", "Mason", "Matthew", "Megan", "Michael",
        "Nancy", "Naomi", "Natalie", "Nathan", "Nicholas", "Nicole", "Noah", "Nolan", "Nora", "Norman",
        "Oakley", "Olivia", "Omar", "Ophelia", "Oscar", "Owen", "Olive", "Octavia", "Orlando", "Otis",
        "Paige", "Pamela", "Patricia", "Patrick", "Paul", "Penelope", "Peter", "Philip", "Phoebe", "Preston",
        "Quentin", "Quincy", "Quinn", "Queenie", "Quinlan", "Quinton", "Quade", "Quilla", "Quora", "Quest",
        "Rachel", "Raymond", "Rebecca", "Richard", "Robert", "Rose", "Ruby", "Russell", "Ryan", "Ryder",
        "Samantha", "Samuel", "Sandra", "Sarah", "Scott", "Sean", "Sebastian", "Sophia", "Steven", "Sydney",
        "Taylor", "Teresa", "Thomas", "Tiffany", "Timothy", "Travis", "Trevor", "Trinity", "Tyler", "Tyrone",
        "Ula", "Ulric", "Ulysses", "Uma", "Uriel", "Ursula", "Usher", "Urban", "Unity", "Ulani",
        "Valerie", "Vanessa", "Victor", "Victoria", "Vincent", "Violet", "Virginia", "Vivian", "Vladimir", "Vance",
        "Walter", "Wayne", "Wendy", "Wesley", "Whitney", "William", "Willow", "Wyatt", "Warren", "Wanda",
        "Xander", "Xavier", "Xena", "Ximena", "Xiomara", "Xyla", "Xanthe", "Xerxes", "Xenia", "Xavi",
        "Yara", "Yasmine", "Yolanda", "Yosef", "Yvette", "Yvonne", "Yahir", "Yasmin", "Yuri", "Yvette",
        "Zachary", "Zane", "Zara", "Zayden", "Zelda", "Zoe", "Zoey", "Zuri", "Zion", "Zeke"]
    apellidos = [
        "Adams", "Alexander", "Allen", "Anderson", "Armstrong", "Arnold", "Austin", "Atkins", "Avery", "Abbott",
        "Bailey", "Baker", "Barnes", "Bell", "Bennett", "Brooks", "Brown", "Bryant", "Butler", "Burton",
        "Campbell", "Carter", "Chapman", "Clark", "Coleman", "Collins", "Cook", "Cooper", "Cox", "Crawford",
        "Daniels", "Davidson", "Davis", "Dawson", "Dean", "Diaz", "Dixon", "Douglas", "Duncan", "Dunn",
        "Edwards", "Ellis", "Elliott", "Evans", "Erickson", "Estrada", "English", "Eaton", "Emerson", "Everett",
        "Farmer", "Ferguson", "Fisher", "Fleming", "Flores", "Floyd", "Ford", "Foster", "Fox", "Franklin",
        "Garcia", "Gardner", "Garrett", "George", "Gibson", "Gilbert", "Gomez", "Gonzalez", "Gordon", "Graham",
        "Hall", "Hamilton", "Hansen", "Harris", "Harrison", "Hart", "Hawkins", "Hayes", "Henderson", "Hill",
        "Ingram", "Irwin", "Iverson", "Isaacs", "Ireland", "Ibarra", "Inman", "Irving", "Ivers", "Ison",
        "Jackson", "Jacobs", "James", "Jenkins", "Jennings", "Jimenez", "Johnson", "Johnston", "Jones", "Jordan",
        "Keller", "Kelly", "Kennedy", "Kim", "King", "Knight", "Knowles", "Kramer", "Kuhn", "Kline",
        "Lambert", "Lane", "Larson", "Lawrence", "Lee", "Lewis", "Little", "Long", "Lopez", "Lynch",
        "Mann", "Marshall", "Martin", "Martinez", "Mason", "Matthews", "Mendoza", "Miller", "Mitchell", "Moore",
        "Nash", "Navarro", "Neal", "Nelson", "Newman", "Nichols", "Nixon", "Noble", "Norris", "Nunez",
        "Oliver", "Olson", "Ortiz", "Osborne", "Owens", "Odom", "Oneal", "Orr", "Ortega",
        "Palmer", "Parker", "Parsons", "Patterson", "Payne", "Perez", "Perkins", "Perry", "Phillips", "Powell",
        "Qualls", "Quigley", "Quinlan", "Quinn", "Quintero", "Quick", "Quade", "Quarles", "Queen", "Quincy",
        "Ramirez", "Ray", "Reed", "Reese", "Reid", "Reynolds", "Rhodes", "Rice", "Richardson", "Rivera",
        "Salazar", "Sanchez", "Sanders", "Scott", "Shaw", "Shelton", "Simpson", "Sims", "Smith", "Stewart",
        "Taylor", "Thomas", "Thompson", "Torres", "Townsend", "Tran", "Tucker", "Turner", "Tyler", "Terry",
        "Underwood", "Upton", "Usher", "Utley", "Ulrich", "Umber", "Urban", "Ullman", "Upchurch", "Urbina",
        "Valdez", "Valencia", "Vance", "Vargas", "Vasquez", "Vaughn", "Vega", "Velasquez", "Vincent", "Vinson",
        "Wade", "Walker", "Wallace", "Walters", "Ward", "Warner", "Washington", "Watkins", "Watson", "Williams",
        "Xander", "Xavier", "Xenos", "Xiong", "Xayasane", "Xayavong", "Xiques", "Xerri", "Ximenes", "Xu",
        "Yancey", "Yang", "Yates", "York", "Young", "Ybarra", "Yeager", "Yoder", "Yoon", "Yu",
        "Zamora", "Zane", "Zavala", "Zimmerman", "Zuniga", "Zapata", "Zeigler", "Zeller", "Zhou", "Zimmer"
    ]
    nombre = random.choice(nombres)
    apellido1 = random.choice(apellidos)
    apellido2 = random.choice(apellidos)
    pNombre = [nombre, apellido1, apellido2]
    return pNombre
def generarFechaNac():
    dia = random.randint(1, 31)
    mes = random.randint(1, 12)
    fechaHoy = datetime.now()
    annoHoy = fechaHoy.year
    annoMin = annoHoy - 65
    annoMax = annoHoy - 18
    anno = random.randint(annoMin, annoMax)
    fechaNac = (str(dia), str(mes), str(anno))
    while not validarFechaNacBD(fechaNac):
        dia = random.randint(1, 31)
        mes = random.randint(1, 12)
        anno = random.randint(annoMin, annoMax)
        fechaNac = (str(dia), str(mes), str(anno))
    return fechaNac
def generarCorreo(nombre):
    dominios = ["costarricense.cr", "racsa.go.cr", "ccss.sa.cr", "gmail.com"]
    nombreStr = nombre[0].lower()  # primer nombre
    apellidoStr = nombre[1].lower()  # primer apellido
    numero = random.randint(1, 999)
    correo = f"{nombreStr}{apellidoStr}{numero}@{random.choice(dominios)}"
    return correo
def generarDatosPersona(bdPersonas):
    datosPersona = []
    cedula = ""
    nombre = generarNombre()
    datosPersona.append(nombre)
    datosPersona.append(generarCedula(cedula, bdPersonas))
    tSangre = (1, 2, 3, 4, 5, 6, 7, 8)
    datosPersona.append(random.choice(tSangre))
    datosPersona.append(random.choice([True, False]))
    datosPersona.append(generarFechaNac())
    datosPersona.append(round(random.uniform(50.1, 119.9), 1))
    correo = generarCorreo(nombre)
    datosPersona.append(correo)
    tel = "0"
    while tel[0] in "0135":
        tel = f"{random.randint(1000,9999)}-{random.randint(1000,9999)}"
    datosPersona.append(tel)
    datosPersona.append(1)
    datosPersona.append(random.randint(0, 7))
    return datosPersona
def generarDonadores(ventanaMenu, ventanaGenerarDon, anchoVentana, altoVentana, posicionX, posicionY, cant, bdDonadores, opcActualizarDatosDonador, opcEliminarDonador, opcReportes):
    contador = 0
    cant = int(cant.get())
    while contador < cant:
        datosPersona = generarDatosPersona(bdDonadores)
        cedula = datosPersona[1]
        bdDonadores[cedula] = [datosPersona[0]] + datosPersona[2:]
        contador += 1
    guardarDonadores(bdDonadores)
    actualizarBotones(opcActualizarDatosDonador, opcEliminarDonador, opcReportes)
    ventanaGenerarDon.withdraw()
    ventanaGenerarDon = tk.Toplevel()
    ventanaGenerarDon.title("Sistema de Banco de Sangre")
    ventanaGenerarDon.geometry(f"{anchoVentana}x{altoVentana}+{posicionX}+{posicionY}")
    mensGenerar = tk.Label(ventanaGenerarDon,
                           text=f"Se han generado {cant} donadores",
                           font=("Arial", 13))
    mensGenerar.place(x=98, y=70)
    botRegresar = tk.Button(ventanaGenerarDon,
                            cursor="Hand2",
                            text="Regresar",
                            relief="groove",
                            font=("Arial", 11),
                            command=lambda: volverMenu(ventanaGenerarDon, ventanaMenu))
    botRegresar.place(x=360, y=500)
def validarCantDon(cant, mensGenerarValidacion):
    cant = cant.widget.get()
    if re.match(r"^\d+$", cant) and int(cant) > 0:
        mensGenerarValidacion.config(text="Cantidad valida",
                                    foreground="green")
    else:
        mensGenerarValidacion.config(
            text="Cantidad invalida. Debe ingresar solo datos numéricos mayores a 0",
            foreground="red")
def ingresarCantDon(ventanaGenerarDon, mensGenerarValidacion):
    cantDonador = tk.Entry(ventanaGenerarDon,
                         font=("Arial", 11))
    cantDonador.place(x=100, y=140)
    cantDonador.bind("<KeyRelease>", lambda cant: validarCantDon(cant, mensGenerarValidacion))
    return cantDonador
def ingresarCantDonAux(ventanaMenu, ventanaGenerarDon, anchoVentana, altoVentana, posicionX, posicionY, mensGenerarValidacion, opcActualizarDatosDonador, opcEliminarDonador, opcReportes):
    ventanaGenerarDon.withdraw()
    ventanaGenerarDon = tk.Toplevel()
    ventanaGenerarDon.title("Sistema de Banco de Sangre")
    ventanaGenerarDon.geometry(f"{anchoVentana}x{altoVentana}+{posicionX}+{posicionY}")
    mensGenerar = tk.Label(ventanaGenerarDon,
                           text="Digite la cantidad de donadores que desea generar: ",
                           font=("Arial", 13))
    mensGenerar.place(x=98, y=90)
    mensGenerarValidacion = tk.Label(ventanaGenerarDon,
                                     text="",
                                     font=("Arial", 10))
    mensGenerarValidacion.place(x=265, y=138)
    cant = ingresarCantDon(ventanaGenerarDon, mensGenerarValidacion)
    bdDonadores = {}
    botGenerar = tk.Button(ventanaGenerarDon,
                                   cursor="Hand2",
                                   text="Generar",
                                   relief="groove",
                                   font=("Arial", 11),
                                   command=lambda: generarDonadores(ventanaMenu,ventanaGenerarDon, anchoVentana, altoVentana, posicionX, posicionY, cant, bdDonadores, opcActualizarDatosDonador, opcEliminarDonador, opcReportes))
    botGenerar.place(x=320, y=500)
    botRegresar = tk.Button(ventanaGenerarDon,
                            cursor="Hand2",
                            text="Regresar",
                            relief="groove",
                            font=("Arial", 11),
                            command=lambda: volverMenu(ventanaGenerarDon, ventanaMenu))
    botRegresar.place(x=410, y=500)
def generarDonadoresAux(ventanaMenu, anchoVentana, altoVentana, posicionX, posicionY, bdDonadores, opcActualizarDatosDonador, opcEliminarDonador, opcReportes):
    ventanaMenu.withdraw()
    ventanaGenerarDonAux = tk.Toplevel()
    ventanaGenerarDonAux.title("Sistema de Banco de Sangre")
    ventanaGenerarDonAux.geometry(f"{anchoVentana}x{altoVentana}+{posicionX}+{posicionY}")
    mensIngresarDonador = tk.Label(ventanaGenerarDonAux,
                                      text="Generar Donadores",
                                      font=("Arial", 12))
    mensIngresarDonador.place(x=340, y=30)
    mensGenerarValidacion = tk.Label(ventanaGenerarDonAux,
                                     text="",
                                     font=("Arial", 10))
    mensGenerarValidacion.place(x=265, y=138)
    if bdDonadores == {}:
        ingresarCantDonAux(ventanaMenu, ventanaGenerarDonAux, anchoVentana, altoVentana, posicionX, posicionY, mensGenerarValidacion, opcActualizarDatosDonador, opcEliminarDonador, opcReportes)
    else:
        mensGenerar = tk.Label(ventanaGenerarDonAux,
                               text="La base de datos está cargada. Desea reescribir los datos: ")
        mensGenerar.place(x=98, y=70)
        continuar = tk.IntVar(value=0)
        opcGenerarDonadores = tk.Button(ventanaGenerarDonAux,
                                        cursor="Hand2",
                                        text="Sí",
                                        relief="groove",
                                        font=("Arial", 11),
                                        command=lambda: ingresarCantDonAux(ventanaMenu, ventanaGenerarDonAux, anchoVentana, altoVentana, posicionX, posicionY, mensGenerarValidacion, opcActualizarDatosDonador, opcEliminarDonador, opcReportes))
        opcGenerarDonadores.place(x=100, y=100)
        opcGenerarDonadores = tk.Button(ventanaGenerarDonAux,
                                        cursor="Hand2",
                                        text="No",
                                        relief="groove",
                                        font=("Arial", 11),
                                        command=lambda: volverMenu(ventanaGenerarDonAux, ventanaMenu))
        opcGenerarDonadores.place(x=150, y=100)

        mensGenerarValidacion = tk.Label(ventanaGenerarDonAux,
                                         text="",
                                         font=("Arial", 10))
        mensGenerarValidacion.place(x=265, y=90)

    botRegresar = tk.Button(ventanaGenerarDonAux,
                                   cursor="Hand2",
                                   text="Regresar",
                                   relief="groove",
                                   font=("Arial", 11),
                                   command=lambda: volverMenu(ventanaGenerarDonAux, ventanaMenu))
    botRegresar.place(x=450, y=500)