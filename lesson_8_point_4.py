class Machines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Model': self.name, 'Price for one': self.price, 'Count': self.quantity}

    def __str__(self):
        return f'{self.name} price {self.price} count {self.quantity}'

    def reception(self):

        try:
            unit = input(f'enter name ')
            unit_p = int(input(f'Price for one cnt '))
            unit_q = int(input(f'Enter quantity '))
            unique = {'<Model>': unit, 'Price for one': unit_p, 'count': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'current list -\n {self.my_store}')
        except:
            return f'Enter data error'

        print(f'For quit type - Q, continue - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'All data -\n {self.my_store_full}')
            return f'Quit'
        else:
            return Machines.reception(self)


class Printer(Machines):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Machines):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Machines):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('IBM', 1234, 5, 13)
unit_2 = Scanner('Apple', 3413, 4, 11)
unit_3 = Copier('Microsoft', 4334, 6, 12)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())

