class TarjetaMetrobus():
    def __init__(self):
        self.__saldo = 0

    def recargar(self, monto):
        saldotemp = self.__saldo+monto
        if all([saldotemp>1, saldotemp<=120]):
            self.__saldo = saldotemp
            return True
        return False
        
    def cobrar(self):
        saldotemp = self.__saldo-6
        if saldotemp>=0:
            self.__saldo=self.__saldo-6
            return True
        return False
    def getSaldo(self):
        return self.__saldo
def menu():
    print("1. Recargar")
    print("2. Pasar al metrobús")
    print("3. Consultar saldo")
    print("4. Salir")

tarjeta = TarjetaMetrobus()
while True:
    menu()
    opcion = int(input("Opción: "))
    if opcion == 1:
        saldo = int(input("Saldo: "))
        if tarjeta.recargar(saldo):
            print("¡Recarga exitosa!")
        else:
            print("¡Recarga fallida!")
    elif opcion == 2:
        if tarjeta.cobrar():
            print("Pase usted")
        else:
            print("Saldo insuficiente")
    elif opcion == 3:
        print("Su saldo es: $" + str(tarjeta.getSaldo()))
    elif opcion == 4:
        print("Gracias por su elección")
        exit(1)
