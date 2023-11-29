from cmu_graphics import *
from PIL import Image
import os, pathlib


def openImage(fileName):
        return Image.open(os.path.join(pathlib.Path(__file__).parent,fileName))


def initialisePlantSprites(app):

    # Cabbage-pult idle

    cabbagePultIdle = openImage('sprites/cabbagepult/idle.png')
    
    app.cabbagePultIdleSprites = []
    for i in range(5):
        # Split up the spritestrip into its separate sprites
        # then save them in a list
        frame = cabbagePultIdle.crop((84*i, 0, 80+84*i, 80))
        sprite = CMUImage(frame)
        app.cabbagePultIdleSprites.append(sprite)
        
    # app.spriteCounter shows which sprite (of the list) 
    # we should currently display
    app.cabbagePultSpriteCounter = 0



    # Peashooter idle

    peashooterIdle = Image.open('sprites/peashooter/idle.png')
    
    app.peashooterIdleSprites = []
    for i in range(6):
        # Split up the spritestrip into its separate sprites
        # then save them in a list
        frame = peashooterIdle.crop((84*i, 0, 80+84*i, 80))
        sprite = CMUImage(frame)
        app.peashooterIdleSprites.append(sprite)
        
    # app.spriteCounter shows which sprite (of the list) 
    # we should currently display
    app.peashooterSpriteCounter = 0



    # Wall-nut idle

    wallnutIdle = Image.open('sprites/wallnut/idle1.png')
    
    app.wallnutIdleSprites = []
    for i in range(3):
        # Split up the spritestrip into its separate sprites
        # then save them in a list
        frame = wallnutIdle.crop((84*i, 0, 80+84*i, 80))
        sprite = CMUImage(frame)
        app.wallnutIdleSprites.append(sprite)
        
    # app.spriteCounter shows which sprite (of the list) 
    # we should currently display
    app.wallnutSpriteCounter = 0



    