from re import A
import tkinter as tk

from algoritmo1 import ClsAl1

from algoritmo2 import ClsAl2

from algoritmo3 import ClsAl3

from algoritmo4 import ClsAl4

from algoritmo5 import ClsAl5

from algoritmo6 import ClsAl6


def llamar_ventanaAlgoritmo1():
    ClsAl1.mainn()

def llamar_ventanaAlgoritmo2():
    ClsAl2.mainn()

def llamar_ventanaAlgoritmo3():
    ClsAl3.mainn()

def llamar_ventanaAlgoritmo4():
    ClsAl4.mainn()

def llamar_ventanaAlgoritmo5():
    ClsAl5.mainn()

def llamar_ventanaAlgoritmo6():
    ClsAl6.mainn()
    


def crear_Ventana_Main():
    ventana_main = tk.Tk()
    ventana_main.title=("ALGORITMOS DE COMPUTER VISION")
    ventana_main.state("zoomed")
    ventana_main.rowconfigure(0, weight=2)
    ventana_main.rowconfigure(1, weight=3 )
    ventana_main.rowconfigure(2, weight=5 )
    ventana_main.columnconfigure(0, weight=3)
    ventana_main.columnconfigure(1, weight=7)


    frm_logo = tk.Frame(master=ventana_main, height=10, borderwidth=2, bg='#2081C3')
    frm_logo.grid(row=0, column=0, sticky=tk.NSEW)

    #definicion de imagenes de carpeta resources
    flecha_siguiente = tk.PhotoImage(file=r"resources/images/flecha_siguiente.png")
    flecha_siguiente = flecha_siguiente.subsample(4,4)
    logo_espe = tk.PhotoImage(file=r"resources/images/logo.png" )
    logo_espe = logo_espe.subsample(3,3)


    lab_logo = tk.Label(master=frm_logo, image=	logo_espe)
    lab_logo.pack()


    frm_titulo  = tk.Frame(master=ventana_main, borderwidth=2, bg='#2081C3')
    frm_titulo.grid(row=0, column=1, sticky=tk.NSEW)
    lbl_titulo = tk.Label(master=frm_titulo, text="Aplicaciones de Algoritmos de Computer Vision",font=("Arial", 25), bg='#2081C3', fg='#F7F9F9', pady=65)
    lbl_titulo.pack()

    frm_integrantes = tk.Frame(master=ventana_main, relief=tk.RAISED, borderwidth=2, bg='#78D5D7')
    frm_integrantes.grid(row=1, columnspan=3, sticky=tk.W+tk.E)
    lbl_integrantes =  tk.Label(master=frm_integrantes, text="David Saá --- Pablo Guevara --- Chevandier Perez --- Henry Salazar",font=("Arial", 15), bg=('#78D5D7'))
    lbl_integrantes.pack()

    

    #codigo basura de ejemplo
    ''' frm_boton_agregar_imagen = tk.Frame(master=ventana_main, relief=tk.RAISED, borderwidth=2, bg='#ffffff')
    frm_boton_agregar_imagen.grid(row=2, column=0, sticky=tk.NSEW)
    lbl_agregar = tk.Label(master=frm_boton_agregar_imagen, text="Seleccionar Imagen:",font=("Arial", 20), bg='#ffffff')
    btn_seleccionar_imagen = tk.Button(master=frm_boton_agregar_imagen, image=carpeta_abrir_imagen)
    btn_next_menu = tk.Button(master=frm_boton_agregar_imagen, text="CONTINUAR", font=("Arial", 25), image=flecha_siguiente)
    lbl_agregar.pack(pady=20)
    btn_seleccionar_imagen.pack()
    btn_next_menu.pack(pady=100)

    frm_mostrar_imagen = tk.Frame(master=ventana_main, relief=tk.RAISED, borderwidth=2, bg='#ffffff')
    frm_mostrar_imagen.grid(row=2, column=1, sticky=tk.NSEW)
    lbl_mostrar_imagen = tk.Label(master=frm_mostrar_imagen, image=imagen_raw_mostrar)
    lbl_mostrar_imagen.pack()'''
    
    frm_menu = tk.Frame(master=ventana_main, bg='#ffffff')
    frm_menu.grid(row=2, columnspan=2)

    frm_submenu1 = tk.Frame(master=frm_menu, bg='#C4D7E0')
    frm_submenu1.grid(row=0, column=0)
    frm_submenu2 = tk.Frame(master=frm_menu, bg='#C4D7E0')
    frm_submenu2.grid(row=0, column=1)
    frm_submenu3 = tk.Frame(master=frm_menu, bg='#C4D7E0')
    frm_submenu3.grid(row=0, column=2)
    frm_submenu4 = tk.Frame(master=frm_menu, bg='#C4D7E0')
    frm_submenu4.grid(row=1, column=0)
    frm_submenu5 = tk.Frame(master=frm_menu, bg='#C4D7E0')
    frm_submenu5.grid(row=1, column=1)
    frm_submenu6 = tk.Frame(master=frm_menu, bg='#C4D7E0')
    frm_submenu6.grid(row=1, column=2)

    btn_algor1 = tk.Button(master=frm_submenu1, text='ALGORITMO 1', command=llamar_ventanaAlgoritmo1)
    btn_algor2 = tk.Button(master=frm_submenu2, text='ALGORITMO 2', command=llamar_ventanaAlgoritmo2)
    btn_algor3 = tk.Button(master=frm_submenu3, text='ALGORITMO 3', command=llamar_ventanaAlgoritmo3)
    btn_algor4 = tk.Button(master=frm_submenu4, text='ALGORITMO 4', command=llamar_ventanaAlgoritmo4)
    btn_algor5 = tk.Button(master=frm_submenu5, text='ALGORITMO 5', command=llamar_ventanaAlgoritmo5)
    btn_algor6 = tk.Button(master=frm_submenu6, text='ALGORITMO 6', command=llamar_ventanaAlgoritmo6)

    btn_algor1.pack(padx=20, pady=20, ipadx=40, ipady=40)
    btn_algor2.pack(padx=20, pady=20, ipadx=40, ipady=40)
    btn_algor3.pack(padx=20, pady=20, ipadx=40, ipady=40)
    btn_algor4.pack(padx=20, pady=20, ipadx=40, ipady=40)
    btn_algor5.pack(padx=20, pady=20, ipadx=40, ipady=40)
    btn_algor6.pack(padx=20, pady=20, ipadx=40, ipady=40)
    tk.mainloop()


def main ():
    crear_Ventana_Main()

if __name__ == "__main__":
    main()