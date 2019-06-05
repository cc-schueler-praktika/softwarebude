from person import Person
from room import Room


class Map:

    def __init__(self):
        self.rooms = []
        self.init_rooms()
        self.current_room = self.rooms[0]
        self.enter_room(self.current_room)

    def init_rooms(self):
        stairwell = Room('Treppenhaus',
                         'Das Treppenhaus. Nicht viel los hier. Aber hey, da steht eine Tür offen.'
                         'Aus dem Büro hört man leise Stimmen. Hinter dir fährt der Aufzug wieder nach unten.'
                         )
        office = Room('Büro',
                      'Das Büro. In diesem Büro ist alles ziemlich dunkel. Viele Schreibtische gibt es hier'
                      'Vereinzelt sitzen Personen zusammen und besprechen Dinge. Einer trinkt Kaffee.'
                      )
        kitchen = Room('Küche',
                       'Die Küche. Hier duftet es nach frischem Kaffee. Ein großes Tisch lädt zum Verweilen ein.'
                       )
        server_room = Room('Serverraum', 'Der Serverraum. Ganz schön viele Kabel liegen hier ...')

        emergancy_exit = Room ('Notausgang',
                               'Der Notausgang! Die Sonne scheint und die Vögel zwitschern.')


        stairwell.set_exits({'norden': office, 'süden':emergancy_exit})
        office.set_exits({'süden': stairwell, 'osten': kitchen, 'westen': server_room})
        kitchen.set_exits({'westen': office})
        server_room.set_exits({'osten': office})
        emergancy_exit.set_exits({'norden':stairwell})

        office.set_persons({
            'robin': Person('Robin',
                            '🧐‍‍',
                            'Ich habe nach etwas gesucht, das mich jeden Tag etwas Neues herausfinden lässt.'
                            'Ein "Knobeln" auf Lebenszeit. 😄 Als ich dann bei ein paar Freunden gesehen habe wie'
                            'viel Spaß sie beim Programmieren in der Schule hatten dachte ich mir, das könnte was'
                            'für mich sein und habe mich für das Studium beworben. Es hat geklappt. 😉'
                            ),
            'julius': Person('Julius',
                             '👨',
                             'Ich habe mich schon immer für Technik und Computer interessiert. Programmieren habe ich'
                             ' aber erst in einer AG in der 10. Klasse gelernt. Das hat mir von Anfang an unheimlich'
                             ' viel Spaß gemacht und mich seitdem nicht mehr losgelassen.'
                             ),
        })

        kitchen.set_persons({
            'ralf': Person('Ralf',
                           '🤠',
                           'Mit 12 Jahren habe ich einen gebrauchten Rechner von meinem Bruder geschenkt bekommen'
                           'und so richtig fasziniert war ich dann später vom C64, auf dem ich dann die ersten'
                           'Text-Adventures (wie dieses) geschrieben habe. Die Möglichkeiten "echte" Probleme,'
                           'wie die Tennisplanung meines Vaters schnell zu lösen, haben mich motiviert mich in diesem'
                           'Thema weiter zu entwicklen.')
        })

        emergancy_exit.set_persons({
            'peter':Person('Peter',
                           'am rauchen',
                           'Mit 15 Jahren habe ich meine Ausbildung angefangen. Schnell wurde mir klar, dass man '
                           'um den Bereich der Informatik nicht mehr drum herum kommt. Also habe ich IT studiert.')
        })

        self.rooms = [stairwell, office]

    def go_in_direction(self, direction=None):
        if not direction or direction not in self.current_room.exits:
            print('Ich kann da nicht hin gehen.')
            return
        self.enter_room(self.current_room.exits[direction])

    def enter_room(self, room):
        print('🚪 Öffne Tür zu Raum', room.name)
        self.current_room = room
        self.current_room.show_description()

    def look(self, somewhere):
        self.current_room.show_content()

    def greet_person(self, name):
        self.current_room.greet_person(name)

    def ask_person(self, name):
        self.current_room.ask_person(name)
