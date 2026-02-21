import art
print(art.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
parameters={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    f=True
    a=float(input("Enter your first number: "))
    while f:
        b=input("+\n"
            "-\n"
            "*\n"
            "/\n"
            "Pick an operator"
            )
        c=float(input("Enter your next number: "))
        answer=parameters[b](a,c)
        print(f"{a} {b} {c} ={answer}")
        e=input("Do you want to continue to calculate?(y/n)")
        if e=="y":
            a=answer
        else:
            f=False
            print("\n"*20)
            calculator()
calculator()
