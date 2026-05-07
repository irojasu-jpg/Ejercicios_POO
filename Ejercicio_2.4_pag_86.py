import math


class Circulo:
    def __init__(self, radio: int):
        self.radio = radio  # Atributo que define el radio de un círculo

    def calcular_area(self) -> float:
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self) -> float:
        return 2 * math.pi * self.radio

class Rectangulo:
    def __init__(self, base: int, altura: int):
        self.base = base      # Atributo que define la base de un rectángulo
        self.altura = altura  # Atributo que define la altura de un rectángulo

    def calcular_area(self) -> float:
        return self.base * self.altura

    def calcular_perimetro(self) -> float:
        return (2 * self.base) + (2 * self.altura)

class Cuadrado:
    def __init__(self, lado: int):
        self.lado = lado  # Atributo que define el lado de un cuadrado

    def calcular_area(self) -> float:
        return self.lado * self.lado

    def calcular_perimetro(self) -> float:
        return 4 * self.lado

class TrianguloRectangulo:
    def __init__(self, base: int, altura: int):
        self.base = base      # Atributo que define la base de un triángulo rectángulo
        self.altura = altura  # Atributo que define la altura de un triángulo rectángulo

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self) -> float:
        return math.pow(self.base * self.base + self.altura * self.altura, 0.5)

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()  # Invoca al método calcular_hipotenusa

    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()
        if (self.base == self.altura) and (self.base == hipotenusa) and (self.altura == hipotenusa):
            print("Es un triángulo equilátero")  # Todos sus lados son iguales
        elif (self.base != self.altura) and (self.base != hipotenusa) and (self.altura != hipotenusa):
            print("Es un triángulo escaleno")    # Todos sus lados son diferentes
        else:
            print("Es un triángulo isósceles")   # De otra manera, es isósceles

class PruebaFiguras:
    @staticmethod
    def main():
        # --- Círculo ---
        print("=== CÍRCULO ===")
        radio = int(input("Ingrese el radio del círculo: "))
        figura1 = Circulo(radio)
        print("El área del círculo es =", figura1.calcular_area())
        print("El perímetro del círculo es =", figura1.calcular_perimetro())

        # --- Rectángulo ---
        print("\n=== RECTÁNGULO ===")
        base_rect = int(input("Ingrese la base del rectángulo: "))
        altura_rect = int(input("Ingrese la altura del rectángulo: "))
        figura2 = Rectangulo(base_rect, altura_rect)
        print("El área del rectángulo es =", figura2.calcular_area())
        print("El perímetro del rectángulo es =", figura2.calcular_perimetro())

        # --- Cuadrado ---
        print("\n=== CUADRADO ===")
        lado = int(input("Ingrese el lado del cuadrado: "))
        figura3 = Cuadrado(lado)
        print("El área del cuadrado es =", figura3.calcular_area())
        print("El perímetro del cuadrado es =", figura3.calcular_perimetro())

        # --- Triángulo Rectángulo ---
        print("\n=== TRIÁNGULO RECTÁNGULO ===")
        base_tri = int(input("Ingrese la base del triángulo rectángulo: "))
        altura_tri = int(input("Ingrese la altura del triángulo rectángulo: "))
        figura4 = TrianguloRectangulo(base_tri, altura_tri)
        print("El área del triángulo es =", figura4.calcular_area())
        print("El perímetro del triángulo es =", figura4.calcular_perimetro())
        figura4.determinar_tipo_triangulo()


# Punto de entrada del programa
if __name__ == "__main__":
    PruebaFiguras.main()