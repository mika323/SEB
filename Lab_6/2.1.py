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
get_stats(all_users, all_workouts)

