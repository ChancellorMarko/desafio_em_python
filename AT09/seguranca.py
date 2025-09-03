class Seguranca:
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def _criptografar_mensagem(self):
        mensagem_criptografada = 'Segredo!'
        return mensagem_criptografada

    def mostrarFraseCriptografada(self):
        return self._criptografar_mensagem()


# Teste
mensagem_crip = 'Olá, Sou maria!'
seguranca = Seguranca(mensagem_crip)
print(f'A mensagem criptografada é: {seguranca.mostrarFraseCriptografada()}')