######################################################################
#
#
#
#
#
#
#
#
######################################################################


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
# in each "s" tuple [0] is the question, [1] is the answer
s = sample(key, 5)

num_right = 0
maze_size = 5
chicken_pics = ['raw_chicken.jpg',
                'egg_chicken.jfif',
                'flour_chicken.jpg',
                'egg_chicken.jfif',
                'breading-chicken.jpg',
                'pan_chicken.jfif',
                ]

chicken_stage = ['1) Raw Chicken',
                 '2) Dipped in Egg',
                 '3) Coated in Flour',
                 '4) Dipped in Egg (again)',
                 '5) Coated in Breading',
                 '6) Cooking'
                 ]

stage = 0

for i in s:

    print("Your current stage is:")
    print(chicken_stage[stage])
    # Show picture
    stage += 1
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass
    # Show and complete maze

    print('')
    print(i[0])
    user_answer = input('Your Guess: ')
    if user_answer.lower() == i[1].lower():
        print('Correct!')
        print('')
        num_right += 1
    else:
        print('Not Correct')
        print('')
# Added a final fraction of correct statement
print('{}/4 Questions Correct'.format(num_right))

# If statement for win or loss
# print 'congrats' or 'better luck next time'
# show winning or losing picture




# Contribution Code
# https://www.freecodecamp.org/forum/t/a-quiz-using-random-module-and-list/246707/2
