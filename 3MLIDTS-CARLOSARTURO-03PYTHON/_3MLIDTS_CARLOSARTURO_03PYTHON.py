import tkinter as tk
from tkinter import messagebox

def radioButton_Selected():
    sel = rbSeleccion.get()
    if sel == "Celsius":
        tbCelsius.config(state="normal")
        tbFahrenheit.config(state="disabled")
        tbKelvin.config(state="disabled")
    elif sel == "Kelvin":
        tbCelsius.config(state="disabled")
        tbFahrenheit.config(state="disabled")
        tbKelvin.config(state="normal")
    elif sel == "Fahrenheit":
        tbCelsius.config(state="disabled")
        tbFahrenheit.config(state="normal")
        tbKelvin.config(state="disabled")

def btnCalcular_Click():
    try:
        if rbSeleccion.get() == "Celsius":
            tbCelsius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")
            celsius = float(tbCelsius.get())
            print(celsius)
            farenheintt = (celsius * 9.0 / 5.0) + 32.0
            print(farenheintt)
            ##tbFahrenheit.insert(0, f" {farenheintt:.2f}")
            tbFahrenheit.insert(0, str(round(farenheintt, 2)))
            kelvin = celsius + 273.0
            print(kelvin)
            ##tbKelvin.insert(0, f"{kelvin:.2f}")
            tbKelvin.insert(0, str(round(kelvin, 2)))
            
        elif rbSeleccion.get() == "Kelvin":
            tbCelsius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")
            kelvin = float(tbKelvin.get())
            celsius = kelvin - 273.0
            tbCelsius.insert(0, str(round(celsius, 2)))
            print(celsius)
            farenheintt = (celsius * 9.0 / 5.0) + 32.0
            print(farenheintt)
            tbFahrenheit.insert(0, str(round(farenheintt, 2)))
            
        elif rbSeleccion.get() == "Fahrenheit":
            tbCelsius.config(state="normal")
            tbKelvin.config(state="normal")
            tbFahrenheit.config(state="normal")
            farenheinth = float(tbFahrenheit.get())
            print(farenheinth)
            celsius = (farenheinth - 32.0) * 5.0 / 9.0
            print(celsius)
            kelvin = celsius + 273.0
            print(kelvin)
            tbCelsius.insert(0, str(round(celsius, 2)))
            tbKelvin.insert(0, str(round(kelvin, 2)))
            
        else:
            messagebox.showwarning("Temperatura Seleccionada", "Seleccione una temperatura de entrada (Kelvin/Fahrenheit/Celsius).")
            
    except ValueError:
        messagebox.showerror("Error", "Ingrese un numero valido en el campo habilitado.")

def btnLimpiar_Click():
    tbKelvin.delete(0, tk.END)
    tbCelsius.delete(0, tk.END)
    tbFahrenheit.delete(0, tk.END)
    tbCelsius.config(state="normal")
    tbFahrenheit.config(state="normal")
    tbKelvin.config(state="normal")
    rbSeleccion.set("")

##Elementos basicos de ventana
ventana = tk.Tk()
ventana.title("Actividad 03 Conversor de Temperatura")
ventana.geometry("450x450")
ventana.config(bg="Pink")

## Elementos graficos
rbSeleccion = tk.StringVar(value="")
tk.Label(ventana, text="Temp. en Celsius: ").pack()
tbCelsius = tk.Entry(ventana, justify="center")
tbCelsius.pack()

tk.Label(ventana, text="Temp. en Fahrenheit: ").pack()
tbFahrenheit = tk.Entry(ventana, justify="center")
tbFahrenheit.config(state="normal")
tbFahrenheit.pack()

tk.Label(ventana, text="Temp. en Kelvin: ").pack()
tbKelvin = tk.Entry(ventana, justify="center")
tbKelvin.pack()

groupBox = tk.LabelFrame(ventana, text="Selecione Temperatura de Entrada:")
groupBox.pack()

rbCelsius = tk.Radiobutton(groupBox, text="Celsius", value="Celsius", variable=rbSeleccion, command=radioButton_Selected)
rbCelsius.grid(row=0, column=0)

rbKelvin = tk.Radiobutton(groupBox, text="Kelvin", value="Kelvin", variable=rbSeleccion, command=radioButton_Selected)
rbKelvin.grid(row=0, column=1)

rbFahrenheit = tk.Radiobutton(groupBox, text="Fahrenheit", value="Fahrenheit", variable=rbSeleccion, command=radioButton_Selected)
rbFahrenheit.grid(row=0, column=2)

btnCalcular = tk.Button(ventana, text="Calcular", command=btnCalcular_Click)
btnCalcular.pack()

btnLimpiar = tk.Button(ventana, text="Limpiar", command=btnLimpiar_Click)
btnLimpiar.pack()

ventana.mainloop()
