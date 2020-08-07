class Alphabet:
    def __init__(self):
        self._value = 123

    @property
    def value1(self):
        print("getting value", self._value)
        return self._value

    @value1.setter
    def value1(self,value):
        print('Setting value to')
        self._value = value

    # deleting the values
    @value1.deleter
    def value1(self):
        print('Deleting value')
        del self._value

X = Alphabet()
X.value = 222
print(X.value)

#
# class Alphabet:
#     def __init__(self, value):
#         self._value = value
#
#         # getting the values
#
#     @property
#     def value(self):
#         print('Getting value')
#         return self._value
#
#         # setting the values
#
#     @value.setter
#     def value(self, value):
#         print('Setting value to ' + value)
#         self._value = value
#
#         # deleting the values
#
#     @value.deleter
#     def value(self):
#         print('Deleting value')
#         del self._value
#
#     # passing the value
#
#
# x = Alphabet('Peter')
# print(x.value)
#
# x.value = 'Diesel'
#
# del x.value