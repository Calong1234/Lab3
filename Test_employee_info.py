import employee_info as employee

print("Test_employee_info")

def test_get_employees_by_age_range():
    age_lower_limit = 25
    age_upper_limit = 40
    result = employee.get_employees_by_age_range(age_lower_limit, age_upper_limit)
    test = [{"name": "John", "age": 30, "department": "Sales", "salary": 50000}, {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000}, {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]
    assert (result == test)

def test_calculate_average_salary():
    result = employee.calculate_average_salary()
    
    assert (result == 60166)

def test_get_employees_by_dept():
    department = 'Engineering'
    result = employee.get_employees_by_dept(department)
    test = [{"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000}, {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000}]

    assert (result == test)