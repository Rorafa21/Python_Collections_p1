class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def depositar(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>>>Codigo {self._codigo} e Saldo {self._saldo}<<<]"

conta1 = ContaSalario(10)
print(conta1)