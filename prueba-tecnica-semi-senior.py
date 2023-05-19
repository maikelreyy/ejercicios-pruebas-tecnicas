'''crear una funcion que convierta numeros romanos en numeros enteros'''

'''creamos una clase para crear el objeto con los numeros y su valor'''
class NumerosRomanos:
    def __init__(self):
        self.valorNumeros = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

    def convertir_a_entero(self, numero_romano):
        resultado = 0
        i = 0
        while i < len(numero_romano):
            if i + 1 < len(numero_romano) and self.valorNumeros.get(numero_romano[i]) < self.valorNumeros.get(numero_romano[i + 1]):
                resultado += self.valorNumeros.get(numero_romano[i + 1]) - self.valorNumeros.get(numero_romano[i])
                i += 2
            else:
                resultado += self.valorNumeros.get(numero_romano[i])
                i += 1
        return resultado


# Crear una instancia de la clase NumerosRomanos
numeros_romanos = NumerosRomanos()

# Ejemplo de conversión de número romano a entero
numero_entero = numeros_romanos.convertir_a_entero('XLIV')
print(numero_entero)  # Imprime: 24

# Ejemplo de conversión de número romano a entero
numero_entero = numeros_romanos.convertir_a_entero('XIV')
print(numero_entero)  # Imprime: 14
