# Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects.

class Example:
    def __init__(harry, value):
        harry.data = value

    def display(harry):
        print(f"The value is: {harry.data}")

obj = Example(42)
obj.display()


class Example:
    def __init__(harry, value):
        harry.data = value

    def display(harry):
        print(f"The value is: {harry.data}")

obj = Example(42)
obj.display()
