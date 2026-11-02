VEL_KP = 7.0
MAX_FORCE = 12.0
LANE = 1.45
CENTER_KP = 12.0

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

    def eje(self):
        if self.direccion in ("+X", "-X"):
            return 0
        return 1

    def calcular_fuerza(self, velocidad_pieza):
        if self.direccion.startswith("+"):
            objetivo = self.velocidad
        else:
            objetivo = -self.velocidad

        fuerza = (objetivo - velocidad_pieza) * VEL_KP
        return max(-MAX_FORCE, min(MAX_FORCE, fuerza))

    def calcular_fuerza_lateral(self, velocidad_lateral, posicion_lateral):
        if self.direccion != "-Y":
            return 0.0

        centro = -LANE
        frenar = -velocidad_lateral * VEL_KP
        centrar = (centro - posicion_lateral) * CENTER_KP
        fuerza = frenar + centrar
        return max(-MAX_FORCE, min(MAX_FORCE, fuerza))

    def conmutar(self):
        self.activa = not self.activa

    def esta_activa(self):
        return self.activa
