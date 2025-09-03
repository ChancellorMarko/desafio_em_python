class Matematica:
    def __init__(self, numero):
        self.numero = numero

    def ePrimo(self):
        if (self.numero % 2) != 0:
            return True
        return False

# Teste

numero3 = Matematica(3)
numero4 = Matematica(4)
numero6 = Matematica(6)
numero7 = Matematica(7)

print(f'O numero 3: {numero3.ePrimo()}')
print(f'O numero 4: {numero4.ePrimo()}')
print(f'O numero 6: {numero6.ePrimo()}')
print(f'O numero 7: {numero7.ePrimo()}')
