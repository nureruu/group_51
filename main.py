
from decouple import config
from logic import play
min_num = config("MIN_NUM")
max_num = config("MAX_NUM")
attemps = config("ATTEMPS")
start_capital = config("START_CAPITAL")

def main():
    print(f'welcome to play a game! You should guess the number from {min_num} to {max_num} for {attemps} attemps!')
    print(f'your starting capital: {start_capital}')
play(MIN_NUM=0, MAX_NUM=50, ATTEMPS=5, START_CAPITAL=500)

if __name__ == "__main__":
    main()