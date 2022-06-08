class Barco:
    def __init__(self, color, bandera, toneladas, matricula):
        self.color = color
        self.bandera = bandera
        self.toneladas = toneladas
        self.matricula = matricula

    def mensaje(self):
        print("Conozco un barco ", self.color, "de bandera", self.bandera, ", su capacidad es de", self.toneladas,
              "toneladas y su matrícula es", self.matricula)


M = barco("azul", "Panameña", 3000, "PMZ876")
M.mensaje()
