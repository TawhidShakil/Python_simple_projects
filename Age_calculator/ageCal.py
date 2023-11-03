import tkinter as tk
from datetime import date
from tkinter import PhotoImage
window = tk.Tk()
# calculate the age
def yearCal():
    year = int(ent_yearBox.get())
    currentYear = date.today().year
    age = currentYear - year
    lbl_result.config(text=f"Your age is {age} years")

window.title("Age Calculator")
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)


# create a frame
frm = tk.Frame(master=window)
frm.grid(row=0, column=0, sticky="nsew")
#create a label
lbl_yearMsg = tk.Label(
    master=frm,
    text="Enter Birth Year",
    font=("Helvatica", 20)
)

lbl_yearMsg.grid(row=0, column=0, padx=20, pady=10)

# create a entry box
ent_yearBox = tk.Entry(
    master=frm
)

ent_yearBox.grid(row=1, column=0, padx=20)

#create a button
btn_showBttton = tk.Button(
    master=frm,
    text="SHOW",
    command=yearCal,
    bg="blue",
    fg= "white"
)

btn_showBttton.grid(row=2, column=0, padx=10, pady=10)

#create another label for showing year
lbl_result = tk.Label(
    master=frm,
    text="",
    font=("Halvatica", 12)
)

lbl_result.grid(row=3, column=0, padx=20, pady=10)

frm.grid_rowconfigure(0, weight=1)
frm.grid_columnconfigure(0, weight=1)

window.mainloop()