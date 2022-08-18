class Parent:
    def __init__(self, attribute1="abc", attribute2=1):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def afunction(self):
        print(self.attribute1 + str(self.attribute2))


class Child(Parent):
    def __init__(self, attribute1="def", attribute2=3):
        super().__init__(attribute1, attribute2)


Child().afunction()
Child("test", 3).afunction()