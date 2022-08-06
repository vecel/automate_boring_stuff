
import random
import pyinputplus as pyip
import time

''' Todo: Powtórz pytania, na które nie udzielono poprawnej odpowiedzi,
          Opcja wpisania zakresu kwadratów, potęg oraz wyboru czy mają być używane (kwadraty/potęgi/oba)'''

def _init_squares(squares_range: int) -> list:
    pool = []
    for base in range(1, squares_range + 1):
        pool.append((base, 2))
    return pool

def _init_powers(basis_range: int, exponents_range: int) -> list:
    pool = []
    for base in range(2, basis_range + 1):
        for exp in range (3, exponents_range + 1):
            pool.append((base, exp))
    return pool

def init_pool(
    *, 
    squares = True, 
    powers = True,
    squares_range: int = 50, 
    basis_range: int = 9, 
    exponents_range: int = 5
    ) -> list:

    pool = []
    if squares:
        pool.extend(_init_squares(squares_range))
    if powers:
        pool.extend(_init_powers(basis_range, exponents_range))
    
    return pool

def play(rounds: int) -> None:
    powers = init_pool()
    points = 0

    for i in range(rounds):
        time.sleep(0.5)
        base, exp = random.choice(powers)
        prompt_msg = f'What is {base} to the power of {exp}?\n'

        try:
            ans = pyip.inputInt(prompt_msg, limit = 1)
            if ans == base ** exp:
                print('Correct.')
                points += 1
            else:
                print(f'Incorrect. Answer is {base ** exp}')
        except:
            print('Wrong format.')
        

    print(f'Score {points} / {rounds}.')
    
if __name__ == '__main__':
    DEFAULT_ROUNDS_NUMBER = 5
    rounds = pyip.inputInt('How many questions do you want: ', blank = True)
    play(rounds or DEFAULT_ROUNDS_NUMBER)