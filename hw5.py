# Задача Иосифа Флавия
# https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B4%D0%B0%D1%87%D0%B0_%D0%98%D0%BE%D1%81%D0%B8%D1%84%D0%B0_%D0%A4%D0%BB%D0%B0%D0%B2%D0%B8%D1%8F
# Задача заключается в следующем: по кругу стоит num_people воинов,
# начиная с первого воина они выводят из круга каждого kill_num по счёту.
# Вы должны правильно указать, кто является «выжившим», то есть: последний элемент списка.
#
# num_people=7, kill_num=3 => Значит 7 человек в кругу и каждый третий из него выходит
# [1,2,3,4,5,6,7] - начальный круг
# [1,2,4,5,6,7] => 3 вышел
# [1,2,4,5,7] => 6 вышел
# [1,4,5,7] => 2 вышел
# [1,4,5] => 7 вышел
# [1,4] => 5 вышел
# [4] => 1 вышел, 4 остался последним т.е. выжившим - это наш ответ survivor.

def josephus_task(num_people, kill_num):
    current_index = 0
    survivor = [i for i in range(1, num_people + 1)]
    while len(survivor) != 1:
        current_index = (current_index + kill_num - 1) % len(survivor)
        killed = survivor.pop(current_index)
        print(killed)
    return survivor


# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ

