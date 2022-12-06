
# Python program to create
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from tkinter import *
import os
import convertapi
# import asyncio
  
# import filedialog module
from tkinter import filedialog

# Variables
convertapi.api_secret = os.getenv('CONVERT_API_SECRET')
inputFormat = 'heic'
outputFormat = 'jpg'
  
# Function for opening the
# file explorer window
def browseFiles():
    filenames = filedialog.askopenfilenames(initialdir = "/",
                                          title = "Seleciona imagen .heic",
                                          filetypes = [("Image File", ".heic")]
    )
      
    # Change label contents
    try:
        for filename in filenames:
            convertapi.convert(outputFormat, {
            'File': filename
            }, from_format = inputFormat).save_files('./fotos/')
        label_response_explore.config(text="Conversión exitosa", bg="green")
        user_info = convertapi.user()
        print(user_info['SecondsLeft'])
    except Exception as e:
        label_response_explore.config(text="Algo salió mal", bg="red")
        print(e)

# Create the root window
window = Tk()
  
# Set window title
window.title('Convertidor')
  
# Set window size
window.geometry("300x200+0+0")
  
#Set window background color
window.config(background = "white")
frameMain = Frame(window, bg="blue")

frameMain.grid(row=0, column=0, sticky="NESW")
frameMain.grid_rowconfigure(0, weight=1)
frameMain.grid_rowconfigure(1, weight=1)
frameMain.grid_rowconfigure(2, weight=1)
frameMain.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
  
# Create a File Explorer label
label_file_explorer = Label(frameMain,
                            text = f"Busca las imagenes y seleccionalas  para transformar de .{inputFormat} a .{outputFormat}",
                            wraplength=200,
                            justify="center",
                            fg = "blue")
  
      
button_explore = Button(frameMain,
                        text = "Buscar y Convertir",
                        command = browseFiles)
  
button_exit = Button(frameMain,
                     text = "Salir",
                     command = exit)

label_response_explore = Label(
            frameMain,
            text="",
            bg="blue"
        )
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 0, row = 0)
  
button_explore.grid(column = 0, row = 1)
  
button_exit.grid(column = 0,row = 2)

label_response_explore.grid(column=0, row=3)

# Let the window wait for any events
window.mainloop()