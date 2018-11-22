class Student(object):

    def __init__(self, name, score):
        self.__name = name     # 私有变量(private)，只能内部访问，外部不能访问
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def __send_message(self):   # 私有方法，只能类内部调用，这样可以保护核心代码
        print("--------1--------")

    def test2(self, new_money):
        if new_money > 100:
            self.__send_message()
        else:
            print("You cannot send message")


## 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
## 以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，
    # 意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。