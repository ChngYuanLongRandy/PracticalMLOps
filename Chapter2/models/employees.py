employee_pool = [
#     {
#     'id':1,
#     'name':'Randy',
#     'rank':'Boss',
#     'pay':'Millions of Dollars',
#     'is_active':True
# },
# {
#     'id':2,
#     'name':'Wan Mun',
#     'rank':'Miss Boss',
#     'pay':'Millions as well',
#     'is_active':False
# }
]

def get_id():
    """
    returns the latest id for the employee
    """
    id = len(employee_pool)

    if id is None:
        return 1
    return id+1

class Employee():
    def __init__(self, name, rank, pay):
        self.id = get_id()
        self.name = name
        self.rank = rank
        self.pay = pay
        self.is_active = True

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'rank': self.rank,
            'pay': self.pay,
            'is_active':self.is_active
        }