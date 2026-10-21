class CintaTransportadora:
    def __init__(self, nombre, velocidad, direccion, activa = True):
        self.nombre = nombre
        self.velocidad = velocidad
        self.direccion = direccion
        self.activa = activa

    def arrancar(self):
        self.activa = True

    def detener(self):
        self.activa = False

    def conmutar(self):
        self.activa = not self.activa

    def esta_activa(self):
        return self.activa
