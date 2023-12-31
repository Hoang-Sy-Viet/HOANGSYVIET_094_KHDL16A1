            
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def display(self):
        print(f"ngày {self.day} tháng {self.month} năm {self.year}")

    def next(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.month == 2 and ((self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)):
            days_in_month[1] = 29
        if self.day < days_in_month[self.month - 1]:    #ngày không phải cuối tháng sẽ +1 ngày
            self.day += 1
        else:          # những ngày cuối tháng
            self.day = 1
            if self.month == 12:    
                self.month = 1
                self.year += 1
            else:
                self.month += 1
        print("_________ngày tiếp theo__________:",end="\n")
        self.display()
#--------------------------------------
d = Date(28,2,2005)
d.display() 
d.next()


        