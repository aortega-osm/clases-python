#Calcular el volumen de un cubo creando una clase cubo asigando el ancho el alto y la profundidad y utilizando un
# metodo que sea el ancho*alto*profundidad
class Cubo:
    def __init__(self, ancho, alto, profundidad):
        self.ancho = ancho
        self.alto = alto
        self.profundidad = profundidad
    def calculo(self):
        return self.ancho * self.alto * self.profundidad

ancho =int(input("Proporcione el ancho:"))
alto =int(input("Proporcione el alto:"))
profundidad =int(input("Proporcione la profundidad:"))

resultado = Cubo( ancho, alto, profundidad)
print(f"El volumen del cubo es:{resultado.calculo()}")