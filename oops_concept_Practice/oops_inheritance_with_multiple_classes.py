class Employee:

    def __init__(self, emp_name, emp_id):
        self.emp_name = emp_name
        self.emp_id = emp_id

    def get_details(self):
        name = self.emp_name
        Id = self.emp_id
        print("Employee Name : ", name, ", ID : ", Id)


class Virtusa(Employee):

    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id)

    def companyType(self, type):
        print("Virtusa  is a ", type, " Company")


class DBS(Virtusa):

    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id)

    def companyType(self, type):
      print("DBS  is a ", type, " Company")


dbs = DBS("Kabira", 192)
dbs.companyType("Product Base")
dbs.get_details()
virtusa = Virtusa("Tom", 189)
virtusa.get_details()
virtusa.companyType("Service Base")
