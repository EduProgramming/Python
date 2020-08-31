class 카트:
    def __init__(self):
        """
        스피드: 카트의 속도
        마찰력: 카트가 커브를 돌 때, 발생하는 속도 저항력
        부스터: 카트의 속도Up/Down
        """
        self.스피드 = 0
        self.마찰력 = 0
        self.부스터 = 0

    def speed_up(self):
        self.스피드 += self.부스터
        return self.스피드

    def speed_down(self):
        self.스피드 -= self.부스터
        return self.스피드

    def curve(self):
        self.스피드 -= self.부스터
        return self.스피드

class 연습용카트(카트):
    def __init__(self):
        self.스피드 = 50
        self.마찰력 = 20
        self.부스터 = 5

class 히페리온(카트):
    def __init__(self):
        self.스피드 = 100
        self.마찰력 = 10
        self.부스터 = 20

class 트랜스포머(카트):
    def __init__(self):
        self.스피드 = 80
        self.마찰력 = 5
        self.부스터 = 50

pratice_cart = 연습용카트()
print(pratice_cart.speed_up())
print(pratice_cart.speed_up())
print(pratice_cart.speed_down())
print(pratice_cart.curve())
print(pratice_cart.speed_down())

hyperion_cart = 히페리온()
print(hyperion_cart.speed_up())
print(hyperion_cart.speed_up())
print(hyperion_cart.speed_down())
print(hyperion_cart.curve())
print(hyperion_cart.speed_down())

tran_cart = 트랜스포머()
print(tran_cart.speed_up())
print(tran_cart.speed_up())
print(tran_cart.speed_down())
print(tran_cart.curve())
print(tran_cart.speed_down())
