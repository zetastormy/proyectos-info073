# Integrantes:
# Cristóbal Veas 21.707.611-0
# Benjamín Rojas V. 21.504.285-5
# Amaru Quintrel 21.391.384-0
# Diego Pérez de Arce 21.714.839-1
# Franco Sepúlveda 21.787.469-6

# Se importan los módulos usados en el juego.
from random import randint, randrange, uniform
import pygame


# Función que genera aleatoria una cantidad aleatoria de "ítems" de algún tipo,
# dentro de un tablero de 20 columnas y 20 filas, siendo lower_limit y upper_limit
# la cantidad mínima y máxima de ítems, respectivamente, utilizando randint para
# generar un número aleatorio en el rango proporcionado; new_board el tablero sobre el
# cual se trabajará y base_id, el ítem que se utilizará como referencia y que será sobreescrito
# por new_id, que es el ítem en cuestión que se busca generar.
# La función retorna un nuevo tablero con lo que se haya solicitado generar.
#
# Dentro de la función se observa el uso de randrange para obtener un "x" (representando
# las columnas del tablero) y un "y" (filas del tablero) al azar, sin contar los límites
# del tablero.
def gen_randomly(lower_limit, upper_limit, new_board, base_id, new_id):
    amount = randint(lower_limit, upper_limit)
    for k in range(amount):
        x = randrange(1, 19)
        y = randrange(1, 19)
        while new_board[x][y] != base_id or x + y <= 3:
            y = randrange(1, 19)

            while new_board[x][y] == new_id:
                x = randrange(1, 19)

        new_board[x][y] = new_id

    return new_board


# Función que realiza los movimientos aleatorios de los enemigos
# recibiendo como argumento el vector de la posición de algún enemigo en cuestión (enemy_pos),
# un contador (counter) que determinará qué determina si el enemigo debe ser movido o no y
# un "límite" para este contador (counter_limit) que servirá para mover a los enemigos en
# distintos intervalos.
#
# Dentro de la función se hace uso de uniform, que retornará un float en el rango de 0 a 1,
# que determinará el tipo de movimiento que hará el enemigo posteriormente.
def enemy_mov(enemy_pos, counter, counter_limit, pos_x, pos_y, enemy_board, enemy_id):
    counter += 1
    if counter == counter_limit:
        counter = 0

        if uniform(0, 1) <= 0.5:
            if uniform(0, 1) <= 0.6 and enemy_board[pos_y][pos_x + 1] != 1 and enemy_board[pos_y][pos_x + 1] != 2:
                enemy_board[pos_y][pos_x] = 0
                enemy_pos.x += 50
                pos_x += 1
                enemy_board[pos_y][pos_x] = enemy_id
            elif enemy_board[pos_y][pos_x - 1] != 1 and enemy_board[pos_y][pos_x - 1] != 2:
                enemy_board[pos_y][pos_x] = 0
                enemy_pos.x -= 50
                pos_x -= 1
                enemy_board[pos_y][pos_x] = enemy_id
        else:
            if uniform(0, 1) <= 0.6 and enemy_board[pos_y + 1][pos_x] != 1 and enemy_board[pos_y + 1][pos_x] != 2:
                enemy_board[pos_y][pos_x] = 0
                enemy_pos.y += 50
                pos_y += 1
                enemy_board[pos_y][pos_x] = enemy_id
            elif enemy_board[pos_y - 1][pos_x] != 1 and enemy_board[pos_y - 1][pos_x] != 2:
                enemy_board[pos_y][pos_x] = 0
                enemy_pos.y -= 50
                pos_y -= 1
                enemy_board[pos_y][pos_x] = enemy_id

    return enemy_pos, counter, pos_x, pos_y, enemy_board


def start_game():
    time_up = 3  # ID del evento de tiempo acabado.
    game_duration = 300000  # Se establece duración del juego a 5 minutos.
    pygame.time.set_timer(time_up, game_duration, loops=0)  # Se empieza a contar.

    # Implementamos la lista de listas que representará el tablero.
    board = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],

        [1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],

        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],

        [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],

        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],

        [1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],

        [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],

        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],

        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]

    running = True  # Establecemos el estado actual del juego.

    # Se cargan los assets correspondientes al piso, muros y muros destructibles.
    floor = pygame.image.load('assets/blocks/floor.jpeg').convert()
    wall = pygame.image.load('assets/blocks/wall.jpeg').convert()
    br_wall = pygame.image.load('assets/blocks/breakable_wall.jpeg').convert()

    # Se cargan los assets correspondientes a la llave, puerta, power-ups y efectoss.
    key = pygame.image.load('assets/items/key.png').convert_alpha()
    door = pygame.image.load('assets/items/door.png').convert_alpha()
    bomb = pygame.image.load('assets/items/bomb.png').convert_alpha()
    explosion = pygame.image.load('assets/items/explosion.png').convert_alpha()

    # Se cargan los assets para visualizar las vidas y su posición en la pantalla.
    hearts = pygame.image.load('assets/lives/3.png').convert_alpha()
    hearts_pos = pygame.Vector2(900, 0)

    player = pygame.image.load('assets/entities/player.png').convert_alpha()  # Se cargan los assets de jugador.
    player_pos = pygame.Vector2(50, 50)  # Se establece vector de posición inicial de jugador.

    enemy1 = pygame.image.load('assets/entities/enemy1.png').convert_alpha()  # Se cargan los assets del primer enemigo.
    enemy1_pos = pygame.Vector2(9999, 9999)  # Se establece el vector de posición inicial del primer enemigo.

    enemy2 = pygame.image.load(
        'assets/entities/enemy2.png').convert_alpha()  # Se cargan los assets del segundo enemigo.
    enemy2_pos = pygame.Vector2(9999, 9999)  # Se establece el vector de posición inicial del segundo enemigo.

    board = gen_randomly(100, 150, board, 0, 2)  # Se genera la posición de paredes las destructibles.
    board = gen_randomly(2, 5, board, 2, 3)  # Se genera la posición de los power-ups.
    board = gen_randomly(1, 1, board, 2, 4)  # Se genera la posición de la llave.
    board = gen_randomly(1, 1, board, 2, 5)  # Se genera la posición de la puerta.
    board = gen_randomly(1, 1, board, 2, 14)  # Se genera la posición del enemigo 1.
    board = gen_randomly(1, 1, board, 2, 15)  # Se genera la posición del enemigo 2.

    counter1 = 0  # Se establece el contador del primer enemigo.
    counter2 = 0  # Se establece el contador del segundo enemigo.

    # Se establece la columna y fila del tablero sobre la cual el jugador se encuentra
    # posicionado actualmente.
    board_pos_x = 1
    board_pos_y = 1

    # Almacena posiciones de enemigos en el tablero, similar al código anterior.
    enemy1_board_pos_x = 0
    enemy1_board_pos_y = 0
    enemy2_board_pos_x = 0
    enemy2_board_pos_y = 0

    lives = 3  # Establecemos las vidas iniciales.
    counterl1 = 50  # Contador que determina la cantidad de tiempo antes de perder una vida (enemigo 1).
    counterl2 = 50  # Contador que determina la cantidad de tiempo antes de perder una vida (enemigo 2).

    bomb_placed = False
    powerup = 0
    trigger_bomb = 1
    has_keys = 0
    enemy1_released = False
    enemy2_released = False

    clear_explosion = 2

    affected_spaces = []

    # Creamos el bucle principal de ejecución.
    while running:
        # Se establece la coordenada "x" e "y" sobre la cual nos encontraremos
        # generando algún ítem del tablero posteriormente.
        gen_pos_x = 0
        gen_pos_y = 0

        # Con el primer bucle recorremos todas las filas del tablero, por lo que de acuerdo
        # a la resolución establecida en un inicio, vamos sumando 50 a la coordenada "y" a medida
        # que vamos bajando hasta el final del tablero. De igual forma, reiniciamos la coordenada "x"
        # porque nuevamente debemos ver los elementos almacenados en esta fila usando el "for" interior.
        for i in range(len(board)):
            # En este bucle recorremos cada elemento existente en la fila actual, para ver qué es
            # lo que debemos generar en la coordenada "x, y" actual, dependiendo del número (id) del
            # ítem que se encuentre en el tablero en la posición actual. Similar al bucle anterior,
            # vamos sumando 50 a la coordenada "x" para indicar que hemos avanzado en la generación.
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    screen.blit(wall, [gen_pos_x, gen_pos_y])
                elif board[i][j] == 0:
                    screen.blit(floor, [gen_pos_x, gen_pos_y])
                elif board[i][j] == 3:
                    screen.blit(bomb, [gen_pos_x, gen_pos_y])
                    screen.blit(br_wall, [gen_pos_x, gen_pos_y])
                elif board[i][j] == 4:
                    screen.blit(key, [gen_pos_x, gen_pos_y])
                    screen.blit(br_wall, [gen_pos_x, gen_pos_y])
                elif board[i][j] == 5:
                    screen.blit(door, [gen_pos_x, gen_pos_y])
                    screen.blit(br_wall, [gen_pos_x, gen_pos_y])
                elif board[i][j] == 14 and not enemy1_released:
                    screen.blit(enemy1, [enemy1_pos.x, enemy1_pos.y])
                    screen.blit(br_wall, [gen_pos_x, gen_pos_y])
                    enemy1_pos.x = gen_pos_x
                    enemy1_pos.y = gen_pos_y
                    enemy1_board_pos_x = j
                    enemy1_board_pos_y = i
                elif board[i][j] == 15 and not enemy2_released:
                    screen.blit(enemy2, [enemy2_pos.x, enemy2_pos.y])
                    screen.blit(br_wall, [gen_pos_x, gen_pos_y])
                    enemy2_pos.x = gen_pos_x
                    enemy2_pos.y = gen_pos_y
                    enemy2_board_pos_x = j
                    enemy2_board_pos_y = i
                elif board[i][j] == 6:
                    screen.blit(floor, [gen_pos_x, gen_pos_y])
                    screen.blit(bomb, [gen_pos_x, gen_pos_y])
                elif board[i][j] == 7:
                    screen.blit(floor, [gen_pos_x, gen_pos_y])
                    screen.blit(explosion, [gen_pos_x, gen_pos_y])
                elif board[i][j] == 8:
                    screen.blit(floor, [gen_pos_x, gen_pos_y])
                    screen.blit(br_wall, [gen_pos_x, gen_pos_y])
                    screen.blit(bomb, [gen_pos_x, gen_pos_y])
                    screen.blit(explosion, [gen_pos_x, gen_pos_y])
                elif board[i][j] == 9:
                    screen.blit(floor, [gen_pos_x, gen_pos_y])
                    screen.blit(bomb, [gen_pos_x, gen_pos_y])
                elif board[i][j] == 10:
                    screen.blit(floor, [gen_pos_x, gen_pos_y])
                    screen.blit(br_wall, [gen_pos_x, gen_pos_y])
                    screen.blit(key, [gen_pos_x, gen_pos_y])
                    screen.blit(explosion, [gen_pos_x, gen_pos_y])
                elif board[i][j] == 11:
                    screen.blit(floor, [gen_pos_x, gen_pos_y])
                    screen.blit(key, [gen_pos_x, gen_pos_y])
                elif board[i][j] == 12:
                    screen.blit(floor, [gen_pos_x, gen_pos_y])
                    screen.blit(br_wall, [gen_pos_x, gen_pos_y])
                    screen.blit(door, [gen_pos_x, gen_pos_y])
                    screen.blit(br_wall, [gen_pos_x, gen_pos_y])
                elif board[i][j] == 13:
                    screen.blit(floor, [gen_pos_x, gen_pos_y])
                    screen.blit(door, [gen_pos_x, gen_pos_y])
                elif board[i][j] == 2:
                    screen.blit(br_wall, [gen_pos_x, gen_pos_y])
                gen_pos_x += 50

            gen_pos_y += 50
            gen_pos_x = 0

        # Llamamos a la función que mueve a los enemigos aleatoriamente.
        if enemy1_released:
            enemy1_pos, counter1, enemy1_board_pos_x, enemy1_board_pos_y, board = enemy_mov(enemy1_pos, counter1, 150,
                                                                                            enemy1_board_pos_x,
                                                                                            enemy1_board_pos_y,
                                                                                            board, 14)
            screen.blit(enemy1, [enemy1_pos.x, enemy1_pos.y])
        if enemy2_released:
            enemy2_pos, counter2, enemy2_board_pos_x, enemy2_board_pos_y, board = enemy_mov(enemy2_pos, counter2, 225,
                                                                                            enemy2_board_pos_x,
                                                                                            enemy2_board_pos_y,
                                                                                            board, 15)
            screen.blit(enemy2, [enemy2_pos.x, enemy2_pos.y])

        for event in pygame.event.get():
            # En caso de que haya que detener el juego, paramos el bucle de ejecución.
            if event.type == pygame.QUIT:
                running = False

            # Lo que sucede cuando se presiona alguna tecla en específico.
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.name(event.key)

                # Dependiendo de si se presionó una tecla para ir para arriba o abajo, izquierda o derecha, vamos
                # a sumar o restar a las coordenadas del jugador 50 y a posición del tablero en el que se encuentra
                # también le sumamos o restamos 1, para así saber qué hay en esa posición actual y poder implementar
                # las colisiones del jugador como se ve en la condición de cada "if", donde se evalúa que lo que haya
                # en la posición a la que se quiera mover no sea un muro destructible (2) o indestructible (1), por lo
                # que sí se elimina la parte posterior al "\", no habrán colisiones.
                if key_pressed == "w" \
                        and not (board[board_pos_y - 1][board_pos_x] == 1 or board[board_pos_y - 1][board_pos_x] == 2 or
                                 board[board_pos_y - 1][board_pos_x] == 3 or board[board_pos_y - 1][board_pos_x] == 4 or
                                 board[board_pos_y - 1][board_pos_x] == 5 or board[board_pos_y - 1][board_pos_x] == 6 or
                                 (board[board_pos_y - 1][board_pos_x] == 14 and not enemy1_released) or
                                 (board[board_pos_y - 1][board_pos_x] == 15 and not enemy2_released)):
                    player_pos.y -= 50
                    board_pos_y -= 1
                elif key_pressed == "s" \
                        and not (board[board_pos_y + 1][board_pos_x] == 1 or board[board_pos_y + 1][board_pos_x] == 2 or
                                 board[board_pos_y + 1][board_pos_x] == 3 or board[board_pos_y + 1][board_pos_x] == 4 or
                                 board[board_pos_y + 1][board_pos_x] == 5 or board[board_pos_y + 1][board_pos_x] == 6 or
                                 (board[board_pos_y + 1][board_pos_x] == 14 and not enemy1_released) or
                                 (board[board_pos_y + 1][board_pos_x] == 15 and not enemy2_released)):
                    player_pos.y += 50
                    board_pos_y += 1
                elif key_pressed == "a" \
                        and not (board[board_pos_y][board_pos_x - 1] == 1 or board[board_pos_y][board_pos_x - 1] == 2 or
                                 board[board_pos_y][board_pos_x - 1] == 3 or board[board_pos_y][board_pos_x - 1] == 4 or
                                 board[board_pos_y][board_pos_x - 1] == 5 or board[board_pos_y][board_pos_x - 1] == 6 or
                                 (board[board_pos_y][board_pos_x - 1] == 14 and not enemy1_released) or
                                 (board[board_pos_y][board_pos_x - 1] == 15 and not enemy2_released)):
                    player_pos.x -= 50
                    board_pos_x -= 1
                elif key_pressed == "d" \
                        and not (board[board_pos_y][board_pos_x + 1] == 1 or board[board_pos_y][board_pos_x + 1] == 2 or
                                 board[board_pos_y][board_pos_x + 1] == 3 or board[board_pos_y][board_pos_x + 1] == 4 or
                                 board[board_pos_y][board_pos_x + 1] == 5 or board[board_pos_y][board_pos_x + 1] == 6 or
                                 (board[board_pos_y][board_pos_x + 1] == 14 and not enemy1_released) or
                                 (board[board_pos_y][board_pos_x + 1] == 15 and not enemy2_released)):
                    player_pos.x += 50
                    board_pos_x += 1
                elif key_pressed == 'space' and not bomb_placed:
                    # Establece que la bomba ha sido colocada y un timer para que esta explote después de un tiempo.
                    bomb_placed = True
                    pygame.time.set_timer(trigger_bomb, 1500, loops=1)
                    board[board_pos_y][board_pos_x] = 6
                    screen.blit(bomb, [player_pos.x, player_pos.y])

                    # Establece el daño hecho por la bomba.
                    affected_spaces = [[board_pos_y + 1, board_pos_x], [board_pos_y - 1, board_pos_x],
                                       [board_pos_y, board_pos_x + 1], [board_pos_y, board_pos_x - 1],
                                       [board_pos_y, board_pos_x]]

                    # Si el jugador tiene un power-up, entonces la explosión se expande y toma en cuenta las diagonales.
                    if powerup > 0:
                        affected_spaces.append([board_pos_y + 1, board_pos_x + 1])
                        affected_spaces.append([board_pos_y + 1, board_pos_x - 1])
                        affected_spaces.append([board_pos_y - 1, board_pos_x + 1])
                        affected_spaces.append([board_pos_y - 1, board_pos_x - 1])
                        powerup = powerup - 1

            # Aplica los destrozos hechos por la bomba.
            if event.type == trigger_bomb:
                for yx in affected_spaces:
                    if board[yx[0]][yx[1]] == 3:
                        board[yx[0]][yx[1]] = 8
                    elif board[yx[0]][yx[1]] == 4:
                        board[yx[0]][yx[1]] = 10
                    elif board[yx[0]][yx[1]] == 5:
                        board[yx[0]][yx[1]] = 12
                    elif board[yx[0]][yx[1]] == 14:
                        if not enemy1_released:
                            enemy1_released = True
                        else:
                            enemy1_released = False
                    elif board[yx[0]][yx[1]] == 15:
                        if not enemy2_released:
                            enemy2_released = True
                        else:
                            enemy2_released = False
                    elif yx[0] == board_pos_y and yx[1] == board_pos_x:
                        lives -= 1
                    elif board[yx[0]][yx[1]] != 1:
                        board[yx[0]][yx[1]] = 7
                    elif player_pos.distance_to([yx[0], yx[1]]) < 50:
                        lives -= 1
                    screen.blit(explosion, [yx[0], yx[1]])
                    pygame.time.set_timer(clear_explosion, 200, loops=1)

            # Coloca los ítems que hayan sido descubiertos después de la explosión.
            if event.type == clear_explosion:
                bomb_placed = False
                for yx in affected_spaces:
                    if board[yx[0]][yx[1]] == 8:
                        board[yx[0]][yx[1]] = 9
                    elif board[yx[0]][yx[1]] == 10:
                        board[yx[0]][yx[1]] = 11
                    elif board[yx[0]][yx[1]] == 12:
                        board[yx[0]][yx[1]] = 13
                    elif board[yx[0]][yx[1]] != 1:
                        board[yx[0]][yx[1]] = 0

            if event.type == time_up:
                defeat_screen("assets/screens/defeat2.jpeg")
                return

        if enemy1_released and board_pos_x == enemy1_board_pos_x and board_pos_y == enemy1_board_pos_y:
            counterl1 += 1
            if counterl1 == 100:
                lives -= 1
                counterl1 = 0
        elif enemy2_released and board_pos_x == enemy2_board_pos_x and board_pos_y == enemy2_board_pos_y:
            counterl2 += 2
            if counterl2 == 100:
                lives -= 1
                counterl2 = 0

        # Se actualiza la posición del jugador.
        screen.blit(player, [player_pos.x, player_pos.y])

        # Se revisa la cantidad de vida y se hace lo que corresponda (cambiar la vida o acabar el juego).
        if lives == 2:
            hearts = pygame.image.load('assets/lives/2.png').convert_alpha()
        elif lives == 1:
            hearts = pygame.image.load('assets/lives/1.png').convert_alpha()
        elif lives == 0:
            defeat_screen("assets/screens/defeat.jpeg")
            return

        screen.blit(hearts, [hearts_pos.x, hearts_pos.y])

        # Cuando el jugador está sobre una superbomba el contador de powerup se actualiza.
        if board[board_pos_y][board_pos_x] == 9:
            powerup = powerup + 1
            board[board_pos_y][board_pos_x] = 0

        # Cuando el jugador se para sobre una llave, esta se añade a su inventario
        if board[board_pos_y][board_pos_x] == 11:
            has_keys = has_keys + 1
            board[board_pos_y][board_pos_x] = 0

        # Cuando el jugador posee una llave y está sobre la puerta, se muestra la pantalla de victoria.
        if board[board_pos_y][board_pos_x] == 13 and has_keys == 1:
            victory_screen()
            return

        # Actualizamos la pantalla.
        pygame.display.flip()

    # Finalizamos pygame.
    pygame.quit()


# Función que implementa la pantalla de derrota.
def defeat_screen(defeat_asset):
    defeat = pygame.image.load(defeat_asset).convert_alpha()
    while True:
        for event in pygame.event.get():
            # En caso de querer cerrar el juego.
            if event.type == pygame.QUIT:
                break

            # Lo que pasa cuando se presiona espacio o escape.
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.name(event.key)
                # Por si el jugador quiere jugar de nuevo.
                if key_pressed == "space":
                    start_game()
                    return
                # Por si el jugador quiere cerrar el juego.
                if key_pressed == "escape":
                    pygame.quit()
                    return

        screen.blit(defeat, [0, 0])
        pygame.display.flip()


# Función que implementa la pantalla de victoria
def victory_screen():
    victory = pygame.image.load("assets/screens/victory.jpeg").convert_alpha()
    while True:
        for event in pygame.event.get():
            # En caso de querer cerrar el juego.
            if event.type == pygame.QUIT:
                break

            # Lo que pasa cuando se presiona espacio o escape.
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.name(event.key)
                # Por si el jugador quiere jugar de nuevo.
                if key_pressed == "space":
                    start_game()
                    return
                # Por si el jugador quiere cerrar el juego.
                if key_pressed == "escape":
                    pygame.quit()
                    return

        screen.blit(victory, [0, 0])
        pygame.display.flip()


# Función que implementa la pantalla de instrucciones para llamarla mas abajo con una tecla
def instructions_screen():
    instructions = pygame.image.load('assets/screens/instructions.jpeg').convert_alpha()
    while True:
        for event in pygame.event.get():
            # En caso de que haya que detener el juego, paramos el bucle de ejecución.
            if event.type == pygame.QUIT:
                break

            # Lo que sucede cuando se presiona alguna tecla en específico.
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.name(event.key)

                if key_pressed == "escape":
                    start_screen()
                    return

        screen.blit(instructions, [0, 0])
        pygame.display.flip()


def start_screen():
    start_image = pygame.image.load('assets/screens/start.png').convert_alpha()

    while True:
        for event in pygame.event.get():
            # En caso de que haya que detener el juego, paramos el bucle de ejecución.
            if event.type == pygame.QUIT:
                break

            # Lo que sucede cuando se presiona alguna tecla en específico.
            if event.type == pygame.KEYDOWN:
                key_pressed = pygame.key.name(event.key)

                if key_pressed == "space":
                    start_game()
                    return

                if key_pressed == "i":
                    instructions_screen()
                    return

                if key_pressed == "escape":
                    start_screen()
                    return

        screen.blit(start_image, [0, 0])
        pygame.display.flip()


pygame.init()  # Iniciamos pygame.
pygame.display.set_caption("Chico bomba")  # Establecemos el nombre de la ventana.
screen = pygame.display.set_mode((1000, 1000))  # Establecemos la resolución de la pantalla a 1000x1000.
start_screen()
