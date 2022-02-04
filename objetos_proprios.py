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

contas = [conta_da_rafa, conta_do_gui]
print (contas)