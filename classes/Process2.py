class Process2:
    def __init__(self, name:str , required:int, deadline: int) -> None:
        self.name = name
        self.required = required
        self.deadline = deadline
        self.start = False
        self.available = True
        self.check = 0
        self.cicle = 1
        self.print = 0
        

    def __repr__(self) -> str:
        return f""" {self.name} {self.print}"""

