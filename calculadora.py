class Usuario:
    def __init__(self, saldo_inicial):
        self.saldo_inicial = saldo_inicial

    def sacar(self, valor):
        self.saldo_inicial -= valor

def main():
    sum = 0
    try:
        numbers = input("Enter a comma-separated list of numbers: ").split(",")
        for num in numbers:
            sum = sum + int(num)
        print(f"Sum of {numbers} = {sum}")
    except ValueError:
        print("Error: invalid input")
        return

result = int(input("valor: "))
match result:
    case 0:
        print("Properly handle zero case.")

    case 1:
        print("Properly handle one case.")

print("ok")

if __name__ == '__main__':
    main()

    usuario_novo = Usuario(1000)
    usuario_novo.sacar(float(input("digite um valor para sacar: ")))