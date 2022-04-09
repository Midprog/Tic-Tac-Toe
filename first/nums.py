theBroad = {'topL':' ', 'topM':' ', 'topR':' ',
            'midL':' ', 'midM':' ', 'midR':' ',
            'lowL':' ', 'lowM':' ', 'lowR':' '}
def printBroad(broad):
    print(broad['topL'] + '|' + broad['topM'] + '|' + broad['topR'])
    print('-+-+-')
    print(broad['midL'] + '|' + broad[ 'midM'] + '|' + broad['midR'])
    print('-+-+-')
    print (broad['lowL'] + '|' + broad['lowM'] + '|' + broad['lowR'])
turn = 'X'
game = True
printBroad(theBroad)

while game:
    print('Just put enter for the end')
    print('Turn for' + turn + '. Move on wich space?')
    move = input()
    if move == ' ':
        break
    elif move not in ['lowL', 'lowM', 'lowR', 'midL', 'midM', 'midR', 'topL', 'topM', 'topR']:
        print('Error, these symbols are not included in the game conditions')
        print('Change your turn:')
        continue
    elif theBroad[move] != ' ':
        print('Error, this cell is already occupied')
        print('Change your turn:')
        continue
    theBroad[move] = turn
    printBroad(theBroad)
    if turn == 'X':
        turn = '0'
    else:
        turn = 'X'