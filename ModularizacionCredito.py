"""
Para gestionar un crédito rotativo se tiene un tomador al que se le asigna un cupo diferido a un numero de cuotas fijas, 
el crédito lo puede utilizar para realizar una o varias compras, cada compra que realiza se le difiere en el número de cuotas 
fijas aprobadas, siempre que el valor total no supere el cupo  disponible, esto implica que el tomador puede tener disponible 
el total del cupo o una parte porque está pagando compras, también puede ocurrir que no pueda comprar porque el cupo disponible 
no es suficiente; cuando se abona a la deuda el cupo disponible aumenta. 
Se requiere realizar el proceso de abstracción y modularización del problema, codificación en Python y prueba de funcionalidad básica.
"""
class Registar:
    def __init__(self,Name,Id_user,status):
        self.Name = Name
        self.Id_user = Id_user
        self.status = status

    def RegisterUser(self):
        self.Name = input("\n Ingrese nombre de usuario: ")
        self.Id_user = input("\n Ingrese numero de id: ")

class Assignment_Credit:
    def __init__(self,credit,fees,buys,cupo,deposit):
        self.credit = credit
        self.fees = fees
        self.cupo = cupo        
        self.buys = buys
        self.deposit = deposit

    def Credit(self):
        print("Su total a pagar es",self.credit)
        print("Va a pagar a ",self.fees,"cuotas")

    def Buys(self):
        print("Tienes cupo de",self.cupo)
        self.buys = int(input("Valor de la compra: "))
        if self.buys > self.cupo:
            print("La Compra tiene que ser Menor a:  ",self.cupo)
        if self.buys <= self.cupo:
            self.cupo -= self.buys
            print("\n Usted Realizo Una Compra Por el Valor De: ", self.buys, "\n Y Ahora Su Cupo Es De: ",
                  self.cupo)
        if self.cupo == 0:
            print("\n No Tiene Cupo Disponoble Por Lo Que No Puede Realizar Su Compra")

    def abono(self):

        print("\n Usted debe la cantidad de : ",self.credit-self.cupo)
        cuota = self.credit/self.fees
        print("\n Cada cuota tiene el valor de : ",cuota)
        self.deposit = int(input("\n Ingrese la cantidad de cuotas que desea pagar : "))
        self.deposit *= cuota
        if self.deposit > self.credit-self.cupo:
            print("\n Su abono supera la deuda\n Debe ser menor a : ",self.credit-self.cupo)
        if self.deposit <= self.credit-self.cupo:
            print("\n Usted abono : ",self.deposit)
            self.cupo += self.deposit
            print("\n Ahora su cupo es de : ",self.cupo)
            self.deposit = 0

p1 = Registar("","",True)
p1.RegisterUser()
p2 = Assignment_Credit(600000,12,0,600000,0)
