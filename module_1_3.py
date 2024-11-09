from ctypes import pythonapi

name = 'Aleksandr'
print(name)
age = 33
print(age)
new_age = '33'
print(new_age)
is_student = True
print(is_student)
print('Name: '+ name)
print('Age: ' + str (age))
print('New age: '+ new_age)
print('Is Student: ' + str (is_student))


homework = 12
spent_time = 1.5
course_name = 'Python'
time_for_one_task = (spent_time/homework)

print('Курс: '+ course_name+', всего задач: '+str (homework)+', затрачено часов: '+ str(spent_time)+', среднее время выполнения '+str(time_for_one_task)+' часа.')
