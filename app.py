from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

#coneccion a datos
def get_db_connection():
    try:
        conn = sqlite3.connect('datosproductos.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None
    
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')  # antes: 'query'
    city = request.args.get('city')  # antes: 'ciudad'
    min_price = request.args.get('min_price')  # antes: 'min_precio'
    max_price = request.args.get('max_price')  # antes: 'max_precio'
    sort_by = request.args.get('sort_by')
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    # Construct query based on parameters
    sql = "SELECT * FROM productos WHERE 1=1 "
    count_sql = "SELECT COUNT(*) FROM productos WHERE 1=1 "
    params = []
    if query:
        sql += "AND nombre LIKE ? "
        count_sql += "AND nombre LIKE ? "
        params.append(f"%{query}%")
    if city:
        sql += "AND ciudad=? "
        count_sql += "AND ciudad=? "
        params.append(city)
    if min_price:
        sql += "AND precio >= ? "
        count_sql += "AND precio >= ? "
        params.append(min_price)
    if max_price:
        sql += "AND precio <= ? "
        count_sql += "AND precio <= ? "
        params.append(max_price)
    if sort_by == 'price':
        sql += "ORDER BY precio DESC"

    # Add pagination
    offset = (page - 1) * per_page
    sql += " LIMIT ? OFFSET ?"
    params_with_pagination = params + [per_page, offset]

    conn = get_db_connection()
    if conn is None:
        return "Error connecting to the database", 500
    cursor = conn.cursor()
    cursor.execute(sql, params_with_pagination)
    results = cursor.fetchall()

    # Get total count for pagination
    cursor.execute(count_sql, params)
    total = cursor.fetchone()[0]

    conn.close()

    # Convert results to list of dictionaries
    productos = [dict(row) for row in results]

    return jsonify({'productos': productos, 'total': total})

if __name__ == '__main__':
    app.run(debug=True)