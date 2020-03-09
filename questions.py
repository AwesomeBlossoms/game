
from random import sample

Questions = ['What is the capital of the United States of America? ',
             'Who is the current president of the United States of America? ',
             'What is the capital of Nigeria? ',
             'Muhammadu Buhari is the president of which country? ',
             'Uhuru Kenyatta is the president of which country? ',
             'What is the capital of France? ',
             'Which state has only one neighbor? ',
             'Where is Amsterdam located? ',
             'Emmanuel Macron is the president of which country? ',
             'Sir Alex Ferguson until his retirement coached which team? '
             ]

Answers = ['Washington DC',
           'President Donald Trump',
           'Abuja',
           'Nigeria',
           'Kenya',
           'Paris',
           'Maine',
           'Netherland',
           'France',
           'Manchester United'
           ]





key = list(zip(Questions, Answers))

# Sample from key now instead of Questions
s = sample(key, 4)

num_right = 0

for i in s:
    # in each "i" tuple [0] is the question, [1] is the answer
    print(i[0])
    user_answer = input('Your Guess: ')
    if user_answer.lower() == i[1].lower():
        print('Correct!!!')
        num_right += 1
    else:
        print('Not Correct')
# Added a final fraction of correct statement
print('{}/4 Questions Correct'.format(num_right))




# Contribution Code
# https://www.freecodecamp.org/forum/t/a-quiz-using-random-module-and-list/246707/2
