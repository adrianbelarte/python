### ÁREA DE UN POLÍGONO ###

"""
/*
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
    Triangulo = Área = (a x p)/2
    cuadrado = Área = Lado x Lado
    Rectangulo =  Área = Largo x ancho
"""
class Poligono:
    @staticmethod
    def calcular_area(tipo, *args):
        if tipo == "triangulo":
            if len(args) != 2:
                raise ValueError("El triángulo necesita base y altura.")
            base, altura = args
            return (base * altura) / 2
        elif tipo == "cuadrado":
            if len(args) != 1:
                raise ValueError("El cuadrado necesita un lado.")
            lado = args[0]
            return lado * lado
        elif tipo == "rectangulo":
            if len(args) != 2:
                raise ValueError("El rectángulo necesita largo y ancho.")
            largo, ancho = args
            return largo * ancho
        else:
            raise ValueError("Tipo de polígono no soportado.")

# Ejemplos de uso
print("Área del triángulo:", Poligono.calcular_area("triangulo", 5, 10))
print("Área del cuadrado:", Poligono.calcular_area("cuadrado", 5))
print("Área del rectángulo:", Poligono.calcular_area("rectangulo", 3, 7))


