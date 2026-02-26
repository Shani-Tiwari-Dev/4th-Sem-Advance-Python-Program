class employee:

    def display(self):
        self.name = "Haiku",
        self.id = 1


class Manager(employee):

    def display(self):
        self.name = "Deku"
        print(self.name)


emp = Manager()

emp.display()
