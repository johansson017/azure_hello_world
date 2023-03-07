""" This is a small script """

def main():
    print("Hello, World!")

class Printables:
    def __init__(self, default="Hello, World!"):
        self.default = default
    
    def personalize(self, person):
        self.default = f"Hello, {person}!"

    def __str__(self):
        return self.default

if __name__=="__main__":
    main()



