import random
while True:
    def play(MIN_NUM, MAX_NUM, ATTEMPS, START_CAPITAL):
        capital = START_CAPITAL

        for ATTEMPS in range(ATTEMPS):
            first = int(input("your starting capital: "))
            if first > capital:
                print("you haven't enough starting capital!")

                continue
                guess = int(input(f"guess the number from {MIN_NUM} to {MAX_NUM}"))
                number_to_guess = random.randint(MIN_NUM, MAX_NUM)
                if guess == number_to_guess:
                    print("congratulasion! you guess!")
                    capital += first
                    break
                else:
                    print("you didn't win!")
        ATTEMPS + 1
