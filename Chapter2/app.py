from distutils.log import debug
from flask import Flask
from flask_restful import Api
from resources.employees import EmployeeResource, EmployeesResource, ActivityEmployeeResource

app = Flask(__name__)
api = Api(app)

api.add_resource(EmployeesResource,'/')
api.add_resource(EmployeeResource,'/<int:employee_id'>)
api.add_resource(ActivityEmployeeResource,'/<int:employee_id>/active')

if __name__ == 'main':
    app.run(port=5000, debug= True)
