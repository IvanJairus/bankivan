from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_PORT'] = 3366
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'testdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)