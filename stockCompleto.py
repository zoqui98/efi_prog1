from baseDeDatos import Database
base = Database('stockDePelis','id','title', 'genre', 'principalActor','director', 'year', 'price','status','activo')

class Pelicula:
    def __init__(self, id, titulo, genero, protagonista, director, year, precio, estado,activo):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.year = year
        self.protagonista = protagonista
        self.director = director
        self.precio = precio
        self.alquilado = estado
        self.activo = activo

    def getId(self):
        return self.id

    def getTitulo(self):
        return self.titulo

    def getGenero(self):
        return self.genero

    def getProtagonista(self):
        return self.protagonista

    def getDirector(self):
        return self.director

    def getYear(self):
        return self.year

    def getPrecio(self):
        return self.precio

    def getEstado(self):
        if self.alquilado == 1:
            return 'Alquilada'
        else:
            return 'NO alquilada'

    def getActivo(self):
        return self.activo

class Stock:
    def __init__(self):
        datos = base.select()
        self.stock = []
        for e in datos:
            if e[8] == 1:
                peli = Pelicula(e[0], e[1], e[2], e[3], e[4], e[5], e[6], e[7], e[8])
                self.stock.append(peli)

    def addPelicula(self,id,titulo,genero,protagonista,director,year,precio): 
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.protagonista = protagonista
        self.director = director
        self.year = year
        self.precio = '$'+str(precio)
        estado = 0
        activo = 1
        base.insert(self.id, self.titulo, self.genero, self.protagonista, self.director, self.year, self.precio, estado, activo)

    def alquilarPelicula(self,titulo):
         for peli in self.stock:
            if titulo == peli.getTitulo():
                base.update(int(peli.getId()),peli.getId(),peli.getTitulo(),peli.getGenero(),peli.getProtagonista(),peli.getDirector(),peli.getYear(),peli.getPrecio(),1,1)

    def modificarPrecio(self,titulo,precio):
        for peli in self.stock:
            if titulo == peli.getTitulo():
                precio = '$'+str(precio)
                base.update(int(peli.getId()),peli.getId(),peli.getTitulo(),peli.getGenero(),peli.getProtagonista(),peli.getDirector(),peli.getYear(),precio,0,1)

    def devolverPelicula(self,titulo):
        for peli in self.stock:
            if titulo == peli.getTitulo():
                base.update(int(peli.getId()),peli.getId(),peli.getTitulo(),peli.getGenero(),peli.getProtagonista(),peli.getDirector(),peli.getYear(),peli.getPrecio(),0,1)

    def deletePelicula(self,titulo):
        for peli in self.stock:
            if titulo == peli.getTitulo():
                base.update(int(peli.getId()),peli.getId(),peli.getTitulo(),peli.getGenero(),peli.getProtagonista(),peli.getDirector(),peli.getYear(),peli.getPrecio(),0,0)

    def getStock(self):
        Stock.__init__(self)
        return self.stock


if __name__ == "__main__":
    n = Stock()

    generos = []
    for e in n.getStock():
        gen = e.getGenero()
        ind = gen.split('|')
        for g in ind:
            if g not in generos:
                generos.append(g)
    print(generos)
