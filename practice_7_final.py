"""
Кейс-стаді — аналіз CSV-файлу

Ваше завдання — пройти весь шлях від порожньої папки до проєкту на GitHub:

1. Створити папку з проєктом
2. Завантажити туди дані
3. Зробити аналіз
4. Зберегти результат у .txt файл
5. Запушити все на GitHub
"""


# ============================================================
# Крок 1. Створіть папку з проєктом
# ============================================================
# У терміналі:
#
#   mkdir students_analysis
#   cd students_analysis
#
# Усі наступні файли мають лежати всередині цієї папки.


# ============================================================
# Крок 2. Завантажте туди дані
# ============================================================
# Скопіюйте файл students.csv у папку students_analysis.
# Формат файлу: name,math,python,english
# (перший рядок — заголовок, далі по одному студенту в рядку)
#
# Також збережіть цей скрипт у ту саму папку як analyze.py.


# ============================================================
# Крок 3. Зробіть аналіз
# ============================================================
# Потрібно порахувати:
#   - середній бал по класу з кожного предмета (math, python, english);
#   - ім'я студента з найвищим середнім балом (по трьох предметах).

INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

# TODO 1: відкрийте INPUT_FILE через with open(...) as f:
#   і пропустіть рядок заголовка (next(f))

with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    next(f)
    lines = f.readlines()


students = 0
sum_math = 0
sum_python = 0
sum_english = 0
best_student = ''
best_student_result = 0
for line in lines:
    students += 1
    line_strip = line.strip()
    line_split = line_strip.split(',')
    line_split[1] = int(line_split[1])
    line_split[2] = int(line_split[2])
    line_split[3] = int(line_split[3])
    sum_math += line_split[1]
    sum_python += line_split[2]
    sum_english += line_split[3]
    average_student = (line_split[1] + line_split[2] + line_split[3]) / 3
    if average_student > best_student_result:
        best_student_result = average_student
        best_student = line_split[0]
average_math = sum_math / students
average_python = sum_python / students
average_english = sum_english / students

print(f'Середній бал по класу:\nmath: {average_math:.1f}\npython: {average_python:.1f}\nenglish: {average_english:.1f}\n')
print(f'Найкращий студент: {best_student} ({best_student_result:.1f})\n')
with open(OUTPUT_FILE, 'w') as f:
    f.write(f'Середній бал по класу:\nmath: {average_math:.1f}\npython: {average_python:.1f}\nenglish: {average_english:.1f}\n')
    f.write(f'Найкращий студент: {best_student} ({best_student_result:.1f})\n')

# TODO 2: пройдіться по рядках файлу (for line in f:), для кожного рядка:
#   - приберіть символ переносу рядка (line.strip())
#   - розбийте рядок по комі (line.split(","))
#   - перетворіть оцінки на числа (int або float)

# TODO 3: по ходу циклу накопичуйте:
#   - суми оцінок з кожного предмета та кількість студентів
#   - найкращого студента (ім'я та його середній бал) — порівнюйте
#     середній бал поточного студента з найкращим на цей момент

# TODO 4: після циклу порахуйте середній бал по класу з кожного предмета
#   (сума / кількість студентів)


# ============================================================
# Крок 4. Збережіть результат у .txt файл
# ============================================================
# TODO 5: відкрийте OUTPUT_FILE в режимі 'w' і запишіть туди результат
#   у такому вигляді (числа округліть до одного знака після коми):
#
#   Середній бал по класу:
#   math: 67.8
#   python: 67.9
#   english: 67.9
#
#   Найкращий студент: Ім'я Прізвище (97.0)
#
# Також виведіть цей самий текст на екран через print().
#
# Запустіть скрипт (python analyze.py) і перевірте, що в папці
# з'явився файл result.txt.


# ============================================================
# Крок 5. Запушіть усе на GitHub
# ============================================================
# 1) Створіть новий ПОРОЖНІЙ репозиторій на github.com
#    (без README і .gitignore).
#
# 2) У терміналі, всередині папки students_analysis:
#
#   git init
#   git add .
#   git commit -m "Students analysis"
#   git branch -M main
#   git remote add origin <посилання_на_ваш_репозиторій>
#   git push -u origin main
#
# 3) Оновіть сторінку репозиторію на GitHub і переконайтеся, що там
#    є students.csv, analyze.py та result.txt.
