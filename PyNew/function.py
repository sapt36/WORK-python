name0 = "Bro"
def hello():
    print("Hello " + name0)
    print("Hava a nice day!")
hello()

def hello(name):
    print("Hello " + name + "!")
hello("Andy")

def hello(first_name,last_name,age):
    print("Hello! " + first_name + last_name)
    #wrong!!! print("You are "+age+" years old!")
    print("You are " + str(age) + " years old!")
hello("Bro"," code",21)