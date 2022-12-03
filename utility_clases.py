class Proceso:
  def __init__(self, name:str , requerido:int, llegada:int) -> None:
    self.name = name
    self.llegada = llegada
    self.requerido = requerido

  def __repr__(self) -> str:
    return f"""{self.name} {self.requerido}"""
