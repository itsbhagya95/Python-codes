class Student:
    school_name='SMC'
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def getStudentInfo(self):
        print('Student name:',self.name)
        print('Student rollno:',self.rollno)
    @classmethod ##decorator
    def getSchoolInfo(cls):
        print('School name:',cls.school_name)
    @staticmethod
    def getSum(a,b):
        return a+b
