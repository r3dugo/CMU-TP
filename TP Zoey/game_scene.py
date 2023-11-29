from cmu_graphics import *
import draw_field
import draw_shop
import initialise_plant_class

def initialiseGame(app):
    
    initialise_plant_class.initialisePlants(app)

    app.sunMode = True
    
    app.rows = 5
    app.cols = 8
    app.field = [[0] * app.cols for row in range(app.rows)]
    app.fieldWidth = app.cols/10 * app.width
    app.fieldHeight = 0.12 * app.rows * app.height
    app.fieldLeft = app.width/2 - app.fieldWidth/2
    app.fieldTop = 0.25 * app.height
    app.cellBorderWidth = 1.2

    app.timer = 0
    app.moneys = 0

    app.boardTop = app.fieldTop + app.fieldHeight
    app.boardHeight = app.height - app.fieldHeight - app.fieldTop
    app.gap = 0.09 * app.boardHeight
    app.squareLength = app.boardHeight - 2*app.gap

    app.numSunflowers = 0


    app.fieldColor = [[0] * app.cols for row in range(app.rows)]

    for row in range(len(app.fieldColor)):
        for col in range(len(app.fieldColor[0])):
            if (row + col) % 2 == 0:
                app.fieldColor[row][col] = 0
            else:
                app.fieldColor[row][col] = 1
    

def drawGame(app):

    # Draw sky
    drawRect(0, 0, app.width, app.fieldTop + 10, 
             fill = gradient('orange', 'gold', start = 'left-bottom'))
    drawStar(app.width-20, 0, app.height/5, 13, roundness = 80, fill = 'yellow')
    drawCircle(app.width-20, 0, app.height/7, fill = 'orange')
    
    draw_field.drawField(app)
    draw_shop.drawShop(app)