
from tkinter import *
import shelve

def mi_horario():

    d = shelve.open('horario.txt')
    horario = d['horario']
    print(d['horario'])
    label4["text"] = horario

    if label4["text"] == "Quitar el polvo":
        label5["text"] = "Barrer"
        label6["text"] = "Fregar"
        d = shelve.open('horario.txt')
        d['horario'] = "Barrer"
        print(d['horario'])
        d.close()

    elif label4["text"] == "Barrer":
        label5["text"] = "Fregar"
        label6["text"] = "Quitar el polvo"
        d = shelve.open('horario.txt')
        d['horario'] = "Fregar"
        print(d['horario'])
        d.close()

    elif label4["text"] == "Fregar":
        label5["text"] = "Quitar el polvo"
        label6["text"] = "Barrer"
        d = shelve.open('horario.txt')
        d['horario'] = "Quitar el polvo"
        print(d['horario'])
        d.close()

root = Tk()

label = Label(root, text="Artur:")
label.grid(row=0, column=0, sticky=W)

label2 = Label(root, text="Alejandro:")
label2.grid(row=1, column=0, sticky=W)

label3 = Label(root, text="Jhonny:")
label3.grid(row=2, column=0, sticky=W)

label4 = Label(root, text="")
label4.grid(row=0, column=1, sticky=W)

label5 = Label(root, text="")
label5.grid(row=1, column=1, sticky=W)

label6 = Label(root, text="")
label6.grid(row=2, column=1, sticky=W)

button = Button(root, text="Click aqui", command=mi_horario)
button.grid(row=3)

root.mainloop()
