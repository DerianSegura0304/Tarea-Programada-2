#Elaborado por: Derian Segura y Juan Gonzalez
#Fecha de creacion: 16/05/2026 19:00
#Ultima modificacion: 
#Version 3.14.3

#importaciones
import funciones
import tkinter as tk

#Menu
def menu(bdDonadores):
    ventanaMenu = tk.Tk()
    ventanaMenu.title("Sistema de Banco de Sangre")

    anchoVentana, altoVentana, posicionX, posicionY = funciones.dimensionarVentana(ventanaMenu)

    mensajeMenu = tk.Label(text="Estas en el Menu Principal. Presione el Boton de la Opcion que Desea",
                           font=("Arial", 12))
    mensajeMenu.place(x=170, y=50)

    opcIngresarDonante = tk.Button(ventanaMenu,
                                   cursor="Hand2",
                                   text="Ingresar Donante",
                                   relief="groove",
                                   font=("Arial", 11),
                                   command=lambda: funciones.insertarDonador(ventanaMenu, anchoVentana, altoVentana, posicionX, posicionY, bdDonadores))
    opcIngresarDonante.place(x=100, y=100)

    opcGenerarDonadores = tk.Button(ventanaMenu,
                                    cursor="Hand2",
                                    text="Generar Donadores",
                                    relief="groove",
                                    font=("Arial", 11))
    opcGenerarDonadores.place(x=100, y=150)

    opcActualizarDatosDonador = tk.Button(ventanaMenu,
                                          cursor="Hand2",
                                          text="Actualizar Datos del Donador",
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

    if len(bdDonadores) == 0:
        opcActualizarDatosDonador.config(state = "disable")
        opcEliminarDonador.config(state = "disable")
        opcReportes.config(state = "disable")
    else:
        opcActualizarDatosDonador.config(state = "normal")
        opcEliminarDonador.config(state = "normal")
        opcReportes.config(state = "normal")

    ventanaMenu.mainloop()


#Programa Principal
bdDonadores = funciones.cargarDonadores()
print(bdDonadores)
menu(bdDonadores)
