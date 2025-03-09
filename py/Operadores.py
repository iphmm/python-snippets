class Operadores:
    @staticmethod
    def demonstrar_operadores():
        a, b = 20, 2  # Definindo variáveis inteiras

        print(f"{a} + {b}  = {a + b}")  # Soma
        print(f"{a} - {b}  = {a - b}")  # Subtração
        print(f"{a} * {b}  = {a * b}")  # Multiplicação
        print(f"{a} / {b}  = {a / b}" ) # Divisão normal - sempre retorna float
        print(f"{a} // {b} = {a // b}") # Divisão inteira - retorna int se ambos forem inteiros
        print(f"{a} % {b}  = {a % b} ") # Resto da divisão
        print(f"{a} ** {b} = {a ** b} ")# Exponenciação

        # Exemplo de divisão entre um int e um float
        c = 20.0  # Agora `c` é um float
        print(f"{c} // {b} = {c // b}") # Divisão inteira com float - retorna float

# Testando os operadores
Operadores.demonstrar_operadores()
