import cv2

class CamaraInspeccion:
    def __init__(self, nombre, cinta):
        self.nombre = nombre
        self.cinta = cinta
        self.objeto_detectado = False
        self.forma_detectada = None
        self.tiempo_parada = -1.0
        self.esperar_salida = False
        self.imagen = None

    def capturar(self, renderer, data):
        renderer.update_scene(data, camera=self.nombre)
        rgb = renderer.render()
        return cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

    def detectar_forma(self, imagen):
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        _, blanco_negro = cv2.threshold(gris, 100, 255, cv2.THRESH_BINARY)
        contornos, _ = cv2.findContours(blanco_negro, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if len(contornos) == 0:
            return None

        mayor = max(contornos, key=cv2.contourArea)
        area = cv2.contourArea(mayor)
        if area < 200:
            return None

        perimetro = cv2.arcLength(mayor, True)
        if perimetro > 0 and (4 * 3.1416 * area) / (perimetro * perimetro) > 0.8:
            return "cilindro"
        return "caja"

    def actualizar(self, renderer, data):
        if self.tiempo_parada >= 0 and data.time - self.tiempo_parada >= 0.8:
            self.cinta.arrancar()
            self.tiempo_parada = -1.0
            self.esperar_salida = True

        imagen = self.capturar(renderer, data)
        self.imagen = imagen
        self.forma_detectada = self.detectar_forma(imagen)
        self.objeto_detectado = self.forma_detectada is not None

        if not self.objeto_detectado:
            self.esperar_salida = False

        if self.objeto_detectado and not self.esperar_salida and self.tiempo_parada < 0:
            self.cinta.detener()
            self.tiempo_parada = data.time
