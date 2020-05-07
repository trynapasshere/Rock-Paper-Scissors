import random

def outcome(user, option, user_ops):
    choices = []
    win = []
    if (user in user_ops) == True and user != option:
        user_pos = user_ops.index(user)
        for i in range(1, len(user_ops) - user_pos):
            choices.append(user_ops[user_pos + i])
        for op in user_ops:
            if user_ops.index(op) < user_pos:
                choices.append(op)
        for i in range(len(choices) // 2):
            win.append(choices[i])
        if (option in win) == False:
            return True
        else:
            return False

name = input('Enter your name: ')

print('Hello, ' + name)

rating = 0

file = open('rating.txt', 'r')

for line in file:
    if name in line:
        space = line.find(' ')
        rating = int(line[space+1:])

user_options = input()

if user_options == '':
    user_options = 'rock,scissors,paper'

print("Okay, let's start")
#> rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
while True:

    user = input()

    user_ops = user_options.split(',')

    if (user in user_ops) == False:
        if user != '!rating' and user != '!exit':
            print('Invalid input')

    if user == '!rating':
        print('Your rating: ' + str(rating))

    if user == '!exit':
        print('Bye!')
        break

    option = user_ops[random.randint(0, len(user_ops)-1)]

    if user == option:
        rating+=50
        print('There is a draw (' + user + ')')

    victory = outcome(user, option, user_ops)

    if victory == True:
        rating+=100
        print('Well done. Computer chose ' + option + ' and failed')

    if victory == False:
        print('Sorry, but computer chose ' + option)




