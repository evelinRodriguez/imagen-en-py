from tkinter import*

raiz=Tk()

mFrame=Frame(raiz,width=500,height=400)

mFrame.pack()

#para aparecer imagen

miImagen=PhotoImage(file="tenor.gif")
#la imagen tiene q estar en gif
# para que aparezca la imagen

#miLabel=Label(mFrame,text="hola",fg="pink",font=(81)) Para el texto
Label(mFrame,image=miImagen).place(x=100,y=20)

#para que aparezca en la pantalla
#Label(mFrame,text="hola").miLabel.place(x=100,y=200) para abreviar



#miLabel.pack()

raiz.mainloop()