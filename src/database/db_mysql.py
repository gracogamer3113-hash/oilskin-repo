from decouple import config
from flask_mysqldb import MySQL

mysql = MySQL()

# Inicializamos la base de datos
def init_db(app):
    try:
        # No lo modifiquen, contiene las credenciales
        app.config['MYSQL_HOST'] = config('MYSQL_HOST', default='localhost')
        app.config['MYSQL_USER'] = config('MYSQL_USER')
        app.config['MYSQL_PASSWORD'] = config('MYSQL_PASSWORD')
        app.config['MYSQL_DB'] = config('MYSQL_DB')
        # Nos protege de los hackers
        app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
        # Iniciamos la base de datos
        mysql.init_app(app)
        # Debug simplecito
        print("Conexion a MySQL realizada exitosamente.")
    # Si no funciona
    except Exception as error:
        print(f"Error al cargar la configuracion de MySQL: {error}")
# Pues hace lo que hace
def get_connection():
    return mysql.connection.cursor()