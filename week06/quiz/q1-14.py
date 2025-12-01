def process(grades):
    processed_grades = {'A': [], 'B': [], 'C': []}
    for grade in grades:
        if grade > 17:
           processed_grades['A'].append(grade)
        elif 12 <= grade <= 17:
            processed_grades['B'].append(grade)
        else:
             processed_grades['C'].append(grade)
    return processed_grades

grades = [8, 13, 20, 18, 15, 10]

print(process(grades))