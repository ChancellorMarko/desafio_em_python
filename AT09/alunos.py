class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcularMedia(self):
        media = sum(self.notas) / len(self.notas)
        return media

    def verificarAprovacao(self):
        media = self.calcularMedia()
        if media >= 7:
            return f'O aluno {self.nome} está aprovado!'
        return f'O aluno {self.nome} não está aprovado!'

# Teste
Jose = Aluno('Jose', [60, 70, 90])
Maria = Aluno('Maria', [50, 60, 49])

print(f'Média de {Maria.nome}: {Maria.calcularMedia()}')
print(f'Média de {Jose.nome}: {Jose.calcularMedia()}')

print(Maria.verificarAprovacao())
print(Jose.verificarAprovacao())