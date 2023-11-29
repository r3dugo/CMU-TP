from cmu_graphics import *

def drawSun(app):
    drawCircle(app.gap+app.squareLength/2, app.boardTop+2/5*app.boardHeight, 25, 
               fill = 'orange')
    
def drawMoon(app):
    drawCircle(app.gap+app.squareLength/2, app.boardTop+2/5*app.boardHeight, 25, 
               fill = 'gray')

def drawShop(app):

    # Shop
    drawRect(0, app.boardTop, app.width, app.boardHeight, fill = 'sienna', 
             borderWidth = 4, border = rgb(90, 30, 5))
    
    # Sunshine/Moonlight
    drawRect(6/5*app.gap, app.boardTop + app.gap, app.squareLength, 
             app.squareLength, fill = rgb(110, 40, 10), borderWidth = 4, 
             border = rgb(90, 30, 5))

    if app.sunMode == True: drawSun(app)
    else: drawMoon(app)

    labelLength = 2/3*app.squareLength
    drawRect(6/5 * app.gap + app.squareLength/2 - labelLength/2, 
             app.boardTop+0.66*app.boardHeight, labelLength, app.boardHeight/5, 
             fill = 'sienna', borderWidth = 2, border = rgb(90, 30, 5))

    drawLabel(f'{app.moneys}', app.gap + app.squareLength/2, 
             app.boardTop+3/4*app.boardHeight)

    # Plants/Zombies
    drawRect(app.boardHeight, app.boardTop+app.gap, app.width-2*app.boardHeight, 
             app.squareLength, fill = rgb(110, 40, 10), borderWidth = 4, 
             border = rgb(90, 30, 5))

    for plant in app.plantCosts:
        print(plant)