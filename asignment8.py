class A:
    def __init__(self, a, b, c):
        self.__a = b  # Private
        self._b = b   # Protected
        self.c = c    # Public

    def display(self):
        print("Values in Class A:")
        try:
            print("Private member a:", self.__a)
        except AttributeError:
            print("Error: Private member 'a' cannot be accessed.")

        print("Protected member b:", self._b)
        print("Public member c:", self.c)


class B(A):
    def display(self):
        print("Values in Class B:")
        print("Protected member b (inherited from Class A):", self._b)
        print("Public member c (inherited from Class A):", self.c)

obj = B(5, 10, 15)
obj.display()