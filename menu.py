#Elaborado por: Derian Segura y Juan Gonzalez
#Fecha de creacion: 16/05/2026 19:00
#Ultima modificacion:
#Version 3.14.3

#importaciones
import funciones
import tkinter as tk

def mostrarOpcionesReportes(ventanaMenu, anchoVentana, altoVentana, posicionX, posicionY):
    ventanaMenu.withdraw()
    ventanaOpcionesReportes = tk.Toplevel()
    ventanaOpcionesReportes.title("Sistema de Banco de Sangre")
    ventanaOpcionesReportes.geometry(f"{anchoVentana}x{altoVentana}+{posicionX}+{posicionY}")

    mensaOpcionesReporte = tk.Label(ventanaOpcionesReportes,
                                    text="Presiona el Reporte que deseas",
                                    font=("Arial", 12))
    mensaOpcionesReporte.place(x=280, y=30)

    opcPorProvincia = tk.Button(ventanaOpcionesReportes,
                                   cursor="Hand2",
                                   text="Por una provincia",
                                   relief="groove",
                                   font=("Arial", 11))
                                #    command=lambda: )
    opcPorProvincia.place(x=90, y=50)

    opcPorEdad = tk.Button(ventanaOpcionesReportes,
                                    cursor="Hand2",
                                    text="Por rango de edad",
                                    relief="groove",
                                    font=("Arial", 11),
                                    command=lambda: funciones.validarRangoEdadHtmlAux(ventanaOpcionesReportes, anchoVentana, altoVentana, posicionX, posicionY))
    opcPorEdad.place(x=90, y=100)

    opcSangreProvincia = tk.Button(ventanaOpcionesReportes,
                                          cursor="Hand2",
                                          text="Por Tipo Sangre y una Provincia",
                                          relief="groove",
                                          font=("Arial", 11))
                                        #   command=lambda: )
    opcSangreProvincia.place(x=90, y=150)

    opcListaCompleta = tk.Button(ventanaOpcionesReportes,
                                   cursor="Hand2",
                                   text="Lista Completa",
                                   relief="groove",
                                   font=("Arial", 11))
                                #    command=lambda: )
    opcListaCompleta.place(x=90, y=200)

    opcMujeresO = tk.Button(ventanaOpcionesReportes,
                                 cursor="Hand2",
                                 text="Mujeres Donantes O-",
                                 relief="groove",
                                 font=("Arial", 11))
                                #  command=lambda: )
    opcMujeresO.place(x=90, y=250)

    opcQuienDonar = tk.Button(ventanaOpcionesReportes,
                            cursor="Hand2",
                            text="A quién donar (Por provincia)",
                            relief="groove",
                            font=("Arial", 11))
                            # command=lambda: )
    opcQuienDonar.place(x=90, y=300)

    opcQuienDonar = tk.Button(ventanaOpcionesReportes,
                            cursor="Hand2",
                            text="De quien recibir (Por provincia)",
                            relief="groove",
                            font=("Arial", 11))
                            # command=lambda: )
    opcQuienDonar.place(x=90, y=350)

    opcQuienDonar = tk.Button(ventanaOpcionesReportes,
                            cursor="Hand2",
                            text="No Activos",
                            relief="groove",
                            font=("Arial", 11))
                            # command=lambda: )
    opcQuienDonar.place(x=90, y=400)

    opcQuienDonar = tk.Button(ventanaOpcionesReportes,
                            cursor="Hand2",
                            text="Lugares de Donación",
                            relief="groove",
                            font=("Arial", 11))
                            # command=lambda: )
    opcQuienDonar.place(x=90, y=450)

    botRegresar = tk.Button(ventanaOpcionesReportes,
                            cursor="Hand2",
                            text="Regresar",
                            relief="groove",
                            font=("Arial", 11),
                            command=lambda: funciones.volverMenu(ventanaOpcionesReportes, ventanaMenu))
    botRegresar.place(x=360, y=500)

#Menu
def menu(bdDonadores):

    ventanaMenu = tk.Tk()
    ventanaMenu.title("Sistema de Banco de Sangre")

    anchoVentana, altoVentana, posicionX, posicionY = funciones.dimensionarVentana(ventanaMenu)

    hospiSJ = ["El Banco Nacional de Sangre","Hospital Mëxico","Hospital San Juan de Dios"]
    diccHospi = {1:hospiSJ,
                8:hospiSJ,
                9:hospiSJ,
                2:["Hospital San Rafael de Alajuela","Hospital de San Ramón","Hospital del Cantón Norteño"],
                3:["Hospital Max Peralta"],
                4:["Hospital San Vicente de Paúl"],
                5:["Hospital La Anexión en Nicoya","Hospital Enrique Baltodano de Liberia"],
                6:["Hospital Monseñor Sanabria"],
                7:["Hospital Tony Facio","Hospital de Guápiles"]}

    mensajeMenu = tk.Label(text="Estas en el Menu Principal. Presione el Boton de la Opcion que Desea",
                           font=("Arial", 12))
    mensajeMenu.place(x=170, y=50)

    
        
    opcIngresarDonante = tk.Button(ventanaMenu,
                                   cursor="Hand2",
                                   text="Ingresar Donante",
                                   relief="groove",
                                   font=("Arial", 11),
                                   command=lambda: funciones.insertarDonador(ventanaMenu, anchoVentana, altoVentana, posicionX, posicionY, bdDonadores, opcActualizarDatosDonador, opcEliminarDonador, opcReportes, diccHospi))
    opcIngresarDonante.place(x=100, y=100)

    opcGenerarDonadores = tk.Button(ventanaMenu,
                                    cursor="Hand2",
                                    text="Generar Donadores",
                                    relief="groove",
                                    font=("Arial", 11),
                                    command=lambda: funciones.generarDonadoresAux(ventanaMenu, anchoVentana, altoVentana,posicionX, posicionY, bdDonadores, opcActualizarDatosDonador, opcEliminarDonador, opcReportes))
    opcGenerarDonadores.place(x=100, y=150)

    opcActualizarDatosDonador = tk.Button(ventanaMenu,
                                          cursor="Hand2",
                                          text="Actualizar Datos del Donador",
                                          relief="groove",
                                          font=("Arial", 11),
                                          command=lambda: funciones.actualizarDatosAux(
                                              ventanaMenu, anchoVentana, altoVentana, posicionX, posicionY,
                                              bdDonadores, opcActualizarDatosDonador,
                                              opcEliminarDonador, opcReportes, diccHospi))
    opcActualizarDatosDonador.place(x=100, y=200)

    opcEliminarDonador = tk.Button(ventanaMenu,
                                   cursor="Hand2",
                                   text="Eliminar Donador",
                                   relief="groove",
                                   font=("Arial", 11),
                                   command=lambda: funciones.eliminarDonadorAux(ventanaMenu, anchoVentana, altoVentana, posicionX, posicionY, bdDonadores))
    opcEliminarDonador.place(x=100, y=250)

    opcLugarDonacion = tk.Button(ventanaMenu,
                                 cursor="Hand2",
                                 text="Insertar lugar de donación según provincia",
                                 relief="groove",
                                 font=("Arial", 11),
                                 command=lambda: funciones.insertarLugarDonacionAux(ventanaMenu, anchoVentana, altoVentana, posicionX, posicionY, diccHospi))
    opcLugarDonacion.place(x=100, y=300)

    opcReportes = tk.Button(ventanaMenu,
                            cursor="Hand2",
                            text="Reportes",
                            relief="groove",
                            font=("Arial", 11),
                            command= lambda: mostrarOpcionesReportes(ventanaMenu, anchoVentana, altoVentana, posicionX, posicionY))
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
menu(bdDonadores)