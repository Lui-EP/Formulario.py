import tkinter as tk
from tkinter import messagebox

### Definici�n de funciones
def limpiar_campos():
    tbNombre.delete(0, tk.END)
    tbApellidos.delete(0, tk.END)
    tbEdad.delete(0, tk.END)
    tbEstatura.delete(0, tk.END)
    tbTelefono.delete(0, tk.END)
    var_genero.set(0)  # Restablecer el valor del Radiobutton

def borrar_fun():
    limpiar_campos()

def guardar_valores():
    # Obtener valores desde los ent
    nombres = tbNombre.get()
    apellidos = tbApellidos.get()
    edad = tbEdad.get()
    estatura = tbEstatura.get()
    telefono = tbTelefono.get()

    # Obtener el genero de los Radiobuttons
    genero = ""
    if var_genero.get() == 1:
        genero = "Hombre"
    elif var_genero.get() == 2:
        genero = "Mujer"

    # Generar la cadena de caracteres
    datos = (
        "Nombres: " + nombres + "\n" +
        "Apellidos: " + apellidos + "\n" +
        "Edad: " + edad + " a�os\n" +
        "Estatura: " + estatura + "\n" +
        "Tel�fono: " + telefono + "\n" +
        "G�nero: " + genero + "\n"
    )
    # Guardar los datos en el archivo TXT
    with open("302024Datos.txt", "a") as archivo:
        archivo.write(datos + "\n\n")

    # Mostrar mensaje de confirmaci�n
    messagebox.showinfo("Informaci�n", "Datos guardados con �xito: \n\n" + datos)

    limpiar_campos()

# Creaci�n de Vetana 
ventana = tk.Tk()
ventana.geometry("520x500")
ventana.title("Formulario Vr.01")

# Crear variable para el RadioButton 
var_genero = tk.IntVar()

# Creaci�n de etiquetas y campos de entrada
lbNombre = tk.Label(ventana, text="Nombres:")
lbNombre.pack()
tbNombre = tk.Entry(ventana)
tbNombre.pack()

lbApellidos = tk.Label(ventana, text="Apellidos:")
lbApellidos.pack()
tbApellidos = tk.Entry(ventana)
tbApellidos.pack()

lbTelefono = tk.Label(ventana, text="Tel�fono:")
lbTelefono.pack()
tbTelefono = tk.Entry(ventana)
tbTelefono.pack()

lbEdad = tk.Label(ventana, text="Edad:")
lbEdad.pack()
tbEdad = tk.Entry(ventana)
tbEdad.pack()

lbEstatura = tk.Label(ventana, text="Estatura:")
lbEstatura.pack()
tbEstatura = tk.Entry(ventana)
tbEstatura.pack()

lbGenero = tk.Label(ventana, text="G�nero")
lbGenero.pack()

rbHombre = tk.Radiobutton(ventana, text="Hombre", variable=var_genero, value=1)
rbHombre.pack()

rbMujer = tk.Radiobutton(ventana, text="Mujer", variable=var_genero, value=2)
rbMujer.pack()

# Creaci�n de Botones
btnBorrar = tk.Button(ventana, text="Borrar valores", command=borrar_fun)
btnBorrar.pack()

btnGuardar = tk.Button(ventana, text="Guardar", command=guardar_valores)
btnGuardar.pack()

# Ejecuci�n de ventana
ventana.mainloop()
