import random
import json
import time
from colorama import Style


chars = "abcdefghijklmnñopqrstuvwxyz"

class Pais:
    def __init__(self, nombre:str = None) -> None:
        if nombre is None:
            name = "".join([random.choice(chars) for i in range(10)])
        else:
            name = nombre
        self.nombre = name.title()

    def __str__(self) -> str:
        return f"{self.nombre}"


def main():
    with open("config.json","r") as file:
        config = json.loads(file.read())

    dias = 0
    poblacion = 2
    paises = []
    muertes = 0
    desastres_naturales = 0

    while True:
        if poblacion <= 1:
            print("¡Has perdido!")
            break

        time.sleep(int(config["dia"]))
        nacimientos_hoy = 0
        muertes_hoy = 0
        desastres_naturales_hoy = 0


        if random.random() < float(config["nacimiento_probabilidad"]):
            nuevo_nacimiento = random.randint(1,5)
            poblacion = poblacion+nuevo_nacimiento
            nacimientos_hoy += nuevo_nacimiento

        if random.random() < float(config["muerte_probabilidad"]):
            muertes_ = random.randint(1, 5)
            if muertes_ > poblacion:
                muertes += poblacion
                muertes_hoy += poblacion
                poblacion = 0
            else:
                poblacion -= muertes_
                muertes_hoy += muertes_
                muertes += muertes_

        if random.random() < float(config["desastre_natural_probabilidad"]):
            muertes_desastre = random.randint(0, 100)

            if muertes_desastre > poblacion:
                poblacion = 0
            else:
                poblacion -= muertes_desastre
            desastres_naturales += 1
            desastres_naturales_hoy += 1

        if poblacion > 100:
            if random.random() < float(config["nuevo_pais_probabilidad"]):
                paises.append(Pais())

        dias += 1
        print("="*100)
        print(f"""{Style.BRIGHT}Dia {dias}{Style.NORMAL}
Población en general: {poblacion}
Muertes en total: {muertes}
Desastres naturales en total: {desastres_naturales}
Nacimientos de hoy: {nacimientos_hoy}
Desastres naturales de hoy: {desastres_naturales_hoy}
Muertes de hoy: {muertes_hoy}


Paises:
""")
        for pais in paises:
            print(f"- {pais.nombre}")
        print("="*100)
        print("\n\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Que tengas un buen dia!.")