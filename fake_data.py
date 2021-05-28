from random import *
alphabets='abcdefghijklmnopqrstuvwxyz'
digits='0123456789'
cities=['Hyderabad', 'Chennai', 'Bangalore', 'Pune' , 'Delhi', 'Mumbai']
designations=['Software Engineer', 'Senior Software Engineer', 'Team Lead', 'Project Lead' , 'Project Manager']

def fake_emp_name():
    name=choice(alphabets).upper()
    n=randint(2,9)
    for i in range(n):
        name=name+choice(alphabets)
        return name
def fake_emp_num():
    eno='e-'
    for i in range(4):
        eno=eno+choice(digits)
    return eno
def fake_emp_sal():
    salary=uniform(10000,50000)
    return salary
def fake_emp_city():
    city=choice(cities)
    return city
def fake_emp_mno():
    mno=choice('6789')
    for i in range(9):
        mno=mno+choice(digits)
    return mno
def fake_emp_desig():
    designation=choice(designations)
def fake_data():
    print('Emp name:',fake_emp_name())
    print('Emp number:',fake_emp_num())
    print('Emp salary is {:0.2f}'.format(fake_emp_sal()))
    print('Emp city:',fake_emp_city())
    print('Emp mobile :',fake_emp_mno())
    print('Emp designation:',fake_emp_desig())
for i in range(10):
    fake_data()
    print()
