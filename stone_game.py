def stone_game(is_playing):


    WALL = "⬛"
    PLAYER = "🙂"
    STONE = "🌑"
    PUSTOTA = "⬜"

    stones = [
        ["🙂","⬛","⬜","⬜","⬛","⬜","⬜","⬛"],
        ["⬜","⬜","⬛","⬜","⬜","⬜","🌑","⬜"],
        ["⬜","🌑","⬜","⬜","⬛","⬜","⬜","⬜"],
        ["⬜","⬜","⬜","🌑","⬜","⬜","⬛","⬜"],
        ["⬛","⬜","⬜","⬜","🌑","⬜","⬜","⬜"],
        ["⬜","⬛","⬜","⬜","⬜","🌑","⬜","⬜"],
        ["⬜","⬜","⬜","⬛","⬜","⬜","⬜","🌑"]
    ]

    x = 0     #текущее положение игрока
    y = 0     #и это тоже

    print('w - вверх, s - вниз, a - влево, d - вправо')
    print('Ваша задача - вытолкнуть все камни за пределы поля. ' \
    'Постарайтесь обходить стены. Если хотите начать игру с начала введите "переиграть"')
    for e in stones:
        print(*e)

    while True:
            go = input().lower().strip()
            if go == 'переиграть':
                return True
            
            if go not in ['w' , 'a' , 's' , 'd']:
                print('Введен неизвестный символ. До самоуничтожения компьютера: 3.. 2... 1... 0... -1... -2...')
                continue
            
            kuda_idti = {'w' : [ x - 1  , y]  , 's' : [x + 1 , y] , 'a' : [x , y - 1] , 'd': [x , y + 1]}
            koordinata = kuda_idti[go]
            xxx = koordinata[0]
            yyy = koordinata[1]

            if not (0 <= xxx < len(stones) and 0 <= yyy < len(stones[0])):
                print('Нельзя покинуть поле')
                continue                        
            if stones[xxx][yyy] == WALL: #чтобы игрок не гулял по стенам
                print('Нельзя наступать на стены, они обидятся')
                continue
            
            if stones[xxx][yyy] == STONE: #игрок толкает камень
                x_stone = xxx * 2 - x #вычисляем положение камня относительно игрока
                y_stone = yyy * 2 - y
                if not 0 <= x_stone < len(stones) or not 0 <= y_stone < len(stones[0]): #проверяем, в пределах ли поля камень
                    stones[xxx][yyy] = PLAYER  #если камень оказывается за пределами поля, то он просто исчезает, а мето, где он раньше был, занимает игрок
                else:
                    if stones[x_stone][y_stone] != PUSTOTA: #проверяем, свободна ли клетка, на которой окажется камень
                        print('Ты не пройдешь! Видимо, туда камень толкнуть нельзя') 
                        continue
                    stones[x_stone][y_stone] = STONE
            stones[x][y] = PUSTOTA
            stones[xxx][yyy] = PLAYER   #ход игрока
            y = yyy   #местонахождение игрока = место, куда он перешел
            x = xxx
            have_st = False #проверка не наличие камней
            for t in stones:
                if STONE  in t:
                    have_st = True
                    break
            if not have_st:
                print('Игра успешно пройдена!' \
                'Вы разобрали камни и путь к свободе открыт. ПОБЕДА🎉')
                return False 
            
            for e in stones:
                print(*e)
    
    return False
