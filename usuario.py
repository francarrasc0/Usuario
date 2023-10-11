class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre =  nombre
        self.apellido = apellido
        self.balance_cuenta = 0
    
    def hacer_deposito (self, amount):
        self.balance_cuenta += amount
    
    def hacer_retiro (self, amount):
        self.balance_cuenta -= amount
    
    def mostrar_balance_usuario (self):
        print (f'{self.nombre} {self.apellido}, Balance: {self.balance_cuenta}')
    
    def transferir_dinero(self, otro_usuario, amount):
        if self.balance_cuenta >= amount:
            self.balance_cuenta -= amount
            otro_usuario.balance_cuenta += amount
            print(f'{self.nombre} ha transferido {amount} a {otro_usuario.nombre}')
        else:
            print('Saldo insuficiente para realizar la transferencia.')

Miguel = Usuario('Miguel', 'Espinoza')
Esteban = Usuario('Esteban', 'Perez')
Camila = Usuario('Camila', 'Martinez')

Miguel.hacer_deposito(200)
Miguel.hacer_deposito(300)
Miguel.hacer_deposito(50)
Miguel.hacer_retiro(200)
Miguel.mostrar_balance_usuario()

Esteban.hacer_deposito(250)
Esteban.hacer_deposito(250)
Esteban.hacer_retiro(100)
Esteban.hacer_retiro(100)
Esteban.mostrar_balance_usuario()

Camila.hacer_deposito(800)
Camila.hacer_retiro(100)
Camila.hacer_retiro(50)
Camila.hacer_retiro(200)
Camila.mostrar_balance_usuario()

Miguel.transferir_dinero(Camila, 200)
Miguel.mostrar_balance_usuario()
Camila.mostrar_balance_usuario()