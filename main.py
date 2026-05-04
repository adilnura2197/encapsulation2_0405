class Talaba:
    def __init__(self, fullname, ball):
        self.fullname = fullname
        self.__ball = ball

    def ball_qosh(self, qiymat):
        self.__ball += qiymat

    def info(self):
        print(f"Ism: {self.fullname}")
        print(f"Ball: {self.__ball}")


t1 = Talaba("Valiyev Ali", 85)
t1.info()

t1.ball_qosh(5)
t1.info()
