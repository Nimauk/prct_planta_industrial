from src.planta import PlantaIndustrial


def main():
    planta = PlantaIndustrial()
    planta.inicializar()
    print(planta.model.nbody)


if __name__ == "__main__":
    main()
