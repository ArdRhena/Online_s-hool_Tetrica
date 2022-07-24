data = {
        'lesson': [1594663200, 1594666800],
        'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
        'tutor': [1594663290, 1594663430, 1594663443, 1594666473]
        }


def time_event(intervals):
    all_time = {}                       # создаю словарь для объект: время;
    for key, value in data.items():     # при помощи итерации получаю ключ: значение;                                 
        ind_key = len(value)             # для дальнейшего цикла, считаю сколько элементов value;
        inp = []                        # создаю список для значений входа; 
        ex = []                         # создаю список для значений выхода;
        for i in range(ind_key):        # при помощи цикла, фильтрую значения на выход и вход,
            if i % 2 == 0:              # каждый чётный добавляю в список выхода, каждый нечётный в список входа
                inp.append(value[i])
            else:
                ex.append(value[i])
        result = sum(ex) - sum(inp)     # нахожу сумму для каждого списка и определяю общее время для объекта
        all_time[key] = result          # добавляю в словарь all_time объект: время
    return all_time                     # возвращаю словарь в вызов функции


print(time_event(data))


# дописав функцию я понял, что нужно было получить время одновременного присутствия учителя и ученика на уроке...
# попробую реализовать это через интервалы и сравнения их, время конечно уже вышло, но всё же.
# код я нашёл, потому что мой выдавал ошибку во втором тесте, и я не смог пофиксить её, так же использовал 
# range но изза того что в тесте идут пересечения учеников, мой код выдавал 92 секунды.
# я разобрался как в этом коде, и могу объяснить как он работает.

def appearance(intervals):
    def in_intervals(i:int, intervals) -> bool:
        k = 0
        while k < len(intervals):
            if i in range(intervals[k], intervals[k+1]) and i <= intervals[k+1]:
                return True
            else: 
                k += 2
        
        return False

    full_range = range(
        min(intervals['lesson'][0], intervals['pupil'][0], intervals['tutor'][0]),
        max(intervals['lesson'][-1], intervals['pupil'][-1], intervals['tutor'][-1]) + 1
    )
    time = 0
    diagram = {}
    for i in full_range:
        diagram[i] = []
        if in_intervals(i, intervals['lesson']):
            diagram[i].append('l')
        if in_intervals(i, intervals['pupil']):
            diagram[i].append('p')
        if in_intervals(i, intervals['tutor']):
            diagram[i].append('t')
        
        if len(diagram[i]) == 3:
            time += 1

    return time


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
