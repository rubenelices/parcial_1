import random

class CuentaBancaria():

    def __init__(self,id,titular,fecha,numerocuenta,saldo):
        self.id=id
        self.titular=titular
        self.fecha=fecha
        self.numerocuenta=numerocuenta
        self.saldo=saldo
 
    #GETTERS
    def get_id(self):
        return self.id

    def get_titular(self):
        return self.titular

    def get_Fecha(self):
        return self.fecha

    def get_numerocuenta(self):
        return self.numerocuenta

    def get_saldo(self):
        return self.saldo
    
    #SETTERS
    def set_id(self,id):
        self.id=id

    def set_titular(self,titular):
        self.titular=titular

    def set_Fecha(self,fecha):
        self.fecha=fecha

    def set_numerocuenta(self,numerocuenta):
        self.numerocuenta=numerocuenta

    def set_saldo(self,saldo):
        self.saldo=saldo

   
    #METODOS
    def retirardinero(self,dinero):
        if (self.saldo>=dinero):
            self.saldo=self.saldo-dinero
        else:
            print("Error, quiere retirar más dinero del que tienes")

    def ingresardinero(self, dinero):
        self.saldo=self.saldo+dinero

    def transferirdinero(self,dinero,cuenta):
        if (self.saldo>=dinero):
            self.saldo=self.saldo-dinero
            cuenta.saldo=cuenta.saldo+dinero
        else:
            print("Error, quiere transferir más dinero del que tienes")

    def cuenta(self):
        return "Cuenta bancaria: " + str(self.id) + " Saldo: " + str(self.saldo)


def esBisiesto(año):
    Bisiesto=False
    if(año%4==0):
        if(año%100==0):
            if(año%400==0):
                Bisiesto=True
        else:
            Bisiesto=True
    return Bisiesto

def escribirfecha():
    año=random.randint(2021,2050)
    mes=random.randint(1,12)
    día=0
    if(mes==2):
        if(esBisiesto(año)==True):
            día=random.randint(1,29)
        else:
            día=random.randint(1,28)
    elif(mes==4 or mes==6 or mes==9 or mes==11):
        día=random.randint(1,30)
    else:
        día=random.randint(1,31)
    fecha=[año,mes,día]
    return fecha

def fechatostring(fecha):
    return str(fecha[2])+"/"+str(fecha[1])+"/"+str(fecha[0])

def compararfechas(fecha1,fecha2):
    fecha3=fechamenor(fecha1,fecha2)
    if(fecha1!=fecha3):
        return 1
    elif(fecha2!=fecha3):
        return -1
    else:
        return 0

def fechamenor(fecha1,fecha2):
    if(fecha1[0]>fecha2[0]):
        mayor=fecha1
        menor=fecha2
    elif(fecha1[0]<fecha2[0]):
        mayor=fecha2
        menor=fecha1
    else:
        if(fecha1[1]>fecha2[1]):
            mayor=fecha1
            menor=fecha2
        elif(fecha1[1]<fecha2[1]):
            mayor=fecha2
            menor=fecha1
        else:
            if(fecha1[2]>fecha2[2]):
                mayor=fecha1
                menor=fecha2
            elif(fecha1[2]<fecha2[2]):
                mayor=fecha2
                menor=fecha1
            else:
                mayor=fecha1
                menor=fecha2
    return menor

def crearnumero():
    numero=0
    for i in range(0,13):
        num=random.randint(0,9)
        numero+=num*10^i
    return numero
