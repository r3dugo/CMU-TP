from cmu_graphics import *
import home_scene
import game_scene

# Initialise Classes




def onAppStart(app):
    app.width = 900
    app.height = 750

    app.homeScreen = True
    app.instructions = False
    app.descriptions = False
    app.gameGo = False

    app.stepsPerSecond = 20
    app.steps = 0

    home_scene.initialiseHomeScreen(app)
    game_scene.initialiseGame(app)


# Scenes


# Switching to another scene

def switchScenesTo(app, scene):
    app.homeScreen = False
    app.instructions = False
    app.descriptions = False
    app.gameGo = False

    if scene == 'home': app.homeScreen = True
    elif scene == 'instructions': app.instructions = True
    elif scene == 'descriptions': app.descriptions = True
    elif scene == 'game': 
        app.timer = 0
        app.moneys = 0
        app.gameGo = True


# If instructions screen

def drawInstructions(app):
    pass


# If descriptions screen

def drawDescriptions(app):
    pass




def redrawAll(app):

    if app.homeScreen == True:
        home_scene.drawHomeScreen(app)
    elif app.instructions == True:
        drawInstructions(app)
    elif app.descriptions == True:
        drawDescriptions(app)
    elif app.gameGo == True:
        game_scene.drawGame(app)



def inOval(x0, y0, x1, y1, w, h):
    return ((x0 - x1)/w) ** 2 + ((y0 - y1)/h) ** 2 < 1


def inButton(app, mouseX, mouseY):
    for button in app.homeButtonList:
        if (((button.x - button.width/2) < mouseX < (button.x + button.width/2))
             and (button.y - button.height/2) < mouseY < (button.y + button.height/2)):
            return button
        elif (inOval(mouseX, mouseY, button.x - button.width/2, button.y, 15, button.height/2)
            or inOval(mouseX, mouseY, button.x + button.width/2, button.y, 15, button.height/2)):
            return button
    

def onMouseMove(app, mouseX, mouseY):

    if app.homeScreen == True:
        hoveredButton = inButton(app, mouseX, mouseY)
        col = 'fireBrick'
        for button in app.homeButtonList: button.color = col
        if hoveredButton != None: 
            col = 'darkRed'
            hoveredButton.color = col
        


def onMouseRelease(app, mouseX, mouseY):

    if app.homeScreen == True:

        pressedButton = None
        pressedButton = inButton(app, mouseX, mouseY)
        if pressedButton != None:
            switchScenesTo(app, pressedButton.func)



def onStep(app):
    app.steps += 1

    if app.gameGo == True:
        if app.steps % 20 == 0 and app.steps != 0:
            app.timer += 1
        if app.steps % 300 == 0 and app.steps != 0:
            app.moneys += 50

def main():
    runApp()


main()