#!/usr/bin/python
# printer setup
from Adafruit_Thermal import *

# ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
# printer = ThermalPrinter(uart, auto_warm_up=False)
# printer.warm_up(12)

import random

# variables
lineSpacer = True
lineWidth = 16

def space_text(string):
    if(len(string) >= 16 and string[16] != " "):
        print(string[16])
        index = string.rfind(" ", 0, 16)
        string = string[:index] + "\n" + string[(index+1):]
        if(len(string) >= 32):
            if(string[32] != " "):
                print(string[32])
                index = string.rfind(" ", 16, 32)
                string = string[:index] + "\n" + string[(index+1):]
            else:
                return string
        else:
            return string
        return string
    else:
        return string

places = ['apartment', 'bathroom', 'cabin', 'cell', 'community garden', 'community pool', 'condo', 'cottage', 'ditch', 'dream', 'environment', 'fish tank', 'friend\'s basement', 'grave', 'house', 'local grocery store', 'local library', 'local park', 'river', 'roof', 'school bus', 'womb', 'workplace']

adjectives = ['charming', 'chilly', 'conflicted', 'damp', 'dusty', 'frivolous', 'glamorous', 'glowing', 'gruesome', 'languid', 'lovely', 'medium', 'messy', 'modern', 'orange', 'ripe', 'rural', 'sad', 'silly', 'sparkly', 'suspicious', 'tasty', 'ugly', 'uncaring', 'underdeveloped', 'unfortunate', 'warm']

verbs = ['annotate', 'avoid', 'bake', 'browse', 'brush', 'burn', 'caress', 'check', 'confess', 'contemplate', 'criticize', 'deny', 'drink', 'eat', 'email', 'feed', 'find', 'forget', 'gamble', 'hear', 'hide from', 'ignore', 'lose', 'lubricate', 'observe', 'part from', 'perform', 'pet', 'pray to', 'press', 'put on', 'question', 'read', 'rearrange', 'rescue', 'restart', 'restore', 'share', 'solve', 'spend', 'steal', 'stop', 'synthesize', 'touch', 'visit', 'wash', 'watch', 'wrestle with', 'write']

moveVerbs = ['amble', 'climb', 'crawl', 'drive', 'escape', 'inch', 'jump in', 'limp', 'march', 'moonwalk', 'prowl', 'ride', 'roll', 'run', 'shimmy','shuffle', 'skate', 'sleepwalk', 'sneak', 'stomp', 'stride', 'strut', 'stumble', 'swim', 'trek', 'walk']

nouns = ['alarm', 'bra', 'breakfast', 'breath', 'cat', 'coffee', 'colonizer', 'crossword', 'cup of water', 'dog', 'elevator button', 'email', 'enemy', 'family', 'future', 'government', 'hope', 'identity', 'income', 'information', 'local news', 'love', 'lover', 'mail', 'meds', 'memory', 'papers', 'phone', 'printer', 'problems', 'reflection', 'roommate', 'sexuality', 'socks', 'spouse', 'sweater', 'teeth', 'television', 'text', 'time', 'toothbrush', 'twin', 'window']

adverbs = ['adequately', 'aggressively', 'automatically', 'begrudgingly', 'carefully', 'carelessly', 'cheerfully', 'dejectedly', 'deliciously', 'delusionally', 'disastrously', 'ethically', 'exclusively', 'gently', 'hastily', 'hypnotically', 'internally', 'loudly', 'lovingly', 'mischievously', 'necessarily', 'notoriously', 'obsessively', 'poorly', 'precariously', 'problematically', 'punctually', 'religiously',
'reluctantly', 'repeatedly', 'secretly', 'shamefully', 'shamelessly', 'soulfully', 'suspiciously', 'tastefully', 'thoughtfully', 'thoughtlessly', 'timidly', 'unfortunately', 'unwillingly']

# wake up in your (adjective) (place). (verb) your (noun) (adverb). (moveVerb) to your (place).
# print
line1 = ("wake up in your " + random.choice(adjectives) + " " + random.choice(places) + ".")
line2 = (random.choice(verbs) + " your " + random.choice(nouns) + " " + random.choice(adverbs) + ".")
line3 = (random.choice(moveVerbs) + " to your " + random.choice(places) + ".")

printer.boldOn()
printer.setSize('L')

#testLine = "rearrange your government thoughtlessly."

#print(space_text(testLine))

print(space_text(line1))
printer.write(space_text(line1))
printer.feed(4)

print(space_text(line2))
printer.write(space_text(line2))
printer.feed(4)

print(space_text(line3))
printer.write(space_text(line3))
printer.feed(4)

#print(line1)
#print len(line1)
#printer.write(line1)
#printer.feed(4)

#print(line2)
#print len(line2)
#printer.write(line2)
#printer.feed(4)

#print(line3)
#print len(line3)
#printer.write(line3)
#printer.feed(4)

printer.boldOff()