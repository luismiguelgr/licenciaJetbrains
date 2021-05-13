import os
import shutil
import tkinter as tk
from tkinter import ttk
from pathlib import Path

# Configuracion ventana
window = tk.Tk()
window.title("Reiniciar licencia Jetbrains")
window.minsize(400, 100)

# Directorios necesarios
home = str(Path.home())
dirConfigJetbrains = home+"/.config/JetBrains"
dirUserprefsJetbrains = home+"/.java/.userPrefs/jetbrains"

# Funciones
def renovarLicencia(nombreCarpeta):
    # Listo ficheros, compruebo que existen preferencia de dicho programa
    # y elimino de la carpeta .userPrefs
    for carpeta in os.listdir(dirUserprefsJetbrains):
        if carpeta in str.lower(nombreCarpeta):
            try:
                shutil.rmtree(dirUserprefsJetbrains+"/"+carpeta)
            except OSError as e:
                print("Error: %s : %s" % (dirUserprefsJetbrains+"/"+carpeta, e.strerror))
    # Elimino ficheros de configuracion y busco solamente l fichero key
    dirEval = dirConfigJetbrains+"/"+nombreCarpeta+"/eval/"
    ficheroOther = dirConfigJetbrains+"/"+nombreCarpeta+"/options/other.xml"
    ficheros = os.listdir(dirConfigJetbrains+"/"+nombreCarpeta+"/eval/")
    ficherosFiltrados = [fichero for fichero in ficheros if fichero.endswith(".key")]
    for fichero in ficherosFiltrados:
        dirFichero = os.path.join(dirConfigJetbrains+"/"+nombreCarpeta+"/eval/", fichero)

    try:
        os.remove(dirFichero)
        os.remove(ficheroOther)
    except OSError as e:
        print("Error: %s : %s" % (dirFichero, e.strerror))


# Graficos
labelTextoFicheros=tk.Label(text="Lista de programas instalados", bg="black", fg="white", font=(None, 12), anchor='w').pack()
separator = ttk.Separator(window, orient='horizontal')
separator.pack(side='top', fill='x')

contenido = os.listdir(dirConfigJetbrains)
style = ttk.Style()
style.configure("TButton", foreground="blue", background="orange")

s = ttk.Style()
s.configure("regular.TButton", background="red")
for carpeta in contenido:
    labelListaFicheros=tk.Label(text=carpeta)
    labelListaFicheros.pack()
    boton_carpeta = ttk.Button(text="Renovar licencia", command=lambda k=carpeta: renovarLicencia(k))
    boton_carpeta.pack()

separator = ttk.Separator(window, orient='horizontal')
separator.pack(side='top', fill='x')
labelTextoFicheros=tk.Label(text="miguelgrdaw@gmail.com", bg="black", fg="red", pady=5, font=(None, 8), anchor='w').pack(fill='both')

# Inicio programa

window.mainloop()
