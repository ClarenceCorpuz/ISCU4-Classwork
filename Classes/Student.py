class Student:
    def __init__(self, name: str, email: str, grade: int):
        self.name = name
        self.email = email
        self.grade = grade

    def get_name(self):
        return self.name

    def set_name(self, new_name: str): 
        new_name = self.name
    
    def get_email(self):
        return self.email
    
    def set_email(self, new_email: str):
        new_email = self.email

    def get_grade(self):
        return self.grade

    def set_grade(self, new_grade: int):
        new_grade = self.grade
