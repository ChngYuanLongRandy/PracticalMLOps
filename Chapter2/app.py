from distutils.log import debug

from flask import Flask
from flask_restful import Api
from resources.employees import (
    ActivityEmployeeResource,
    EmployeeResource,
    EmployeesResource,
    HealthResource,
)

app = Flask(__name__)
api = Api(app)

api.add_resource(EmployeesResource, "/")
api.add_resource(EmployeeResource, "/<int:input_employee_id>")
api.add_resource(ActivityEmployeeResource, "/<int:input_employee_id>/active")
api.add_resource(HealthResource, "/health")

if __name__ == "main":
    app.run(port=5000, debug=True)
