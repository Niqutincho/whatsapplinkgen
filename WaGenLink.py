import tkinter as tk
import pyperclip

def generate_whatsapp_link():
    phone_number = phone_entry.get()
    # Eliminar espacios y guiones y agregar +54
    phone_number = "+54" + phone_number.replace(" ", "").replace("-", "")
    whatsapp_link = "https://wa.me/" + phone_number
    result_label.config(text=f"Enlace de WhatsApp: {whatsapp_link}")
    copy_button.config(state=tk.NORMAL)  # Habilitar el botón de copia

def copy_to_clipboard():
    whatsapp_link = result_label.cget("text").split(": ")[1]  # Obtiene el enlace directo
    pyperclip.copy(whatsapp_link)

app = tk.Tk()
app.title("Generador de Enlace de WhatsApp")
app.geometry("400x200")

phone_label = tk.Label(app, text="Ingrese el número de teléfono:")
phone_label.pack(pady=10)

phone_entry = tk.Entry(app)
phone_entry.pack(pady=5)

generate_button = tk.Button(app, text="Generar Enlace", command=generate_whatsapp_link)
generate_button.pack(pady=10)

copy_button = tk.Button(app, text="Copiar Enlace", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack(pady=5)

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
