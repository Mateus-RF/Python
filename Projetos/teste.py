import tkinter as tk

def celsius_to_kelvin():
    celsius = float(entry_celsius.get())
    kelvin_result.set(celsius + 273.15)

def celsius_to_fahrenheit():
    celsius = float(entry_celsius.get())
    fahrenheit_result.set((celsius * 9/5) + 32)

def fahrenheit_to_celsius():
    fahrenheit = float(entry_fahrenheit.get())
    celsius_result.set((fahrenheit - 32) * 5/9)

def fahrenheit_to_kelvin():
    fahrenheit = float(entry_fahrenheit.get())
    kelvin_result.set((fahrenheit - 32) * 5/9 + 273.15)

def kelvin_to_celsius():
    kelvin = float(entry_kelvin.get())
    celsius_result.set(kelvin - 273.15)

def kelvin_to_fahrenheit():
    kelvin = float(entry_kelvin.get())
    fahrenheit_result.set((kelvin - 273.15) * 9/5 + 32)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Conversor de Temperatura")

# Celsius para Kelvin
label_celsius_to_kelvin = tk.Label(root, text="Celsius para Kelvin:")
label_celsius_to_kelvin.grid(row=0, column=0)
entry_celsius = tk.Entry(root)
entry_celsius.grid(row=0, column=1)
button_celsius_to_kelvin = tk.Button(root, text="Converter", command=celsius_to_kelvin)
button_celsius_to_kelvin.grid(row=0, column=2)
kelvin_result = tk.DoubleVar()
label_kelvin_result = tk.Label(root, textvariable=kelvin_result)
label_kelvin_result.grid(row=0, column=3)

# Celsius para Fahrenheit
label_celsius_to_fahrenheit = tk.Label(root, text="Celsius para Fahrenheit:")
label_celsius_to_fahrenheit.grid(row=1, column=0)
button_celsius_to_fahrenheit = tk.Button(root, text="Converter", command=celsius_to_fahrenheit)
button_celsius_to_fahrenheit.grid(row=1, column=2)
fahrenheit_result = tk.DoubleVar()
label_fahrenheit_result = tk.Label(root, textvariable=fahrenheit_result)
label_fahrenheit_result.grid(row=1, column=3)

# Fahrenheit para Celsius
label_fahrenheit_to_celsius = tk.Label(root, text="Fahrenheit para Celsius:")
label_fahrenheit_to_celsius.grid(row=2, column=0)
entry_fahrenheit = tk.Entry(root)
entry_fahrenheit.grid(row=2, column=1)
button_fahrenheit_to_celsius = tk.Button(root, text="Converter", command=fahrenheit_to_celsius)
button_fahrenheit_to_celsius.grid(row=2, column=2)
celsius_result = tk.DoubleVar()
label_celsius_result = tk.Label(root, textvariable=celsius_result)
label_celsius_result.grid(row=2, column=3)

# Fahrenheit para Kelvin
label_fahrenheit_to_kelvin = tk.Label(root, text="Fahrenheit para Kelvin:")
label_fahrenheit_to_kelvin.grid(row=3, column=0)
button_fahrenheit_to_kelvin = tk.Button(root, text="Converter", command=fahrenheit_to_kelvin)
button_fahrenheit_to_kelvin.grid(row=3, column=2)

# Kelvin para Celsius
label_kelvin_to_celsius = tk.Label(root, text="Kelvin para Celsius:")
label_kelvin_to_celsius.grid(row=4, column=0)
entry_kelvin = tk.Entry(root)
entry_kelvin.grid(row=4, column=1)
button_kelvin_to_celsius = tk.Button(root, text="Converter", command=kelvin_to_celsius)
button_kelvin_to_celsius.grid(row=4, column=2)

# Kelvin para Fahrenheit
label_kelvin_to_fahrenheit = tk.Label(root, text="Kelvin para Fahrenheit:")
label_kelvin_to_fahrenheit.grid(row=5, column=0)
button_kelvin_to_fahrenheit = tk.Button(root, text="Converter", command=kelvin_to_fahrenheit)
button_kelvin_to_fahrenheit.grid(row=5, column=2)

root.mainloop()