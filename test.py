class basel:
    def __init__(self, name):
        self.name = name

    def bas(self):
        new_string = ""
        for i in self.name:
            if 97 <= ord(i) <= 122:
                c=chr(ord(i) - 32)
                new_string +=c
            else:
                new_string += i
        return new_string


n = basel("Martinooo")
print(n.bas())
