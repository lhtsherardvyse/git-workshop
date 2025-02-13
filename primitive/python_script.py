def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__=="__main__":
    user_name= input("What is your name?")
    print(greet(user_name))
