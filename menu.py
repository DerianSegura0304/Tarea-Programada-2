#Elaborado por: Derian Segura y Juan Gonzalez
#Fecha de creacion: 16/05/2026 19:00
#Ultima modificacion: 
#Version 3.14.3

#importaciones
import funciones
import tkinter as tk

#Menu
def menu():
    ventanaMenu = tk.Tk()
    ventanaMenu.title("Sistema de Banco de Sangre")

    anchoPantalla = ventanaMenu.winfo_screenwidth()
    altoPantalla = ventanaMenu.winfo_screenheight()
    anchoVentana = 800
    altoVentana = 600
    posicionX = round((anchoPantalla / 2) - (anchoVentana / 2))
    posicionY = round((altoPantalla / 2) - (altoVentana / 2))
    ventanaMenu.geometry(f"{anchoVentana}x{altoVentana}+{posicionX}+{posicionY}")

    mensajeMenu = tk.Label(text="Estas en el Menu Principal. Presione el Boton de la Opcion que Desea",
                           font=("Arial", 12))
    mensajeMenu.place(x=170, y=50)

    opcIngresarDonante = tk.Button(ventanaMenu,
                                   cursor="Hand2",
                                   text="Ingresar Donante",
                                   relief="groove",
                                   font=("Arial", 11),
                                   command=lambda: funciones.insertarDonador(ventanaMenu, anchoVentana, altoVentana, posicionX, posicionY))
    opcIngresarDonante.place(x=100, y=100)

    opcGenerarDonadores = tk.Button(ventanaMenu,
                                    cursor="Hand2",
                                    text="Generar Donadores",
                                    relief="groove",
                                    font=("Arial", 11))
    opcGenerarDonadores.place(x=100, y=150)

    opcActualizarDatosDonador = tk.Button(ventanaMenu,
                                          cursor="Hand2",
                                          text="Actualizar Dtos del Donador",
                                          relief="groove",
                                          font=("Arial", 11))
    opcActualizarDatosDonador.place(x=100, y=200)

    opcEliminarDonador = tk.Button(ventanaMenu,
                                   cursor="Hand2",
                                   text="Eliminar Donador",
                                   relief="groove",
                                   font=("Arial", 11))
    opcEliminarDonador.place(x=100, y=250)

    opcLugarDonacion = tk.Button(ventanaMenu,
                                 cursor="Hand2",
                                 text="Insertar lugar de donación según provincia",
                                 relief="groove",
                                 font=("Arial", 11))
    opcLugarDonacion.place(x=100, y=300)

    opcReportes = tk.Button(ventanaMenu,
                            cursor="Hand2",
                            text="Reportes",
                            relief="groove",
                            font=("Arial", 11))
    opcReportes.place(x=100, y=350)

    opcSalir = tk.Button(ventanaMenu,
                         cursor="Hand2",
                         text="Salir",
                         relief="groove",
                         font=("Arial", 11))
    opcSalir.place(x=100, y=400)

    ventanaMenu.mainloop()


#Programa Principal
bdDonadores = funciones.cargarDonadores()
hospitales = {"1":{"San José":["El Banco Nacional de Sangre","Hospital Mëxico","Hospital San Juan de Dios"]},
              "2":{"Alajuela":["Hospital San Rafael de Alajuela","Hospital de San Ramón","Hospital del Cantón Norteño"]},
              "3":{"Cartago":["Hospital Max Peralta"]},
              "4":{"Heredia":["Hospital San Vicente de Paúl"]},
              "5":{"Guanacaste":["Hospital La Anexión en Nicoya","Hospital Enrique Baltodano de Liberia"]},
              "6":{"Puntarenas":["Hospital Monseñor Sanabria"]},
              "7":{"Limón":["Hospital Tony Facio","Hospital de Guápiles"]}}
tSangres = {1:"O+", 2:"O-", 3:"A+",4:"A-", 5:"B+", 6:"B-", 7:"AB+", 8:"AB-"}
justificaciones = {0:"N/A",1:"Enfermedades Infecciosas/Crónicas", 3:"Conductas de Riesgo",4:"Factores de Salud Física",
                   5:"Procedimientos Médicos",6:"Uso de medicamentos",7:"Situaciones Específicas"}
menu()