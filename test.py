from countdown import Countdown
from escape_room import EscapeRoom
from task import Task
from room import Room
import time
import threading


task = Task('Was ist 2 + 2?', 4)

server_room = Room('Serverraum', 'Der Serverraum. Ganz schön viele Kabel liegen hier ...')

escape_room = EscapeRoom('Arbeitspaltz',
                         'Das ist ein Arbeitsplatz. Hier knobeln die Mitarbeiter an Schwierigen aufgaben.'
                         , task)

escape_room.escape_room_intro()



