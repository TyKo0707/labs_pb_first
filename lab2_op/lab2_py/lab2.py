while True:

    x = float(input('Введите координаты х: '))  # Вводимо координату х
    y = float(input('Введите координаты y: '))  # Вводимо координату у

    if -1 <= x <= 3:  # Перевіряємо, чи належить введений x дозволеній зоні
        if -1 <= x <= 1:  # Перевіряємо, чи належить х півколу
            y1 = (4 - ((x - 1) ** 2)) ** (1 / 2)  # Підставимо х у формулу кола щоб найти дозволену границю у для введеного х
            if -y1 <= y <= y1:  # Перевіряємо, чи належить введений у дозволеній зоні заштрихованої фігури
                print('Точка належить заштрихованій зоні!')
            else:
                print('Точка НЕ належить заштрихованій зоні!')
        else:
            y2 = 3 - x  # Підставимо х у формулу прямої щоб найти дозволену границю у для введеного х
            if -y2 <= y <= y2:  # Перевіряємо, чи належить введений у дозволеній зоні заштрихованої фігури
                print('Точка належить заштрихованій зоні!')
            else:
                print('Точка НЕ належить заштрихованій зоні!')
    else:
        print('Точка НЕ належить заштрихованій зоні!')
