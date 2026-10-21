class CamaraInspeccion:
    def __init__(self, nombre, cinta):
        self.nombre = nombre
        self.cinta = cinta
        self.objeto_detectado = False
        self.forma_detectada = None

    def capturar(self, renderer, data):
        pass

    def detectar_forma(self, imagen):
        pass

    def actualizar(self, renderer, data):
        pass
