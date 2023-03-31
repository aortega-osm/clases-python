#Calcular el area de un rectangulo  A=base x altura
#ejercicio realizado por mi
class Calculo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
def Multiplicar(base,altura):
        area=base*altura
        return area

base= int(input("Proporcione una base:"))
altura= int(input("Proporcione una altura:"))

rectangulo =Multiplicar(base,altura)
print(f"Area:{rectangulo}")



