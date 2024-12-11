import tkinter as tk
import random
import string


def generate_key():
    input_key = key_input.get().strip().upper()

    if len(input_key) != 5 or not all(c in string.ascii_uppercase + string.digits for c in input_key):
        messagebox.showwarning("Ошибка", "Введите корректный первый блок ключа (5 символов: A-Z, 0-9)")
        return

    second_block = shift_block(input_key, 3)
    third_block = shift_block(input_key, -5)
    full_key = f"{input_key}-{second_block}-{third_block}"
    generated_key.set(full_key)


def shift_block(block, shift):
    characters = string.ascii_uppercase + string.digits
    shifted_block = ""
    for char in block:
        index = characters.index(char)
        shifted_block += characters[(index + shift) % len(characters)]
    return shifted_block


def close_app():
    window.destroy()


# окно
window = tk.Tk()
window.title("Генератор ключей")
window.geometry("600x400")

bg_image = tk.PhotoImage(file="background.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

frame = tk.Frame(window, bg="lightgray")
frame.place(relx=0.5, rely=0.5, anchor="center")

tk.Label(frame, text="Введите первый блок ключа (XXXXX):", font=("Arial", 14), bg="lightgray").grid(row=0, column=0,
                                                                                                    padx=10, pady=10)
key_input = tk.Entry(frame, width=10, font=("Arial", 14))
key_input.grid(row=0, column=1, padx=10, pady=10)

tk.Button(frame, text="Сгенерировать ключ", command=generate_key, font=("Arial", 12)).grid(row=1, column=0,
                                                                                           columnspan=2, pady=15)

generated_key = tk.StringVar()
generated_key.set("XXXXX-XXXXX-XXXXX")
key_output = tk.Entry(frame, textvariable=generated_key, width=30, font=("Arial", 14), state="readonly",
                      justify="center")
key_output.grid(row=2, column=0, columnspan=2, pady=10)

tk.Button(frame, text="Выход", command=close_app, font=("Arial", 12)).grid(row=3, column=0, columnspan=2, pady=15)

window.mainloop()
