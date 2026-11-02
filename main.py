from src.planta import PlantaIndustrial


def main():
    planta = PlantaIndustrial()
    planta.inicializar()
    print(len(planta.cintas))


if __name__ == "__main__":
    main()
