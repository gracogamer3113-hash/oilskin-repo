from flask import Flask
from src.database.db_mysql import init_db
from src.routes import main_routes
from src.models.ModeloCategoria import ModeloCategoria
import os

def create_app():
    # Obtener la ruta base absoluta, evitamos problemas en el hosting con la integracion de tailwind, pronto refactor
    base_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(base_dir, 'src', 'templates')
    static_dir = os.path.join(base_dir, 'src', 'static')
    
    # Crear la app especificando template y static folders (se supone)
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir, static_url_path='/static')

    # Revisar modulo database para mas informacion
    init_db(app)

    # Blueprint para rutas 
    app.register_blueprint(main_routes.main, url_prefix='/')

    # No sirve xd arreglenlo
    @app.context_processor
    def inject_categories():
        categorias = ModeloCategoria.get_all_categories()
        return dict(categorias_menu=categorias)

    return app

# Pa que funcione bruh
if __name__ == '__main__':
     app = create_app()
     app.run(debug=True, port=5000)
 