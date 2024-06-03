import random
def deckCounter(deck):
    number_of_points = 0
    countA = 0
    for card in deck:
        if card == "A":
            countA += 1
        else:
            number_of_points += card
    while countA > 0:
        if number_of_points + 11 > 21:
            number_of_points += 1
        else:
            number_of_points+= 11
        countA -= 1
    return number_of_points

cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def playgame():
    userDeck = []
    computerDeck = []
    for i in range(2):
        randomCard = cards[random.randint(0, len(cards) - 1)]
        userDeck.append(randomCard)
        if i == 1:
            randomCard = cards[random.randint(0, len(cards) - 1)]
            computerDeck.append(randomCard)
    shouldContinue = True
    while shouldContinue:

        score = deckCounter(userDeck)
        print(f"Your cards: {userDeck} total points -> {deckCounter(userDeck)}")
        print(f"Computer deck: {computerDeck} total points -> {deckCounter(computerDeck)}")
        if score == 21:
            print("Congrats!! You win!")
            break

        if input("would you like to continue? type 'y' to continue ") == "y":
            randomCard = cards[random.randint(0, len(cards) - 1)]
            userDeck.append(randomCard)
            score = deckCounter(userDeck)
            print(f"New deck: {userDeck} total score: {score}")

            if score > 21:
                print(f"New deck: {userDeck} total score: {score}")
                print("You busted!")
                break
        else:
            while True:
                score = deckCounter(userDeck)
                computerScore = deckCounter(computerDeck)
                if computerScore > score:
                    print("Computer WINS!!")
                    print(f"Enemy deck: {computerDeck} and score = {computerScore}")
                    shouldContinue = False
                    break
                elif computerScore == score:
                    print("Its draw!")
                    print(f"Enemy deck: {computerDeck} and score = {computerScore}")
                    print(f"Your deck: {userDeck} total score: {score}")
                    shouldContinue = False
                    break
                randomCard = cards[random.randint(0, len(cards) - 1)]
                print(f"Computer take a new card: {randomCard}")
                computerDeck.append(randomCard)
                computerScore = deckCounter(computerDeck)
                if computerScore > 21:
                    print("Congrats!! You win!")
                    print(f"Your cards: {userDeck} total points -> {deckCounter(userDeck)}")
                    print(f"Computer deck: {computerDeck} total points -> {deckCounter(computerDeck)}")
                    shouldContinue = False
                    break
while True:
    if input("Would you like to play game? type 'y' ") == "y":
        playgame()
    else:
        break