class Tienda:
    def __init__(self, precio, precioC, descuento, alta_baja):
        self.precio = precio
        self.precioC = precioC
        self.descuento = descuento
        self.alta_baja = alta_baja

    def precio_(self):
        print("El precio del producto es de: ", self.precio)

    def cambiar_p(self):
        self.precio == self.precioC
        print("El nuevo precio del producto es de: ", self.precioC)

    def descuentos(self):
        print("El producto tiene un descuento del: ", self.descuento, "%")

    def dadoA_B(self):
        if self.alta_baja == True:
            print("El producto fue dado de alta")
        else:
            print("El producto fue dado de baja")


producto = tienda(5000, 6500, 10, False)
producto.precio_()
producto.cambiar_p()
producto.descuentos()
producto.dadoA_B()
