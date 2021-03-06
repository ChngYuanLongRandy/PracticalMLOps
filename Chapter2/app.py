from distutils.log import debug

from flask import Flask
from flask_restful import Api
from .resources.employees import (
    ActivityEmployeeResource,
    EmployeeResource,
    EmployeesResource,
    HealthResource,
)

def create_app():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(EmployeesResource, "/")
    api.add_resource(EmployeeResource, "/<int:input_employee_id>")
    api.add_resource(ActivityEmployeeResource, "/<int:input_employee_id>/active")
    api.add_resource(HealthResource, "/health")

    return app

if __name__ == "main":
    app = create_app()
    app.run(port=5000, debug=True)
