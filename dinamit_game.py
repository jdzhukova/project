def use_dinamit():

    from random import randint
    print('Чтобы зажечь динамит, пройдите задание.')
    print('У вас есть 4 рычага. 🔴 - выключен , 🟢 - включен , введя номер над рычагом, вы включите или выключите его.')
    print('Ваша задача - найти правильную последовательность рычагов.')

    game = [
        ['1️⃣' , '2️⃣' , '3️⃣' , '4️⃣'],
        ['🔴' , '🔴' , '🔴' , '🔴']
    ]
    
    while True:
        st = input('Чтобы начать игру , введите "старт"')
        if st.lower().strip() == 'старт':
            break
        else:
            print('Команда не распознана')
            continue

    while True:
        for line in game:
            print(*line)
        number = input('Введите номер (1 - 4):').strip()
        if number in ['1' , '2' , '3' , '4']:
            if game[1][int(number) - 1] == "🔴":
                game[1][int(number) - 1] = '🟢'
            elif game[1][int(number) - 1] == '🟢':
                game[1][int(number) - 1] = '🔴'
        else:
            print('Введен неизвестный символ')
            continue
        if game[1] == ['🟢' , '🔴' , '🟢' , '🟢']:
            print('Вы угадали правильную последовательность!')
            a = randint(1 , 2)
            if a == 1:
                print('Вы успешно выбрались из-под завалов камней. Выход открыт! ПОБЕДА')
            else:
                print('Вы слышите грохот. К сожалению взрыв задел и вас, вы погибли. ПРОИГРЫШ')
            return True
            
