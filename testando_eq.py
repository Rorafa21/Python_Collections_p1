class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._valor = 0

    def depositar(self, valor):
        self._saldo += valor

    def __str__(self):
        return f"[>>>Codigo {self._codigo} e Saldo {self._saldo}<<<]"

conta1 = ContaSalario(10)
print(conta1)