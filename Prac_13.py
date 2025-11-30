# j = [3,3,4,5,2,1111,5]
# print(1111 in j)  

class Std:
    def __init__(self,name,grd, percent):
        self.name = name
        self.grd = grd
        self.percent = percent

    def std_details(self):
        print(f"{self.name} is in class {self.grd}, with{self.percent}%")

std1 = Std("Vinayak", 11, 78)
std2 = Std('Jaya', 12,87)