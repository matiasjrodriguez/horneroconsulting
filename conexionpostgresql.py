import psycopg2

class ConexionPostgreSQL:
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conn = None

    def obtener_cursor(self):
        if self.conn is None:
            raise Exception('No hay conexión establecida. Primero debes llamar al método "conectar()".')
        else:
            return self.conn.cursor()
        
    def conectar(self):
        self.conn = psycopg2.connect(
            host = self.host,
            port = self.port,
            database = self.database,
            user = self.user,
            password = self.password
        )

    def desconectar(self):
        if self.conn is not None:
            self.conn.close()

    def obtener_cantidad_tablas(self):
        cur = self.obtener_cursor()

        cur.execute('SELECT count(*) FROM information_schema.tables WHERE table_schema=\'public\'')
        cantidad_tablas = cur.fetchone()[0]
        cur.close()

        return cantidad_tablas
    
    def crear_tabla(self):
        cur = self.obtener_cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS contacto (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(50),
                mail VARCHAR(100),
                whatsapp VARCHAR(20),
                mensaje TEXT
            )
        """)

        self.conn.commit()
        cur.close()

        print("La tabla ha sido creada con éxito")

    def insertar_datos(self, nombre, mail, whatsapp, mensaje):
        cur = self.obtener_cursor()
        cur.execute("""
            INSERT INTO contacto (nombre, mail, whatsapp, mensaje)
            VALUES (%s, %s, %s, %s)
        """, (nombre, mail, whatsapp, mensaje))

        self.conn.commit()
        cur.close()

        print("Datos insertados con éxito")