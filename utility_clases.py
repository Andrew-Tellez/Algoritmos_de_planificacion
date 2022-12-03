class Proceso:
  def __init__(self, name:str , requerido:int, asignado:int, llegada:int) -> None:
    self.name = name
    self.requerido = requerido
    self.asignado = asignado
    self.tiempos = 0
    self.aux_requerido = requerido
    self.llegada = llegada

  def __repr__(self) -> str:
    return f"""
    [  
      name:{self.name} 
      requerido:{self.requerido} 
      asignado:{self.asignado} 
      ciclos:{self.ciclos} 
      llegada:{self.llegada}
    ] """
