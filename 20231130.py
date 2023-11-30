class Student:
    def __init__(self, SchoolName, DepartmentName, DepartmentChairName, StudentName, StudentID,Address,Score,GPA):
        self.SchoolName = SchoolName
        self.DepartmentName = DepartmentName
        self.DepartmentChairName = DepartmentChairName
        self.StudentName = StudentName
        self.StudentID = StudentID
        self.Address = Address
        self.Score = Score
        self.GPA = GPA

    def GetSchoolName(self):
        return self.SchoolName
        
    def SetSchoolName(self, Val):
        self.SchoolName = Val

    def GetDepartmentName(self):
        return self.DepartmentName
        
    def SetDepartmentName(self, Val):
        self.DepartmentName = Val

    def GetDepartmentChairName(self):
        return self.DepartmentChairName
        
    def SetDepartmentChairName(self, Val):
        self.DepartmentChairName = Val

    def GetStudentName(self):
        return self.StudentName
        
    def SetStudentName(self, Val):
        self.StudentName = Val

    def GetStudentID(self):
        return self.StudentID
        
    def SetStudentID(self, Val):
        self.StudentID = Val

    def GetAddress(self):
        return self.Address
        
    def SetAddress(self, Val):
        self.Address = Val

    def GetScore(self):
        return self.Score
        
    def SetScore(self, Val):
        self.Score = Val

    def GetGPA(self):
        return self.GPA
        
    def SetGPA(self, Val):
        self.GPA = Val
        

g_Student = Student("Stust", "IF", "LE", "Tim" , "4B0G0037" , "123" , 100 , 40)


print(g_Student.GetSchoolName())
print(g_Student.GetDepartmentName())
print(g_Student.GetDepartmentChairName())
print(g_Student.GetStudentName())
print(g_Student.GetStudentID())
print(g_Student.GetAddress())
print(g_Student.GetScore())
g_Student.SetScore(Val = 150)
print(g_Student.GetScore())
print(g_Student.GetGPA()) 