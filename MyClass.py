from Field import String as FieldString


class String(FieldString):
    def __init__(self, str_with_blankspace):
        super().__init__(str_with_blankspace)

    def modify_string(self):
        return self.str_with_blankspace.strip()


string = FieldString.modify_string('    1    ')
print(string)
