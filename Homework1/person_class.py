class Person:
    def __init__ (self, last, first, mi, id, phone):
        self.last = last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone

    def display (self):
        print('Employee id: ', self.id)
        print('\t', self.first, self.mi, self.last)
        print('\t', self.phone)
        print()
