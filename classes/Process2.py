class Process2:
    def __init__(self, name:str , required:int, deadline: int, finish: bool, task: int) -> None:
        self.name = name
        self.required = required
        self.deadline = deadline
        self.finish = finish
        self.task = task
        self.print = ''
        

    def __repr__(self) -> str:

        return 

    def check(self) -> None:
        self.finish = (self.required - self.task) == 0