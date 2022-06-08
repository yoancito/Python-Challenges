class Compra:
    def __init__(self, precioU, cantU, dcto):
        self.precioU = precioU
        self.cantU = cantU
        self.dcto = dcto

    def pagoSinIva(self):
        return self.precioU * self.cantU

    def cobroIva(self):
        return self.pagoSinIva() * 0.19

    def pagoTotalIva(self):
        return self.pagoSinIva() + self.cobroIva()

    def descuento(self):
        return self.pagoTotalIva() * self.dcto

    def pagoTotal(self):
        return self.pagoTotalIva() - self.descuento()


c1 = Compra(6500, 6, 0.25)
print("El pago sin IVA es: ", c1.pagoSinIva())
print("El cobro del IVA es: ", c1.cobroIva())
print("El cobro total con IVA es: ", c1.pagoTotalIva())
print("El descuento es de: ", c1.descuento())
print("El pago total con descuento e IVA incluido es de: ", c1.pagoTotal())
