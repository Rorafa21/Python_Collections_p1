#LISTAS - Mutavel
class Contacorrente:


    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return f"[>>Codigo {self.codigo} Saldo {self.saldo}<<<]"

conta_do_gui = Contacorrente(15)
print(conta_do_gui)
conta_do_gui.deposita(500)
print(conta_do_gui)


conta_da_rafa = Contacorrente(47685)
conta_da_rafa.deposita(1000)
print(conta_da_rafa)

#TUPLA - Imutavel

guilherme = ("Guilherme", 37, 1981)
rafaelly = ("Rafaelly", 20, 2001)

#paulo = (21, "Paulo", 2005) - desfaz a ordem.
#conta_do_gui = (15, 1000) funciona mas não seria possivel alterar valores de forma simples.

