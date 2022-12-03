class Proceso:
  def __init__(self, name:str , requerido:int, llegada:int, prioridad=0) -> None:
    self.name = name
    self.llegada = llegada
    self.requerido = requerido
    self.prioridad = prioridad

  def __repr__(self) -> str:
    return f"""{self.name} {self.requerido}"""
