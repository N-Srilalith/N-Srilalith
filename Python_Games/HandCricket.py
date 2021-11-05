import random

def toss(coin):
    outcome = random.choice(['Heads', 'Tails'])
    result = ''
    if coin == outcome.lower():
        side = input("You win, Bat or Bowl?").capitalize()
        print("You\'ve chosen to ", side,'.')
        if side.lower() == 'bat':
            result = 'user'
        else:
            result = 'computer'
    
    else:
        side = random.choice(['Bat', 'Bowl'])
        print("You lost the toss, I choose to ",side,'.')
        if side.lower() == 'bat':
            result = 'computer'
        else:
            result = 'user'
        
    return side.lower(), result                                            #Result tells us who's batting first

def innings(side, player):
    wickets = 3
    score = 0
    while wickets>0:
        computer_n = random.randint(1,6)
        user_in = int(input('Pick a number: '))
        print(f"Computer picked: {computer_n}")
        if user_in == computer_n:
            wickets-=1
            print(f"Out! {wickets} wickets left!")
        elif user_in>6 or user_in<1:
            print('Invalid Input! Try picking an integer between 1 and 6')
        else:
            if player == 'user':
                score+=user_in
                print(f"User's score {score}")
            else:
                score+=computer_n
                print(f"Computer's score {score}")
    return score

def match():
    choices = ['bat', 'bowl']
    players = ['user', 'computer']
    coin = input("Heads or Tails?").lower()
    side, result = toss(coin)
    score_1 = innings(side, result)
    print(f"The {result} has scored {score_1} runs!")
    players.remove(result)
    print(f"The {players[0]} needs {score_1 + 1} runs to win!")
    print("Innings 1 has ended. Switch sides!")
    choices.remove(side)
    score_2 = innings(choices, players)
    print("Innings 2 has also concluded!")
    print("Results are: ")
    print(f"{result}: {score_1}\n{players}: {score_2}")
    if score_1 > score_2:
        print(f"{result} wins the Game!")
    elif score_1 < score_2:
        print(f"{players} wins the Game!")
    else:
        print("It\'s a tie!")

if __name__ == '__main__':
    match()