import sqlite3

# 1. Conexión a la base local
conexion = sqlite3.connect("mi_prueba.db")
cursor = conexion.cursor()

# 2. Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    rol TEXT NOT NULL,
    email TEXT
)
""")

# 3. Si la tabla ya existía de antes sin email, le añadimos la columna
try:
    cursor.execute("ALTER TABLE usuarios ADD COLUMN email TEXT")
except sqlite3.OperationalError:
    pass  # Ya existe la columna

# 4. Actualizar correos para las filas existentes
cursor.execute("UPDATE usuarios SET email = 'fer.admin@test.com' WHERE id = 1")
cursor.execute("UPDATE usuarios SET email = 'fer.dev@test.com' WHERE id = 2")
conexion.commit()

# 5. Consultar y listar con la nueva columna
cursor.execute("SELECT id, nombre, rol, email FROM usuarios")
usuarios = cursor.fetchall()

print("\n--- REGISTROS CON EMAIL EN MI_PRUEBA.DB ---")
for usuario in usuarios:
    print(f"ID: {usuario[0]} | Nombre: {usuario[1]} | Rol: {usuario[2]} | Email: {usuario[3]}")
print("-------------------------------------------\n")

conexion.close()
