class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

class TamGiacVuong(TamGiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def kiem_tra_tam_giac_vuong(self):
        if self.a ** 2 + self.b ** 2 == self.c ** 2 or self.a ** 2 + self.c ** 2 == self.b ** 2 or self.b ** 2 + self.c ** 2 == self.a ** 2:
            return True
        else:
            return False

class TamGiacCan(TamGiac):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    def kiem_tra_tam_giac_can(self):
        if self.a == self.b or self.a == self.c or self.b == self.c:
            return True
        else:
            return False

class TamGiacDeu(TamGiacCan):
    def __init__(self, a, b, c):
        super().__init__(a, b, c)
    def kiem_tra_tam_giac_deu(self):
        if self.a == self.b and self.a == self.c:
            return True
        else:
            return False