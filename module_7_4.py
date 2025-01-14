if __name__ == '__main__':
  team1_num = 5 #Команда Мастера кода
  team2_num = 6 #Команда Волшебники данных
  score_1 = 40  #количество решённых задач team1_num
  score_2 = 42  #количество решённых задач team2_num
  team1_time = 1552.512 #время за которое команда 2 решила задачи
  team2_time = 2153.31451   #время за которое команда 2 решила задачи
  tasks_total = ""  #количество задач
  time_avg = ""   #среднее время решения
  challenge_result = ""   #исход соревнования

# Определение результата challenge_result
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = "Победа команды Мастера кода!"
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = "Победа команды Волшебники Данных!"
else:
    challenge_result = "Ничья!"
    
# Определение результата tasks_total
tasks_total = score_1 + score_2

# Определение результата time_avg
time_avg = round((team1_time + team2_time) / tasks_total, 2)

"""
Использование %
"""
print("В команде Мастера кода участников: %s !" % team1_num)
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

"""
Использование format()
"""
print("Команда Волшебники данных решила задач: {} !".format(score_2))
print("Волшебники данных решили задачи за {} с !".format(team1_time))

"""
Использование f-строк
"""
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")