import tkinter as tk

class ClsAl6():
    def mainn():
        ventana = tk.Tk()
        ventana.title=("ALGORITMOS DE XXXXXXXXXXXXXXX")
        ventana.state("zoomed")

        ventana.rowconfigure(0, weight= 2)
        ventana.rowconfigure(1, weight= 10)
        ventana.rowconfigure(2, weight= 1)
        ventana.columnconfigure(0, weight=1 )
        #ventana.columnconfigure(1, weight= 1)

        frm_vista = tk.Frame(master=ventana)       
        frm_vista.grid(row=0, column=0, sticky=tk.NSEW)

        #titulo
        frm_titulo = tk.Frame(master=ventana, bg='#ffffff')
        frm_titulo.grid(row=0, column=0, sticky=tk.NSEW)
        lbl_titulo = tk.Label(master=frm_titulo, bg='#6E85B7', fg='#ffffff', text="NOMBRE DE ALGORITMO DOS", font=40)
        lbl_titulo.pack()    

        #cuerpo
        frm_cuerpo = tk.Frame(master=ventana,bg='#6E85B7')
        frm_cuerpo.grid(row=1, column=0, sticky=tk.NSEW)
        
        
        #aqui va el contenido

                
        lbl_titulo111 = tk.Label(master=frm_cuerpo, bg='#EB1D36', fg='#ABC9FF', text="CONTENIDO")
        lbl_titulo111.grid(row=0, column=0)

        #-----------       
        #pie
        frm_menu = tk.Frame(master=ventana, relief=tk.RAISED, borderwidth=2, bg='#78D5D7')
        frm_menu.grid(row=2, column=0, sticky=tk.E)
        frm_submenu1 = tk.Frame(master=frm_menu, bg='#C4D7E0')
        frm_submenu1.grid(row=0, column=0)
        btn_atras = tk.Button(master=frm_submenu1, text='ATRAS')
        btn_atras.grid(row=0, column=0, ipadx=20, ipady =20, padx=20, pady=20)
        btn_sigu = tk.Button(master=frm_submenu1, text='SALIR')
        btn_sigu.grid(row=0, column=1, ipadx=20, ipady =20, padx=20, pady=20)

        

        ventana.mainloop()