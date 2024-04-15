import random
import time

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.,$§-/* !?()[]{}+ěščřžýáíé+ĚŠČŘŽÝÁÍÉ˚$ůúˇ%<>\\+-":;#<>^'

text_to_bf = input("Enter text to bruteforce -> ")
letters_to_bf = list(text_to_bf)

iterations = 0

start_time = time.time()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while letters_to_bf:
    char = random.choice(chars)
    iterations += 1
    print(bcolors.WARNING + f"Chose {char}")
    if char in letters_to_bf:
        letters_to_bf.remove(char)
        print(bcolors.OKGREEN + f"\nFound letter {char}")

end_time = time.time()

elapsed_time = end_time - start_time

print(bcolors.OKCYAN + f"\nDone in {round(elapsed_time,5)}s! {iterations} iterations")
print(bcolors.OKCYAN + f'You entered "{text_to_bf}"')
