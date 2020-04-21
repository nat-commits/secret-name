try:
    with open('Discover Weekly 20200420', 'r') as lol:
        beat_this_one = ['abcdefghijklmnopqrstuvwxyz'.index(letter) for index, letter in enumerate(''.join(sorted((possibly_misformatted_line.lower().strip().replace(' ', '').split('?')[0].split('/')[-1] for possibly_misformatted_line in lol.read().split())))) if letter not in '1234567890' and index % 30 == 3]
        try:
            with open('NAME', 'r') as garbled_name:
                okay_ill_try = secret_name = ''.join(('abcdefghijklmnopqrstuvwxyz'[('abcdefghijklmnopqrstuvwxyz'.index(garbled_letter) - beat_this_one[index % len(beat_this_one)]) % 26] for index, garbled_letter in enumerate(garbled_name.read())))
                print('Your secret name is', secret_name, 'or maybe it\'s still secret')
        except Exception:
            secret_name = input('What is your secret name? ').lower()
            garbledeegook = ''.join(('abcdefghijklmnopqrstuvwxyz'[('abcdefghijklmnopqrstuvwxyz'.index(secret_letter) + beat_this_one[index % len(beat_this_one)]) % 26] for index, secret_letter in enumerate(secret_name)))
            with open('NAME', 'w') as garbled_name:
                garbled_name.write(garbledeegook)
except Exception:
    print('Make a file called Discover Weekly 20200420 and paste in thirty URLs from the Disover Weekly playlist creaded by Spotify for Nat the week of April 20, 2020. April is the fourth month of the year get it?')
