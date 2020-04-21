status1 = str(input())
status2 = str(input())
status3 = str(input())

if status1 == 'vertebrado':
    if status2 == 'ave':
        if status3 == 'carnivoro':
            print("aguia")
        elif status3 == 'onivoro':
            print('pomba')
    elif status2 == 'mamifero':
        if status3 == 'onivoro':
            print("homem")
        elif status3 == 'herbivoro':
            print('vaca')
else:
    if status1 == 'invertebrado':
        if status2 == 'inseto':
            if status3 == 'hematofago':
                print('pulga')
            elif status3 == 'herbivoro':
                print('lagarta')
        elif status2 == 'anelideo':
            if status3 == 'hematofago':
                print('sanguessuga')
            elif status3 == 'onivoro':
                print('minhoca')