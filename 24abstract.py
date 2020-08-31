from abc import *

# class AbstractClass(metaclass=ABCMeta):
#     @abstractmethod
#     def test_method(self):
#         print('test')

# test = AbstractClass()


class Coffee(metaclass=ABCMeta):
    @abstractmethod
    def put(self):
        pass

    @abstractmethod
    def grinder(self):
        pass

    @abstractmethod
    def drip(self):
        pass

    @abstractmethod
    def make(self):
        self.put()
        self.grinder()
        self.drip()

class KenyaCoffee(Coffee):
    def __init__(self):
        self.__coffee = '케냐'

    def put(self):
        print(f'{self.__coffee} 원두를 담습니다.')

    def grinder(self):
        print(f'{self.__coffee} 원두를 갈아줍니다.')
        
    def drip(self):
        print(f'{self.__coffee} 원두를 추출합니다.')

    def make(self):
        super().make()
    
kenya = KenyaCoffee()
kenya.make()

class ColombianCoffee(Coffee):
    def __init__(self):
        self.__coffee = '콜롬비아'

    def put(self):
        print(f'{self.__coffee} 원두를 담습니다.')

    def grinder(self):
        print(f'{self.__coffee} 원두를 갈아줍니다.')
        
    def drip(self):
        print(f'{self.__coffee} 원두를 추출합니다.')

    def make(self):
        super().make()

colombian = ColombianCoffee()
colombian.make()