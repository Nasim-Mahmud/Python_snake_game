class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breath(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breath(self):
        super().breath()
        print("Doing this underwater.")

    def swim(self):
        print("Swimming.....")


nemo = Fish()

nemo.swim()
nemo.breath()
print(nemo.num_of_eyes)
