#!/usr/bin/python3

class Intern:
    def __init__(self, Name = "My name? I'm nobody, an intern, I have no name."):
        self.Name = Name

    def __str__(self):
        return self.Name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")
    
    def make_coffee(self):
        return self.Coffee()
    
def create_intern():
    intern = Intern()
    mark = Intern("Mark")

    print("Name of the first intern:", intern)
    print("Name of the second intern:", mark)
    print(f"{mark}: {mark.make_coffee()}")

    try:
        intern.work()
    except Exception as e:
        print(f"{intern}: {e}")

if __name__ == '__main__':
    create_intern()