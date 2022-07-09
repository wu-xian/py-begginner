class Human:
    def speak(self):
        print("Human")
    def hi(self):
        print("Human:hi")

class Man(Human):
    def speak(self):
        print("Man")

class Child(Man):
    def speak(self):
        print("Child")

c = Child()
c.speak()
super(Man,c).speak()