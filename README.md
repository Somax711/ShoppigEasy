# ShoppigEasy
 ShoppingEasy es una aplicación web diseñada para facilitar la búsqueda de productos en una base de datos. Utilizando tecnologías modernas como Flask, Bootstrap y jQuery, la aplicación ofrece una interfaz de usuario intuitiva y responsiva. 

# ShoppingEasy

ShoppingEasy es una aplicación web que permite a los usuarios buscar productos en una base de datos. La aplicación proporciona una interfaz de usuario intuitiva para realizar búsquedas filtradas por nombre, ciudad, stock, precio mínimo y máximo, y ordenación por precio. Los resultados de la búsqueda se muestran en una tabla con paginación.

## Características

- **Búsqueda de productos**: Los usuarios pueden buscar productos por nombre, ciudad, stock, precio mínimo y máximo.
- **Ordenación**: Los resultados pueden ordenarse por precio (ascendente o descendente).
- **Paginación**: Los resultados se muestran con paginación, permitiendo a los usuarios navegar entre las páginas de resultados.
- **Interfaz de usuario responsiva**: La aplicación utiliza Bootstrap para asegurar que la interfaz se adapte a diferentes tamaños de pantalla.
- **Efecto Glass**: La interfaz incluye un contenedor con efecto glass para una apariencia moderna y atractiva.
- **Spinner de carga**: Se muestra un spinner mientras se cargan los datos de búsqueda.
- **Obtención de datos**: Los datos de los productos se obtuvieron mediante web scraping utilizando BeautifulSoup y Selenium con WebDriver.

## Tecnologías Utilizadas

- **Flask**: Framework web utilizado para construir la aplicación.
- **SQLite**: Base de datos utilizada para almacenar los productos.
- **Bootstrap**: Framework CSS utilizado para el diseño responsivo.
- **jQuery**: Biblioteca JavaScript utilizada para manejar las solicitudes AJAX y la manipulación del DOM.
- **Font Awesome**: Biblioteca de iconos utilizada para el ícono de búsqueda.
- **BeautifulSoup**: Biblioteca de Python utilizada para extraer datos de archivos HTML y XML.
- **Selenium**: Herramienta utilizada para automatizar navegadores web, utilizada junto con WebDriver para realizar web scraping.

## Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu-usuario/shoppingeasy.git
    cd shoppingeasy
    ```

2. Crea un entorno virtual e instala las dependencias:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Configura la base de datos:
    - Asegúrate de tener un archivo [datosproductos.db](http://_vscodecontentref_/0) en la raíz del proyecto con la tabla `productos` configurada.

4. Ejecuta la aplicación:
    ```bash
    flask run
    ```

5. Abre tu navegador y navega a `http://127.0.0.1:5000` para ver la aplicación.

## Estructura del Proyecto
