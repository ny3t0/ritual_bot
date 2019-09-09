# printer setup
import board
import busio

import adafruit_gps

import serial
uart = serial.Serial("/dev/serial0", baudrate=19200, timeout=3000)
# uart = busio.UART(RX, baudrate=19200, timeout=3000)

import adafruit_thermal_printer
ThermalPrinter = adafruit_thermal_printer.get_printer_class(2.69)

printer = ThermalPrinter(uart, auto_warm_up=False)
printer.warm_up(12)
printer.print("Some bullshit to get rid of the x(J crap?")
printer.feed(2)

import random

places = ['apartment', 'bathroom', 'cabin', 'cell', 'community garden', 'community pool', 'condo', 'cottage', 'ditch', 'dream', 'environment', 'fish tank', 'friend\'s basement', 'grave', 'house', 'local grocery store', 'local library', 'local park', 'river', 'roof', 'school bus', 'womb', 'workplace']

adjectives = ['charming', 'chilly', 'conflicted', 'damp', 'dusty', 'frivolous', 'glamorous', 'glowing', 'gruesome', 'languid', 'lovely', 'medium', 'messy', 'modern', 'orange', 'ripe', 'rural', 'sad', 'silly', 'sparkly', 'suspicious', 'tasty', 'ugly', 'uncaring', 'underdeveloped', 'unfortunate', 'warm']

verbs = ['annotate', 'avoid', 'bake', 'browse', 'brush', 'burn', 'caress', 'check', 'confess', 'contemplate', 'criticize', 'deny', 'drink', 'eat', 'email', 'feed', 'find', 'forget', 'gamble', 'hear', 'hide from', 'ignore', 'lose', 'lubricate', 'observe', 'part from', 'perform', 'pet', 'pray to', 'press', 'put on', 'question', 'read', 'rearrange', 'rescue', 'restart', 'restore', 'share', 'solve', 'spend', 'steal', 'stop', 'synthesize', 'touch', 'visit', 'wash', 'watch', 'wrestle with', 'write']

moveVerbs = ['amble', 'climb', 'crawl', 'drive', 'escape', 'inch', 'jump in', 'limp', 'march', 'moonwalk', 'prowl', 'ride', 'roll', 'run', 'shimmy','shuffle', 'skate', 'sleepwalk', 'sneak', 'stomp', 'stride', 'strut', 'stumble', 'swim', 'trek', 'walk']

nouns = ['alarm', 'bra', 'breakfast', 'breath', 'cat', 'coffee', 'colonizer', 'crossword', 'cup of water', 'dog', 'elevator button', 'email', 'enemy', 'family', 'future', 'government', 'hope', 'identity', 'income', 'information', 'local news', 'love', 'lover', 'mail', 'meds', 'memory', 'papers', 'phone', 'printer', 'problems', 'reflection', 'roommate', 'sexuality', 'socks', 'spouse', 'sweater', 'teeth', 'television', 'text', 'time', 'toothbrush', 'twin', 'window']

adverbs = ['adequately', 'aggressively', 'automatically', 'begrudgingly', 'carefully', 'carelessly', 'cheerfully', 'dejectedly', 'deliciously', 'delusionally', 'disastrously', 'ethically', 'exclusively', 'gently', 'hastily', 'hypnotically', 'internally', 'loudly', 'lovingly', 'mischievously', 'necessarily', 'notoriously', 'obsessively', 'poorly', 'precariously', 'problematically', 'punctually', 'religiously',
'reluctantly', 'repeatedly', 'secretly', 'shamefully', 'shamelessly', 'soulfully', 'suspiciously', 'tastefully', 'thoughtfully', 'thoughtlessly', 'timidly', 'unfortunately', 'unwillingly']

# wake up in your (adjective) (place). (verb) your (noun) (adverb). (moveVerb) to your (place).
# print
line1 = (f"wake up in your {random.choice(adjectives)} {random.choice(places)}.")
line2 = (f"{random.choice(verbs)} your {random.choice(nouns)} {random.choice(adverbs)}.")
line3 = (f"{random.choice(moveVerbs)} to your {random.choice(places)}.")

print(line1)
printer.print(line1)
printer.feed(2)

print(line2)
printer.print(line2)
printer.feed(2)

print(line3)
printer.print(line3)
printer.feed(2)