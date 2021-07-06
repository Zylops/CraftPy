import pyautogui as controller
import time as t
import pyperclip

class CraftPyError(Exception):
    pass
class InvalidDirection(CraftPyError):
    pass
class VersionError(CraftPyError):
    pass
class PermissionError(CraftPyError):
    pass

class Player():
    def __init__(self, version, cheats):
        self.version = version
        self.cheats = cheats

    def walk(self, seconds):
        controller.keyDown('w')
        t.sleep(seconds)
        controller.keyUp('w')

    def hit(self):
        controller.click()

    def interact(self):
        controller.rightClick()

    def look(self, direction, pixels):
        if direction == 'up':
            controller.moveRel((0, -pixels))
        if direction == 'down':
            controller.moveRel((0, pixels))
        if direction == 'right':
            controller.moveRel((100, pixels))
        if direction == 'left':
            controller.moveRel((-100, pixels))
        else:
            raise InvalidDirection("Invalid directions. Available directions are 'left', 'right', 'up', and 'down'")

    def jump(self):
        controller.hotkey(['space'])

    def sneak(self, toggle):
        if toggle == True:
            controller.keyDown('shift')
        elif toggle == False:
            controller.keyUp('shift')

    def sprint(self, toggle):
        if toggle == True:
            controller.keyDown('ctrl')
        elif toggle == False:
            controller.keyUp('ctrl')

    def crit(self):
        if self.version >= 1.9:
            self.jump()
            self.hit()
        else:
            raise VersionError("Version is below 1.9, crits are not a feature before Minecraft version 1.9")

    def switchitem(self, slot):
        controller.press(str(slot))

    def shield(self, toggle):
        if toggle == True:
            controller.mouseDown('right')
        elif toggle == False:
            controller.mouseUp('right')

    def bow(self, load):
        controller.mouseDown('right')
        t.sleep(load)
        controller.mouseUp('right')

    def mine(self, toggle):
        if toggle == True:
            controller.mouseDown('left')
        elif toggle == False:
            controller.mouseUp('left')

    def throw(self):
        controller.press('q')

    def chat(self, message):
        controller.press('t')
        controller.typewrite(message)
        controller.press('return')

    def inventory(self):
        controller.press('e')

    def offhand(self):
        controller.press('f')

    def perspective(self):
        controller.press('f5')

    def reloadchunks(self):
        controller.hotkey(['f3', 'a'])

    def gamemode(self):
        if self.cheats == True:
            controller.hotkey(['f3', 'f4'])
        else:
            PermissionError('You do not have cheats enabled. Gamemode cannot be changed without cheats')

    def chunkborders(self):
        controller.hotkey(['f3', 'f'])

    def togglehitboxes(self):
        controller.hotkey(['f3', 'b'])

    def coordinates(self):
        controller.hotkey(['f3', 'c'])
        command = pyperclip.paste()
        coords = ' '.join(command.split(' ')[7:10])
        return coords

    def clearchat(self):
        controller.hotkey(['f3', 'd'])

    def renderdistance(self, increase):
        if increase == True:
            controller.hotkey(['f3', 'F'])
        else:
            controller.hotkey(['f3', 'shift', 'f'])




