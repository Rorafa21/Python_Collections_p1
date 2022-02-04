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