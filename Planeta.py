class Planeta:

  def __init__(
      self,
      nombre: str,
      masa: float,
      radio: float,
      distancia_al_sol: float,
      tiene_vida: bool = False,
  ):
    self.nombre = nombre
    self.masa = masa
    self.radio = radio
    self.distancia_al_sol = distancia_al_sol
    self.tiene_vida = tiene_vida

  def calcular_densidad(self) -> float:
    pi = 3.141592653589793
    return self.masa /((4 / 3) * pi * (self.radio**3))

  def es_planeta_exterior(self) -> bool:
    return self.distancia_al_sol > 5.2

  def __str__(self) -> str:
    densidad = self.calcular_densidad()
    tipo = "Exterior" if self.es_planeta_exterior() else "Interior"
    vida = "Sí" if self.tiene_vida else "No"
    return (
        f"Planeta: {self.nombre} | Densidad: {densidad:.2f} kg/m³ | Tipo:"
        f" {tipo} | Vida: {vida}"
    )



