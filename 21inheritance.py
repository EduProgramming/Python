class Parent:
    def __init__(self):
        print('부모 클래스')

    def inheritance_test(self):
        print('물려줄 메서드')


class Child(Parent):
    def __init__(self):
        print('자식 클래스')

    def inheritance_test(self):
        print('물려받은 메서드')

    def child_method(self):
        print('자식의 요소')

child = Child()
child.inheritance_test()
