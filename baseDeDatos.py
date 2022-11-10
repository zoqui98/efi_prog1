import os
import sqlite3
from pprint import pprint


class Database:
    def __init__(self, base, *args) -> None:
        """ 
            Parámetros: Nombre de la base de datos y de los atributos 
            Ejemplo: base = Database("Persona", "nombre", "edad")
        """
        self.base = base
        self.fields = args
        conn = self.connection()
        self.sArgs = ",".join(args)
        fieldNames = f"('id' integer primary key autoincrement, {self.sArgs})"
        try:
            conn.execute(f"create table {base} {fieldNames}")
            print(f"\n{base} creada")
        except sqlite3.OperationalError:
            pass
            # print(f"\n{base} OK")
        conn.close()

    def connection(self):
        return sqlite3.connect(f"{self.base}.db")

    def insert(self, *args):
        conn = self.connection()
        sql = f"INSERT INTO {self.base}({self.sArgs}) VALUES {args}"
        conn.execute(sql)
        print(f"\n{args} fila agregada")
        conn.commit()
        conn.close()

    def select(self) -> list:
        conn = self.connection()
        sql = f"SELECT * FROM {self.base}"
        recordSet = list(conn.execute(sql))
        # print(sql)
        # print(f"\nObtengo todas las filas de {self.base}\n")
        conn.close()
        return recordSet

    def delete(self, id):
        conn = self.connection()
        sql = f"DELETE FROM {self.base} WHERE id={id}"
        conn.execute(sql)
        print(f"\nFila #{id} borrada")
        conn.commit()
        conn.close()

    def update(self, *args):
        conn = self.connection()
        updating = f""
        for f in self.fields:
            updating += f"{f} = ?,"
        updating = updating[:-1]
        id = args[0]
        sql = f"Update {self.base} set {updating} where id = {id}"
        columnValues = args[1:]
        conn.execute(sql, columnValues)
        print(f"\n{args} Fila #{id} actualizada")
        conn.commit()
        conn.close()


if __name__ == '__main__':

    base = Database('stockDePelis', 'id', 'title', 'genre', 'principalActor','director', 'year', 'price','status','activo')
 
    data = base.select()
    print(len(data))
    for i in range(len(data)):
        id = data[i][0]
        title = data[i][1]
        genre = data[i][2]
        principalActor = data[i][3]
        director=data[i][4]
        year= data[i][5]
        price= data[i][6]
        
        base.update(i+1,id,title,genre,principalActor,director,year,price,0,1)