# """
# 1. 콧물감기
# 2. 재채기
# 3. 코막힘

# 약을 먹어서 환자가 낫는 프로그램

# 종합감기약
# 1,2,3 -> 치유
# """

# class 콧물감기:
#     def 감기약(self):
#         print('콧물 감기가 낫습니다.')

# class 재채기:
#     def 감기약(self):
#         print('재채기가 낫습니다.')

# class 코막힘:
#     def 감기약(self):
#         print('코막힘이 낫습니다.')

# class 환자:
#     def 콧물감기(self, 감기약):
#         감기약.감기약()

#     def 재채기(self, 감기약):
#         감기약.감기약()
    
#     def 코막힘(self, 감기약):
#         감기약.감기약()

# patient = 환자()

# 콧물약 = 콧물감기()
# 재채기약 = 재채기()
# 코막힘약 = 코막힘()

# patient.콧물감기(콧물약)
# patient.재채기(재채기약)
# patient.코막힘(코막힘약)



# 캡슐화
class 콧물감기:
    def 감기약(self):
        print('콧물 감기가 낫습니다.')

class 재채기:
    def 감기약(self):
        print('재채기가 낫습니다.')

class 코막힘:
    def 감기약(self):
        print('코막힘이 낫습니다.')

class 종합감기약:
    def __init__(self):
        self.콧물약 = 콧물감기()
        self.재채기약 = 재채기()
        self.코막힘약 = 코막힘()

    def 감기약(self):
        self.콧물약.감기약()
        self.재채기약.감기약()
        self.코막힘약.감기약()

class 환자:
    def 감기약(self, 종합감기약):
        종합감기약.감기약()

patient = 환자()
pill = 종합감기약()

patient.감기약(pill)