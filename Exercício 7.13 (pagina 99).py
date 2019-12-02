class Conta:
    def __init__(self, numero, titular,saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite


    def deposita(self, valor):
        self.saldo += valor
        
    def saca(self, valor):
        if(self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            return True
        
    def extrato(self):
        print("numero: {] \nsaldo; {}".format(self.numero, self.saldo))
        
    def transfere_para(self, destino, valor):
        retirou = self.saca(valor)
        if(retirou == false):
            return false
        else:
            destino.deposita(valor)
            return True
        
minha_conta = Conta('123-4','Joao',120.0,1000.0)
minha_conta.saca(100)
print(minha_conta.saldo)
    
