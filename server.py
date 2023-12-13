from _thread import *
import socket
from warnings import catch_warnings
import dataconvertor
# generate random integer values
from random import seed
from random import randint



#playerNumber
number=2

allcon=False
closedcon=0
clients=[]
iw=False
winer=0
mostct=0

class Serversudoku:

    def __init__(self,temp,stat,ct,ans) :
        self.board=temp
        self.boardstat=stat
        self.isfinished=False
        self.currentx=0
        self.currenty=0
        self.count=ct
        self.validType=True
        self.answ=ans
        self.iswin=False
        self.is_loose=False

    def lose(self):
        self.is_loose=False

    def SetPosittion(self,x,y):
        self.currentx=int(x)
        self.currenty=int(y)

    def IsValid(self,num):
        if num<10 and num>0:
            return True
        return False

    def IsFilled(self):
        return self.boardstat[self.currentx][self.currenty]>1#3=preset 2=true 1=false 0=empty


    def IsCorrect(self,num):
        if num==self.answ[self.currentx][self.currenty]:
            return True
        self.boardstat[self.currentx][self.currenty]=1
        return False
        

    def SetNumber(self,num):
        if self.IsValid(num):

            if not self.IsFilled():
                self.board[self.currentx][self.currenty]=num
                if self.IsCorrect(num):
                    self.count+=1
                    global mostct
                    if self.count>mostct:
                        mostct=self.count
                    if self.count==81:
                        self.iswin=True
                        return "W"
                    return "T,F,T"
                else:
                    return "T,F,F"
            else :
                return "T,T,F"
        else:
            return "F,T,F"

    def RunGame(self,client):
        global mostct,allcon

        while allcon==False:
            pass
        client.send("T".encode('utf-8'))
        while self.count<81:
            mass=client.recv(1024).decode('utf-8')
            if mass=="L":
                m=str(mostct)
                client.send(m.encode('utf-8'))
            else:
                m=mass.split(',')
                numbe = int(m[2]) 
                self.SetPosittion(m[0],m[1])
                vfc=self.SetNumber(numbe)
                if self.is_loose==True:
                    vfc='L'
                try:
                    client.send(vfc.encode('utf-8'))
                except:
                    pass

def make(n,tempstr,stat,ct,answ):
    client, addr = server.accept()
    global clients
    clients.append(client)
    client.send("g".encode('utf-8'))
    client.send(tempstr.encode('utf-8'))
    start_new_thread(sodserv,(client,n,stat,ct,answ,))
    pass


def win(ids):
    global iw,winer
    winer=ids
    iw=True


def sodserv(cl,id,stat,ct,answ):
    sod=Serversudoku(temp,stat,ct,answ)
    try:
        sod.RunGame(cl)
    except:
        global closedcon
        closedcon+=1
    while sod.iswin==False:
        pass
    win(id)
    for clin in clients:
        clin.send('L'.encode('utf-8'))

ip = '127.0.0.1'
port = 5230
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip , port))
server.listen(number)

#random sudoku
csvf = open("sudoku.csv")
sudreader = csvf.readlines()
seed(1)
i = randint(1, 99)
sudy=sudreader[i].split(',')
tempstr=sudy[0]
answstr=sudy[1]

csvf.close
csvf="0"



temp=dataconvertor.ConvertToSudoko(tempstr)
statandct=dataconvertor.statmaker(temp)
stat=statandct[0]
answ=dataconvertor.ConvertToSudoko(answstr)

ct=statandct[1]
mostct=ct
for i in range(number):
    make(i,tempstr,stat,ct,answ)
    if i==number-1:
        allcon=True

while iw==False:
    pass
print("winer =",winer)

while closedcon!=number-1:
    pass

for clin in clients:
        clin.close()  

server.close()

