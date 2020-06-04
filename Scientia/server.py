from flask import Flask, render_template, request, jsonify
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

app = Flask(__name__)
api = Api(app)


# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_DATABASE_PORT'] = '3306'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'vijay4004'
# app.config['MYSQL_DB'] = 'employees'

# mysql = MySQL(app)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['name']
        designation = details['designation']
        address = details['address']
        phone = details['phone']
        print(name)
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO empdetails(name, designation, address, phone) VALUES (%s, %s, %s, %s)", (name, designation, address, phone))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('home.html')

class Employee(Resource):
    def get(self):
        return {"employees":[1,2,3,4]}

    def post(self):
        details = json.loads(request.form.get('payload'))
        name = details['name']
        designation = details['designation']
        address = details['address']
        phone = details['phone']
        print(details)

api.add_resource(Employee, '/')

if __name__ == '__main__':
    app.run(port='5002')