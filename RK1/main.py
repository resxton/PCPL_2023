from operator import itemgetter

class Conductor:
    """Дирижер"""
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

class Orchestra:
    """Оркестр"""
    def __init__(self, id, name, conductor_id):
        self.id = id
        self.name = name
        self.conductor_id = conductor_id

class ConductorOrchestra:
    """
    'Дирижеры оркестра' для реализации связи многие-ко-многим
    """
    def __init__(self, conductor_id, orchestra_id):
        self.conductor_id = conductor_id
        self.orchestra_id = orchestra_id

conductors = [
    Conductor(1, 'John Smith', 5000),
    Conductor(2, 'Emily Johnson', 6000),
    Conductor(3, 'Michael Davis', 5500)
]

orchestras = [
    Orchestra(1, 'Symphony Orchestra', 1),
    Orchestra(2, 'Chamber Orchestra', 2),
    Orchestra(3, 'Philharmonic Orchestra', 3)
]

conductor_orchestras = [
    ConductorOrchestra(1, 1),
    ConductorOrchestra(2, 2),
    ConductorOrchestra(3, 3),
    ConductorOrchestra(1, 2),
    ConductorOrchestra(2, 1),
    ConductorOrchestra(3, 2),
]

def main():
    # Задание A1 (Соединение данных один-ко-многим)
    one_to_many = [(c.name, c.salary, o.name) for o in orchestras for c in conductors if o.conductor_id == c.id]

    print('Задание A1')
    res_A1 = sorted(one_to_many, key=itemgetter(2))
    print(res_A1)

    # Задание A2
    res_A2_unsorted = []
    for orchestra in orchestras:
        conductor_ids = [co.conductor_id for co in conductor_orchestras if co.orchestra_id == orchestra.id]
        total_salary = sum([c.salary for c in conductors if c.id in conductor_ids])
        res_A2_unsorted.append((orchestra.name, total_salary))

    res_A2 = sorted(res_A2_unsorted, key=itemgetter(1), reverse=True)  # Сортировка по убыванию суммарной зарплаты
    print('\nЗадание A2')
    print(res_A2)

    # Задание A3
    res_A3 = {}
    for orchestra in orchestras:
        if 'Symphony' in orchestra.name:
            conductor_ids = [co.conductor_id for co in conductor_orchestras if co.orchestra_id == orchestra.id]
            conductor_names = [c.name for c in conductors if c.id in conductor_ids]
            res_A3[orchestra.name] = conductor_names

    print('\nЗадание A3')
    print(res_A3)

if __name__ == '__main__':
    main()
