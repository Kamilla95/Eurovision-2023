import random
answers1 = ['Azerbaijan', 'Croatia', 'Czech Republic', 'Finland', 'Ireland', 'Israel', 'Latvia', 'Malta',
            'Moldova', 'The Netherlands', 'Norway', 'Portugal', 'Serbia', 'Sweden', 'Switzerland']
answers2 = ['Albania', 'Armenia', 'Australia', 'Austria', 'Belgium', 'Cyprus', 'Denmark', 'Estonia', 'Georgia',
            'Greece', 'Iceland', 'Lithuania', 'Poland', 'Romania', 'San Marino', 'Slovenia']
answers3 = ['France', 'Germany', 'Italy', 'Spain', 'Ukraine', 'United Kingdom']
answers4 = ['Azerbaijan', 'Croatia', 'Czech Republic', 'Finland', 'Ireland', 'Israel', 'Latvia', 'Malta',
            'Moldova', 'The Netherlands', 'Norway', 'Portugal', 'Serbia', 'Sweden', 'Switzerland', 'Albania', 'Armenia',
            'Australia', 'Austria', 'Belgium', 'Cyprus', 'Denmark', 'Estonia', 'Georgia',
            'Greece', 'Iceland', 'Lithuania', 'Poland', 'Romania', 'San Marino', 'Slovenia', 'France', 'Germany',
            'Italy', 'Spain', 'Ukraine', 'United Kingdom']

print('Hello. I can predict Eurovision 2023 results.')
name = input('What is your name? ')
print(f'Hello {name}')
print('What is interesting you? \n 1.The qualifiers from semifinal 1 will be \n 2.The qualifiers from semifinal 2 will be'
      '\n 3.The best country from Big 5 will be \n 4.The winner of Eurovision 2023 will be \n 5.The last place will be')

again1 = 'y'
while again1.lower() == 'y':
    question1 = input('Chose predictions ')
    if question1.lower() == '1':
        print('The qualifiers from semifinal 1 are: ', *random.sample(answers1, 10))
    elif question1.lower() == '2':
        print('The qualifiers from semifinal 2 are: ', *random.sample(answers2, 10))
    elif question1.lower() == '3':
        print('The best country from Big 5 will be: ', *random.sample(answers3, 1))
    elif question1.lower() == '4':
        print('The winner of Eurovision 2023 will be: ', *random.sample(answers4, 1))
    elif question1.lower() == '5':
        print('The last place will be: ', *random.sample(answers4, 1))
    again1 = input('Do you want to try again? Y/N ')


print('See you next time!')