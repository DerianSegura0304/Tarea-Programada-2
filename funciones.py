#Elaborado por: Derian Segura y Juan Gonzalez
#Fecha de creacion: 16/05/2026 19:00
#Ultima modificacion: 
#Version 3.14.3

#importaciones
import re
import pickle
import tkinter as tk
from tkinter.ttk import *
from datetime import datetime
from tkinter import messagebox

#funciones
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
                    #ventanaIngresarDon, anchoVentana, altoVentana, posicionX, posicionY, cedulaStr, nombreLista, fechaNacTupla, tipoSangreInt, sexoBool, pesoFloat, telefonoStr, correoStr, bdDonadores, fechaNacStr, ventanaMenu
def registrarDonador(ventanaIngresarDon, anchoVentana, altoVentana, posicionX, posicionY, cedulaStr, nombreLista, fechaNacTupla, tipoSangreInt, sexoBool, pesoFloat, telefonoStr, correoStr, bdDonadores, ventanaMenu):
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

def formatoFechaNacIngresarDon(fechaNac):
    if not re.match("^\\d{2}/\\d{2}/\\d{4}$", fechaNac):
        return False
    return True

def registrarDonadorAux(ventanaIngresarDon, anchoVentana, altoVentana, posicionX, posicionY, cedula, nombre, fechaNac, tipoSangre, sexoBool, peso, telefono, correo, bdDonadores, ventanaMenu):
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
                        return registrarDonador(ventanaIngresarDon, anchoVentana, altoVentana, posicionX, posicionY, cedulaStr, nombreLista, fechaNacTupla, tipoSangreInt, sexoBool, pesoFloat, telefonoStr, correoStr, bdDonadores, ventanaMenu)
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
        if re.match("^[1-7]{1}-\\d{4}-\\d{4}$", pCedula):
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
        patron = r"^[a-zA-Z0-9._%+-]+@(costarricense\.cr|racsa\.go\.cr|ccss\.sa\.cr|gmail+\.com)$"
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
        return {}
#Guardar base de datos
def guardarDonadores(bdDonadores):
    with open("bdDonadores.txt", "wb") as f:
        pickle.dump(bdDonadores, f)
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
def insertarDonador(ventanaMenu, anchoVentana, altoVentana, posicionX, posicionY, bdDonadores):
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
                                   command=lambda: registrarDonadorAux(ventanaIngresarDon, anchoVentana, altoVentana, posicionX, posicionY, cedula, nombre, fechaNac, tipoSangre, sexoBool, peso, telefono, correo, bdDonadores, ventanaMenu))
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
