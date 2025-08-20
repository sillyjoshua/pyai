import tkinter as tk

window = tk.Tk()

window.title("pyai info")

window.geometry("1920 x 1080")

label = tk.Label(window, text="pyai is used to do tasks a normal ai agent would'nt", font=("Arial", 24))

label.pack(pady=20)

button = tk.Button(window, text="Close", command=window.destroy, font=("Arial", 18))

button.pack(pady=20)

window.mainloop()
window.configure(bg='lightblue')