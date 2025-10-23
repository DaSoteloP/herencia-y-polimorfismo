class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad
    def hablar(self):
        pass
    def moverse(self):
        pass
    def describeme(self):
        print("Soy un animal del tipo", type(self).__name__)

class perro(Animal):
    def __init__(self, especie, edad,dueño):
        super().__init__(especie, edad)
        self.dueño = dueño
    def hablar(self):
        print("guau")
    def moverse(self):
        print("caminando con 4 patas")
    def casa(self):
        print("vivo con mi dueñ@:", self.dueño)

class Vaca(Animal):
    def hablar(self):
        print("moo")
    def moverse(self):
        print("caminando con 4 pataas")

class abeja(Animal):
    def hablar(self):
        print("Bzzz")
    def moverse(self):
        print("volando")
    def picar(self):
        print("atacar")

class gato(Animal):    
    def __init__(self, especie, edad,dueño):
        super().__init__(especie, edad)
        self.dueño = dueño
    def hablar(self):
        print('miau')
    def moverse(self):
        print("caminando a cuatro patas")
    def casa(self):
        print("vivo con mi dueñ@:", self.dueño)



class Pez(Animal):
    def hablar(self):
        print('glu glu glu')
    def moverse(self):
        print("nadando")

mi_perro = perro('mamifero',10,'javi')
mi_vaca = Vaca('mamifero',6)
esa_abeja = abeja("insecto",1)
gatito = gato("mamifero",4,"martha")

def main():
    mi_perro.describeme()
    mi_perro.hablar()
    mi_perro.casa()

    mi_vaca.hablar()
    mi_vaca.moverse()
    
    esa_abeja.picar()
    
    gatito.casa()

if __name__ == "__main__":
    main()