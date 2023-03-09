import random

gp = 500_000

def fifty_five_x_two(gp):
    numerize = {
        'k' : 1000,
        'm' : 1000000
    }
    total = 0
    goal_profit = 10 * numerize['m']

    print(f"Coin Pouch: {gp:,}")
    while True:
        wager = input("Enter amount: ").lower()
        for i in wager[-1]:
            total = float(wager[0:-1])
            if i.isalpha() and i in numerize:
                wager = total * numerize[i]
            else:
                wager = float(wager)

        if gp == 0:
            return f"You're current balance is: {gp}."
        if wager > gp:
            print(f"You don't have enough to cover that... Current balance: {gp:,} gp")
            continue
        
        roll = random.randint(1, 100)
        if roll > 55:
            print(f"Congratulations! You win with a roll of: {roll}")
            gp += wager
            total += wager
        else:
            print(f"Sorry! You lose with a roll of: {roll}")
            gp -= wager
            total -= wager
        print(f"Current Balance: {gp:,} gp")
        if gp >= goal_profit:
            return f"Congratulations! You've reached the goal amount!"
        replay = input('Play again? (Y/N): ').lower()
        if replay == 'n':
            print('Thanks for playing!')
            print(f"Your net toal from this session is: {total:,}! Your current gp stands at: {gp:,} gp")
            break

print(fifty_five_x_two(gp))