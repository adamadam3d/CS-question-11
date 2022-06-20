class student:
    all = []

    def _init_(self, age: int, house: str, rt: float):
        # validation
        # assert 12 < age < 16
        # assert house == "saturn" or house == "mars"
        # assigning
        self.age = age
        self.house = house
        self.rt = rt
        # list
        student.all.append(self)


def average(age1: int, house1: str):
    try:
        total = sum(i.rt for i in student.all if i.age == age1 and i.house == str(house1))
        counter = sum(i.age == int(age1) and i.house == str(house1) for i in student.all)
        return total / counter
    except ZeroDivisionError:
        return "no student fits the criteria"


def lowest(age, house):
    try:
        return min(i.rt for i in student.all if i.age == age and i.house == str(house))
    except:
        return "no student fits the criteria"


for x in range(3):
    a = int(input("age"))
    b = str(input("house"))
    c = float(input("reaction time"))

    studentx = student(a, b, c)

# house average
for x in ["mars", "saturn"]:
    try:
        total = sum(i.rt for i in student.all if i.house == x)
        count = sum(i.house == x for i in student.all)
        print(x, total / count)
    except ZeroDivisionError:
        print("no student in the %s house" % x)
