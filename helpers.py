import os
import time
def gotoxy(x,y):
    print("%c[%d;%df"%(0x1B,y,x),end="")

def borrarPantalla():
    os.system("cls") 

def mensaje(msg,f,c):
    pass

class valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True: 
            gotoxy(col,fil)            
            valor = input()
            try:
                if int(valor) > 0:
                    break
            except:
                gotoxy(col,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col,fil);print(" "*40)
        return valor

    def solo_letras(self,mensajeError,col,fil): 
        while True:
            gotoxy(col,fil) 
            valor = str(input())
            if valor.isalpha():
                break
            else:
                gotoxy(col,fil);print("<<{}>>".format(mensajeError))
                time.sleep(1)
                gotoxy(col,fil);print(" "*40)
        return valor

    def solo_decimales(self,mensaje,mensajeError):
        while True:
            valor = str(input(" {} ".format(mensaje)))
            try:
                valor = float(valor)
                if valor > float(0):
                    break
            except:
                print("          ------><  | {} ".format(mensajeError))
        return valor