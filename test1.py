# cse30
# pa5
# test module game.py output

import os

if __name__ == '__main__':

    command = 'python' # may need to change to python3 or py
    module = 'game.py'
    total = 10
    try:
        os.system(f'{command} {module} 2> errors')
        score = int(input(f'Enter the score for the {module} on the scale 1 - {total}: '))

    except Exception:
        score = 0
        
    with open('tmp', 'w') as f:
        f.write(str(score))
