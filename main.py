import tkinter as tk
from tkinter import *
import tkinter.messagebox

# create a window for the gui
root = tk.Tk()
# create the window tittle
root.title("Franspai Currency converter")
Tops = Frame(root, width=2000, height=400, relief="ridge")
Tops.grid(row=0, column=0)
headlabel = tk.Label(Tops, font=('Helvetica', 30, 'bold'), text="\n     Franspai's Currency converter", bg='white', fg='black')
headlabel.grid(row=1, column=0, sticky=W)
# assign variables
var1 = tk.StringVar(root)
var2 = tk.StringVar(root)

var1.set("currency")
var2.set("currency")
# get currency conversion rates
def CurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()

    from_currency = var1.get()
    to_currency = var2.get()

    if (Amount1_field.get() == ""):
        tkinter.messagebox.showinfo("Shit", "Enter a valid value bro\n 1, 2, 3, 4, 5 etc.")

    elif (from_currency == "currency" or to_currency == "currency"):
        tkinter.messagebox.showinfo("Shit",
                                    "no currency selected\n select from to currency from menu")

    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))

def clear_all():
        Amount1_field.delete(0, tk.END)
        Amount2_field.delete(0, tk.END)

CurrenyCode_list = ["PLN", "INR", "USD", "CAD", "CNY", "DKK", "EUR", "GBP", "CHF", "JPY", "SEK", "CZK"]

root.configure(background='white')
root.geometry("700x400")

Label_1 = Label(root, font=('Helvetica', 27, 'bold'), text="", padx=2, pady=2, bg="white", fg="black")
Label_1.grid(row=1, column=0, sticky=W)
label1 = tk.Label(root, font=('Helvetica', 15, 'bold'), text="\t    Amount  :  ", bg="white", fg="black")
label1.grid(row=2, column=0, sticky=W)
label1 = tk.Label(root, font=('Helvetica', 15, 'bold'), text="\t    From  :  ", bg="white", fg="black")
label1.grid(row=3, column=0, sticky=W)
label1 = tk.Label(root, font=('Helvetica', 15, 'bold'), text="\t    To  :  ", bg="white", fg="black")
label1.grid(row=4, column=0, sticky=W)
label1 = tk.Label(root, font=('Helvetica', 15, 'bold'), text="\t    Converted  :  ", bg="white", fg="black")
label1.grid(row=8, column=0, sticky=W)
Label_1 = Label(root, font=('Helvetica', 7, 'bold'), text="", padx=2, pady=2, bg="white", fg="black")
Label_1.grid(row=5, column=0, sticky=W)
Label_1 = Label(root, font=('Helvetica', 7, 'bold'), text="", padx=2, pady=2, bg="white", fg="black")
Label_1.grid(row=7, column=0, sticky=W)

FromCurrency_option = tk.OptionMenu(root, var1, *CurrenyCode_list)
ToCurrency_option = tk.OptionMenu(root, var2, *CurrenyCode_list)
FromCurrency_option.grid(row=3, column=0, ipadx=45, sticky=E)
ToCurrency_option.grid(row=4, column=0, ipadx=45, sticky=E)
Amount1_field = tk.Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=28, sticky=E)
Amount2_field = tk.Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=31, sticky=E)
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Convert  ", padx=2, pady=2, bg="#ba25b5", fg="white",
                 command=CurrencyConversion)
Label_9.grid(row=6, column=0)
Label_1 = Label(root, font=('Helvetica', 7, 'bold'), text="", padx=2, pady=2, bg="white", fg="black")
Label_1.grid(row=9, column=0, sticky=W)
Label_9 = Button(root, font=('arial', 15, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="#ba25b5", fg="white",
                 command=clear_all)
Label_9.grid(row=10, column=0)

light = PhotoImage(file="lighton.png")
dark = PhotoImage(file="lightoff.png")

switch_value = True

# Button toggle light and dark


def toggle():
    global switch_value
    if switch_value:
        switch.config(image=dark, bg="#ba25b5",
                      activebackground="#ba25b5")

        # change window color
        root.config(bg="black")
        switch_value = False

    else:
        switch.config(image=light, bg="white",
                      activebackground="white")

        # Change back to light
        root.config(bg="white")
        switch_value = True

switch = Button(root, image=light, bd=0, bg="white", activebackground="white", command=toggle)
switch.grid(row=1, column=0, padx=5, pady=10)

root.mainloop()
