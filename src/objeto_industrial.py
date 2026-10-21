class ObjetoIndustrial:
    def __init__(self, id, forma, body_id, dof_adr, segmento=0):
        self.id = id
        self.forma = forma
        self.body_id = body_id
        self.dof_adr = dof_adr
        self.segmento = segmento

    def actualizar_segmento(self, segmento):
        self.segmento = segmento
