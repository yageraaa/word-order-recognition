import os
import pandas as pd

audio_dir = os.path.join("..", "data", "audio")

metadata = []

for file_name in os.listdir(audio_dir):
    if file_name.endswith(".wav"):
        parts = file_name.split("_")
        sentence_id = int(parts[1])
        variant_id = int(parts[2].replace("var", "").replace(".wav", ""))

        if sentence_id == 1:
            if variant_id == 1:
                text = "Утром я пью горячий кофе"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "Я пью горячий кофе утром"
                is_correct = 1
                word_positions = [2, 3, 4, 5, 1]
            elif variant_id == 3:
                text = "Горячий кофе я пью утром"
                is_correct = 1
                word_positions = [4, 2, 3, 1, 5]
            elif variant_id == 4:
                text = "Пью утром кофе я горячий"
                is_correct = 0
                word_positions = [3, 1, 5, 2, 4]

        elif sentence_id == 2:
            if variant_id == 1:
                text = "Собака гоняется за мячом в парке"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5, 6]
            elif variant_id == 2:
                text = "В парке собака гоняется за мячом"
                is_correct = 1
                word_positions = [5, 1, 2, 3, 4, 6]
            elif variant_id == 3:
                text = "За мячом в парке гоняется собака"
                is_correct = 1
                word_positions = [4, 5, 6, 3, 2, 1]
            elif variant_id == 4:
                text = "Гоняется парке в мячом за собака"
                is_correct = 0
                word_positions = [3, 6, 5, 4, 2, 1]

        elif sentence_id == 3:
            if variant_id == 1:
                text = "Дети рисуют красками на бумаге"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "На бумаге дети рисуют красками"
                is_correct = 1
                word_positions = [5, 1, 2, 3, 4]
            elif variant_id == 3:
                text = "Красками дети рисуют на бумаге"
                is_correct = 1
                word_positions = [3, 1, 2, 5, 4]
            elif variant_id == 4:
                text = "Рисуют бумаге на красками дети"
                is_correct = 0
                word_positions = [2, 5, 4, 3, 1]

        elif sentence_id == 4:
            if variant_id == 1:
                text = "Вечером мы смотрим новый фильм"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "Новый фильм мы смотрим вечером"
                is_correct = 1
                word_positions = [4, 2, 3, 1, 5]
            elif variant_id == 3:
                text = "Мы вечером смотрим новый фильм"
                is_correct = 1
                word_positions = [2, 1, 3, 4, 5]
            elif variant_id == 4:
                text = "Смотрим мы новый вечером фильм"
                is_correct = 0
                word_positions = [3, 2, 4, 1, 5]

        elif sentence_id == 5:
            if variant_id == 1:
                text = "В саду цветут красные розы"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "Красные розы цветут в саду"
                is_correct = 1
                word_positions = [4, 5, 3, 1, 2]
            elif variant_id == 3:
                text = "Цветут в саду красные розы"
                is_correct = 1
                word_positions = [3, 1, 2, 4, 5]
            elif variant_id == 4:
                text = "Розы красные в саду цветут"
                is_correct = 0
                word_positions = [5, 4, 1, 2, 3]

        elif sentence_id == 6:
            if variant_id == 1:
                text = "Мальчик играет в футбол с друзьями"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5, 6]
            elif variant_id == 2:
                text = "С друзьями мальчик играет в футбол"
                is_correct = 1
                word_positions = [5, 6, 1, 2, 3, 4]
            elif variant_id == 3:
                text = "В футбол мальчик играет с друзьями"
                is_correct = 1
                word_positions = [3, 4, 1, 2, 5, 6]
            elif variant_id == 4:
                text = "Играет мальчик друзьями в с футбол"
                is_correct = 0
                word_positions = [2, 1, 6, 3, 5, 4]

        elif sentence_id == 7:
            if variant_id == 1:
                text = "Дождь идёт уже целый час"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "Уже целый час дождь идёт"
                is_correct = 1
                word_positions = [3, 4, 5, 1, 2]
            elif variant_id == 3:
                text = "Целый час уже дождь идёт"
                is_correct = 1
                word_positions = [4, 5, 3, 1, 2]
            elif variant_id == 4:
                text = "Идёт дождь целый уже час"
                is_correct = 0
                word_positions = [2, 1, 4, 3, 5]

        elif sentence_id == 8:
            if variant_id == 1:
                text = "Студенты пишут конспекты в библиотеке"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "В библиотеке студенты пишут конспекты"
                is_correct = 1
                word_positions = [4, 5, 1, 2, 3]
            elif variant_id == 3:
                text = "Конспекты студенты пишут в библиотеке"
                is_correct = 1
                word_positions = [3, 1, 2, 4, 5]
            elif variant_id == 4:
                text = "Пишут в студенты библиотеке конспекты"
                is_correct = 0
                word_positions = [2, 4, 1, 5, 3]

        elif sentence_id == 9:
            if variant_id == 1:
                text = "Солнце светит ярко на небе"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "На небе солнце светит ярко"
                is_correct = 1
                word_positions = [4, 5, 1, 2, 3]
            elif variant_id == 3:
                text = "Ярко светит солнце на небе"
                is_correct = 1
                word_positions = [3, 2, 1, 4, 5]
            elif variant_id == 4:
                text = "Светит ярко небе на солнце"
                is_correct = 0
                word_positions = [2, 3, 5, 4, 1]

        elif sentence_id == 10:
            if variant_id == 1:
                text = "Мама варит суп на кухне"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "На кухне мама варит суп"
                is_correct = 1
                word_positions = [4, 5, 1, 2, 3]
            elif variant_id == 3:
                text = "Суп мама варит на кухне"
                is_correct = 1
                word_positions = [3, 1, 2, 4, 5]
            elif variant_id == 4:
                text = "Варит мама кухне на суп"
                is_correct = 0
                word_positions = [2, 1, 5, 4, 3]

        elif sentence_id == 11:
            if variant_id == 1:
                text = "Поезд отправляется с платформы через пять минут"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5, 6, 7]
            elif variant_id == 2:
                text = "Через пять минут поезд отправляется с платформы"
                is_correct = 1
                word_positions = [5, 6, 7, 1, 2, 3, 4]
            elif variant_id == 3:
                text = "С платформы поезд отправляется через пять минут"
                is_correct = 1
                word_positions = [3, 4, 1, 2, 5, 6, 7]
            elif variant_id == 4:
                text = "Отправляется платформы с поезд минут пять через"
                is_correct = 0
                word_positions = [2, 4, 3, 1, 7, 6, 5]

        elif sentence_id == 12:
            if variant_id == 1:
                text = "Книга лежит на столе рядом с лампой"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5, 6, 7]
            elif variant_id == 2:
                text = "Рядом с лампой книга лежит на столе"
                is_correct = 1
                word_positions = [5, 6, 7, 1, 2, 3, 4]
            elif variant_id == 3:
                text = "На столе книга лежит рядом с лампой"
                is_correct = 1
                word_positions = [3, 4, 1, 2, 5, 6, 7]
            elif variant_id == 4:
                text = "Лежит книга лампой с рядом столе на"
                is_correct = 0
                word_positions = [2, 1, 7, 6, 5, 4, 3]

        elif sentence_id == 13:
            if variant_id == 1:
                text = "Ветер гонит тучи над городом"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "Над городом ветер гонит тучи"
                is_correct = 1
                word_positions = [4, 5, 1, 2, 3]
            elif variant_id == 3:
                text = "Тучи ветер гонит над городом"
                is_correct = 1
                word_positions = [3, 1, 2, 4, 5]
            elif variant_id == 4:
                text = "Гонит городом над тучи ветер"
                is_correct = 0
                word_positions = [2, 5, 4, 3, 1]

        elif sentence_id == 14:
            if variant_id == 1:
                text = "Папа чинит машину в гараже"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "В гараже папа чинит машину"
                is_correct = 1
                word_positions = [4, 5, 1, 2, 3]
            elif variant_id == 3:
                text = "Машину папа чинит в гараже"
                is_correct = 1
                word_positions = [3, 1, 2, 4, 5]
            elif variant_id == 4:
                text = "Чинит папа гараже в машину"
                is_correct = 0
                word_positions = [2, 1, 5, 4, 3]

        elif sentence_id == 15:
            if variant_id == 1:
                text = "Луна светит ярко в ночном небе"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5, 6]
            elif variant_id == 2:
                text = "В ночном небе луна светит ярко"
                is_correct = 1
                word_positions = [4, 5, 6, 1, 2, 3]
            elif variant_id == 3:
                text = "Ярко светит луна в ночном небе"
                is_correct = 1
                word_positions = [3, 2, 1, 4, 5, 6]
            elif variant_id == 4:
                text = "Светит луна ночном в ярко небе"
                is_correct = 0
                word_positions = [2, 1, 5, 4, 3, 6]

        elif sentence_id == 16:
            if variant_id == 1:
                text = "Ученики решают задачи у доски"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "У доски ученики решают задачи"
                is_correct = 1
                word_positions = [4, 5, 1, 2, 3]
            elif variant_id == 3:
                text = "Задачи ученики решают у доски"
                is_correct = 1
                word_positions = [3, 1, 2, 4, 5]
            elif variant_id == 4:
                text = "Решают ученики доски у задачи"
                is_correct = 0
                word_positions = [2, 1, 5, 4, 3]

        elif sentence_id == 17:
            if variant_id == 1:
                text = "Река течёт быстро после дождя"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "После дождя река течёт быстро"
                is_correct = 1
                word_positions = [4, 5, 1, 2, 3]
            elif variant_id == 3:
                text = "Быстро течёт река после дождя"
                is_correct = 1
                word_positions = [3, 2, 1, 4, 5]
            elif variant_id == 4:
                text = "Течёт дождя после река быстро"
                is_correct = 0
                word_positions = [2, 5, 4, 1, 3]

        elif sentence_id == 18:
            if variant_id == 1:
                text = "Бабушка вяжет шарф для внучки"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "Для внучки бабушка вяжет шарф"
                is_correct = 1
                word_positions = [4, 5, 1, 2, 3]
            elif variant_id == 3:
                text = "Шарф бабушка вяжет для внучки"
                is_correct = 1
                word_positions = [3, 1, 2, 4, 5]
            elif variant_id == 4:
                text = "Вяжет бабушка внучки для шарф"
                is_correct = 0
                word_positions = [2, 1, 5, 4, 3]

        elif sentence_id == 19:
            if variant_id == 1:
                text = "Самолёт взлетает с взлётной полосы"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "С взлётной полосы самолёт взлетает"
                is_correct = 1
                word_positions = [3, 4, 5, 1, 2]
            elif variant_id == 3:
                text = "Взлетает самолёт с взлётной полосы"
                is_correct = 1
                word_positions = [2, 1, 3, 4, 5]
            elif variant_id == 4:
                text = "Взлётной самолёт с полосы взлетает"
                is_correct = 0
                word_positions = [4, 1, 3, 5, 2]

        elif sentence_id == 20:
            if variant_id == 1:
                text = "Фотограф снимает закат на море"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "На море фотограф снимает закат"
                is_correct = 1
                word_positions = [4, 5, 1, 2, 3]
            elif variant_id == 3:
                text = "Закат фотограф снимает на море"
                is_correct = 1
                word_positions = [3, 1, 2, 4, 5]
            elif variant_id == 4:
                text = "Снимает море на фотограф закат"
                is_correct = 0
                word_positions = [2, 5, 4, 1, 3]

        elif sentence_id == 21:
            if variant_id == 1:
                text = "Повар готовит соус по новому рецепту"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5, 6]
            elif variant_id == 2:
                text = "По новому рецепту повар готовит соус"
                is_correct = 1
                word_positions = [4, 5, 6, 1, 2, 3]
            elif variant_id == 3:
                text = "Соус повар готовит по новому рецепту"
                is_correct = 1
                word_positions = [3, 1, 2, 4, 5, 6]
            elif variant_id == 4:
                text = "Готовит повар рецепту новому по соус"
                is_correct = 0
                word_positions = [2, 1, 6, 5, 4, 3]

        elif sentence_id == 22:
            if variant_id == 1:
                text = "Врач назначает лекарство пациенту"
                is_correct = 1
                word_positions = [1, 2, 3, 4]
            elif variant_id == 2:
                text = "Пациенту врач назначает лекарство"
                is_correct = 1
                word_positions = [4, 1, 2, 3]
            elif variant_id == 3:
                text = "Лекарство врач назначает пациенту"
                is_correct = 1
                word_positions = [3, 1, 2, 4]
            elif variant_id == 4:
                text = "Назначает пациенту врач лекарство"
                is_correct = 0
                word_positions = [2, 4, 1, 3]

        elif sentence_id == 23:
            if variant_id == 1:
                text = "Спортсмен бежит по беговой дорожке"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "По беговой дорожке спортсмен бежит"
                is_correct = 1
                word_positions = [3, 4, 5, 1, 2]
            elif variant_id == 3:
                text = "Бежит спортсмен по беговой дорожке"
                is_correct = 1
                word_positions = [2, 1, 3, 4, 5]
            elif variant_id == 4:
                text = "Беговой спортсмен по дорожке бежит"
                is_correct = 0
                word_positions = [4, 1, 3, 5, 2]

        elif sentence_id == 24:
            if variant_id == 1:
                text = "Птицы улетают на юг осенью"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "Осенью птицы улетают на юг"
                is_correct = 1
                word_positions = [5, 1, 2, 3, 4]
            elif variant_id == 3:
                text = "На юг птицы улетают осенью"
                is_correct = 1
                word_positions = [3, 4, 1, 2, 5]
            elif variant_id == 4:
                text = "Улетают осенью юг на птицы"
                is_correct = 0
                word_positions = [2, 5, 4, 3, 1]

        elif sentence_id == 25:
            if variant_id == 1:
                text = "Официант подаёт кофе с молоком"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5]
            elif variant_id == 2:
                text = "С молоком официант подаёт кофе"
                is_correct = 1
                word_positions = [4, 5, 1, 2, 3]
            elif variant_id == 3:
                text = "Кофе официант подаёт с молоком"
                is_correct = 1
                word_positions = [3, 1, 2, 4, 5]
            elif variant_id == 4:
                text = "Подаёт официант молоком с кофе"
                is_correct = 0
                word_positions = [2, 1, 5, 4, 3]

        elif sentence_id == 26:
            if variant_id == 1:
                text = "Зимой дети лепят снеговика во дворе"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5, 6]
            elif variant_id == 2:
                text = "Во дворе зимой дети лепят снеговика"
                is_correct = 1
                word_positions = [5, 6, 1, 2, 3, 4]
            elif variant_id == 3:
                text = "Снеговика зимой дети лепят во дворе"
                is_correct = 1
                word_positions = [4, 1, 2, 3, 5, 6]
            elif variant_id == 4:
                text = "Лепят зимой дети двор во снеговика"
                is_correct = 0
                word_positions = [3, 1, 2, 6, 5, 4]

        elif sentence_id == 27:
            if variant_id == 1:
                text = "Музыкант играет на скрипке в оркестре"
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5, 6]
            elif variant_id == 2:
                text = "В оркестре музыкант играет на скрипке"
                is_correct = 1
                word_positions = [5, 6, 1, 2, 3, 4]
            elif variant_id == 3:
                text = "На скрипке музыкант играет в оркестре"
                is_correct = 1
                word_positions = [3, 4, 1, 2, 5, 6]
            elif variant_id == 4:
                text = "Играет музыкант оркестре в на скрипке"
                is_correct = 0
                word_positions = [2, 1, 6, 5, 3, 4]

        elif sentence_id == 28:
            if variant_id == 1:
                text = "Рыбаки ловят рыбу в озере на рассвете."
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5, 6, 7]
            elif variant_id == 2:
                text = "На рассвете рыбаки ловят рыбу в озере."
                is_correct = 1
                word_positions = [6, 7, 1, 2, 3, 4, 5]
            elif variant_id == 3:
                text = "В озере рыбаки ловят рыбу на рассвете."
                is_correct = 1
                word_positions = [4, 5, 1, 2, 3, 6, 7]
            elif variant_id == 4:
                text = "Ловят рыбаки рассвете на в озере рыбу."
                is_correct = 0
                word_positions = [2, 1, 7, 6, 4, 5, 3]

        elif sentence_id == 29:
            if variant_id == 1:
                text = "Художник рисует портрет маслом на холсте."
                is_correct = 1
                word_positions = [1, 2, 3, 4, 5, 6]
            elif variant_id == 2:
                text = "На холсте художник рисует портрет маслом."
                is_correct = 1
                word_positions = [5, 6, 1, 2, 3, 4]
            elif variant_id == 3:
                text = "Маслом художник рисует портрет на холсте."
                is_correct = 1
                word_positions = [4, 1, 2, 3, 5, 6]
            elif variant_id == 4:
                text = "Рисует портрет холсте на художник маслом."
                is_correct = 0
                word_positions = [2, 3, 6, 5, 1, 4]

            elif sentence_id == 30:
                if variant_id == 1:
                    text = "Птицы строят гнёзда на высоких деревьях."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5, 6]
                elif variant_id == 2:
                    text = "На высоких деревьях птицы строят гнёзда."
                    is_correct = 1
                    word_positions = [4, 5, 6, 1, 2, 3]
                elif variant_id == 3:
                    text = "Гнёзда птицы строят на высоких деревьях."
                    is_correct = 1
                    word_positions = [3, 1, 2, 4, 5, 6]
                elif variant_id == 4:
                    text = "Строят деревьях высоких на птицы гнёзда."
                    is_correct = 0
                    word_positions = [2, 6, 5, 4, 1, 3]

            elif sentence_id == 31:
                if variant_id == 1:
                    text = "Повар режет овощи острым ножом."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5]
                elif variant_id == 2:
                    text = "Острым ножом повар режет овощи."
                    is_correct = 1
                    word_positions = [4, 5, 1, 2, 3]
                elif variant_id == 3:
                    text = "Овощи повар режет острым ножом."
                    is_correct = 1
                    word_positions = [3, 1, 2, 4, 5]
                elif variant_id == 4:
                    text = "Режет повар ножом острым овощи."
                    is_correct = 0
                    word_positions = [2, 1, 5, 4, 3]

            elif sentence_id == 32:
                if variant_id == 1:
                    text = "Собака лает на почтальона у ворот."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5, 6]
                elif variant_id == 2:
                    text = "У ворот собака лает на почтальона."
                    is_correct = 1
                    word_positions = [5, 6, 1, 2, 3, 4]
                elif variant_id == 3:
                    text = "На почтальона собака лает у ворот."
                    is_correct = 1
                    word_positions = [3, 4, 1, 2, 5, 6]
                elif variant_id == 4:
                    text = "Лает собака ворот у на почтальона."
                    is_correct = 0
                    word_positions = [2, 1, 6, 5, 3, 4]

            elif sentence_id == 33:
                if variant_id == 1:
                    text = "Учитель объясняет задачу у доски."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5]
                elif variant_id == 2:
                    text = "У доски учитель объясняет задачу."
                    is_correct = 1
                    word_positions = [4, 5, 1, 2, 3]
                elif variant_id == 3:
                    text = "Задачу учитель объясняет у доски."
                    is_correct = 1
                    word_positions = [3, 1, 2, 4, 5]
                elif variant_id == 4:
                    text = "Объясняет учитель доски у задачу."
                    is_correct = 0
                    word_positions = [2, 1, 5, 4, 3]

            elif sentence_id == 34:
                if variant_id == 1:
                    text = "Дети собирают грибы в осеннем лесу."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5, 6]
                elif variant_id == 2:
                    text = "В осеннем лесу дети собирают грибы."
                    is_correct = 1
                    word_positions = [4, 5, 6, 1, 2, 3]
                elif variant_id == 3:
                    text = "Грибы дети собирают в осеннем лесу."
                    is_correct = 1
                    word_positions = [3, 1, 2, 4, 5, 6]
                elif variant_id == 4:
                    text = "Собирают дети лесу осеннем в грибы."
                    is_correct = 0
                    word_positions = [2, 1, 6, 5, 4, 3]

            elif sentence_id == 35:
                if variant_id == 1:
                    text = "Птица клюёт зёрна на подоконнике."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5]
                elif variant_id == 2:
                    text = "На подоконнике птица клюёт зёрна."
                    is_correct = 1
                    word_positions = [4, 5, 1, 2, 3]
                elif variant_id == 3:
                    text = "Зёрна птица клюёт на подоконнике."
                    is_correct = 1
                    word_positions = [3, 1, 2, 4, 5]
                elif variant_id == 4:
                    text = "Клюёт подоконнике на птица зёрна."
                    is_correct = 0
                    word_positions = [2, 5, 4, 1, 3]

            elif sentence_id == 36:
                if variant_id == 1:
                    text = "Автобус едет в аэропорт через центр."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5, 6]
                elif variant_id == 2:
                    text = "Через центр автобус едет в аэропорт."
                    is_correct = 1
                    word_positions = [5, 6, 1, 2, 3, 4]
                elif variant_id == 3:
                    text = "В аэропорт автобус едет через центр."
                    is_correct = 1
                    word_positions = [3, 4, 1, 2, 5, 6]
                elif variant_id == 4:
                    text = "Едет автобус центр через в аэропорт."
                    is_correct = 0
                    word_positions = [2, 1, 6, 5, 3, 4]

            elif sentence_id == 37:
                if variant_id == 1:
                    text = "Девочка кормит голубей в парке."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5]
                elif variant_id == 2:
                    text = "В парке девочка кормит голубей."
                    is_correct = 1
                    word_positions = [4, 5, 1, 2, 3]
                elif variant_id == 3:
                    text = "Голубей девочка кормит в парке."
                    is_correct = 1
                    word_positions = [3, 1, 2, 4, 5]
                elif variant_id == 4:
                    text = "Кормит девочка парке в голубей."
                    is_correct = 0
                    word_positions = [2, 1, 5, 4, 3]

            elif sentence_id == 38:
                if variant_id == 1:
                    text = "Мальчик катается на велосипеде по тропинке."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5, 6]
                elif variant_id == 2:
                    text = "По тропинке мальчик катается на велосипеде."
                    is_correct = 1
                    word_positions = [5, 6, 1, 2, 3, 4]
                elif variant_id == 3:
                    text = "На велосипеде мальчик катается по тропинке."
                    is_correct = 1
                    word_positions = [3, 4, 1, 2, 5, 6]
                elif variant_id == 4:
                    text = "Катается мальчик тропинке по на велосипеде."
                    is_correct = 0
                    word_positions = [2, 1, 6, 5, 3, 4]

            elif sentence_id == 39:
                if variant_id == 1:
                    text = "Солнце садится за горизонт вечером."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5]
                elif variant_id == 2:
                    text = "Вечером солнце садится за горизонт."
                    is_correct = 1
                    word_positions = [5, 1, 2, 3, 4]
                elif variant_id == 3:
                    text = "За горизонт солнце садится вечером."
                    is_correct = 1
                    word_positions = [3, 4, 1, 2, 5]
                elif variant_id == 4:
                    text = "Садится солнце вечером горизонт за."
                    is_correct = 0
                    word_positions = [2, 1, 5, 4, 3]

            elif sentence_id == 40:
                if variant_id == 1:
                    text = "Повар добавляет специи в суп."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5]
                elif variant_id == 2:
                    text = "В суп повар добавляет специи."
                    is_correct = 1
                    word_positions = [4, 5, 1, 2, 3]
                elif variant_id == 3:
                    text = "Специи повар добавляет в суп."
                    is_correct = 1
                    word_positions = [3, 1, 2, 4, 5]
                elif variant_id == 4:
                    text = "Добавляет повар суп в специи."
                    is_correct = 0
                    word_positions = [2, 1, 5, 4, 3]

            elif sentence_id == 41:
                if variant_id == 1:
                    text = "Паук плетёт паутину в углу комнаты."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5, 6]
                elif variant_id == 2:
                    text = "В углу комнаты паук плетёт паутину."
                    is_correct = 1
                    word_positions = [4, 5, 6, 1, 2, 3]
                elif variant_id == 3:
                    text = "Паутину паук плетёт в углу комнаты."
                    is_correct = 1
                    word_positions = [3, 1, 2, 4, 5, 6]
                elif variant_id == 4:
                    text = "Плетёт паук комнаты углу в паутину."
                    is_correct = 0
                    word_positions = [2, 1, 6, 5, 4, 3]

            elif sentence_id == 42:
                if variant_id == 1:
                    text = "Лошадь скачет по полю на закате."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5, 6]
                elif variant_id == 2:
                    text = "На закате лошадь скачет по полю."
                    is_correct = 1
                    word_positions = [5, 6, 1, 2, 3, 4]
                elif variant_id == 3:
                    text = "По полю лошадь скачет на закате."
                    is_correct = 1
                    word_positions = [3, 4, 1, 2, 5, 6]
                elif variant_id == 4:
                    text = "Скачет лошадь закате на по полю."
                    is_correct = 0
                    word_positions = [2, 1, 6, 5, 3, 4]

            elif sentence_id == 43:
                if variant_id == 1:
                    text = "Турист фотографирует водопад в горах."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5]
                elif variant_id == 2:
                    text = "В горах турист фотографирует водопад."
                    is_correct = 1
                    word_positions = [4, 5, 1, 2, 3]
                elif variant_id == 3:
                    text = "Водопад турист фотографирует в горах."
                    is_correct = 1
                    word_positions = [3, 1, 2, 4, 5]
                elif variant_id == 4:
                    text = "Фотографирует турист горах в водопад."
                    is_correct = 0
                    word_positions = [2, 1, 5, 4, 3]

            elif sentence_id == 44:
                if variant_id == 1:
                    text = "Пчёлы собирают нектар с цветов."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5]
                elif variant_id == 2:
                    text = "С цветов пчёлы собирают нектар."
                    is_correct = 1
                    word_positions = [4, 5, 1, 2, 3]
                elif variant_id == 3:
                    text = "Нектар пчёлы собирают с цветов."
                    is_correct = 1
                    word_positions = [3, 1, 2, 4, 5]
                elif variant_id == 4:
                    text = "Собирают пчёлы цветов с нектар."
                    is_correct = 0
                    word_positions = [2, 1, 5, 4, 3]

            elif sentence_id == 45:
                if variant_id == 1:
                    text = "Кошка спит на диване под пледом."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5, 6]
                elif variant_id == 2:
                    text = "Под пледом кошка спит на диване."
                    is_correct = 1
                    word_positions = [5, 6, 1, 2, 3, 4]
                elif variant_id == 3:
                    text = "На диване кошка спит под пледом."
                    is_correct = 1
                    word_positions = [3, 4, 1, 2, 5, 6]
                elif variant_id == 4:
                    text = "Спит кошка пледом под на диване."
                    is_correct = 0
                    word_positions = [2, 1, 6, 5, 3, 4]

            elif sentence_id == 46:
                if variant_id == 1:
                    text = "Учитель объясняет новую тему у доски."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5, 6]
                elif variant_id == 2:
                    text = "У доски учитель объясняет новую тему."
                    is_correct = 1
                    word_positions = [5, 6, 1, 2, 3, 4]
                elif variant_id == 3:
                    text = "Новую тему учитель объясняет у доски."
                    is_correct = 1
                    word_positions = [3, 4, 1, 2, 5, 6]
                elif variant_id == 4:
                    text = "Объясняет учитель доски у тему новую."
                    is_correct = 0
                    word_positions = [2, 1, 6, 5, 4, 3]

            elif sentence_id == 47:
                if variant_id == 1:
                    text = "Повар жарит рыбу на сковороде."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5]
                elif variant_id == 2:
                    text = "На сковороде повар жарит рыбу."
                    is_correct = 1
                    word_positions = [4, 5, 1, 2, 3]
                elif variant_id == 3:
                    text = "Рыбу повар жарит на сковороде."
                    is_correct = 1
                    word_positions = [3, 1, 2, 4, 5]
                elif variant_id == 4:
                    text = "Жарит повар сковороде на рыбу."
                    is_correct = 0
                    word_positions = [2, 1, 5, 4, 3]

            elif sentence_id == 48:
                if variant_id == 1:
                    text = "Дети играют в песочнице во дворе."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5, 6]
                elif variant_id == 2:
                    text = "Во дворе дети играют в песочнице."
                    is_correct = 1
                    word_positions = [5, 6, 1, 2, 3, 4]
                elif variant_id == 3:
                    text = "В песочнице дети играют во дворе."
                    is_correct = 1
                    word_positions = [3, 4, 1, 2, 5, 6]
                elif variant_id == 4:
                    text = "Играют дети дворе во в песочнице."
                    is_correct = 0
                    word_positions = [2, 1, 6, 5, 3, 4]

            elif sentence_id == 49:
                if variant_id == 1:
                    text = "Автомобиль едет по шоссе в горах."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5, 6]
                elif variant_id == 2:
                    text = "В горах автомобиль едет по шоссе."
                    is_correct = 1
                    word_positions = [5, 6, 1, 2, 3, 4]
                elif variant_id == 3:
                    text = "По шоссе автомобиль едет в горах."
                    is_correct = 1
                    word_positions = [3, 4, 1, 2, 5, 6]
                elif variant_id == 4:
                    text = "Едет автомобиль горах в по шоссе."
                    is_correct = 0
                    word_positions = [2, 1, 6, 5, 3, 4]

            elif sentence_id == 50:
                if variant_id == 1:
                    text = "Дедушка читает газету на веранде."
                    is_correct = 1
                    word_positions = [1, 2, 3, 4, 5]
                elif variant_id == 2:
                    text = "На веранде дедушка читает газету."
                    is_correct = 1
                    word_positions = [4, 5, 1, 2, 3]
                elif variant_id == 3:
                    text = "Газету дедушка читает на веранде."
                    is_correct = 1
                    word_positions = [3, 1, 2, 4, 5]
                elif variant_id == 4:
                    text = "Читает дедушка веранде на газету."
                    is_correct = 0
                    word_positions = [2, 1, 5, 4, 3]

        metadata.append({
            "audio_path": os.path.join(audio_dir, file_name),
            "text": text,
            "is_correct": is_correct,
            "word_positions": word_positions
        })

df = pd.DataFrame(metadata)

output_path = os.path.join("..", "data", "metadata.csv")
df.to_csv(output_path, index=False, encoding="utf-8")

print(f"Метаданные сохранены в {output_path}")