class Logica:
    def __init__(self, lista=None):
        self.__lista = lista

    @property
    def lista(self):
        return self.__lista

    @lista.setter
    def lista(self, valor):
        self.__lista = valor

    def parImpar(self, numero):
        rec = numero % 2
        if rec == 0:
            print('{} es par.'.format(numero))
        else:
            print('{} es impar.'.format(numero))

    def perfecto(self, numero):
        cont = 0
        for contador in range(1, numero):
            rec = numero % contador
            if rec == 0:
                cont += contador
        if cont == numero:
            print('{} es perfecto.'.format(numero))
        else:
            print('{} no es perfecto.'.format(numero))


class Ejercicio(Logica):
    def __init__(self, lista, numero):
        super().__init__(lista)
        self.dato = numero

    def suma(self, n1, n2):
        return n1 + n2

    def parImpar(self, numero):
        super().parImpar(numero)
        return numero % 2


obj_ej = Ejercicio([1, 3, 5], 20)
if obj_ej.parImpar(6) == 0:
    print('Par')
else:
    print('Impar')
print(obj_ej.lista)