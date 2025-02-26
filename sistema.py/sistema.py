class Supermercado:
    def __init__(self):
        self.catalogo = {'arroz': 10.0, 'feijao': 8.5, 'macarrao':5.0, 'carne':25.0}
        self.carrinho = {}
        self.total = 0.0
        
   
    def comprar(self):
        while True:
            print('catalogo de produtos:')
            for produto, preco in self.catalogo.items():
                print(f'{produto.capitalize()} - R${preco:.2f}')
                
            escolha = input('digite o nome do produto que deseja comprar(ou "sair" para encerrar):')
            if escolha.lower() == 'sair':
                break
            
            if escolha in self.catalogo:
                quantidade = int(input('digite a quantidade desejada:'))
                if escolha in self.carrinho:
                    self.carrinho[escolha] += quantidade
                else:
                    self.carrinho[escolha] = quantidade
                print(f'{quantidade} unidades de {escolha.capitalize()} adicionadas ao carrinho.')    
            else:
                print('produto nao encontrado no catalogo. Tente novamente.')
                
        print('\nResumo da compra')
        for produto, quantidade in self.carrinho.items():
            preco_unitario = self.catalogo[produto]
            preco_total = preco_unitario * quantidade 
            print(f'{quantidade} unidades de {produto.capitalize()} - R${preco_total:.2f}')   
            self.total += preco_total
            
        print(f'Total da compra: R${self.total:.2f}')
        self.pagar
    
    def pagar(self):
        pagamento = input('Digite o valor recebido pelo cliente (ou "cancelar" para cancelar a compra)')
        if pagamento.lower() == 'cancelar':
            print('Compra cancelada.')
            return
        
        valor_pago = float(pagamento)
        troco = valor_pago - self.total
        
        if troco > 0:
            print(f'Valor insuficiente. Faltam R${-troco:.2f}.')
            self.pagar()
        else:
             if troco > 0:
              print(f'Troco: R${troco:.2f}')
        cpf_nota = input('Deseja informar o CPF na nota fiscal? (sim/não):')
        if cpf_nota.lower() == 'sim':
            cpf = input('Digite o CPF:')
            print(f'Nota fiscal: Total da compra - R${self.total:.2f} | CPF - {cpf}')
        else:
            print(f'Nota fiscal: Total da compra - R${self.total:.2f}') 
               
        self.catalogo = {'arroz': 10.0, 'feijao': 8.5, 'macarrao':5.0, 'carne':25.0}
        self.carrinho = {}
        self.total = 0.0
        
mercado = Supermercado()
mercado.comprar()            
            
        
       
                           