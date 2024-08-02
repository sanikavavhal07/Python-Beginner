def greet():
    print("Hello Sanika")
    print("Have a good day Sanika")
greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Have a good day {name}")
greet_with_name("Saksham")

def greet_with_names(name1,location):
    print(f"Hello, my name is {name1}")
    print(f"I am from {location}")
greet_with_names("Nilesh","Pune")

def greet_with_keyword_arg(name2 = "Shreyas",location2 = "Wagholi"):
    print(f"Hello, my name is {name2}")
    print(f"I am from {location2}")
greet_with_keyword_arg()
