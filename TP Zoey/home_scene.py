from cmu_graphics import *

class Buttons:

    def __init__(self, func, label, locX, locY, width, height):
        self.func = func
        self.label = label
        self.x = locX
        self.y = locY
        self.width = width
        self.height = height
        self.color = 'fireBrick'

    def __repr__(self):
        return f'<{self.func}>'
    
    def __hash__(self):
        return hash(str(self))
    
    def __eq__(self, other):
        if type(other) != Buttons: return False
        return self.label == other.label and self.x == other.x and self.y == other.y

    def draw(self):

        drawOval(self.x - self.width/2, self.y, 30, self.height, 
                fill = self.color, borderWidth = 5, border = 'white')
        drawOval(self.x + self.width/2, self.y, 30, self.height, 
                fill = self.color, borderWidth = 5, border = 'white')
        drawRect(self.x, self.y, self.width, self.height, align = 'center', 
                fill = self.color, )
        
        gap = self.height/2 - 2.5
        drawLine(self.x - self.width/2, self.y - gap, self.x + self.width/2, 
                self.y - gap, lineWidth = 5, fill = 'white')
        drawLine(self.x - self.width/2, self.y + gap, self.x + self.width/2, 
                self.y + gap, lineWidth = 5, fill = 'white')

        drawLabel(f'{self.label}', self.x, self.y, size = 30, fill = 'white', 
                bold = True)
        



# If home screen

def initialiseHomeScreen(app):

    app.playButton = Buttons('game', 'PLAY', app.width/2, 2/5*app.height, 150, 80)
    app.instructionsButton = Buttons('instructions', 'INSTRUCTIONS', 
                                     app.width/2, 4/7*app.height, 280, 70)
    app.descriptionsButton = Buttons('descriptions', 'DESCRIPTIONS',
                                     app.width/2, 5/7*app.height, 280, 70)

    app.homeButtonList = [app.playButton, app.instructionsButton,
                          app.descriptionsButton]



def drawHomeScreen(app):

    # Draw sky
    drawRect(0, 0, app.width, app.fieldTop+10, fill = gradient(rgb(10, 10, 85), 
             rgb(70, 90, 140), rgb(235, 165, 10), rgb(255, 215, 0), 
             start = 'left-bottom'))
    drawStar(app.width-20, 0, app.height/5, 13, roundness = 80, fill = 'yellow')
    drawCircle(app.width-20, 0, app.height/7, fill = 'orange')

    
    # Draw field
    drawRect(app.fieldLeft, app.fieldTop, app.fieldWidth, app.height,
                fill = gradient(rgb(50, 139, 50), rgb(20, 100, 20), 
                start = 'top'))
    drawRect(0, app.fieldTop - 15, app.fieldLeft, app.height, fill = 'darkGray')
    drawRect(app.fieldLeft + app.fieldWidth, app.fieldTop + 10,
             app.width - app.fieldLeft - app.fieldWidth, app.height, 
             fill = 'darkGray')
    


    drawLabel('Greens and Ghouls', app.width/2, app.height/7, size = 65, 
              font='orbitron', bold = True, fill = gradient('green', 'red', start = 'right'))


    # Draw buttons
    app.playButton.draw()
    app.instructionsButton.draw()
    app.descriptionsButton.draw()

    app.playButton.draw()
    app.instructionsButton.draw()
    app.descriptionsButton.draw()


