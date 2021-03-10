# TODO: Inventory / Pick up
# TODO: Examine
# TODO:


directions = ['north', 'south', 'east', 'west']
# Ide a keywordök amik működnek majd az examine-hoz
examine = ['']


def clear():
    print('\n' * 50)


def intro():
    clear()
    print('Egy 4 szobás ház átkutatása.\n')
    game('default', 0)


class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # Ide helyezi be az épp lehetséges választási lehetőségeket{pl:northern -- > south, west}
        self.linkedLocations = {}

    # Le ellenőrzi, hogy a beütött irány megfelelő-e a directions listának(lásd fent), majd lecsekkolja, hogy a beütött irány lehetséges-e.
    def addLink(self, direction, destination):
        if direction not in directions:
            raise ValueError("Invalid Direction")
        elif destination not in locations:
            raise ValueError("Invalid Destination")
        # Ha minden kritériumnak megfelel, behelyezi a linkedLocations directory-ba
        else:
            self.linkedLocations[direction] = destination


def game(startLoc, dictionary):
    if startLoc == 'default':
        currentLoc = locations['north']
    else:
        currentLoc = dictionary['location']

    while True:
        print(currentLoc.description)
        for linkDirection, linkedLocation in currentLoc.linkedLocations.items():
            print(linkDirection + ': ' + locations[linkedLocation].name)
        command = input(f"{directions}> ").lower()
        if command in directions:
            if command not in currentLoc.linkedLocations:
                print("\nArra nem mehetsz!!\n")
            else:
                newLocID = currentLoc.linkedLocations[command]
                currentLoc = locations[newLocID]
        else:
            print(f'\nNem megfelelő irány!')


# Szeretnék majd minden szobában bizonyos tárgyakat elrejteni(pl. könyvespolcba, vagy asztal alá)
# class Item():
#     #Minden item classja
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description


locations = {'north': Location("northern room", "\nJelenleg a northern szobában vagy!"),
             'south': Location("southern room", "\nJelenleg a southern szobában vagy!"),
             'west': Location("western room", "\nJelenleg a western szobában vagy!"),
             'east': Location("eastern room", "\nJelenleg az eastern szobában vagy!")
             }

locations['south'].addLink('east', 'east')
locations['south'].addLink('north', 'north')
locations['north'].addLink('south', 'south')
locations['north'].addLink('west', 'west')
locations['west'].addLink('east', 'north')
locations['east'].addLink('west', 'south')


startgame = input('Egy történettel készültem, szeretnél játzani? (Y / N)')
startgame = startgame.upper()
if startgame == 'N':
    print('Talán majd legközelebb, mikor több időd lesz')
else:
    intro()
