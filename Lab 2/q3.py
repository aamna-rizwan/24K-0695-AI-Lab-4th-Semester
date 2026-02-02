class Result:
    def __init__(self,marks):
        self.__marks=marks
    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def calculate_grade(self):
        mark=self.__marks
        if(mark>=80 and mark<=100):
            print("Grade : A")
        elif(mark>=60 and mark<=79):
            print("Grade : B")
        elif(mark>=50 and mark<=59):
            print("Grade : C")
        elif(mark<50):
            print("Grade : Fail")

s1=Result(76)
print("Student 1")
print("Marks : ", s1.get_marks())
s1.calculate_grade()
s2=Result(45)
print("\nStudent 2")
print("Marks : ", s2.get_marks())
s2.calculate_grade()
s2.set_marks(51)
print("Updated Marks : ",s2.get_marks())
s2.calculate_grade()
