from scripts.car import Car
from scripts.turtle import Turtle

class Log:
    def __init__(self, x, y, tamanho, direcao, speed, graphicos, tipo, sink=False):
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.speed = speed
        self.direcao = direcao
        self.graphicos = graphicos
        self.sink = sink
        if tipo == "log":
            self.objeto = self.build_log()
        if tipo == "turtle":
            self.objeto = self.build_turtle()

    def build_log(self):
        if len(self.graphicos) > 1:
            pontas = [Car(self.x+(16*part[0]), self.y, self.direcao, self.speed, self.graphicos[part[1]]) for part in ((0,0), (self.tamanho-1,2))]
            b_meio = [Car(self.x+(16*part), self.y, self.direcao, self.speed, self.graphicos[1] if len(self.graphicos) > 1 else self.graphicos[0]) for part in range(1,self.tamanho-1)]
            return [pontas[0]] + b_meio + [pontas[1]]
        else:
            return [Car(self.x+(16*part), self.y, self.direcao, self.speed, self.graphicos[0]) for part in range(self.tamanho)]

    def build_turtle(self):
        if len(self.graphicos) > 1:
            return [Turtle(self.x+(16*part), self.y, self.direcao, self.speed, self.graphicos, self.sink) for part in range(self.tamanho)]

    def draw_log(self, screen, dt):
        for i,part in enumerate(self.objeto[::self.direcao*(-1)]):
                if i == 0:
                    part.draw(screen, dt)
                else:
                    part.draw(screen, dt, self.objeto[::self.direcao*(-1)][i-1].x)