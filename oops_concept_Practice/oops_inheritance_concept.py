class User:

    def login(self):
        print("Login")

    def register(self):
        print("Register")


class Student(User):

    def enroll(self):
        print("Enroll")

    def review(self):
        print("Review")


std1 = Student()
std1.register()
std1.login()
std1.enroll()
std1.review()
