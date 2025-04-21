from utils import *

if __name__ == "__main__":

  print("Voici quelques tests:")

  liste1 = [1, 2, 3, 4, 5]
  moyenne1 = calculer_moyenne(liste1)
  print(f"La moyenne de {liste1} est : {moyenne1}")

  celsius = 25
  fahrenheit = convertir_temperature(celsius, 'C', 'F')
  print(f"{celsius}°C est égal à {fahrenheit}°F")

