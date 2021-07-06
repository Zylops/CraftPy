# CraftPy
A package that allows to use functions to control minecraft built on pyautogui.

To make an instance of the player class, use:

    CraftPy.Player({version_number}, {Cheats (True if enabled)})

# Player methods:

+ def __init__(self, Float: version, Boolean: cheats)

+ def walk(self, Integer: seconds)

+ def hit(self)

+ def interact(self)

+ def look(self, String: direction, Integer: pixels)

+ def jump(self)

+ def sneak(self, Boolean: toggle)

+ def sprint(self, Boolean: toggle)

+ def crit(self)

+ def switchitem(self, Integer: slot)

+ def shield(self, Boolean: toggle)

+ def bow(self, Integer: load)

+ def mine(self, Boolean: toggle)

+ def throw(self)

+ def chat(self, String: message)

+ def inventory(self)

+ def offhand(self)

+ def perspective(self)

+ def reloadchunks(self)

+ def gamemode(self)

+ def chunkborders(self)

+ def togglehitboxes(self)

+ def coordinates(self)

+ def clearchat(self)

+ def renderdistance(self, Boolean: increase)