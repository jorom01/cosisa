# -*- coding: utf-8 -*-
from Tkinter import *
import ttk
import tkFileDialog
import tkMessageBox
from subproceso import arcgis
import os
from PIL import Image, ImageTk 
import tkinter as tk
ventana = Tk()
ventana.geometry('1100x550')
ventana.title("COSISA: Co-seismic Slope Instabilities Susceptibility Assessment")
ventana.resizable(width=False , height=False)
centiInicialSetupDirectorio = False
uriMapaFriccion10,uriMapaFriccion50,uriMapaFriccion90 = None, None, None
uriMapaCohesion10,uriMapaCohesion50,uriMapaCohesion90 = None, None, None
uriMapaDensidad10,uriMapaDensidad50,uriMapaDensidad90 = None, None, None
uriMapaLitologico, uriMapaPendientes, uriMapaPGA, uriMapaIA, uriSalidaMapas = None, None, None, None, None 
pendMin,MW, SATURADO,espesorNiveles = 10,None, 0, 1
JR07_1,JR07_2,JR07_3,JR07_4,BT07,SR08_1,SR08_2,RS09,HL11,JL18,DJ20 = False,False,False,False,False,False,False,False,False,False,False
PesJR07_1,PesJR07_2,PesJR07_3,PesJR07_4,PesBT07,PesSR08_1,PesSR08_2,PesRS09,PesHL11,PesJL18,PesDJ20 = 1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0
PesFi10,PesFi50,PesFi90, PesCoeh10,PesCoeh50,PesCoeh90, PesD10, PesD50, PesD90 = 1.0,1.0,1.0, 1.0,1.0,1.0, 1.0,1.0,1.0
valorPendiente = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,3,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,4,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,5,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,6,6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8,6.9,7,7.1,7.2,7.3,7.4,7.5,7.6,7.7,7.8,7.9,8,8.1,8.2,8.3,8.4,8.5,8.6,8.7,8.8,8.9,9,9.1,9.2,9.3,9.4,9.5,9.6,9.7,9.8,9.9,10,10.1,10.2,10.3,10.4,10.5,10.6,10.7,10.8,10.9,11,11.1,11.2,11.3,11.4,11.5,11.6,11.7,11.8,11.9,12,12.1,12.2,12.3,12.4,12.5,12.6,12.7,12.8,12.9,13,13.1,13.2,13.3,13.4,13.5,13.6,13.7,13.8,13.9,14,14.1,14.2,14.3,14.4,14.5,14.6,14.7,14.8,14.9,15,15.1,15.2,15.3,15.4,15.5,15.6,15.7,15.8,15.9,16,16.1,16.2,16.3,16.4,16.5,16.6,16.7,16.8,16.9,17,17.1,17.2,17.3,17.4,17.5,17.6,17.7,17.8,17.9,18,18.1,18.2,18.3,18.4,18.5,18.6,18.7,18.8,18.9,19,19.1,19.2,19.3,19.4,19.5,19.6,19.7,19.8,19.9,20,20.1,20.2,20.3,20.4,20.5,20.6,20.7,20.8,20.9,21,21.1,21.2,21.3,21.4,21.5,21.6,21.7,21.8,21.9,22,22.1,22.2,22.3,22.4,22.5,22.6,22.7,22.8,22.9,23,23.1,23.2,23.3,23.4,23.5,23.6,23.7,23.8,23.9,24,24.1,24.2,24.3,24.4,24.5,24.6,24.7,24.8,24.9,25,25.1,25.2,25.3,25.4,25.5,25.6,25.7,25.8,25.9,26,26.1,26.2,26.3,26.4,26.5,26.6,26.7,26.8,26.9,27,27.1,27.2,27.3,27.4,27.5,27.6,27.7,27.8,27.9,28,28.1,28.2,28.3,28.4,28.5,28.6,28.7,28.8,28.9,29,29.1,29.2,29.3,29.4,29.5,29.6,29.7,29.8,29.9,30,30.1,30.2,30.3,30.4,30.5,30.6,30.7,30.8,30.9,31,31.1,31.2,31.3,31.4,31.5,31.6,31.7,31.8,31.9,32,32.1,32.2,32.3,32.4,32.5,32.6,32.7,32.8,32.9,33,33.1,33.2,33.3,33.4,33.5,33.6,33.7,33.8,33.9,34,34.1,34.2,34.3,34.4,34.5,34.6,34.7,34.8,34.9,35,35.1,35.2,35.3,35.4,35.5,35.6,35.7,35.8,35.9,36,36.1,36.2,36.3,36.4,36.5,36.6,36.7,36.8,36.9,37,37.1,37.2,37.3,37.4,37.5,37.6,37.7,37.8,37.9,38,38.1,38.2,38.3,38.4,38.5,38.6,38.7,38.8,38.9,39,39.1,39.2,39.3,39.4,39.5,39.6,39.7,39.8,39.9,40,40.1,40.2,40.3,40.4,40.5,40.6,40.7,40.8,40.9,41,41.1,41.2,41.3,41.4,41.5,41.6,41.7,41.8,41.9,42,42.1,42.2,42.3,42.4,42.5,42.6,42.7,42.8,42.9,43,43.1,43.2,43.3,43.4,43.5,43.6,43.7,43.8,43.9,44,44.1,44.2,44.3,44.4,44.5,44.6,44.7,44.8,44.9,45,45.1,45.2,45.3,45.4,45.5,45.6,45.7,45.8,45.9,46,46.1,46.2,46.3,46.4,46.5,46.6,46.7,46.8,46.9,47,47.1,47.2,47.3,47.4,47.5,47.6,47.7,47.8,47.9,48,48.1,48.2,48.3,48.4,48.5,48.6,48.7,48.8,48.9,49,49.1,49.2,49.3,49.4,49.5,49.6,49.7,49.8,49.9,50,50.1,50.2,50.3,50.4,50.5,50.6,50.7,50.8,50.9,51,51.1,51.2,51.3,51.4,51.5,51.6,51.7,51.8,51.9,52,52.1,52.2,52.3,52.4,52.5,52.6,52.7,52.8,52.9,53,53.1,53.2,53.3,53.4,53.5,53.6,53.7,53.8,53.9,54,54.1,54.2,54.3,54.4,54.5,54.6,54.7,54.8,54.9,55,55.1,55.2,55.3,55.4,55.5,55.6,55.7,55.8,55.9,56,56.1,56.2,56.3,56.4,56.5,56.6,56.7,56.8,56.9,57,57.1,57.2,57.3,57.4,57.5,57.6,57.7,57.8,57.9,58,58.1,58.2,58.3,58.4,58.5,58.6,58.7,58.8,58.9,59,59.1,59.2,59.3,59.4,59.5,59.6,59.7,59.8,59.9,60,60.1,60.2,60.3,60.4,60.5,60.6,60.7,60.8,60.9,61,61.1,61.2,61.3,61.4,61.5,61.6,61.7,61.8,61.9,62,62.1,62.2,62.3,62.4,62.5,62.6,62.7,62.8,62.9,63,63.1,63.2,63.3,63.4,63.5,63.6,63.7,63.8,63.9,64,64.1,64.2,64.3,64.4,64.5,64.6,64.7,64.8,64.9,65,65.1,65.2,65.3,65.4,65.5,65.6,65.7,65.8,65.9,66,66.1,66.2,66.3,66.4,66.5,66.6,66.7,66.8,66.9,67,67.1,67.2,67.3,67.4,67.5,67.6,67.7,67.8,67.9,68,68.1,68.2,68.3,68.4,68.5,68.6,68.7,68.8,68.9,69,69.1,69.2,69.3,69.4,69.5,69.6,69.7,69.8,69.9,70,70.1,70.2,70.3,70.4,70.5,70.6,70.7,70.8,70.9,71,71.1,71.2,71.3,71.4,71.5,71.6,71.7,71.8,71.9,72,72.1,72.2,72.3,72.4,72.5,72.6,72.7,72.8,72.9,73,73.1,73.2,73.3,73.4,73.5,73.6,73.7,73.8,73.9,74,74.1,74.2,74.3,74.4,74.5,74.6,74.7,74.8,74.9,75,75.1,75.2,75.3,75.4,75.5,75.6,75.7,75.8,75.9,76,76.1,76.2,76.3,76.4,76.5,76.6,76.7,76.8,76.9,77,77.1,77.2,77.3,77.4,77.5,77.6,77.7,77.8,77.9,78,78.1,78.2,78.3,78.4,78.5,78.6,78.7,78.8,78.9,79,79.1,79.2,79.3,79.4,79.5,79.6,79.7,79.8,79.9,80,80.1,80.2,80.3,80.4,80.5,80.6,80.7,80.8,80.9,81,81.1,81.2,81.3,81.4,81.5,81.6,81.7,81.8,81.9,82,82.1,82.2,82.3,82.4,82.5,82.6,82.7,82.8,82.9,83,83.1,83.2,83.3,83.4,83.5,83.6,83.7,83.8,83.9,84,84.1,84.2,84.3,84.4,84.5,84.6,84.7,84.8,84.9,85,85.1,85.2,85.3,85.4,85.5,85.6,85.7,85.8,85.9,86,86.1,86.2,86.3,86.4,86.5,86.6,86.7,86.8,86.9,87,87.1,87.2,87.3,87.4,87.5,87.6,87.7,87.8,87.9,88,88.1,88.2,88.3,88.4,88.5,88.6,88.7,88.8,88.9,89,89.1,89.2,89.3,89.4,89.5,89.6,89.7,89.8,89.9]
valorMW = valorPendiente[0:99]
valorFREATICO = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
num_niveles, peso_niveles, num_casos_saturacion, saturaciones = [1],[1],[1],[1]
enablePeso = True 
Info_Welcome = "COSISA is a software developed by researcher J.C. Roman-Herrera from the Complutense University of Madrid,\nin collaboration with the University of Alicante. It automates risk mapping and calculations to assess slope stability\nin co-seismic landslides. Developed in Python and ArcGIS, COSISA optimizes analysis by efficiently managing\ngeoreferenced raster data, such as geomorphological variables, geotechnical properties, and seismic parameters,\nusing Newmark displacement and a probabilistic tree methodology."
Info_MapaBase = "                            Enter the slope map in sexagesimal degrees with ArcGIS format. Simply select the root folder where it is located.\n\n                            The minimum working slope angle can be filtered in order to use only those values with a slope greater than or equal\n                                to the angle selected in the minimum work slope field."
Info_DatosGeotecnicos ="                            Select the corresponding georeferenced maps in the correct units as input data for the program."
Info_ProfundidadRotura = "    Select the degree of soil saturation (0 for dry, 100 for complete saturation), the number of levels to analyze, and the average depth, which is homogeneous for all."
def componentes_tab1(tabulador):
    def buscarPendientes():
        filename = tkFileDialog.askdirectory()
        if filename == "":
            filename = "No file selected, please try again." 
        else:
            global uriMapaPendientes
            uriMapaPendientes = filename
        lbl_uri_pend.configure(text=filename)
        btn_search_pend.configure(text="Change") 
    def confirmarPendMin(): 
        if spin_pend_min.get() == valorPendiente[0]:
            global pendMin
            pendMin = valorPendiente[0]
        elif float(spin_pend_min.get()) in valorPendiente:
            pendMin = float(spin_pend_min.get())
        spin_pend_min.configure(state='disabled')
        btn_pend_min.configure(text="Confirmed", state='disable')     
    tabulador.rowconfigure(0, weight=1)
    tabulador.rowconfigure(1, weight=1)
    tabulador.rowconfigure(2, weight=1)
    tabulador.rowconfigure(3, weight=1)
    tabulador.columnconfigure(0, weight=1)
    tabulador.columnconfigure(1, weight=6)
    tabulador.columnconfigure(2, weight=1)
    lbl_mapaBase = ttk.Label(tabulador, text=Info_MapaBase, font=('Arial', 11, 'normal'))
    lbl_mapaBase.grid(row=0, column=0, sticky="NEWS", pady=5, padx=1, columnspan=3)
    lbl_pend = ttk.Label(tabulador, text="SLOPE MAP: ", font=('Arial', 9, 'bold'), anchor="e")  
    lbl_uri_pend = ttk.Label(tabulador, text="Select the slope map in sexagesimal degrees for the study area") 
    btn_search_pend = ttk.Button(tabulador, text="Search", command=buscarPendientes)
    lbl_pend.grid(row=1, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_pend.grid(row=1, column=1, sticky="NEWS", pady=10)
    btn_search_pend.grid(row=1, column=2, sticky="NEWS", pady=10, padx=5)
    lbl_pend_min = ttk.Label(tabulador, text="MINIMUM WORKING SLOPE IN DEGREES: ", font=('Arial', 9, 'bold'), anchor="e") 
    lbl_pend_min.grid(row=2, column=0, sticky="NEWS", pady=10, padx=5)
    spin_pend_min = Spinbox(tabulador, from_=0, to=90, values="", state='normal') 
    btn_pend_min = ttk.Button(tabulador, text="Confirm", command=confirmarPendMin) 
    spin_pend_min.grid(row=2, column=1, sticky="NEWS", pady=10)
    btn_pend_min.grid(row=2, column=2, sticky="NEWS", pady=10, padx=5)
    lbl_RellenoMapaBase = ttk.Label(tabulador, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", font=('Arial', 11, 'normal'))
    lbl_RellenoMapaBase.grid(row=3, column=0, sticky="NEWS", pady=1, padx=1, columnspan=3)
def componentes_tab2(tabulador):
    def confirmarPesoFriccion():
        global PesFi10, PesFi50, PesFi90
        PesFi10, PesFi50, PesFi90 = entry_per_10_fric.get(), entry_per_50_fric.get(), entry_per_90_fric.get()
        entry_per_10_fric.configure(state='disable')
        entry_per_50_fric.configure(state='disable')
        entry_per_90_fric.configure(state='disable')
        btn_peso_fri.configure(text='Confirmed', state='disable')  
    def confirmarPesoCohesion():
        global PesCoeh10,PesCoeh50,PesCoeh90
        PesCoeh10,PesCoeh50,PesCoeh90 = entry_per_10_cohe.get(),entry_per_50_cohe.get(),entry_per_90_cohe.get()
        entry_per_10_cohe.configure(state='disable')
        entry_per_50_cohe.configure(state='disable')
        entry_per_90_cohe.configure(state='disable')
        btn_peso_cohe.configure(text='Confirmed',state='disable')  
    def confirmarPesoDensidad():
        global PesD10, PesD50, PesD90
        PesD10, PesD50, PesD90 = entry_per_10_densidad.get(), entry_per_50_densidad.get(), entry_per_90_densidad.get()
        entry_per_10_densidad.configure(state='disable')
        entry_per_50_densidad.configure(state='disable')
        entry_per_90_densidad.configure(state='disable')
        btn_peso_densidad.configure(text='Confirmed', state='disable')  
    def buscarDensidad10():
        filename = tkFileDialog.askdirectory()
        if filename == "":
            filename = "No file selected, please try again."  
        else:
            global uriMapaDensidad10
            uriMapaDensidad10 = filename
        lbl_uri_densidad_10.configure(text=filename)
        btn_search_densidad_10.configure(text="Change")     
    def buscarDensidad50():
        filename = tkFileDialog.askdirectory()
        if filename == "":
            filename = "No file selected, please try again."  
        else:
            global uriMapaDensidad50
            uriMapaDensidad50 = filename
        lbl_uri_densidad_50.configure(text=filename)
        btn_search_densidad_50.configure(text="Change")     
    def buscarDensidad90():
        filename = tkFileDialog.askdirectory()
        if filename == "":
            filename = "No file selected, please try again."  
        else:
            global uriMapaDensidad90
            uriMapaDensidad90 = filename
        lbl_uri_densidad_90.configure(text=filename)
        btn_search_densidad_90.configure(text="Change")  
    def buscarFriccion10():
        filename = tkFileDialog.askdirectory()
        if filename == "":
            filename = "No file selected, please try again."  
        else:
            global uriMapaFriccion10
            uriMapaFriccion10 = filename
        lbl_uri_fric_10.configure(text=filename)
        btn_search_fric_10.configure(text="Change")   
        if enablePeso:
            pass
        else:
            entry_per_10_fric.configure(state='disable')
            entry_per_50_fric.configure(state='disable')
            entry_per_90_fric.configure(state='disable')
            btn_peso_fri.configure(state='disable')
            entry_per_10_cohe.configure(state='disable')
            entry_per_50_cohe.configure(state='disable')
            entry_per_90_cohe.configure(state='disable')
            btn_peso_cohe.configure(state='disable')
            entry_per_10_densidad.configure(state='disable')
            entry_per_50_densidad.configure(state='disable')
            entry_per_90_densidad.configure(state='disable')
            btn_peso_densidad.configure(state='disable')
    def buscarFriccion50():
        filename = tkFileDialog.askdirectory()
        if filename == "":
            filename = "No file selected, please try again."  
        else:
            global uriMapaFriccion50
            uriMapaFriccion50 = filename
        lbl_uri_fric_50.configure(text=filename)
        btn_search_fric_50.configure(text="Change")  
    def buscarFriccion90():
        filename = tkFileDialog.askdirectory()
        if filename == "":
            filename = "No file selected, please try again."  
        else:
            global uriMapaFriccion90
            uriMapaFriccion90 = filename
        lbl_uri_fric_90.configure(text=filename)
        btn_search_fric_90.configure(text="Change")  
    def buscarCohesion10():
        filename = tkFileDialog.askdirectory()
        if filename == "":
            filename = "No file selected, please try again."  
        else:
            global uriMapaCohesion10
            uriMapaCohesion10 = filename
        lbl_uri_cohe_10.configure(text=filename)
        btn_search_cohe_10.configure(text="Change")  
    def buscarCohesion50():
        filename = tkFileDialog.askdirectory()
        if filename == "":
            filename = "No file selected, please try again."  
        else:
            global uriMapaCohesion50
            uriMapaCohesion50 = filename
        lbl_uri_cohe_50.configure(text=filename)
        btn_search_cohe_50.configure(text="Change")  
    def buscarCohesion90():
        filename = tkFileDialog.askdirectory()
        if filename == "":
            filename = "No file selected, please try again."  
        else:
            global uriMapaCohesion90
            uriMapaCohesion90 = filename
        lbl_uri_cohe_90.configure(text=filename)
        btn_search_cohe_90.configure(text="Change")  
    tabulador.rowconfigure(0, weight=1)
    tabulador.rowconfigure(1, weight=1)
    tabulador.rowconfigure(2, weight=1)
    tabulador.rowconfigure(3, weight=1)
    tabulador.rowconfigure(4, weight=1)
    tabulador.rowconfigure(5, weight=1)
    tabulador.rowconfigure(6, weight=1)
    tabulador.rowconfigure(7, weight=1)
    tabulador.rowconfigure(8, weight=1)
    tabulador.rowconfigure(9, weight=1)
    tabulador.rowconfigure(10, weight=1)
    tabulador.columnconfigure(0, weight=1)
    tabulador.columnconfigure(1, weight=1)
    tabulador.columnconfigure(2, weight=1)
    tabulador.columnconfigure(3, weight=1)
    tabulador.columnconfigure(4, weight=4)
    tabulador.columnconfigure(5, weight=1)
    tabulador.columnconfigure(6, weight=1)
    tabulador.columnconfigure(7, weight=1)
    tabulador.columnconfigure(8, weight=1)
    lbl_DatosGeotecnicos = ttk.Label(tabulador, text=Info_DatosGeotecnicos, font=('Arial', 11, 'normal'))
    lbl_DatosGeotecnicos.grid(row=0, column=0, sticky="NEWS", pady=5, padx=1, columnspan=7)
    lbl_per_10 = ttk.Label(tabulador, text="WEIGHTS", font=('Arial', 9, 'bold'), anchor="center")  
    lbl_per_10.grid(row=1, column=6, sticky="SNEW", pady=10)
    btn_peso_fri = ttk.Button(tabulador, text="Confirm Friction Weights", command=confirmarPesoFriccion)  
    btn_peso_fri.grid(row=2, column=7, sticky="NEWS", pady=10, padx=5, rowspan=3, columnspan=1)
    btn_peso_cohe = ttk.Button(tabulador, text="Confirm Cohesion Weights", command=confirmarPesoCohesion)  
    btn_peso_cohe.grid(row=5, column=7, sticky="NEWS", pady=10, padx=5, rowspan=3, columnspan=1)
    btn_peso_densidad = ttk.Button(tabulador, text="Confirm Density Weights", command=confirmarPesoDensidad)  
    btn_peso_densidad.grid(row=8, column=7, sticky="NEWS", pady=10, padx=5, rowspan=3, columnspan=1)
    lbl_fric_10 = ttk.Label(tabulador, text="FRICTION MAP P10: ", font=('Arial', 9, 'bold'), anchor="e")  
    lbl_uri_fric_10 = ttk.Label(tabulador, text="Select the friction map corresponding to the tenth percentile in sexagesimal degrees.")  
    btn_search_fric_10  = ttk.Button(tabulador, text="Search", command=buscarFriccion10)  
    lbl_fric_10.grid(row=2, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_fric_10.grid(row=2, column=1, sticky="NEWS", pady=10,columnspan=4)
    btn_search_fric_10.grid(row=2, column=5, sticky="NEWS", pady=10, padx=5)
    entry_per_10_fric = ttk.Entry(tabulador, width=5)
    entry_per_10_fric.insert(0, "0.333")
    entry_per_10_fric.grid(row=2, column=6, sticky="NEWS", pady=10)
    lbl_fric_50 = ttk.Label(tabulador, text="FRICTION MAP P50: ", font=('Arial', 9, 'bold'), anchor="e")  
    lbl_uri_fric_50 = ttk.Label(tabulador, text="Select the friction map corresponding to the fiftieth percentile in sexagesimal degrees.")  
    btn_search_fric_50  = ttk.Button(tabulador, text="Search", command=buscarFriccion50)  
    lbl_fric_50.grid(row=3, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_fric_50.grid(row=3, column=1, sticky="NEWS", pady=10,columnspan=4)
    btn_search_fric_50.grid(row=3, column=5, sticky="NEWS", pady=10, padx=5)
    entry_per_50_fric = ttk.Entry(tabulador, width=5)
    entry_per_50_fric.insert(0, "0.333")
    entry_per_50_fric.grid(row=3, column=6, sticky="NEWS", pady=10)
    lbl_fric_90 = ttk.Label(tabulador, text="FRICTION MAP P90: ", font=('Arial', 9, 'bold'), anchor="e")  
    lbl_uri_fric_90 = ttk.Label(tabulador, text="Select the friction map corresponding to the ninetieth percentile in sexagesimal degrees.")  
    btn_search_fric_90  = ttk.Button(tabulador, text="Search", command=buscarFriccion90)  
    lbl_fric_90.grid(row=4, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_fric_90.grid(row=4, column=1, sticky="NEWS", pady=10,columnspan=4)
    btn_search_fric_90.grid(row=4, column=5, sticky="NEWS", pady=10, padx=5)
    entry_per_90_fric = ttk.Entry(tabulador, width=5)
    entry_per_90_fric.insert(0, "0.333")
    entry_per_90_fric.grid(row=4, column=6, sticky="NEWS", pady=10)
    lbl_cohe_10 = ttk.Label(tabulador, text="COHESION MAP P10 (kN/m2): ", font=('Arial', 9, 'bold'), anchor="e")  
    lbl_uri_cohe_10 = ttk.Label(tabulador, text="Select the cohesion map corresponding to the tenth percentile in kilonewtons per square meter (kN/m2)")  
    btn_search_cohe_10 = ttk.Button(tabulador, text="Search", command=buscarCohesion10)  
    lbl_cohe_10.grid(row=5, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_cohe_10.grid(row=5, column=1, sticky="NEWS", pady=10,columnspan=4)
    btn_search_cohe_10.grid(row=5, column=5, sticky="NEWS", pady=10, padx=5)
    entry_per_10_cohe = ttk.Entry(tabulador, width=5)
    entry_per_10_cohe.insert(0, "0.333")
    entry_per_10_cohe.grid(row=5, column=6, sticky="NEWS", pady=10)
    lbl_cohe_50 = ttk.Label(tabulador, text="COHESION MAP P50 (kN/m2): ", font=('Arial', 9, 'bold'), anchor="e")  
    lbl_uri_cohe_50 = ttk.Label(tabulador, text="Select the cohesion map corresponding to the fiftieth percentile in kilonewtons per square meter (kN/m2)")  
    btn_search_cohe_50 = ttk.Button(tabulador, text="Search", command=buscarCohesion50)  
    lbl_cohe_50.grid(row=6, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_cohe_50.grid(row=6, column=1, sticky="NEWS", pady=10,columnspan=4)
    btn_search_cohe_50.grid(row=6, column=5, sticky="NEWS", pady=10, padx=5)
    entry_per_50_cohe = ttk.Entry(tabulador, width=5)
    entry_per_50_cohe.insert(0, "0.333")
    entry_per_50_cohe.grid(row=6, column=6, sticky="NEWS", pady=10)
    lbl_cohe_90 = ttk.Label(tabulador, text="COHESION MAP P90 (kN/m2): ", font=('Arial', 9, 'bold'), anchor="e")  
    lbl_uri_cohe_90 = ttk.Label(tabulador, text="Select the cohesion map corresponding to the ninetieth percentile in kilonewtons per square meter (kN/m2)")  
    btn_search_cohe_90 = ttk.Button(tabulador, text="Search", command=buscarCohesion90)  
    lbl_cohe_90.grid(row=7, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_cohe_90.grid(row=7, column=1, sticky="NEWS", pady=10,columnspan=4)
    btn_search_cohe_90.grid(row=7, column=5, sticky="NEWS", pady=10, padx=5)
    entry_per_90_cohe = ttk.Entry(tabulador, width=5)
    entry_per_90_cohe.insert(0, "0.333")
    entry_per_90_cohe.grid(row=7, column=6, sticky="NEWS", pady=10)
    lbl_densidad_10 = ttk.Label(tabulador, text="UNIT WEIGHT MAP P10 (kN/m3): ", font=('Arial', 9, 'bold'), anchor="e")  
    lbl_uri_densidad_10 = ttk.Label(tabulador, text="Select the unit weight map in kilonewtons per cubic meter (kN/m3)")  
    btn_search_densidad_10 = ttk.Button(tabulador, text="Search", command=buscarDensidad10)  
    lbl_densidad_10.grid(row=8, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_densidad_10.grid(row=8, column=1, sticky="NEWS", pady=10,columnspan=4)
    btn_search_densidad_10.grid(row=8, column=5, sticky="NEWS", pady=10, padx=5)
    entry_per_10_densidad = ttk.Entry(tabulador, width=5)
    entry_per_10_densidad.insert(0, "0.333")
    entry_per_10_densidad.grid(row=8, column=6, sticky="NEWS", pady=10)
    lbl_densidad_50 = ttk.Label(tabulador, text="UNIT WEIGHT MAP P50 (kN/m2): ", font=('Arial', 9, 'bold'), anchor="e")  
    lbl_uri_densidad_50 = ttk.Label(tabulador, text="Select the unit weight map in kilonewtons per cubic meter (kN/m3)") 
    btn_search_densidad_50 = ttk.Button(tabulador, text="Search", command=buscarDensidad50) 
    lbl_densidad_50.grid(row=9, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_densidad_50.grid(row=9, column=1, sticky="NEWS", pady=10,columnspan=4)
    btn_search_densidad_50.grid(row=9, column=5, sticky="NEWS", pady=10, padx=5)
    entry_per_50_densidad = ttk.Entry(tabulador, width=5)
    entry_per_50_densidad.insert(0, "0.333")
    entry_per_50_densidad.grid(row=9, column=6, sticky="NEWS", pady=10)
    lbl_densidad_90 = ttk.Label(tabulador, text="UNIT WEIGHT MAP P90 (kN/m2): ", font=('Arial', 9, 'bold'), anchor="e")  
    lbl_uri_densidad_90 = ttk.Label(tabulador, text="Select the unit weight map in kilonewtons per cubic meter (kN/m3)")  
    btn_search_densidad_90 = ttk.Button(tabulador, text="Search", command=buscarDensidad90)  
    lbl_densidad_90.grid(row=10, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_densidad_90.grid(row=10, column=1, sticky="NEWS", pady=10,columnspan=4)
    btn_search_densidad_90.grid(row=10, column=5, sticky="NEWS", pady=10, padx=5)
    entry_per_90_densidad = ttk.Entry(tabulador, width=5)
    entry_per_90_densidad.insert(0, "0.333")
    entry_per_90_densidad.grid(row=10, column=6, sticky="NEWS", pady=10)
def componentes_tab3(tabulador):
    def confirmarEC():
        if check_variable_1.get() == 1:
            global JR07_1,PesJR07_1
            JR07_1 = True
            PesJR07_1 = entry_EcDN_1.get()
        else:
            JR07_1 = False
            entry_EcDN_1.delete("1.0", "end")
            entry_EcDN_1.insert(0, "Disabled")
        if check_variable_2.get() == 1:
            global JR07_2,PesJR07_2
            JR07_2 = True
            PesJR07_2 = entry_EcDN_2.get()
        else:
            JR07_2 = False
            entry_EcDN_2.delete(0, "end")
            entry_EcDN_2.insert(0, "Disabled")
        if check_variable_3.get() == 1:
            global JR07_3, PesJR07_3
            JR07_3 = True
            PesJR07_3 = entry_EcDN_3.get()
        else:
            JR07_3 = False
            entry_EcDN_3.delete(0, "end")
            entry_EcDN_3.insert(0, "Disabled")
        if check_variable_4.get() == 1:
            global JR07_4, PesJR07_4
            JR07_4 = True
            PesJR07_4 = entry_EcDN_4.get()
        else:
            JR07_4 = False
            entry_EcDN_4.delete(0, "end")
            entry_EcDN_4.insert(0, "Disabled")
        if check_variable_5.get() == 1:
            global BT07, PesBT07
            BT07 = True
            PesBT07 = entry_EcDN_5.get()
        else:
            BT07 = False
            entry_EcDN_5.delete(0, "end")
            entry_EcDN_5.insert(0, "Disabled")
        if check_variable_6.get() == 1:
            global SR08_1, PesSR08_1
            SR08_1 = True
            PesSR08_1 = entry_EcDN_6.get()
        else:
            SR08_1 = False
            entry_EcDN_6.delete(0, "end")
            entry_EcDN_6.insert(0, "Disabled")
        if check_variable_7.get() == 1:
            global SR08_2, PesSR08_2
            SR08_2 = True
            PesSR08_2 = entry_EcDN_7.get()
        else:
            SR08_2 = False
            entry_EcDN_7.delete(0, "end")
            entry_EcDN_7.insert(0, "Disabled")
        if check_variable_8.get() == 1:
            global RS09, PesRS09
            RS09 = True
            PesRS09 = entry_EcDN_8.get()
        else:
            RS09 = False
            entry_EcDN_8.delete(0, "end")
            entry_EcDN_8.insert(0, "Disabled")
        if check_variable_9.get() == 1:
            global HL11, PesHL11
            HL11 = True
            PesHL11 = entry_EcDN_9.get()
        else:
            HL11 = False
            entry_EcDN_9.delete(0, "end")
            entry_EcDN_9.insert(0, "Disabled")
        if check_variable_10.get() == 1:
            global JL18, PesJL18
            JL18 = True
            PesJL18 = entry_EcDN_10.get()
        else:
            JL18 = False
            entry_EcDN_10.delete(0, "end")
            entry_EcDN_10.insert(0, "Disabled")
        if check_variable_11.get() == 1:
            global DJ20, PesDJ20
            DJ20 = True
            PesDJ20 = entry_EcDN_11.get()
        else:
            DJ20 = False
            entry_EcDN_11.delete(0, "end")
            entry_EcDN_11.insert(0, "Disabled")
        chk_confirmar.configure(text="Confirmed", state='disable')  
        chk_EcDN_1.configure(state='disable')
        entry_EcDN_1.configure(state='disable')
        chk_EcDN_2.configure(state='disable')
        entry_EcDN_2.configure(state='disable')
        chk_EcDN_3.configure(state='disable')
        entry_EcDN_3.configure(state='disable')
        chk_EcDN_4.configure(state='disable')
        entry_EcDN_4.configure(state='disable')
        chk_EcDN_5.configure(state='disable')
        entry_EcDN_5.configure(state='disable')
        chk_EcDN_6.configure(state='disable')
        entry_EcDN_6.configure(state='disable')
        chk_EcDN_7.configure(state='disable')
        entry_EcDN_7.configure(state='disable')
        chk_EcDN_8.configure(state='disable')
        entry_EcDN_8.configure(state='disable')
        chk_EcDN_9.configure(state='disable')
        entry_EcDN_9.configure(state='disable')
        chk_EcDN_10.configure(state='disable')
        entry_EcDN_10.configure(state='disable')
        chk_EcDN_11.configure(state='disable')
        entry_EcDN_11.configure(state='disable')
    tabulador.rowconfigure(0, weight=1)
    tabulador.rowconfigure(1, weight=1)
    tabulador.rowconfigure(2, weight=1)
    tabulador.rowconfigure(3, weight=1)
    tabulador.rowconfigure(4, weight=1)
    tabulador.rowconfigure(5, weight=1)
    tabulador.rowconfigure(6, weight=1)
    tabulador.rowconfigure(7, weight=1)
    tabulador.rowconfigure(8, weight=1)
    tabulador.rowconfigure(9, weight=1)
    tabulador.rowconfigure(10, weight=1)
    tabulador.rowconfigure(11, weight=1)
    tabulador.rowconfigure(12, weight=1)
    tabulador.rowconfigure(13, weight=1)
    tabulador.columnconfigure(0, weight=1)
    tabulador.columnconfigure(1, weight=1)
    tabulador.columnconfigure(2, weight=1)
    tabulador.columnconfigure(3, weight=1)
    lbl_seleccionEC = ttk.Label(tabulador, text="MODEL SELECTION", font=('Arial', 9, 'bold'), anchor="center")  
    lbl_seleccionEC.grid(row=0, column=0, sticky="SNEW", pady=10, padx=0 )
    lbl_referenciaEC = ttk.Label(tabulador, text="REFERENCE", font=('Arial', 9, 'bold'), anchor="w")  
    lbl_referenciaEC.grid(row=0, column=1, sticky="SNEW", pady=10, padx=0 )
    lbl_ec = ttk.Label(tabulador, text="EQUATIONS", font=('Arial', 9, 'bold'), anchor="w")  
    lbl_ec.grid(row=0, column=2, sticky="SNEW", pady=10, padx=0 )
    lbl_ec_peso = ttk.Label(tabulador, text="Weights", font=('Arial', 9, 'bold'), anchor="center")  
    lbl_ec_peso.grid(row=0, column=3, sticky="SNEW", pady=10, padx=5)   
    check_variable_1 = IntVar()
    chk_EcDN_1 = Checkbutton(tabulador, text="JR07_1", variable=check_variable_1, anchor="w")
    chk_EcDN_1.grid(row=1, column=0, sticky="NEWS", padx=50, pady=10)
    lbl_RefEcDN_1 = ttk.Label(tabulador, text="Jibson (2007)", font=('Arial', 9, 'italic'), anchor="w")
    lbl_RefEcDN_1.grid(row=1, column=1, sticky="SNEW", pady=10, padx=0 )
    lbl_EcDN_1 = ttk.Label(tabulador, text="log(Dn) = 0.215 + 2.341 * log[1-(ky/PGA)] - 1.438 * log(ky/PGA)",font=('Arial', 9, 'roman'), anchor="w")
    lbl_EcDN_1.grid(row=1, column=2, sticky="SNEW", pady=10, padx=5)
    entry_EcDN_1 = ttk.Entry(tabulador, width=5)
    entry_EcDN_1.insert(0, "1.0")
    entry_EcDN_1.grid(row=1, column=3, sticky="NEWS", pady=10)
    check_variable_2 = IntVar()
    chk_EcDN_2 = Checkbutton(tabulador, text="JR07_2", variable=check_variable_2, anchor="w")
    chk_EcDN_2.grid(row=2, column=0, sticky="NEWS", padx=50, pady=10)
    lbl_RefEcDN_2 = ttk.Label(tabulador, text="Jibson (2007)", font=('Arial', 9, 'italic'), anchor="w")
    lbl_RefEcDN_2.grid(row=2, column=1, sticky="SNEW", pady=10, padx=0 )
    lbl_EcDN_2 = ttk.Label(tabulador, text="log(Dn) = -2.710 + 2.335 * log[1-(ky/PGA)] - 1.478 * log(ky/PGA) + 0.424 * Mw",font=('Arial', 9, 'roman'), anchor="w")
    lbl_EcDN_2.grid(row=2, column=2, sticky="SNEW", pady=10, padx=5)
    entry_EcDN_2 = ttk.Entry(tabulador, width=5)
    entry_EcDN_2.insert(0, "1.0")
    entry_EcDN_2.grid(row=2, column=3, sticky="NEWS", pady=10)
    check_variable_3 = IntVar()
    chk_EcDN_3 = Checkbutton(tabulador, text="JR07_3", variable=check_variable_3, anchor="w")
    chk_EcDN_3.grid(row=3, column=0, sticky="NEWS", padx=50, pady=10)
    lbl_RefEcDN_3 = ttk.Label(tabulador, text="Jibson (2007)", font=('Arial', 9, 'italic'), anchor="w")
    lbl_RefEcDN_3.grid(row=3, column=1, sticky="SNEW", pady=10, padx=0 )
    lbl_EcDN_3 = ttk.Label(tabulador,text="log(Dn) = 2.401 * log(IA) - 3.481 * log(ky) - 3.230",font=('Arial', 9, 'roman'), anchor="w")
    lbl_EcDN_3.grid(row=3, column=2, sticky="SNEW", pady=10, padx=5)
    entry_EcDN_3 = ttk.Entry(tabulador, width=5)
    entry_EcDN_3.insert(0, "1.0")
    entry_EcDN_3.grid(row=3, column=3, sticky="NEWS", pady=10)
    check_variable_4 = IntVar()
    chk_EcDN_4 = Checkbutton(tabulador, text="JR07_4", variable=check_variable_4, anchor="w")
    chk_EcDN_4.grid(row=4, column=0, sticky="NEWS", padx=50, pady=10)
    lbl_RefEcDN_4 = ttk.Label(tabulador, text="Jibson (2007)", font=('Arial', 9, 'italic'), anchor="w")
    lbl_RefEcDN_4.grid(row=4, column=1, sticky="SNEW", pady=10, padx=0 )
    lbl_EcDN_4 = ttk.Label(tabulador, text="log(Dn) = 0.561 * log(IA) - 3.833 * log(ky/PGA) - 1.474",font=('Arial', 9, 'roman'), anchor="w")
    lbl_EcDN_4.grid(row=4, column=2, sticky="SNEW", pady=10, padx=5)
    entry_EcDN_4 = ttk.Entry(tabulador, width=5)
    entry_EcDN_4.insert(0, "1.0")
    entry_EcDN_4.grid(row=4, column=3, sticky="NEWS", pady=10)
    check_variable_5 = IntVar()
    chk_EcDN_5 = Checkbutton(tabulador, text="BT07", variable=check_variable_5, anchor="w")
    chk_EcDN_5.grid(row=5, column=0, sticky="NEWS", padx=50, pady=10)
    lbl_RefEcDN_5 = ttk.Label(tabulador, text="Bray & Travasarou (2007)", font=('Arial', 9, 'italic'), anchor="w")
    lbl_RefEcDN_5.grid(row=5, column=1, sticky="SNEW", pady=10, padx=0 )
    lbl_EcDN_5 = ttk.Label(tabulador, text="ln(Dn) = -0.22 - 2.83 * ln(ky) - 0.333 * (ln(ky))^2 + 0.566 * ln(ky) * ln(PGA) + 3.04 * ln(PGA) - 0.244 * (lnPGA )^2 + 0.278 * (Mw - 7)",font=('Arial', 9, 'roman'), anchor="w")
    lbl_EcDN_5.grid(row=5, column=2, sticky="SNEW", pady=10, padx=5)
    entry_EcDN_5 = ttk.Entry(tabulador, width=5)
    entry_EcDN_5.insert(0, "1.0")
    entry_EcDN_5.grid(row=5, column=3, sticky="NEWS", pady=10)
    check_variable_6 = IntVar()
    chk_EcDN_6 = Checkbutton(tabulador, text="SR08_1", variable=check_variable_6, anchor="w")
    chk_EcDN_6.grid(row=6, column=0, sticky="NEWS", padx=50, pady=10)
    lbl_RefEcDN_6 = ttk.Label(tabulador, text="Saygili & Rathje (2008)", font=('Arial', 9, 'italic'), anchor="w")
    lbl_RefEcDN_6.grid(row=6, column=1, sticky="SNEW", pady=10, padx=0 )
    lbl_EcDN_6 = ttk.Label(tabulador, text="ln(Dn) = 5.52 - 4.43 * (ky/PGA) - 20.39 * (ky/PGA)^2 + 42.61 * (ky/PGA)^3 - 28.74 * (ky/PGA)^4 + 0.72 * ln(PGA)",font=('Arial', 9, 'roman'), anchor="w")
    lbl_EcDN_6.grid(row=6, column=2, sticky="SNEW", pady=10, padx=5)
    entry_EcDN_6 = ttk.Entry(tabulador, width=5)
    entry_EcDN_6.insert(0, "1.0")
    entry_EcDN_6.grid(row=6, column=3, sticky="NEWS", pady=10)
    check_variable_7 = IntVar()
    chk_EcDN_7 = Checkbutton(tabulador, text="SR08_2", variable=check_variable_7, anchor="w")
    chk_EcDN_7.grid(row=7, column=0, sticky="NEWS", padx=50, pady=10)
    lbl_RefEcDN_7 = ttk.Label(tabulador, text="Saygili & Rathje (2008)", font=('Arial', 9, 'italic'), anchor="w")
    lbl_RefEcDN_7.grid(row=7, column=1, sticky="SNEW", pady=10, padx=0 )
    lbl_EcDN_7 = ttk.Label(tabulador, text="ln(Dn) = 2.39 - 5.24 *(ky/PGA) - 18.78 * (ky/PGA)^2 + 42.01 * (ky/PGA)^3 - 29.15 * (ky/PGA)^4 - 1.56 * ln(PGA) + 1.38 * ln(IA)",font=('Arial', 9, 'roman'), anchor="w")
    lbl_EcDN_7.grid(row=7, column=2, sticky="SNEW", pady=10, padx=5)
    entry_EcDN_7 = ttk.Entry(tabulador, width=5)
    entry_EcDN_7.insert(0, "1.0")
    entry_EcDN_7.grid(row=7, column=3, sticky="NEWS", pady=10)
    check_variable_8 = IntVar()
    chk_EcDN_8 = Checkbutton(tabulador, text="RS09", variable=check_variable_8, anchor="w")
    chk_EcDN_8.grid(row=8, column=0, sticky="NEWS", padx=50, pady=10)
    lbl_RefEcDN_8 = ttk.Label(tabulador, text="Rathje & Saygili (2009)", font=('Arial', 9, 'italic'), anchor="w")
    lbl_RefEcDN_8.grid(row=8, column=1, sticky="SNEW", pady=10, padx=0 )
    lbl_EcDN_8 = ttk.Label(tabulador, text="ln(Dn) = 4.89 - 4.85 * (ky/PGA) - 19.64 * (ky/PGA)^2 + 42.49 * (ky/PGA)^3 - 29.06 * (ky/PGA)^4 + 0.72 * ln(PGA) + 0.89 * (MW-6)",font=('Arial', 9, 'roman'), anchor="w")
    lbl_EcDN_8.grid(row=8, column=2, sticky="SNEW", pady=10, padx=5)
    entry_EcDN_8 = ttk.Entry(tabulador, width=5)
    entry_EcDN_8.insert(0, "1.0")
    entry_EcDN_8.grid(row=8, column=3, sticky="NEWS", pady=10)
    check_variable_9 = IntVar()
    chk_EcDN_9 = Checkbutton(tabulador, text="HL11", variable=check_variable_9, anchor="w")
    chk_EcDN_9.grid(row=9, column=0, sticky="NEWS", padx=50, pady=10)
    lbl_RefEcDN_9 = ttk.Label(tabulador, text="Hsieh & Lee (2011)", font=('Arial', 9, 'italic'), anchor="w")
    lbl_RefEcDN_9.grid(row=9, column=1, sticky="SNEW", pady=10, padx=0 )
    lbl_EcDN_9 = ttk.Label(tabulador, text="log(Dn) = 0.847 * log(IA) - 10.62 * ky + 6.587 * ky * log(IA) + 1.84",font=('Arial', 9, 'roman'), anchor="w")
    lbl_EcDN_9.grid(row=9, column=2, sticky="SNEW", pady=10, padx=5)
    entry_EcDN_9 = ttk.Entry(tabulador, width=5)
    entry_EcDN_9.insert(0, "1.0")
    entry_EcDN_9.grid(row=9, column=3, sticky="NEWS", pady=10)
    check_variable_10 = IntVar()
    chk_EcDN_10 = Checkbutton(tabulador, text="JL18", variable=check_variable_10, anchor="w")
    chk_EcDN_10.grid(row=10, column=0, sticky="NEWS", padx=50, pady=10)
    lbl_RefEcDN_10 = ttk.Label(tabulador, text="Jia-Liang et al. (2018)", font=('Arial', 9, 'italic'), anchor="w")
    lbl_RefEcDN_10.grid(row=10, column=1, sticky="SNEW", pady=10, padx=0 )
    lbl_EcDN_10 = ttk.Label(tabulador, text="log(Dn) = 0.465 * log(IA) + 12.896 * ky * log(IA) - 22.201 * ky + 2.092",font=('Arial', 9, 'roman'), anchor="w")
    lbl_EcDN_10.grid(row=10, column=2, sticky="SNEW", pady=10, padx=5)
    entry_EcDN_10 = ttk.Entry(tabulador, width=5)
    entry_EcDN_10.insert(0, "1.0")
    entry_EcDN_10.grid(row=10, column=3, sticky="NEWS", pady=10)
    check_variable_11 = IntVar()
    chk_EcDN_11 = Checkbutton(tabulador, text="DJ20", variable=check_variable_11, anchor="w")
    chk_EcDN_11.grid(row=11, column=0, sticky="NEWS", padx=50, pady=10)
    lbl_RefEcDN_11 = ttk.Label(tabulador, text="Delgado et al. (2020)", font=('Arial', 9, 'italic'), anchor="w")
    lbl_RefEcDN_11.grid(row=11, column=1, sticky="SNEW", pady=10, padx=0 )
    lbl_EcDN_11 = ttk.Label(tabulador, text="log(Dn) = 1.416 - 11.110 * (ky/PGA)^2 + 20.421 * (ky/PGA)^3 - 13.303 * (ky/PGA)^4 - 0.279 * log(PGA) + 1.056 * log(IA)",font=('Arial', 9, 'roman'), anchor="w")
    lbl_EcDN_11.grid(row=11, column=2, sticky="SNEW", pady=10, padx=5)
    entry_EcDN_11 = ttk.Entry(tabulador, width=5)
    entry_EcDN_11.insert(0, "1.0")
    entry_EcDN_11.grid(row=11, column=3, sticky="NEWS", pady=10)
    chk_confirmar = ttk.Button(tabulador, text="CONFIRM SELECTIONS", command=confirmarEC)
    chk_confirmar.grid(row=12, column=0, sticky="NEWS", columnspan= 4, rowspan=2)
def componentes_tab4(tabulador):
    def confirmarEspesorNivel():
        global espesorNiveles
        espesorNiveles = entry_espesorNivel.get()
        entry_espesorNivel.configure(state='disable')
        btn_espesorNivel.configure(text='Confirmed',state='disable')  
    def confirmarProfundidad():
        if spin_niveles.get() == 1:
            global num_niveles
            num_niveles = [1]
        elif int(spin_niveles.get()) in [1, 2, 3, 4, 5]:
            num_niveles = list(range(1, int(spin_niveles.get()) + 1))
        spin_niveles.configure(state='disabled')
        btn_confirmar_niveles.configure(text="Confirmed", state='disable')  
        if len(num_niveles) == 1:
            entry_pesZ1.configure(state='normal')
        elif len(num_niveles) == 2:
            entry_pesZ1.configure(state='normal')
            entry_pesZ2.configure(state='normal')
        elif len(num_niveles) == 3:
            entry_pesZ1.configure(state='normal')
            entry_pesZ2.configure(state='normal')
            entry_pesZ3.configure(state='normal')
        elif len(num_niveles) == 4:
            entry_pesZ1.configure(state='normal')
            entry_pesZ2.configure(state='normal')
            entry_pesZ3.configure(state='normal')
            entry_pesZ4.configure(state='normal')
        else:
            entry_pesZ1.configure(state='normal')
            entry_pesZ2.configure(state='normal')
            entry_pesZ3.configure(state='normal')
            entry_pesZ4.configure(state='normal')
            entry_pesZ5.configure(state='normal')
        chk_confirmar_pesos.configure(state='normal')
    def confirmarPesos():
        global peso_niveles
        if len(num_niveles) == 1:
            peso_niveles = [float(entry_pesZ1.get())]
            entry_pesZ1.configure(state='disable')
        elif len(num_niveles) == 2:
            peso_niveles = [float(entry_pesZ1.get()), float(entry_pesZ2.get())]
            entry_pesZ1.configure(state='disable')
            entry_pesZ2.configure(state='disable')
        elif len(num_niveles) == 3:
            peso_niveles = [float(entry_pesZ1.get()), float(entry_pesZ2.get()), float(entry_pesZ3.get())]
            entry_pesZ1.configure(state='disable')
            entry_pesZ2.configure(state='disable')
            entry_pesZ3.configure(state='disable')
        elif len(num_niveles) == 4:
            peso_niveles = [float(entry_pesZ1.get()), float(entry_pesZ2.get()), float(entry_pesZ3.get()),
                            float(entry_pesZ4.get())]
            entry_pesZ1.configure(state='disable')
            entry_pesZ2.configure(state='disable')
            entry_pesZ3.configure(state='disable')
            entry_pesZ4.configure(state='disable')
        else:
            peso_niveles = [float(entry_pesZ1.get()), float(entry_pesZ2.get()), float(entry_pesZ3.get()),
                            float(entry_pesZ4.get()), float(entry_pesZ5.get())]
            entry_pesZ1.configure(state='disable')
            entry_pesZ2.configure(state='disable')
            entry_pesZ3.configure(state='disable')
            entry_pesZ4.configure(state='disable')
            entry_pesZ5.configure(state='disable')
        chk_confirmar_pesos.configure(text="Confirmed", state='disable')  
    tabulador.rowconfigure(0, weight=1)
    tabulador.rowconfigure(1, weight=1)
    tabulador.rowconfigure(2, weight=1)
    tabulador.rowconfigure(3, weight=1)
    tabulador.rowconfigure(4, weight=1)
    tabulador.rowconfigure(5, weight=1)
    tabulador.rowconfigure(6, weight=1)
    tabulador.rowconfigure(7, weight=1)
    tabulador.rowconfigure(8, weight=1)
    tabulador.columnconfigure(0, weight=1)
    tabulador.columnconfigure(1, weight=1)
    tabulador.columnconfigure(2, weight=1)
    lbl_ProfundidadRotura = ttk.Label(tabulador, text=Info_ProfundidadRotura, font=('Arial', 11, 'normal'))
    lbl_ProfundidadRotura.grid(row=0, column=0, sticky="NEWS", pady=5, padx=1, columnspan=7)
    lbl_espesorNivel = ttk.Label(tabulador, text="WIDTH OF THE LEVELS IN METERS: ", font=('Arial', 9, 'bold', 'italic'), anchor="e")  
    lbl_espesorNivel.grid(row=7, column=0, sticky="SNEW", pady=10, padx=5)
    entry_espesorNivel = ttk.Entry(tabulador, width=5, state='normal')
    entry_espesorNivel.insert(0, 1.0)
    entry_espesorNivel.grid(row=7, column=1, sticky="NEWS", pady=10)
    btn_espesorNivel = ttk.Button(tabulador, text="Confirm", command=confirmarEspesorNivel)  
    btn_espesorNivel.grid(row=7, column=2, sticky="NEWS", pady=10, padx=5)
    lbl_niveles = ttk.Label(tabulador, text="NUMBER OF DEPTH TO ANALYZE: ", font=('Arial', 9, 'bold'),anchor="e")  
    spin_niveles = Spinbox(tabulador, from_=0, to=90, values=[1, 2, 3, 4, 5], state='normal')
    btn_confirmar_niveles = ttk.Button(tabulador, text="Confirm", command=confirmarProfundidad)  
    lbl_niveles.grid(row=1, column=0, sticky="NEWS", pady=10, padx=5)
    spin_niveles.grid(row=1, column=1, sticky="NEWS", pady=10)
    btn_confirmar_niveles.grid(row=1, column=2, sticky="NEWS", pady=10, padx=5)
    lbl_Z1 = ttk.Label(tabulador, text="Weight Z1: ", font=('Arial', 9, 'bold', 'italic'), anchor="e")  
    lbl_Z1.grid(row=2, column=0, sticky="SNEW", pady=10, padx=5)
    entry_pesZ1 = ttk.Entry(tabulador, width=5, state='disable')
    entry_pesZ1.insert(0, 1.0)
    entry_pesZ1.grid(row=2, column=1, sticky="NEWS", pady=10)
    lbl_Z2 = ttk.Label(tabulador, text="Weight Z2: ", font=('Arial', 9, 'bold', 'italic'), anchor="e")  
    lbl_Z2.grid(row=3, column=0, sticky="SNEW", pady=10, padx=5)
    entry_pesZ2 = ttk.Entry(tabulador, width=5, state='disable')
    entry_pesZ2.insert(0, 1.0)
    entry_pesZ2.grid(row=3, column=1, sticky="NEWS", pady=10)
    lbl_Z3 = ttk.Label(tabulador, text="Weight Z3: ", font=('Arial', 9, 'bold', 'italic'), anchor="e")  
    lbl_Z3.grid(row=4, column=0, sticky="SNEW", pady=10, padx=5)
    entry_pesZ3 = ttk.Entry(tabulador, width=5, state='disable')
    entry_pesZ3.insert(0, 1.0)
    entry_pesZ3.grid(row=4, column=1, sticky="NEWS", pady=10)
    lbl_Z4 = ttk.Label(tabulador, text="Weight Z4: ", font=('Arial', 9, 'bold', 'italic'), anchor="e")  
    lbl_Z4.grid(row=5, column=0, sticky="SNEW", pady=10, padx=5)
    entry_pesZ4 = ttk.Entry(tabulador, width=5, state='disable')
    entry_pesZ4.insert(0, 1.0)
    entry_pesZ4.grid(row=5, column=1, sticky="NEWS", pady=10)
    lbl_Z5 = ttk.Label(tabulador, text="Weight Z5: ", font=('Arial', 9, 'bold', 'italic'), anchor="e")  
    lbl_Z5.grid(row=6, column=0, sticky="SNEW", pady=10, padx=5)
    entry_pesZ5 = ttk.Entry(tabulador, width=5, state='disable')
    entry_pesZ5.insert(0, 1.0)
    entry_pesZ5.grid(row=6, column=1, sticky="NEWS", pady=10)
    chk_confirmar_pesos = ttk.Button(tabulador, text="Confirm Weights", command=confirmarPesos, state='disable')  
    chk_confirmar_pesos.grid(row=2, column=2, sticky="NEWS", rowspan=5)
    lbl_RellenoMapaProfundidaddeRotura = ttk.Label(tabulador, text="\n\n\n\n\n\n\n\n\n", font=('Arial', 11, 'normal'))
    lbl_RellenoMapaProfundidaddeRotura.grid(row=8, column=0, sticky="NEWS", pady=1, padx=1, columnspan=3)
def componentes_tab5(tabulador):
    def buscarSalida():
        filename = tkFileDialog.askdirectory()
        if filename == "":
            filename = "No file selected, please try again."  
        else:
            global uriSalidaMapas
            uriSalidaMapas = filename
            global centiInicialSetupDirectorio
            centiInicialSetupDirectorio = True
        lbl_uri_salida.configure(text=filename)
        btn_search_salida.configure(text="Change") 
    def confirmarCalculoPonderado():
        if radio_variable.get() == 1:
            global enablePeso
            enablePeso = True
        else:
            enablePeso = False
    def BotonConfirmarCalculoPonderado():
        rbt_calculoPonderado1.configure(state='disabled')
        rbt_calculoPonderado2.configure(state='disabled')
        btn_ConfirmarCalculoPesos.configure(state='disabled')
    tabulador.rowconfigure(0, weight=1)
    tabulador.rowconfigure(1, weight=1)
    tabulador.rowconfigure(2, weight=1)
    tabulador.rowconfigure(3, weight=1)
    tabulador.rowconfigure(4, weight=1)
    tabulador.columnconfigure(0, weight=1)
    tabulador.columnconfigure(1, weight=10)
    tabulador.columnconfigure(2, weight=1)
    lbl_salida = ttk.Label(tabulador, text="RESULTS WRITING FOLDER: ", font=('Arial', 9, 'bold'), anchor="e") 
    lbl_uri_salida = ttk.Label(tabulador, text="Select the output directory where the calculated maps will be saved") 
    btn_search_salida = ttk.Button(tabulador, text="Search", command=buscarSalida) 
    lbl_salida.grid(row=0, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_salida.grid(row=0, column=1, sticky="NEWS", pady=10)
    btn_search_salida.grid(row=0, column=2, sticky="NEWS", pady=10, padx=5)
    lbl_calculoPonderado = ttk.Label(tabulador, text="WEIGHT BOXES: ", font=('Arial', 9, 'bold'), anchor="e")
    radio_variable = IntVar()
    rbt_calculoPonderado1 = ttk.Radiobutton(tabulador, text="Disable", variable=radio_variable, value=0, command=confirmarCalculoPonderado) 
    rbt_calculoPonderado2 = ttk.Radiobutton(tabulador, text="Activate", variable=radio_variable, value=1,command=confirmarCalculoPonderado) 
    lbl_calculoPonderado.grid(row=1, column=0, sticky="NEWS", pady=10, padx=5)
    rbt_calculoPonderado2.grid(row=1, column=1, sticky="NEWS", pady=10, padx=5)
    rbt_calculoPonderado1.grid(row=2, column=1, sticky="NEWS", pady=10, padx=5)
    btn_ConfirmarCalculoPesos = ttk.Button(tabulador, text="Confirm", command=BotonConfirmarCalculoPonderado)
    btn_ConfirmarCalculoPesos.grid(row=1, column=2, sticky="NEWS", pady=10, padx=5)
    etr_relleno = ttk.Label(tabulador, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", state='readonly', anchor="n")
    etr_relleno.grid(row=3, column=0, sticky="NEWS", rowspan=1, columnspan=3)
def componentes_tab6(tabulador):
    def buscarPGA():
        filename = tkFileDialog.askdirectory()
        if filename == "":
            filename = "No file selected, please try again." 
        else:
            global uriMapaPGA
            uriMapaPGA = filename
        lbl_uri_PGA.configure(text=filename)
        btn_search_PGA.configure(text="Change") 
    def buscarIA():
        filename = tkFileDialog.askdirectory()
        if filename == "":
            filename = "No file selected, please try again." 
        else:
            global uriMapaIA
            uriMapaIA = filename
        lbl_uri_IA.configure(text=filename)
        btn_search_IA.configure(text="Change") 
    def confirmarMW():
        if lbl_uri_MW.get() == "" or lbl_uri_MW.get() == "Variable desactivada al no existir valor":
            global MW
            MW = None
        elif float(lbl_uri_MW.get()) not in valorMW:
            print " "
        elif float(lbl_uri_MW.get()) in valorMW:
            MW = float(lbl_uri_MW.get())
        lbl_uri_MW.configure(state='disabled')
        btn_search_MW.configure(text="Confirmed")  
    tabulador.rowconfigure(0, weight=1)
    tabulador.rowconfigure(1, weight=1)
    tabulador.rowconfigure(2, weight=1)
    tabulador.rowconfigure(3, weight=1)
    tabulador.rowconfigure(4, weight=1)
    tabulador.columnconfigure(0, weight=1)
    tabulador.columnconfigure(1, weight=10)
    tabulador.columnconfigure(2, weight=1)
    lbl_PGA = ttk.Label(tabulador, text="PGA MAP: ", font=('Arial', 9, 'bold'), anchor="e")  
    lbl_uri_PGA = ttk.Label(tabulador, text="Select the PGA map in g unit")  
    btn_search_PGA = ttk.Button(tabulador, text="Search", command=buscarPGA)  
    lbl_PGA.grid(row=1, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_PGA.grid(row=1, column=1, sticky="NEWS", pady=10)
    btn_search_PGA.grid(row=1, column=2, sticky="NEWS", pady=10, padx=5)
    lbl_IA = ttk.Label(tabulador, text="IA MAP: ", font=('Arial', 9, 'bold'), anchor="e")  
    lbl_uri_IA = ttk.Label(tabulador, text="Select the IA map in unit of meters per second (m/s)")  
    btn_search_IA = ttk.Button(tabulador, text="Search", command=buscarIA)  
    lbl_IA.grid(row=2, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_IA.grid(row=2, column=1, sticky="NEWS", pady=10)
    btn_search_IA.grid(row=2, column=2, sticky="NEWS", pady=10, padx=5)
    lbl_MW = ttk.Label(tabulador, text="MAGNITUDE IN MW UNIT: ", font=('Arial', 9, 'bold'), anchor="e")  
    lbl_uri_MW = Spinbox(tabulador, from_=0, to=10, values="", state='normal') 
    btn_search_MW = ttk.Button(tabulador, text="Confirm", command=confirmarMW)  
    lbl_MW.grid(row=3, column=0, sticky="NEWS", pady=10, padx=5)
    lbl_uri_MW.grid(row=3, column=1, sticky="NEWS", pady=10)
    btn_search_MW.grid(row=3, column=2, sticky="NEWS", pady=10, padx=5)
    etr_relleno2 = ttk.Label(tabulador, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", state='readonly', anchor="n")
    etr_relleno2.grid(row=4, column=0, sticky="NEWS", rowspan=1, columnspan=3)
def componentes_tab7(tabulador):
    def cargar_y_redimensionar_imagen_con_pil(ruta, ancho, alto):
        imagen_original = Image.open(ruta)
        imagen_redimensionada = imagen_original.resize((ancho, alto), Image.ANTIALIAS)
        imagen_tk = ImageTk.PhotoImage(imagen_redimensionada)
        return imagen_tk
    def cargar_y_redimensionar_imagen_con_tkinter(ruta, width, height):
        imagen = tk.PhotoImage(file=ruta)
        imagen_redimensionada = imagen.subsample(width // 16, height // 16)
        return imagen_redimensionada
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen_ucm = os.path.join(ruta_actual, "ucm.png")
    ruta_imagen_ua = os.path.join(ruta_actual, "ua.png")
    tabulador.rowconfigure(0, weight=1)
    tabulador.rowconfigure(1, weight=1)
    tabulador.rowconfigure(2, weight=1)
    tabulador.columnconfigure(0, weight=1)
    tabulador.columnconfigure(1, weight=1)
    tabulador.columnconfigure(2, weight=1)
    lbl_texto = ttk.Label(tabulador, text=Info_Welcome, font=('Arial', 11, 'normal'))
    lbl_texto.grid(row=1, column=2, sticky="NEWS", pady=5, padx=1, columnspan=3)
    if os.path.exists(ruta_imagen_ucm):
        ucm = cargar_y_redimensionar_imagen_con_pil(ruta_imagen_ucm, 100, 100)
        lbl_ucm = ttk.Label(tabulador, image=ucm)
        lbl_ucm.image = ucm  
        lbl_ucm.grid(row=1, column=0, sticky="NEWS", pady=10, padx=15)
    else:
        lbl_ucm = ttk.Label(tabulador, text="UCM: ", font=('Arial', 9, 'bold'), anchor="e")
        lbl_ucm.grid(row=1, column=0, sticky="NEWS", pady=10, padx=15)
    if os.path.exists(ruta_imagen_ua):  
        ua = cargar_y_redimensionar_imagen_con_pil(ruta_imagen_ua, 100, 100)
        lbl_ua = ttk.Label(tabulador, image=ua)
        lbl_ua.image = ua  
        lbl_ua.grid(row=1, column=1, sticky="NEWS", pady=10, padx=5)
    else:  
        lbl_ua = ttk.Label(tabulador, text="UA: ", font=('Arial', 9, 'bold'), anchor="e")
        lbl_ua.grid(row=1, column=1, sticky="NEWS", pady=10, padx=5)
def componentes_tab8(tabulador):    
    def confirmarNumeroNivelesAgua():
        if spin_niveles.get() == 1:
            global num_casos_saturacion
            num_casos_saturacion = [1]
        elif int(spin_niveles.get()) in [1, 2, 3]:
            num_casos_saturacion = list(range(1, int(spin_niveles.get()) + 1))
        spin_niveles.configure(state='disabled')
        btn_confirmar_niveles.configure(text="Confirmed", state='disable')  
        if len(num_casos_saturacion) == 1:
            entry_pesZ1.configure(state='normal')
        elif len(num_casos_saturacion) == 2:
            entry_pesZ1.configure(state='normal')
            entry_pesZ2.configure(state='normal')
        else:
            entry_pesZ1.configure(state='normal')
            entry_pesZ2.configure(state='normal')
            entry_pesZ3.configure(state='normal')
        chk_confirmar_pesos.configure(state='normal')
    def confirmarNivelesAgua():
        global saturaciones 
        if len(num_casos_saturacion) == 1:
            saturaciones = [float(entry_pesZ1.get())]
            entry_pesZ1.configure(state='disable')
        elif len(num_casos_saturacion) == 2:
            saturaciones = [float(entry_pesZ1.get()), float(entry_pesZ2.get())]
            entry_pesZ1.configure(state='disable')
            entry_pesZ2.configure(state='disable')
        else:
            saturaciones = [float(entry_pesZ1.get()), float(entry_pesZ2.get()), float(entry_pesZ3.get())]
            entry_pesZ1.configure(state='disable')
            entry_pesZ2.configure(state='disable')
            entry_pesZ3.configure(state='disable')        
        chk_confirmar_pesos.configure(text="Confirmed", state='disable')  
    tabulador.rowconfigure(0, weight=1)
    tabulador.rowconfigure(1, weight=1)
    tabulador.rowconfigure(2, weight=1)
    tabulador.rowconfigure(3, weight=1)
    tabulador.rowconfigure(4, weight=1)
    tabulador.rowconfigure(5, weight=1)
    tabulador.columnconfigure(0, weight=1)
    tabulador.columnconfigure(1, weight=1)
    tabulador.columnconfigure(2, weight=1)
    tabulador.columnconfigure(3, weight=1)
    tabulador.columnconfigure(4, weight=1)
    tabulador.columnconfigure(5, weight=1)
    tabulador.columnconfigure(6, weight=1)
    lbl_ProfundidadRotura = ttk.Label(tabulador, text=Info_ProfundidadRotura, font=('Arial', 11, 'normal'))
    lbl_ProfundidadRotura.grid(row=0, column=0, sticky="NEWS", pady=5, padx=1, columnspan=7)
    lbl_niveles = ttk.Label(tabulador, text="NUMBER OF WATER TABLE LEVELS TO ANALYZE PER UNITS : ", font=('Arial', 9, 'bold'),anchor="e")  
    spin_niveles = Spinbox(tabulador, from_=0, to=90, values=[1, 2, 3], state='normal')
    btn_confirmar_niveles = ttk.Button(tabulador, text="Confirm", command=confirmarNumeroNivelesAgua)  
    lbl_niveles.grid(row=1, column=0, sticky="NEWS", pady=10, padx=5)
    spin_niveles.grid(row=1, column=1, sticky="NEWS", pady=10)
    btn_confirmar_niveles.grid(row=1, column=2, sticky="NEWS", pady=10, padx=5)
    lbl_Z1 = ttk.Label(tabulador, text="Level 1: ", font=('Arial', 9, 'bold', 'italic'), anchor="e")  
    lbl_Z1.grid(row=2, column=0, sticky="SNEW", pady=10, padx=5)
    entry_pesZ1 = ttk.Entry(tabulador, width=5, state='disable')
    entry_pesZ1.grid(row=2, column=1, sticky="NEWS", pady=10)
    lbl_Z2 = ttk.Label(tabulador, text="Level 2: ", font=('Arial', 9, 'bold', 'italic'), anchor="e")  
    lbl_Z2.grid(row=3, column=0, sticky="SNEW", pady=10, padx=5)
    entry_pesZ2 = ttk.Entry(tabulador, width=5, state='disable')
    entry_pesZ2.insert(0, 1.0)
    entry_pesZ2.grid(row=3, column=1, sticky="NEWS", pady=10)
    lbl_Z3 = ttk.Label(tabulador, text="Level 3: ", font=('Arial', 9, 'bold', 'italic'), anchor="e")  
    lbl_Z3.grid(row=4, column=0, sticky="SNEW", pady=10, padx=5)
    entry_pesZ3 = ttk.Entry(tabulador, width=5, state='disable')
    entry_pesZ3.insert(0, 1.0)
    entry_pesZ3.grid(row=4, column=1, sticky="NEWS", pady=10)
    chk_confirmar_pesos = ttk.Button(tabulador, text="Confirm", command=confirmarNivelesAgua, state='disable') 
    chk_confirmar_pesos.grid(row=2, column=2, sticky="NEWS", rowspan=3)
    lbl_RellenoMapaProfundidaddeRotura = ttk.Label(tabulador, text="\n\n\n\n\n\n\n\n\n", font=('Arial', 11, 'normal'))
    lbl_RellenoMapaProfundidaddeRotura.grid(row=5, column=0, sticky="NEWS", pady=1, padx=1, columnspan=3)
def componentes_tab9(tabulador):
    def calcular():
        resumen = str("*"*101 + "\n" +
                      "RESUMEN DE VARIABLES".center(75+len("RESUMEN DE VARIABLES"),"*") + "\n" +
                      "*"*101 + "\n" +
                      "DIRECTORIO DE SALIDAS: " + ("No se ha asignado ningun directorio." if uriSalidaMapas == None else str(uriSalidaMapas)) + "\n" +
                      "URI_LITOLOGICO: " + ("No se ha cargado mapa litologico." if uriMapaLitologico==None else str(uriMapaLitologico)) + "\n" +
                      "URI_PENDIENTES: " + ("No se ha cargado mapa de pendientes." if uriMapaPendientes==None else str(uriMapaPendientes)) + "\n" +
                      "PENDIENTE_MINIMA: " + str(pendMin) + "(grad)." + "\n" +
                      "URI_FRICCION10: " + ("No se ha cargado mapa de friccion 10." if uriMapaFriccion10 == None else str(uriMapaFriccion10)) + "\n" +
                      "URI_FRICCION50: " + ("No se ha cargado mapa de friccion 50." if uriMapaFriccion50 == None else str(uriMapaFriccion50)) + "\n" +
                      "URI_FRICCION90: " + ("No se ha cargado mapa de friccion 90." if uriMapaFriccion90 == None else str(uriMapaFriccion90)) + "\n" +
                      "PESO_FRICCION(10,50,90): " + str(PesFi10) + " - " + str(PesFi50) + " - " + str(PesFi90) + "\n" +
                      "URI_COHESION10: " + ("No se ha cargado mapa de cohesion 10." if uriMapaCohesion10 == None else str(uriMapaCohesion10)) + "\n" +
                      "URI_COHESION50: " + ("No se ha cargado mapa de cohesion 50." if uriMapaCohesion50 == None else str(uriMapaCohesion50)) + "\n" +
                      "URI_COHESION90: " + ("No se ha cargado mapa de cohesion 90." if uriMapaCohesion90 == None else str(uriMapaCohesion90)) + "\n" +
                      "PESO_COHESION(10,50,90): " + str(PesCoeh10) + " - " + str(PesCoeh50) + " - " + str(PesCoeh90) + "\n" +
                      "URI_DENSIDAD: " + ("No se ha cargado mapa de densidad." if uriMapaDensidad==None else str(uriMapaDensidad)) + "\n" +
                      "URI_PGA: " + ("No se ha cargado mapa de PGA." if uriMapaPGA==None else str(uriMapaPGA))  + "\n" +
                      "URI_IA: " + ("No se ha cargado mapa de IA." if uriMapaIA==None else str(uriMapaIA)) + "\n" +
                      "MAGNITUD: " + ("No se ha eligido magnitud." if MW==None else str(MW)+" mw") + "\n" +
                      "EC_JR07_1: " + ("No se ha seleccionado la ecuacion para el calculo." if JR07_1==False else "Se ha seleccionado para el calculo, con un peso de " +str(PesJR07_1)) + "\n" +
                      "EC_JR07_2: " + ("No se ha seleccionado la ecuacion para el calculo." if JR07_2==False else "Se ha seleccionado para el calculo, con un peso de " +str(PesJR07_2)) + "\n" +
                      "EC_JR07_3: " + ("No se ha seleccionado la ecuacion para el calculo." if JR07_3==False else "Se ha seleccionado para el calculo, con un peso de " +str(PesJR07_3)) + "\n" +
                      "EC_JR07_4: " + ("No se ha seleccionado la ecuacion para el calculo." if JR07_4==False else "Se ha seleccionado para el calculo, con un peso de " +str(PesJR07_4)) + "\n" +
                      "EC_BT07: " + ("No se ha seleccionado la ecuacion para el calculo." if BT07==False else "Se ha seleccionado para el calculo, con un peso de " +str(PesBT07)) + "\n" +
                      "EC_SR08_1: " + ("No se ha seleccionado la ecuacion para el calculo." if SR08_1==False else "Se ha seleccionado para el calculo, con un peso de " +str(PesSR08_1)) + "\n" +
                      "EC_SR08_2: " + ("No se ha seleccionado la ecuacion para el calculo." if SR08_2==False else "Se ha seleccionado para el calculo, con un peso de " +str(PesSR08_2)) + "\n" +
                      "EC_RS09: " + ("No se ha seleccionado la ecuacion para el calculo." if RS09==False else "Se ha seleccionado para el calculo, con un peso de " +str(PesRS09)) + "\n" +
                      "EC_HL11: " + ("No se ha seleccionado la ecuacion para el calculo." if HL11==False else "Se ha seleccionado para el calculo, con un peso de " +str(PesHL11)) + "\n" +
                      "EC_JL18: " + ("No se ha seleccionado la ecuacion para el calculo." if JL18==False else "Se ha seleccionado para el calculo, con un peso de " +str(PesJL18)) + "\n" +
                      "EC_DJ20: " + ("No se ha seleccionado la ecuacion para el calculo." if DJ20==False else "Se ha seleccionado para el calculo, con un peso de " +str(PesDJ20)) + "\n" +
                      "NIVEL_FRATICO: " + ("Sin nivel freatico (m=0)" if SATURADO==0 else "Todos los materiales saturados (m=1)") + "\n" +
                      "ESPESOR DE LOS NIVELES: " + str(espesorNiveles)+ "(m)."  + "\n" +
                      "NUMERO DE NIVELES: " + str(len(num_niveles)) + " cuyos pesos son: " + str(peso_niveles) + "\n" +
                      "*"*101 + "\n" +
                      "*"*101 + "\n" +
                      "*"*101 + "\n")
        etr_resumen.configure(text=resumen)
        btn_calcular.configure(text="Calculating", state='disable') 
        btn_search_salida.configure(text="Fixed", state='disable') 
        arcgis(MW,uriSalidaMapas,SATURADO,uriMapaPendientes,uriMapaIA,uriMapaPGA,uriMapaDensidad,num_niveles, uriMapaFriccion10,uriMapaFriccion50,uriMapaFriccion90,uriMapaCohesion10,uriMapaCohesion50,uriMapaCohesion90,JR07_1,JR07_2,JR07_3,JR07_4,BT07,SR08_1,SR08_2,RS09,HL11,JL18,DJ20)
    tabulador.rowconfigure(0, weight=1)
    tabulador.rowconfigure(1, weight=1)
    tabulador.columnconfigure(0, weight=1)
    tabulador.columnconfigure(1, weight=10)
    etr_resumen = ttk.Label(tabulador, text="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", state='readonly', anchor="n")
    etr_resumen.grid(row=0, column=0, sticky="NEWS", rowspan=1, columnspan=3)
    btn_calcular = ttk.Button(tabulador, text="CALCULATE MAPS", command=calcular, state='disable') 
    btn_calcular.grid(row=1, column=0, sticky="NEWS", columnspan=3)
def crearTabs():
    ctrlTabs = ttk.Notebook(ventana)
    tab1 = ttk.Frame(ctrlTabs)
    tab2 = ttk.Frame(ctrlTabs)
    tab3 = ttk.Frame(ctrlTabs)
    tab4 = ttk.Frame(ctrlTabs)
    tab5 = ttk.Frame(ctrlTabs)
    tab6 = ttk.Frame(ctrlTabs)
    tab7 = ttk.Frame(ctrlTabs)
    tab8 = ttk.Frame(ctrlTabs)
    tab9 = ttk.Frame(ctrlTabs)
    ctrlTabs.add(tab7, text="Welcome")
    ctrlTabs.add(tab5, text="Initial Setup")
    ctrlTabs.add(tab1, text="Basemaps")
    ctrlTabs.add(tab2, text="Geotechnical data")
    ctrlTabs.add(tab8, text="Degree of Saturation")
    ctrlTabs.add(tab4, text="Failure depth")
    ctrlTabs.add(tab3, text="Newmark displacement equations")
    ctrlTabs.add(tab6, text="Seismic scenario")
    ctrlTabs.add(tab9, text="Calculate and Results")
    ctrlTabs.pack(fill="both")
    componentes_tab1(tab1)
    componentes_tab2(tab2)
    componentes_tab3(tab3)
    componentes_tab4(tab4)
    componentes_tab5(tab5)
    componentes_tab6(tab6)
    componentes_tab7(tab7)
    componentes_tab8(tab8)
    componentes_tab9(tab9)
crearTabs()
ventana.mainloop()