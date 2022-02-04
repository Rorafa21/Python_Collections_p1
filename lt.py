from operator import attrgetter

class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        return self._saldo < outro._saldo

    def depositar(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>>>Codigo {self._codigo} e Saldo {self._saldo}<<<]"

conta_do_gui = ContaSalario(17)
conta_do_gui.depositar (500)

conta_da_rafa = ContaSalario(3)
conta_da_rafa.depositar(1000)

conta_do_ita = ContaSalario(8)
conta_do_ita.depositar(2000)

contas = [conta_da_rafa, conta_do_gui, conta_do_ita]

print(conta_do_gui > conta_da_rafa)

for conta in sorted(contas):
    print (conta)