from flask import Blueprint, render_template
from src.models.ModeloProductos import ModeloProducto
from src.models.ModeloCategoria import ModeloCategoria

main = Blueprint('product_blueprint', __name__)

@main.route('/')
def index():
    try:
        return render_template('index.jinja')
    except Exception as Error:
        return render_template('error_page', mensaje=f"Pagina No Encontrada, {Error}")
@main.route('/sobre_nosotros')
def about():
    try:
        return render_template('sobre_nosotros.jinja')
    except Exception as Error:
        return render_template('error_page', mensaje=f"Pagina No Encontrada, {Error}")

@main.route('/producto/<int:id>')
def get_product(id):
    producto = ModeloProducto.get_by_id(id)
    if producto:
        return render_template('detalle.jinja', producto=producto)
    return render_template('error_page', mensaje=f"Producto no Encontrado")

@main.route('/categoria/<int:category_id>')
def show_category(category_id):
    try:
        productos = ModeloProducto.get_by_category_id(category_id)
        print(f"DEBUG: Productos obtenidos: {productos}")
        print(f"DEBUG: Cantidad: {len(productos) if productos else 0}")
        
        descripcion = ModeloCategoria.get_description_by_id(category_id)
        category_name = ModeloCategoria.get_name_by_id(category_id)
        
        print(f"DEBUG: Categoría: {category_name}, Descripción: {descripcion}")
        
        if not productos:
            print(f"❌ No hay productos para id_categoria={category_id}")
            return render_template('error_page.jinja', mensaje=f"No hay productos disponibles en esta categoría")
        
        return render_template('category.jinja', productos=productos, descripcion=descripcion, category_name=category_name)
    except Exception as ex:
        print(f"❌ Error en show_category: {ex}")
        return render_template('error_page.jinja', mensaje=f"Error: {ex}")    