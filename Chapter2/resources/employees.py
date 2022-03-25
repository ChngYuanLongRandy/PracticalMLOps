from http import HTTPStatus
from flask import request
from flask_restful import Resource
from models.employees import employee_pool , Employee

class EmployeesResource(Resource):
    def get(self):
        employee_pool_display = []
        for emp in employee_pool:
            if emp.active == True:
                employee_pool_display.append(emp)

        return employee_pool_display, HTTPStatus.OK
    def post(self):
        data = request.get_json()
        employee = Employee(
            name = data['data'],
            rank = data['rank'],
            pay=data['pay']
        )
        employee_pool.append(employee)

        return employee.data, HTTPStatus.CREATED

class EmployeeResource(Resource):
    def get(self,input_employee_id):
        employee = next((employee for employee in employee_pool if employee.id == input_employee_id), None)

        if not employee:
            return {'message':'employee not found'}, HTTPStatus.NOT_FOUND
        return employee.data , HTTPStatus.OK
    def put(self,input_employee_id):
        employee = next((employee for employee in employee_pool if employee.id == input_employee_id), None)

        if not employee:
            return {'message':'employee not found'}, HTTPStatus.NOT_FOUND
        
        employee.name = data['name']
        employee.rank = data['rank']
        employee.pay = data['pay']

        return employee.data , HTTPStatus.OK
    
class ActivityEmployeeResource(Resource):

    def put(self,input_employee_id):
        employee = next((employee for employee in employee_pool if employee.id == input_employee_id), None)

        if not employee:
            return {'message':'employee not found'}, HTTPStatus.NOT_FOUND
        
        employee.active = True

        return {} , HTTPStatus.OK

    def delete(self,input_employee_id):
        employee = next((employee for employee in employee_pool if employee.id == input_employee_id), None)

        if not employee:
            return {'message':'employee not found'}, HTTPStatus.NOT_FOUND
        
        employee.active = False

        return {} , HTTPStatus.OK