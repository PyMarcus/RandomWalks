import matplotlib.pyplot as plt

from passeios_aleatorios import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walks()
    # define o tamanho da tela:
    plt.figure(figsize=(10.24, 7.20))
    point_numbers = list(range(rw.num_points))
    # realcando o percurso com a lista de pontos totais:
    plt.scatter(rw.x, rw.y, s=15, c=point_numbers, edgecolors='none')
    # ralcando  o primeiro ponto:
    plt.scatter(0, 0, c='pink', edgecolors='none', s=100)
    # realcando ultimo ponto:
    plt.scatter(rw.x[-1], rw.y[-1], c='red', edgecolors='none', s=100)
    # limpando eixos:
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)
    plt.title("Passeios aleatórios")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.savefig('graficu.png', bbox_inches='tight')
    make_other = input('fazer outro: ')
    if make_other == 'n':
        break
