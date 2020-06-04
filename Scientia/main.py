from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = '3306'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'vijay4004'
app.config['MYSQL_DB'] = 'employees'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
  return render_template('home.html')


if __name__ == '__main__':
    app.run()