#!/usr/bin/ python
# Make a number of quiz files + answer files for them

import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'NewMexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'WestVirginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

states = list(capitals.keys())
ans = 'ABCDE'

for QuizNum in range(1,6):
    quizfile = open('/home/andrew/capitals_quiz_{:04d}.txt'.format(QuizNum),'w')
    answfile = open('/home/andrew/capitals_answer_{:04d}.txt'.format(QuizNum),'w')

    # Quiz Header
    quizfile.write('\n\nName: ________\n\nDate: ________\n\nPeriod: ________\n\n')
    quizfile.write('{:>50}'.format('State Capitals Quiz (Form {:04d})\n\n\n'.format(QuizNum)))

    # Quiz Body
    random.shuffle(states)

    for i,state in enumerate(states,1):
        quizfile.write('\n{0}. Can you name the capital city of {1}.\n'.format(i,state))
        cityes = list(capitals.values())
        answers = [capitals[state]]
        cityes.remove(answers[0])
        answers += random.sample(cityes,4)
        for char in ans:
            variant = random.choice(answers)
            answers.remove(variant)
            quizfile.write('\t{0}. {1}\n'.format(char, variant))
            if variant == capitals[state]:
                answfile.write('{0}. {1} - {2}\n\n'.format(i,char, variant))


quizfile.close()
answfile.close()