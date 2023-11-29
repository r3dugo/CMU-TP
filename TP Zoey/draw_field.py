from cmu_graphics import *


def drawField(app):

    drawRect(0, app.fieldTop - 15, app.fieldLeft, app.height, fill = 'darkGray')
    drawRect(app.fieldLeft + app.fieldWidth, app.fieldTop + 10,
             app.width - app.fieldLeft - app.fieldWidth, app.height, 
             fill = 'darkGray')

    for row in range(app.rows):
        for col in range(app.cols):
            color = None
            if app.fieldColor[row][col] == 0: color = 'darkGreen'
            else: color = 'forestGreen'
            drawCell(app, row, col, color)


def drawFieldBorder(app):
    drawRect(app.fieldLeft, app.fieldTop, app.fieldWidth, app.fieldHeight,
           fill=None, border='black',
           borderWidth=2*app.cellBorderWidth)


def drawCell(app, row, col, color):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight,
             fill=color, border='green',
             borderWidth=app.cellBorderWidth)


def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.fieldLeft + col * cellWidth
    cellTop = app.fieldTop + row * cellHeight
    return (cellLeft, cellTop)


def getCellSize(app):
    cellWidth = app.fieldWidth / app.cols
    cellHeight = app.fieldHeight / app.rows
    return (cellWidth, cellHeight)
