from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_USER'] = 'sql6482269'
app.config['MYSQL_DATABASE_PASSWORD'] = 'kbTESaeeFb'
app.config['MYSQL_DATABASE_DB'] = 'sql6482269'
app.config['MYSQL_DATABASE_HOST'] = 'sql6.freemysqlhosting.net'

mysql.init_app(app)