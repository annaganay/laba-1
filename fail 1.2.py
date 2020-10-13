characters = 0
spaces = 0
punctuation = 0
words = 0
offers = 0
s = ''
p = ''
with open(r'C:\Users\User\PycharmProjects\pythonProject\steam_description_data.csv',encoding='utf-8') as f:
    for line in f:
        for j in line:
            characters += 1
            if j == ' ':
                spaces += 1
            if j.isalnum:
                punctuation += 1
            if j.isalnum  and j in '., ':
                words += 1
            s = j
            if j != '.' and j != '!' and j != '?':
                p += j
            elif p != '':
                offers += 1
                p = ''
print('Количество символов:',characters)
print('Количество символов без пробелов:',characters - spaces)
print('Количество символов без знаков препинания:', punctuation + spaces)
print('Количество слов:',words)
print('Количество предложений:',offers)