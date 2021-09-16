# muitos movimentos do cotidiano são aleatórios
from random import choice


class RandomWalk():
    """Gera passeios aleatórios"""
    def __init__(self, num_points=5000):
        # todos os passeios começam em 0, 0
        self.x = [0]
        self.y = [0]
        self.num_points = num_points

    # método para gerar pontos:
    def fill_walks(self):
        # até o tamanho de pontos, dá os passos
        while len(self.x) < self.num_points:
            # decide a direção a ser percorrida
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3 , 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # rejeitar não movimentos:
            if x_step == 0 and y_step == 0:
                continue

            # calcula os próximos valores de x e de y:
            next_x = self.x[-1] + x_step
            next_y = self.y[-1] + y_step
            self.x.append(next_x)
            self.y.append(next_y)



rw = RandomWalk()
rw.fill_walks()
print(rw.x)