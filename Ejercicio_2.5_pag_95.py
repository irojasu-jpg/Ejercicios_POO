from enum import Enum

# Tipo de cuenta como un valor enumerado
class Tipo(Enum):
    AHORROS = "AHORROS"
    CORRIENTE = "CORRIENTE"


"""
Esta clase define objetos que representan una cuenta bancaria que
tienen un nombre y apellidos del titular, un número de cuenta, un
tipo de cuenta (ahorros o corriente) y un saldo.
@version 1.2/2020
"""
class CuentaBancaria:
    def __init__(self, nombres_titular: str, apellidos_titular: str,
                 numero_cuenta: int, tipo_cuenta: Tipo):
        """
        Constructor de la clase CuentaBancaria
        @param nombres_titular: Parámetro que define los nombres del titular de una cuenta bancaria
        @param apellidos_titular: Parámetro que define los apellidos del titular de una cuenta bancaria
        @param numero_cuenta: Parámetro que define el número de una cuenta bancaria
        @param tipo_cuenta: Parámetro que define el tipo de una cuenta bancaria (puede ser ahorros o corriente)
        Tener en cuenta que no se pasa como parámetro el saldo ya que inicialmente es cero.
        """
        self.nombres_titular = nombres_titular    # Atributo que define los nombres del titular de la cuenta bancaria
        self.apellidos_titular = apellidos_titular  # Atributo que define los apellidos del titular de la cuenta bancaria
        self.numero_cuenta = numero_cuenta        # Atributo que define el número de la cuenta bancaria
        self.tipo_cuenta = tipo_cuenta            # Atributo que define el tipo de cuenta bancaria
        self.saldo: float = 0                     # Atributo que define el saldo de la cuenta bancaria con valor inicial cero

    def imprimir(self):
        """
        Método que imprime en pantalla los datos de una cuenta bancaria
        """
        print("Nombres del titular =", self.nombres_titular)
        print("Apellidos del titular =", self.apellidos_titular)
        print("Número de cuenta =", self.numero_cuenta)
        print("Tipo de cuenta =", self.tipo_cuenta.value)
        print("Saldo =", self.saldo)

    def consultar_saldo(self):
        """
        Método que imprime en pantalla el saldo actual de una cuenta bancaria
        """
        print("El saldo actual es =", self.saldo)

    def consignar(self, valor: int) -> bool:
        """
        Método que actualiza y devuelve el saldo de una cuenta bancaria a
        partir de un valor a consignar
        @param valor: Parámetro que define el valor a consignar en la cuenta bancaria.
                      El valor debe ser mayor que cero
        @return: Valor booleano que indica si el valor a consignar es válido o no
        """
        # El valor a consignar debe ser mayor que cero
        if valor > 0:
            self.saldo = self.saldo + valor  # Se actualiza el saldo de la cuenta con el valor consignado
            print(f"Se ha consignado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor: int) -> bool:
        """
        Método que actualiza y devuelve el saldo de una cuenta bancaria a
        partir de un valor a retirar
        @param valor: Parámetro que define el valor a retirar en la cuenta bancaria.
                      El valor debe ser mayor que cero y el saldo de la cuenta
                      debe quedar con un valor positivo o igual a cero
        @return: Valor booleano que indica si el valor a retirar es válido o no
        """
        # El valor debe ser mayor que cero y no debe superar el saldo actual
        if (valor > 0) and (valor <= self.saldo):
            self.saldo = self.saldo - valor  # Se actualiza el saldo de la cuenta con el valor retirado
            print(f"Se ha retirado ${valor} en la cuenta. El nuevo saldo es ${self.saldo}")
            return True
        else:
            print("El valor a retirar debe ser menor que el saldo actual.")
            return False


"""
Esta clase prueba las operaciones de una cuenta bancaria.
@version 1.2/2020
"""
class PruebaCuenta:
    @staticmethod
    def main():
        """
        Método main que crea una cuenta bancaria sobre la cual se
        realizan las operaciones de consignar y retirar
        """
        print("=== CREAR CUENTA BANCARIA ===")
        nombres = input("Ingrese los nombres del titular: ")
        apellidos = input("Ingrese los apellidos del titular: ")
        numero_cuenta = int(input("Ingrese el número de cuenta: "))

        print("Tipo de cuenta:")
        print("  1. AHORROS")
        print("  2. CORRIENTE")
        opcion = input("Seleccione una opción (1 o 2): ")
        tipo_cuenta = Tipo.AHORROS if opcion == "1" else Tipo.CORRIENTE

        cuenta = CuentaBancaria(nombres, apellidos, numero_cuenta, tipo_cuenta)

        print("\n=== DATOS DE LA CUENTA ===")
        cuenta.imprimir()

        print("\n=== OPERACIONES ===")
        while True:
            print("\n¿Qué operación desea realizar?")
            print("  1. Consignar")
            print("  2. Retirar")
            print("  3. Consultar saldo")
            print("  4. Salir")
            op = input("Seleccione una opción: ")

            if op == "1":
                valor = int(input("Ingrese el valor a consignar: "))
                cuenta.consignar(valor)
            elif op == "2":
                valor = int(input("Ingrese el valor a retirar: "))
                cuenta.retirar(valor)
            elif op == "3":
                cuenta.consultar_saldo()
            elif op == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")


# Punto de entrada del programa
if __name__ == "__main__":
    PruebaCuenta.main()