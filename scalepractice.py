

def ScalePicker():
        #variables
        import random
        keys = ["A", "Bb", "B", "C", "Db", "C#", "D", "Eb", "E", "F", "Gb", "F#", "G", "Ab"]
        modes = ["Ionian", "Dorian", "Phrygian", "Lydian", "Mixolydian", "Aeolian", "Locrian"]
        your_key = random.choice(keys)
        your_mode = random.choice(modes)
        ionian_hint = 'Major, baby.'
        dorian_hint = '1 2 b3 4 5 6 b7 8'
        phrygian_hint = '1 b2 b3 4 5 b6 b7 8'
        lydian_hint = '1 2 3 #4 5 6 7 8'
        mixolydian_hint = '1 2 3 4 5 6 b7 8'
        aeolian_hint = '1 2 b3 4 5 b6 b7 (aka: natural minor)'
        locrian_hint = '1 b2 b3 4 b5 b6 b7 8'
        bravos = ["Cool Beans!", "BAT!", "Noooooice", "Weird", "Look at you!", "Go musician go!", "Yarr"]

        #start
        print('*-*-*-*-*-*-*-*-*-*-*-*-*-*')
        print('Key: ' + your_key + ' | ' + 'Mode: ' + your_mode)

        #hints
        while True:
            print('Do you need a hint? Y/N')
            hint=input()
            if hint == 'Y' or hint == 'y':
                print('*-*-*-*-*-*-*-*-*-*-*-*-*-*')
                print(your_mode)
                if your_mode == 'Ionian':
                    print(ionian_hint)
                    break
                elif your_mode == 'Dorian':
                    print(dorian_hint)
                    break
                elif your_mode == 'Phrygian':
                    print(phrygian_hint)
                    break
                elif your_mode == 'Lydian':
                    print(lydian_hint)
                    break
                elif your_mode == 'Mixolydian':
                    print(mixolydian_hint)
                    break
                elif your_mode == 'Aeolian':
                    print(aeolian_hint)
                    break
                elif your_mode == 'Phrygian':
                    print(phrygian_hint)
                    break
                elif your_mode =='Locrian':
                    print(locrian_hint)
                    break
            elif hint == 'N' or hint == 'n':
                print('*-*-*-*-*-*-*-*-*-*-*-*-*-*')
                print(random.choice(bravos))
                break


while True:
    print('*-*-*-*-*-*-*-*-*-*-*-*-*-*')
    print('Are you ready? Y/N')
    Ready = input()
    if Ready == 'Y' or Ready == 'y':
        ScalePicker()
    elif Ready == 'N' or Ready == 'n':
        print('Take your time, musician.')
    elif Ready != 'Y' and Ready != 'N' and Ready !='y' and Ready !='n':
        print('Y or N')




