"""
Coffee
1. 원두를 담는 작업
2. 원두 가는 작업
3. 커피 추출 작업

원두Coffee Bean ->

1. Kenya
2. Colombian
3. Ethiopia
"""

class Coffee:
    def __init__(self, bean):
        self.bean = bean

    def __put(self):
        print(f'{self.bean} 원두를 담습니다.')

    def __grinder(self):
        print(f'{self.bean} 원두를 갈아줍니다.')

    def __drip(self):
        print(f'{self.bean} 원두 추출합니다.')

    def make(self):
        self.__put()
        self.__grinder()
        self.__drip()

class Kenya(Coffee):
    def __init__(self, bean):
        # super().__init__(bean)
        self.bean = bean

class Colombian(Coffee):
    def __init__(self, bean):
        self.bean = bean

class Ethiopia(Coffee):
    def __init__(self, bean):
        self.bean = bean

kenya = Kenya('kenya')    
kenya.make()

colombian = Colombian('Colombian')
colombian.make()

ethiopia = Ethiopia('Ethiopia')
ethiopia.make()