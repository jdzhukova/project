def use_radio(is_playing):
    from random import randint

    work = '🔴'
    kanal = {0 : '⬜' , 1 : '1️⃣' , 2 : '2️⃣' , 3 : '3️⃣' , 4 : '4️⃣' , 5 : '5️⃣'}
    right_kanal = randint(1 , 5)
    is_on = False
    chance_to_call = randint(1 , 2)
    
    def print_radio(work , kanal_x , kanal):
        radio = [
            ['🟪','🟪','🟪','🟪','🟪' ],
            ['🟪','⬜','⬜',kanal[kanal_x] ,'🟪' ],
            ['🟪','📶','⬜','⬜','🟪' ],
            ['🟪','🟪','🟪','🟪','🟪' ],
            ['🟪',work,'🟪','🆘','🟪' ],
            ['🟪','🟪','🟪','🟪','🟪' ]
            ]
        for i in radio:
            print(*i)
    
    while True:
        if not is_on:
            turn_on = input('Чтобы включить рацию введите "включить":  ').lower().strip()
            if turn_on == 'включить':
                is_on = True
                work = '🟢'
            else:
                print('Рация не включилась')
                continue
        kanal_x = input('Введите номер канала от 1 до 5:').strip()
        try:
            kanal_x = int(kanal_x)
        except ValueError:
            print('А это не число')
            continue
        if kanal_x not in [1 , 2 , 3 , 4 , 5]:
            print('Неверный номер канала')
            continue
    
        print_radio(work , kanal_x , kanal)

        if kanal_x == right_kanal and is_on :
            break
                
            

    if chance_to_call == 1:
        print('Вы смогли выйти на связь с людьми и объяснить им свое местоположение.' \
        'Через час томительного ожидания вас нашли и вызволили нa свободу. ПОБЕДА🏆')
        is_playing = False
        return is_playing
    else:
        print('К сожалению, вам не удалось связаться с людьми. Придется искать другой способ выбраться.')
        