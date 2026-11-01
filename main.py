from src.planta import PlantaIndustrial


def main():
    planta = PlantaIndustrial()
    planta.inicializar()
    print(len(planta.objetos))


if __name__ == "__main__":
    main()
