from cmu_graphics import *
import plant_sprites


def initialisePlants(app):

    # Plant Class


    # Initialise plant variables
    app.plantCosts = {'peashooter': 80, 'wall-nut': 50, 'cabbage-pult': 30}
    app.plantNames = {'peashooter': 'Peashooter', 'wall-nut': 'Wall-nut', 
                      'cabbage-pult': 'Cabbage-Pult'}
    app.plantDefences = {'peashooter': 1, 'wall-nut': 5, 'cabbage-pult': 1}
    app.plantRanges = {'peashooter': 6, 'wall-nut': 0, 'cabbage-pult': 8}
    app.plantDamages = {'peashooter': 1, 'wall-nut': 0, 'cabbage-pult': 2}
    app.plantAttackSpeed = {'peashooter': 2, 'wall-nut': 0, 'cabbage-pult': 1}

    app.sprites = []

    plant_sprites.initialisePlantSprites(app)


    class Plant:

        def __init__(self, type, x, y):
            self.type = type
            self.sunCost = app.plantCosts[type]
            self.name = app.plantNames[type]
            self.defence = app.plantDefences[type]
            self.x = x
            self.y = y

        def __repr__(self):
            return f'<{self.type}: ({self.x}, {self.y})>'

        def __hash__(self):
            return hash(str(self))

        def __eq__(self, other):
            return self.type == other.type and self.x == other.x and self.y == other.y
        

             