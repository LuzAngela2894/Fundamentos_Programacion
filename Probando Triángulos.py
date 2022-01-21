def esUnTriangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

#Teorema de Pitagoras
def esUnTrianguloRectangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2

#Fórmula de Heron
def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5

def campoTriangulo(a, b, c):
    if not esUnTriangulo(a, b, c):
        return None
    return heron(a, b, c)

a = float(input("Ingresa la longitud del primer lado: "))
b = float(input("Ingresa la longitud del segundo lado: "))
c = float(input("Ingresa la longitud del tercer lado: "))

if esUnTriangulo(a, b, c):
    print("Felicidades, puede ser un triángulo.")
else:
    print("Lo siento, no puede ser un triángulo.")

if esUnTrianguloRectangulo(a, b, c):
    print("Felicidades, puede ser un triángulo rectángulo.")
else:
    print("Lo siento, no puede ser un triángulo rectángulo.")

print(campoTriangulo(1., 1., 2. ** .5))
