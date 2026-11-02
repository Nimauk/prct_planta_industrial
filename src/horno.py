class Horno:
    def __init__(self, geom_id, temp_inicial = 20.0, temp_min = 20.0, temp_max = 200.0):
        self.numero_piezas = 0
        self.temperatura = temp_inicial
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.estado = "Apagado"
        self.geom_id = geom_id

    def registrar_pieza(self):
        self.numero_piezas += 1

    def aumentar_temperatura(self, temperatura):
        if self.temperatura + temperatura <= self.temp_max:
            self.temperatura += temperatura
        else:
            self.temperatura = self.temp_max

    def disminuir_temperatura(self, temperatura):
        if self.temperatura - temperatura >= self.temp_min:
            self.temperatura -= temperatura
        else:
            self.temperatura = self.temp_min

    def obtener_temperatura(self):
        return self.temperatura

    def actualizar_color(self, model):
        if self.temperatura < 50:
            color = [0.1, 0.3, 1.0, 1.0]
        elif self.temperatura < 100:
            color = [1.0, 0.6, 0.1, 1.0]
        else:
            color = [1.0, 0.1, 0.1, 1.0]

        model.geom_rgba[self.geom_id] = color
