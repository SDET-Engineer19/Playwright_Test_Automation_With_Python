def get_user_details(user_name, emp_id):
    print("Employee Name : ", user_name, " and Employee ID : ", emp_id)


get_user_details("Kabira",89)  # Positional Arguments
get_user_details(emp_id=98,user_name="Tom")  # Positional Arguments by changing the variables position

get_user_details(user_name=None,emp_id=None)  # Positional Arguments by passing empty values as None
