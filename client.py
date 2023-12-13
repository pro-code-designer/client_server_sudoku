from cProfile import label
from multiprocessing.sharedctypes import Value
import time
import tkinter as tk
import socket
import dataconvertor

from click import command

class App:
    def __init__(self, root):
        self.username=""
        self.d=[]
        self.ip = "127.0.0.1"
        self.port = 5230

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((self.ip , self.port))
        self.data = self.s.recv(1024).decode('utf-8')
        self.tempstr = self.s.recv(1024).decode('utf-8')
        self.s.recv(1024).decode('utf-8')
        self.temp=dataconvertor.ConvertToSudoko(self.tempstr) 
        self.statandct=dataconvertor.statmaker(self.temp)
        self.stat=self.statandct[0]
        self.ctk=self.statandct[1]
        #setting title
        root.title("undefined")
        #setting window size
        width=630
        height=630
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        tex=str(self.ctk)+" filed and most is"+str(self.ctk)

        self.lables=tk.Label(root,font=("Roboto Medium", 15),text=tex)
        self.lables.place(x=100,y=30,width=200,height=50)
        #row1-------------------------------------------------------
        self.lable1=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable1.place(x=80,y=80,width=50,height=50)

        self.lable2=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable2.place(x=130,y=80,width=50,height=50)

        self.lable3=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable3.place(x=180,y=80,width=50,height=50)

        self.lable4=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable4.place(x=235,y=80,width=50,height=50)

        self.lable5=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable5.place(x=285,y=80,width=50,height=50)

        self.lable6=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable6.place(x=335,y=80,width=50,height=50)

        self.lable7=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable7.place(x=390,y=80,width=50,height=50)

        self.lable8=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable8.place(x=440,y=80,width=50,height=50)

        self.lable9=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable9.place(x=490,y=80,width=50,height=50)



        #row2-------------------------------------------------------
        self.lable10=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable10.place(x=80,y=130,width=50,height=50)

        self.lable11=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable11.place(x=130,y=130,width=50,height=50)

        self.lable12=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable12.place(x=180,y=130,width=50,height=50)

        self.lable13=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable13.place(x=235,y=130,width=50,height=50)

        self.lable14=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable14.place(x=285,y=130,width=50,height=50)

        self.lable15=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable15.place(x=335,y=130,width=50,height=50)

        self.lable16=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable16.place(x=390,y=130,width=50,height=50)

        self.lable17=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable17.place(x=440,y=130,width=50,height=50)

        self.lable18=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable18.place(x=490,y=130,width=50,height=50)



        #row3-------------------------------------------------------
        self.lable19=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable19.place(x=80,y=180,width=50,height=50)

        self.lable20=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable20.place(x=130,y=180,width=50,height=50)

        self.lable21=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable21.place(x=180,y=180,width=50,height=50)

        self.lable22=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable22.place(x=235,y=180,width=50,height=50)

        self.lable23=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable23.place(x=285,y=180,width=50,height=50)

        self.lable24=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable24.place(x=335,y=180,width=50,height=50)

        self.lable25=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable25.place(x=390,y=180,width=50,height=50)

        self.lable26=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable26.place(x=440,y=180,width=50,height=50)

        self.lable27=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable27.place(x=490,y=180,width=50,height=50)


        #row4-------------------------------------------------------
        self.lable28=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable28.place(x=80,y=235,width=50,height=50)

        self.lable29=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable29.place(x=130,y=235,width=50,height=50)

        self.lable30=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable30.place(x=180,y=235,width=50,height=50)

        self.lable31=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable31.place(x=235,y=235,width=50,height=50)

        self.lable32=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable32.place(x=285,y=235,width=50,height=50)

        self.lable33=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable33.place(x=335,y=235,width=50,height=50)

        self.lable34=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable34.place(x=390,y=235,width=50,height=50)

        self.lable35=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable35.place(x=440,y=235,width=50,height=50)

        self.lable36=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable36.place(x=490,y=235,width=50,height=50)



        #row5-------------------------------------------------------
        self.lable37=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable37.place(x=80,y=285,width=50,height=50)

        self.lable38=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable38.place(x=130,y=285,width=50,height=50)

        self.lable39=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable39.place(x=180,y=285,width=50,height=50)

        self.lable40=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable40.place(x=235,y=285,width=50,height=50)

        self.lable41=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable41.place(x=285,y=285,width=50,height=50)

        self.lable42=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable42.place(x=335,y=285,width=50,height=50)

        self.lable43=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable43.place(x=390,y=285,width=50,height=50)

        self.lable44=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable44.place(x=440,y=285,width=50,height=50)

        self.lable45=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable45.place(x=490,y=285,width=50,height=50)



        #row6-------------------------------------------------------
        self.lable46=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable46.place(x=80,y=335,width=50,height=50)

        self.lable47=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable47.place(x=130,y=335,width=50,height=50)

        self.lable48=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable48.place(x=180,y=335,width=50,height=50)

        self.lable49=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable49.place(x=235,y=335,width=50,height=50)

        self.lable50=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable50.place(x=285,y=335,width=50,height=50)

        self.lable51=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable51.place(x=335,y=335,width=50,height=50)

        self.lable52=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable52.place(x=390,y=335,width=50,height=50)

        self.lable53=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable53.place(x=440,y=335,width=50,height=50)

        self.lable54=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable54.place(x=490,y=335,width=50,height=50)


        #row7-------------------------------------------------------
        self.lable55=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable55.place(x=80,y=390,width=50,height=50)

        self.lable56=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable56.place(x=130,y=390,width=50,height=50)

        self.lable57=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable57.place(x=180,y=390,width=50,height=50)

        self.lable58=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable58.place(x=235,y=390,width=50,height=50)

        self.lable59=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable59.place(x=285,y=390,width=50,height=50)

        self.lable60=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable60.place(x=335,y=390,width=50,height=50)

        self.lable61=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable61.place(x=390,y=390,width=50,height=50)

        self.lable62=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable62.place(x=440,y=390,width=50,height=50)

        self.lable63=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable63.place(x=490,y=390,width=50,height=50)



        #row8-------------------------------------------------------
        self.lable64=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable64.place(x=80,y=440,width=50,height=50)

        self.lable65=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable65.place(x=130,y=440,width=50,height=50)

        self.lable66=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable66.place(x=180,y=440,width=50,height=50)

        self.lable67=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable67.place(x=235,y=440,width=50,height=50)

        self.lable68=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable68.place(x=285,y=440,width=50,height=50)

        self.lable69=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable69.place(x=335,y=440,width=50,height=50)

        self.lable70=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable70.place(x=390,y=440,width=50,height=50)

        self.lable71=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable71.place(x=440,y=440,width=50,height=50)

        self.lable72=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable72.place(x=490,y=440,width=50,height=50)



        #row9-------------------------------------------------------
        self.lable73=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable73.place(x=80,y=490,width=50,height=50)

        self.lable74=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable74.place(x=130,y=490,width=50,height=50)

        self.lable75=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable75.place(x=180,y=490,width=50,height=50)

        self.lable76=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable76.place(x=235,y=490,width=50,height=50)

        self.lable77=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable77.place(x=285,y=490,width=50,height=50)

        self.lable78=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable78.place(x=335,y=490,width=50,height=50)

        self.lable79=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable79.place(x=390,y=490,width=50,height=50)

        self.lable80=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable80.place(x=440,y=490,width=50,height=50)

        self.lable81=tk.Entry(root,font=("Roboto Medium", 15),justify="center",bg="#e5e5e5")
        self.lable81.place(x=490,y=490,width=50,height=50)
        
        #keybinding
        self.full_table()
        self.lable1.bind("<KeyRelease>", lambda event:self.valid_get(self.lable1,0,0))
        self.lable2.bind("<KeyRelease>", lambda event:self.valid_get(self.lable2,0,1))
        self.lable3.bind("<KeyRelease>", lambda event:self.valid_get(self.lable3,0,2))
        self.lable4.bind("<KeyRelease>", lambda event:self.valid_get(self.lable4,0,3))
        self.lable5.bind("<KeyRelease>", lambda event:self.valid_get(self.lable5,0,4))
        self.lable6.bind("<KeyRelease>", lambda event:self.valid_get(self.lable6,0,5))
        self.lable7.bind("<KeyRelease>", lambda event:self.valid_get(self.lable7,0,6))
        self.lable8.bind("<KeyRelease>", lambda event:self.valid_get(self.lable8,0,7))
        self.lable9.bind("<KeyRelease>", lambda event:self.valid_get(self.lable9,0,8))
        #///////////////////////////////////////////////
        self.lable10.bind("<KeyRelease>", lambda event:self.valid_get(self.lable10,1,0))
        self.lable11.bind("<KeyRelease>", lambda event:self.valid_get(self.lable11,1,1))
        self.lable12.bind("<KeyRelease>", lambda event:self.valid_get(self.lable12,1,2))
        self.lable13.bind("<KeyRelease>", lambda event:self.valid_get(self.lable13,1,3))
        self.lable14.bind("<KeyRelease>", lambda event:self.valid_get(self.lable14,1,4))
        self.lable15.bind("<KeyRelease>", lambda event:self.valid_get(self.lable15,1,5))
        self.lable16.bind("<KeyRelease>", lambda event:self.valid_get(self.lable16,1,6))
        self.lable17.bind("<KeyRelease>", lambda event:self.valid_get(self.lable17,1,7))
        self.lable18.bind("<KeyRelease>", lambda event:self.valid_get(self.lable18,1,8))
        #///////////////////////////////////////////////
        self.lable19.bind("<KeyRelease>", lambda event:self.valid_get(self.lable19,2,0))
        self.lable20.bind("<KeyRelease>", lambda event:self.valid_get(self.lable20,2,1))
        self.lable21.bind("<KeyRelease>", lambda event:self.valid_get(self.lable21,2,2))
        self.lable22.bind("<KeyRelease>", lambda event:self.valid_get(self.lable22,2,3))
        self.lable23.bind("<KeyRelease>", lambda event:self.valid_get(self.lable23,2,4))
        self.lable24.bind("<KeyRelease>", lambda event:self.valid_get(self.lable24,2,5))
        self.lable25.bind("<KeyRelease>", lambda event:self.valid_get(self.lable25,2,6))
        self.lable26.bind("<KeyRelease>", lambda event:self.valid_get(self.lable26,2,7))
        self.lable27.bind("<KeyRelease>", lambda event:self.valid_get(self.lable27,2,8))
        #///////////////////////////////////////////////
        self.lable28.bind("<KeyRelease>", lambda event:self.valid_get(self.lable28,3,0))
        self.lable29.bind("<KeyRelease>", lambda event:self.valid_get(self.lable29,3,1))
        self.lable30.bind("<KeyRelease>", lambda event:self.valid_get(self.lable30,3,2))
        self.lable31.bind("<KeyRelease>", lambda event:self.valid_get(self.lable31,3,3))
        self.lable32.bind("<KeyRelease>", lambda event:self.valid_get(self.lable32,3,4))
        self.lable33.bind("<KeyRelease>", lambda event:self.valid_get(self.lable33,3,5))
        self.lable34.bind("<KeyRelease>", lambda event:self.valid_get(self.lable34,3,6))
        self.lable35.bind("<KeyRelease>", lambda event:self.valid_get(self.lable35,3,7))
        self.lable36.bind("<KeyRelease>", lambda event:self.valid_get(self.lable36,3,8))
        #///////////////////////////////////////////////
        self.lable37.bind("<KeyRelease>", lambda event:self.valid_get(self.lable37,4,0))
        self.lable38.bind("<KeyRelease>", lambda event:self.valid_get(self.lable38,4,1))
        self.lable39.bind("<KeyRelease>", lambda event:self.valid_get(self.lable39,4,2))
        self.lable40.bind("<KeyRelease>", lambda event:self.valid_get(self.lable40,4,3))
        self.lable41.bind("<KeyRelease>", lambda event:self.valid_get(self.lable41,4,4))
        self.lable42.bind("<KeyRelease>", lambda event:self.valid_get(self.lable42,4,5))
        self.lable43.bind("<KeyRelease>", lambda event:self.valid_get(self.lable43,4,6))
        self.lable44.bind("<KeyRelease>", lambda event:self.valid_get(self.lable44,4,7))
        self.lable45.bind("<KeyRelease>", lambda event:self.valid_get(self.lable45,4,8))
        #///////////////////////////////////////////////
        self.lable46.bind("<KeyRelease>", lambda event:self.valid_get(self.lable46,5,0))
        self.lable47.bind("<KeyRelease>", lambda event:self.valid_get(self.lable47,5,1))
        self.lable48.bind("<KeyRelease>", lambda event:self.valid_get(self.lable48,5,2))
        self.lable49.bind("<KeyRelease>", lambda event:self.valid_get(self.lable49,5,3))
        self.lable50.bind("<KeyRelease>", lambda event:self.valid_get(self.lable50,5,4))
        self.lable51.bind("<KeyRelease>", lambda event:self.valid_get(self.lable51,5,5))
        self.lable52.bind("<KeyRelease>", lambda event:self.valid_get(self.lable52,5,6))
        self.lable53.bind("<KeyRelease>", lambda event:self.valid_get(self.lable53,5,7))
        self.lable54.bind("<KeyRelease>", lambda event:self.valid_get(self.lable54,5,8))
        #///////////////////////////////////////////////
        self.lable55.bind("<KeyRelease>", lambda event:self.valid_get(self.lable55,6,0))
        self.lable56.bind("<KeyRelease>", lambda event:self.valid_get(self.lable56,6,1))
        self.lable57.bind("<KeyRelease>", lambda event:self.valid_get(self.lable57,6,2))
        self.lable58.bind("<KeyRelease>", lambda event:self.valid_get(self.lable58,6,3))
        self.lable59.bind("<KeyRelease>", lambda event:self.valid_get(self.lable59,6,4))
        self.lable60.bind("<KeyRelease>", lambda event:self.valid_get(self.lable60,6,5))
        self.lable61.bind("<KeyRelease>", lambda event:self.valid_get(self.lable61,6,6))
        self.lable62.bind("<KeyRelease>", lambda event:self.valid_get(self.lable62,6,7))
        self.lable63.bind("<KeyRelease>", lambda event:self.valid_get(self.lable63,6,8))
        #///////////////////////////////////////////////
        self.lable64.bind("<KeyRelease>", lambda event:self.valid_get(self.lable64,7,0))
        self.lable65.bind("<KeyRelease>", lambda event:self.valid_get(self.lable65,7,1))
        self.lable66.bind("<KeyRelease>", lambda event:self.valid_get(self.lable66,7,2))
        self.lable67.bind("<KeyRelease>", lambda event:self.valid_get(self.lable67,7,3))
        self.lable68.bind("<KeyRelease>", lambda event:self.valid_get(self.lable68,7,4))
        self.lable69.bind("<KeyRelease>", lambda event:self.valid_get(self.lable69,7,5))
        self.lable70.bind("<KeyRelease>", lambda event:self.valid_get(self.lable70,7,6))
        self.lable71.bind("<KeyRelease>", lambda event:self.valid_get(self.lable71,7,7))
        self.lable72.bind("<KeyRelease>", lambda event:self.valid_get(self.lable72,7,8))
        #///////////////////////////////////////////////
        self.lable73.bind("<KeyRelease>", lambda event:self.valid_get(self.lable73,8,0))
        self.lable74.bind("<KeyRelease>", lambda event:self.valid_get(self.lable74,8,1))
        self.lable75.bind("<KeyRelease>", lambda event:self.valid_get(self.lable75,8,2))
        self.lable76.bind("<KeyRelease>", lambda event:self.valid_get(self.lable76,8,3))
        self.lable77.bind("<KeyRelease>", lambda event:self.valid_get(self.lable77,8,4))
        self.lable78.bind("<KeyRelease>", lambda event:self.valid_get(self.lable78,8,5))
        self.lable79.bind("<KeyRelease>", lambda event:self.valid_get(self.lable79,8,6))
        self.lable80.bind("<KeyRelease>", lambda event:self.valid_get(self.lable80,8,7))
        self.lable81.bind("<KeyRelease>", lambda event:self.valid_get(self.lable81,8,8))
        self.loose_check()



    def show_ms(self,tx):
        window = tk.Tk()
        window.geometry("300x150")
        label = tk.Label(window, text=tx,font=("Roboto Medium", 15))
        label.pack(side="top", fill="both", expand=True, padx=40, pady=40)
        self.s.close()
        root.destroy()
        window.mainloop()
        
        

    def loose_check(self):
        self.s.send("L".encode('utf-8'))
        m=self.s.recv(1024).decode('utf-8')
        if m=="L":
            self.show_ms("you lose")
        tex=str(self.ctk)+" filed and most is"+m
        self.lables.config(text = tex)
        self.lables.after(1000, self.loose_check)

    def valid_get(self,w,x,y):
        strs=w.get()
        if len(strs)>1:
            strs=strs[:-1]
            w.delete(0,tk.END)
            w.insert(0,strs)
        else:
            try:
                i=int(strs)
            except:
                return 0
            if i!=0:
                mass=str(x)+','+str(y)+','+str(i)
                self.s.send(mass.encode('utf-8'))
                m=self.s.recv(1024).decode('utf-8')
                if m=="T,F,T":
                    self.ctk+=1
                    w.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="green")
                elif m=="W":
                    w.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="green")
                    self.show_ms("you win")
                elif m=="L":
                    self.show_ms("you lose")
                else:
                    w.configure(fg="red")

                
    
    def full_table(self):
        if self.temp[0][0]!=0:
            self.lable1.insert(0,self.temp[0][0])
            self.lable1.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[0][1]!=0:
            self.lable2.insert(0,self.temp[0][1])
            self.lable2.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[0][2]!=0:
            self.lable3.insert(0,self.temp[0][2])
            self.lable3.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[0][3]!=0:
            self.lable4.insert(0,self.temp[0][3])
            self.lable4.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[0][4]!=0:
            self.lable5.insert(0,self.temp[0][4])
            self.lable5.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[0][5]!=0:
            self.lable6.insert(0,self.temp[0][5])
            self.lable6.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[0][6]!=0:
            self.lable7.insert(0,self.temp[0][6])
            self.lable7.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[0][7]!=0:
            self.lable8.insert(0,self.temp[0][7])
            self.lable8.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[0][8]!=0:
            self.lable9.insert(0,self.temp[0][8])
            self.lable9.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        #===================================
        if self.temp[1][0]!=0:
            self.lable10.insert(0,self.temp[1][0])
            self.lable10.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[1][1]!=0:
            self.lable11.insert(0,self.temp[1][1])
            self.lable11.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[1][2]!=0:
            self.lable12.insert(0,self.temp[1][2])
            self.lable12.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[1][3]!=0:
            self.lable13.insert(0,self.temp[1][3])
            self.lable13.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[1][4]!=0:
            self.lable14.insert(0,self.temp[1][4])
            self.lable14.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[1][5]!=0:
            self.lable15.insert(0,self.temp[1][5])
            self.lable15.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[1][6]!=0:
            self.lable16.insert(0,self.temp[1][6])
            self.lable16.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[1][7]!=0:
            self.lable17.insert(0,self.temp[1][7])
            self.lable17.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[1][8]!=0:
            self.lable18.insert(0,self.temp[1][8])
            self.lable18.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        #===================================
        if self.temp[2][0]!=0:
            self.lable19.insert(0,self.temp[2][0])
            self.lable19.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[2][1]!=0:
            self.lable20.insert(0,self.temp[2][1])
            self.lable20.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[2][2]!=0:
            self.lable21.insert(0,self.temp[2][2])
            self.lable21.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[2][3]!=0:
            self.lable22.insert(0,self.temp[2][3])
            self.lable22.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[2][4]!=0:
            self.lable23.insert(0,self.temp[2][4])
            self.lable23.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[2][5]!=0:
            self.lable24.insert(0,self.temp[2][5])
            self.lable24.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[2][6]!=0:
            self.lable25.insert(0,self.temp[2][6])
            self.lable25.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[2][7]!=0:
            self.lable26.insert(0,self.temp[2][7])
            self.lable26.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[2][8]!=0:
            self.lable27.insert(0,self.temp[2][8])
            self.lable27.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        #===================================
        if self.temp[3][0]!=0:
            self.lable28.insert(0,self.temp[3][0])
            self.lable28.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[3][1]!=0:
            self.lable29.insert(0,self.temp[3][1])
            self.lable29.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[3][2]!=0:
            self.lable30.insert(0,self.temp[3][2])
            self.lable30.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[3][3]!=0:
            self.lable31.insert(0,self.temp[3][3])
            self.lable31.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[3][4]!=0:
            self.lable32.insert(0,self.temp[3][4])
            self.lable32.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[3][5]!=0:
            self.lable33.insert(0,self.temp[3][5])
            self.lable33.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[3][6]!=0:
            self.lable34.insert(0,self.temp[3][6])
            self.lable34.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[3][7]!=0:
            self.lable35.insert(0,self.temp[3][7])
            self.lable35.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[3][8]!=0:
            self.lable36.insert(0,self.temp[3][8])
            self.lable36.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        #===================================
        if self.temp[4][0]!=0:
            self.lable37.insert(0,self.temp[4][0])
            self.lable37.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[4][1]!=0:
            self.lable38.insert(0,self.temp[4][1])
            self.lable38.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[4][2]!=0:
            self.lable39.insert(0,self.temp[4][2])
            self.lable39.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[4][3]!=0:
            self.lable40.insert(0,self.temp[4][3])
            self.lable40.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[4][4]!=0:
            self.lable41.insert(0,self.temp[4][4])
            self.lable41.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[4][5]!=0:
            self.lable42.insert(0,self.temp[4][5])
            self.lable42.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[4][6]!=0:
            self.lable43.insert(0,self.temp[4][6])
            self.lable43.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[4][7]!=0:
            self.lable44.insert(0,self.temp[4][7])
            self.lable44.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[4][8]!=0:
            self.lable45.insert(0,self.temp[4][8])
            self.lable45.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        #===================================
        if self.temp[5][0]!=0:
            self.lable46.insert(0,self.temp[5][0])
            self.lable46.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[5][1]!=0:
            self.lable47.insert(0,self.temp[5][1])
            self.lable47.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[5][2]!=0:
            self.lable48.insert(0,self.temp[5][2])
            self.lable48.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[5][3]!=0:
            self.lable49.insert(0,self.temp[5][3])
            self.lable49.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[5][4]!=0:
            self.lable50.insert(0,self.temp[5][4])
            self.lable50.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[5][5]!=0:
            self.lable51.insert(0,self.temp[5][5])
            self.lable51.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[5][6]!=0:
            self.lable52.insert(0,self.temp[5][6])
            self.lable52.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[5][7]!=0:
            self.lable53.insert(0,self.temp[5][7])
            self.lable53.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[5][8]!=0:
            self.lable54.insert(0,self.temp[5][8])
            self.lable54.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        #===================================
        if self.temp[6][0]!=0:
            self.lable55.insert(0,self.temp[6][0])
            self.lable55.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[6][1]!=0:
            self.lable56.insert(0,self.temp[6][1])
            self.lable56.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[6][2]!=0:
            self.lable57.insert(0,self.temp[6][2])
            self.lable57.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[6][3]!=0:
            self.lable58.insert(0,self.temp[6][3])
            self.lable58.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[6][4]!=0:
            self.lable59.insert(0,self.temp[6][4])
            self.lable59.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[6][5]!=0:
            self.lable60.insert(0,self.temp[6][5])
            self.lable60.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[6][6]!=0:
            self.lable61.insert(0,self.temp[6][6])
            self.lable61.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[6][7]!=0:
            self.lable62.insert(0,self.temp[6][7])
            self.lable62.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[6][8]!=0:
            self.lable63.insert(0,self.temp[6][8])
            self.lable63.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        #===================================
        if self.temp[7][0]!=0:
            self.lable64.insert(0,self.temp[7][0])
            self.lable64.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[7][1]!=0:
            self.lable65.insert(0,self.temp[7][1])
            self.lable65.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[7][2]!=0:
            self.lable66.insert(0,self.temp[7][2])
            self.lable66.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[7][3]!=0:
            self.lable67.insert(0,self.temp[7][3])
            self.lable67.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[7][4]!=0:
            self.lable68.insert(0,self.temp[7][4])
            self.lable68.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[7][5]!=0:
            self.lable69.insert(0,self.temp[7][5])
            self.lable69.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[7][6]!=0:
            self.lable70.insert(0,self.temp[7][6])
            self.lable70.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[7][7]!=0:
            self.lable71.insert(0,self.temp[7][7])
            self.lable71.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[7][8]!=0:
            self.lable72.insert(0,self.temp[7][8])
            self.lable72.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        #===================================
        if self.temp[8][0]!=0:
            self.lable73.insert(0,self.temp[8][0])
            self.lable73.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[8][1]!=0:
            self.lable74.insert(0,self.temp[8][1])
            self.lable74.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[8][2]!=0:
            self.lable75.insert(0,self.temp[8][2])
            self.lable75.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[8][3]!=0:
            self.lable76.insert(0,self.temp[8][3])
            self.lable76.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[8][4]!=0:
            self.lable77.insert(0,self.temp[8][4])
            self.lable77.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[8][5]!=0:
            self.lable78.insert(0,self.temp[8][5])
            self.lable78.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[8][6]!=0:
            self.lable79.insert(0,self.temp[8][6])
            self.lable79.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[8][7]!=0:
            self.lable80.insert(0,self.temp[8][7])
            self.lable80.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        if self.temp[8][8]!=0:
            self.lable81.insert(0,self.temp[8][8])
            self.lable81.configure(state="disabled", disabledbackground="#b3b3ba",disabledforeground="black")
        #===================================

        
        


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
