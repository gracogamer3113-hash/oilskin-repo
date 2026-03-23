from src.database.db_mysql import mysql

class ModeloProducto:
    @classmethod
    def get_all(cls):
        cur=mysql.connection.cursor()
        cur.execute("SELECT nombre_producto, descripcion, precio, stock from producto ORDER BY nombre_producto ASC")
        return cur.fetchall()
    @classmethod
    def get_by_id(cls, id_producto):
        cur=mysql.connection.cursor()
        cur.execute("SELECT * FROM producto WHERE id_producto = %s", (id_producto,))
        return cur.fetchone()