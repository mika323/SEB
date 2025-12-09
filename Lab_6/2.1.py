import xml.etree.ElementTree as ET
def load_users_data():
    try:
        users_tree = ET.parse('users.xml')
        users = []
        for user_elem in users_tree.getroot().findall('user'):
            user = {
                'user_id': int(user_elem.find('user_id').text),
                'name': user_elem.find('name').text,
                'age': int(user_elem.find('age').text),
                'weight': int(user_elem.find('weight').text),
                'fitness_level': user_elem.find('fitness_level').text,
                'workouts': []
            }
            users.append(user)
        return users
    except FileNotFoundError:
        print("Файл не найден")

        return []

def  load_workouts_data():
    try:
        workouts_tree = ET.parse('workouts.xml')
        workouts = []
        for workout_elem in workouts_tree.getroot().findall('workout'):
            workout = {
                'workout_id': int(workout_elem.find('workout_id').text),
                'user_id' : int(workout_elem.find('user_id').text),
                'date': workout_elem.find('date').text,
                'type': workout_elem.find('type').text,
                'duration': int(workout_elem.find('duration').text),
                'distance': float(workout_elem.find('distance').text),
                'calories': int(workout_elem.find('calories').text),
                'avg_heart': int(workout_elem.find('avg_heart').text),
                'intensity': workout_elem.find('intensity').text
            }
            workouts.append(workout)
        return workouts
    except FileNotFoundError:
        print("Файл не найден")
        return []

def get_stats(users, workouts):
    count_users = len(users)
    count_workouts = len(workouts)
    total_calories = sum(workout['calories'] for workout in workouts)
    total_time = sum(workout['duration'] for workout in workouts) / 60
    total_distance = sum(workout['distance'] for workout in workouts)
    print('ОБЩАЯ СТАТИСТИКА')
    print('===========================')
    print(f'Всего тренировок: {count_workouts}')
    print(f'Всего пользователей: {count_users}')
    print(f'Сожжено калорий: {total_calories}')
    print(f'Общее время: {total_time:.1f} часов')
    print(f'Пройдено дистанции: {total_distance} км')

all_users = load_users_data()
all_workouts = load_workouts_data()

def analyze_user_activity(users):
    workouts_by_user_id = {}
    for workout in all_workouts:
        user_id = workout['user_id']
        if user_id not in workouts_by_user_id:
            workouts_by_user_id[user_id] = []
        workouts_by_user_id[user_id].append(workout)

    for user in users:
        user_id = user['user_id']
        user_workouts = workouts_by_user_id.get(user_id, [])
        user['workouts'] = user_workouts
    user_summary_stats = []

    for user in users:
        user_workouts = user['workouts']
        num_workouts = len(user_workouts)
        total_calories = sum(w['calories'] for w in user_workouts)
        total_duration_hours = sum(w['duration'] for w in user_workouts) / 60
        user_summary_stats.append({
            'user_id': user['user_id'],
            'name': user['name'],
            'fitness_level': user['fitness_level'],
            'num_workouts': num_workouts,
            'total_calories': total_calories,
            'total_duration_hours': total_duration_hours
        })

    sorted_users = sorted(
        user_summary_stats,
        key=lambda x: (x['num_workouts'], x['total_calories']),
        reverse=True
    )
    print('\nТОП-3 АКТИВНЫХ ПОЛЬЗОВАТЕЛЕЙ:')
    for i, u_stats in enumerate(sorted_users[:3]):
        print(f"{i + 1}. {u_stats['name']} ({u_stats['fitness_level']}):")
        print(f"   Тренировок: {u_stats['num_workouts']}")
        print(f"   Калорий: {u_stats['total_calories']}")
        print(f"   Время: {u_stats['total_duration_hours']:.1f} часов\n")

def analyze_workout_types(workouts):
    type_stats = {}
    total_workouts = len(workouts)
    for workout in workouts:
        workout_type = workout['type']
        duration = workout.get('duration', 0)
        calories = workout.get('calories', 0)

        if workout_type in type_stats:
            type_stats[workout_type]['count'] += 1
            type_stats[workout_type]['duration_sum'] += duration
            type_stats[workout_type]['calories_sum'] += calories
        else:
            type_stats[workout_type] = {
                'count': 1,
                'duration_sum': duration,
                'calories_sum': calories
            }

    print('РАСПРЕДЕЛЕНИЕ ПО ТИПАМ ТРЕНИРОВОК:')
    for key, stats in type_stats.items():
        key = key.capitalize()
        print(f'{key}: {stats['count']} тренировок({stats['count']/total_workouts * 100:.1f}%)')
        print(f' Средняя длительность: {stats['duration_sum'] / stats['count']:.0f} мин')
        print(f' Средняя длительность: {stats['calories_sum'] / stats['count']:.0f} ккал')

def find_user_workouts(users, user_name):
    for user in users:
        if user['name'] == user_name:
            return user['workouts']
    return []

def analyze_user(user):
    user_workouts = find_user_workouts(all_users, user)
    count_workouts = len(user_workouts)

    print(f'\nДЕТАЛЬНЫЙ АНАЛИЗ ДЛЯ ПОЛЬЗОВАТЕЛЯ: {user}')
    print(f'===========================================')

    if count_workouts > 0:
        total_calories = sum(workout['calories'] for workout in user_workouts)
        total_time = sum(workout['duration'] for workout in user_workouts) / 60
        total_distance = sum(workout['distance'] for workout in user_workouts)
        avg_calories = total_calories / count_workouts

        types = {}
        for workout in user_workouts:
            tip = workout['type']
            types[tip] = types.get(tip, 0) + 1
        favorite_workout = max(types, key=types.get)

        user_found = False
        for u in all_users:
            if user == u['name']:
                print(f'Возраст: {u["age"]} лет, Вес: {u["weight"]} кг')
                print(f'Уровень: {u["fitness_level"]}')
                user_found = True
                break

        if user_found:
            print(f'Тренировок: {count_workouts}')
            print(f'Сожжено калорий: {total_calories}')
            print(f'Общее время: {total_time:.1f} часов')
            print(f'Пройдено дистанции: {total_distance:.1f} км')
            print(f'Средние калории за тренировку: {avg_calories:.0f}')
            print(f'Любимый тип тренировки: {favorite_workout}')
        else:
            print('Пользователь не найден.')
    else:
        print(f'У пользователя {user} нет тренировок.')

def circle(workouts):
    count_run = 0
    count_strength = 0
    count_bike = 0
    count_swim = 0
    count_walk = 0

    for workout in workouts:
        if workout['type'] == 'бег':
            count_run += 1
        elif workout['type'] == 'силовая тренировка':
            count_strength += 1
        elif workout['type'] == 'велосипед':
            count_bike += 1
        elif workout['type'] == 'плавание':
            count_swim += 1
        else:
            count_walk += 1

    y = np.array(
        [(count_run / len(workouts) * 100),
         (count_strength / len(workouts) * 100),
         (count_bike / len(workouts) * 100),
         (count_swim / len(workouts) * 100),
         (count_walk / len(workouts) * 100)]
    )
    my_labels = ["бег", "силовая тренировка", "велосипед", "плавание", "ходьба"]
    plt.pie(y,
            labels=my_labels,
            startangle=90,
            autopct='%1.1f%%',
            textprops={'fontsize': 6})
    plt.title('Распределение типов тренировок', fontweight='bold')

    plt.show()


def users_activity(users):
    users_inf = {}

    for user in users:
        if user['name'] not in users_inf:
            users_inf[user['name']] = len(user['workouts'])
        else:
            users_inf[user['name']] += len(user['workouts'])

    sorted_activity = sorted(users_inf.items(), key=lambda x: x[1], reverse=True)
    names = [u[0] for u in sorted_activity]
    activity = [u[1] for u in sorted_activity]

    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(names, activity, color='lightblue')
    ax.set_title('Активность пользователей (количество тренировок)', fontweight='bold', fontsize=10, pad=10)
    ax.set_xlabel('Пользователи', fontsize=10)
    ax.set_ylabel('Количество тренировок', fontsize=10)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2,
                height + 0.3,
                f'{int(height)}',
                ha='center', va='bottom',
                fontsize=10)

    plt.xticks(rotation=45, ha='right',
               fontsize=10)

    ax.set_ylim(0, max(activity) + 1.5)

    fig.patch.set_edgecolor('lightblue')
    fig.patch.set_linewidth(2)

    plt.tight_layout()
    plt.show()


def effectiveness_of_training(workouts):
    workout_inf = {}
    for workout in workouts:
        if workout['type'] not in workout_inf:
            workout_inf[workout['type']] = [workout['duration'], workout['calories']]
        else:
            workout_inf[workout['type']][0] += workout['duration']
            workout_inf[workout['type']][1] += workout['calories']
 
    sorted_activity = sorted(workout_inf.items(), key=lambda x: x[1][1] / x[1][0], reverse=True)

    workout_types = [w[0] for w in sorted_activity]
    calories_per_minute = [w[1][1] / w[1][0] for w in sorted_activity]

    fig, ax = plt.subplots(figsize=(8 , 5))
    bars = ax.bar(workout_types, calories_per_minute, color = 'purple' )
    ax.set_title('Эффективность тренировок (калории/минуту)', fontweight = 'bold', fontsize=10)
    ax.set_xlabel('Тип тренировки', fontsize=10)
    ax.set_ylabel('Калории в минуту', fontsize=10)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2,
                height + 0.05,
                f'{height:.2f}',
                ha = 'center', va = 'bottom',
                fontsize = 10)

    ax.set_ylim(0, max(calories_per_minute) + 0.7)

    plt.xticks(rotation = 45, ha = 'right')

    fig.patch.set_edgecolor('lightblue')
    fig.patch.set_linewidth(2)

    plt.tight_layout()
    plt.show()


def pillar_users_calories(users):
    stat = {}
    for user in users:
        if user['name'] not in stat:
            user_calories = 0
            for workout in user['workouts']:
                user_calories += workout['calories']
            stat[user['name']] = user['fitness_level'], user_calories
        else:
            existing_fitness_level, existing_calories = stat[user['name']]
            additional_calories = sum(workout['calories'] for workout in user['workouts'])
            stat[user['name']] = (existing_fitness_level, existing_calories + additional_calories)

    sorted_stat = sorted(stat.items(), key=lambda x: x[1][1], reverse=True)

    users = [u[0] for u in sorted_stat]
    levels = [u[1][0] for u in sorted_stat]
    u_calories = [u[1][1] for u in sorted_stat]

    level_colors = {
        'продвинутый': 'red',
        'средний': 'orange',
        'начальный': 'green'
    }

    colors_for_bars = [level_colors[level] for level in levels]

    fig, ax = plt.subplots(figsize=(12, 7))
    bars = ax.bar(users, u_calories, color=colors_for_bars)
    ax.set_title('Сравнение пользователей по общим затраченным калориям', fontweight = 'bold', fontsize=16, pad=10)
    ax.set_xlabel('Пользователи', fontsize=12)
    ax.set_ylabel('Общие калории', fontsize=12)

    plt.xticks(rotation=45, ha='right')

    fig.patch.set_edgecolor('lightblue')
    fig.patch.set_linewidth(2)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2,
                height + 100,
                f'{int(height)}',
                ha = 'center', va = 'bottom'
                )

    ax.set_ylim(0, max(u_calories) + 300)

    legend_handles = [plt.Rectangle((0, 0), 1, 1, color=level_colors[level]) for level in level_colors]
    legend_labels = list(level_colors.keys())
    ax.legend(legend_handles, legend_labels, loc='upper right', fontsize=10)

    plt.tight_layout()
    plt.show()






