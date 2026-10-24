class Parent:
    def __init__(self, Eye_Colour, Height):
        self.Eye_Colour = Eye_Colour
        self.Height = Height

    def display(self):
        print("Eye Colour:", self.Eye_Colour)
        print("Height:", self.Height)

class Child(Parent):
    def __init__(self, Age, Name, Eye_Colour, Height):
        super().__init__(Eye_Colour, Height)
        self.Age = Age
        self.Name = Name

    def display(self):
        super().display()
        print("Age:", self.Age)
        print("Name:", self.Name)

    def favourite_hobby(self, hobby):
        print(f"{self.Name}'s favourite hobby is {hobby}.")

child=Child(13, "Vedant", "Blue", "5'6\"")

child.display()
child.favourite_hobby("Playing Football")

print("Is Child an instance of Parent?", isinstance(child, Parent))
print("Is Child a subclass of Parent?", issubclass(Child, Parent))