class Process:
  def __init__(self, name:str , required:int, arrival:int) -> None:
    self.name = name
    self.required = required
    self.arrival = arrival

  def __repr__(self) -> str:
    return f"""{self.name} required:{self.required} start:{self.arrival}"""
