class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.persons = {}

    def show_content(self):
        self.show_description()
        self.show_exits()
        self.show_persons()

    def show_description(self):
        print(self.description)

    def show_persons(self):
        for person in self.persons:
            self.persons[person].show_description()

    def show_exits(self):
        for direction in ["Norden", "Osten", "Süden", "Westen"]:
            if direction.lower() in self.exits:
                print("🚪 Tür in Richtung", direction)

    def set_exits(self, exits):
        self.exits = exits

    def set_persons(self, persons):
        self.persons = persons

    def greet_person(self, name):
        if name not in self.persons:
            print(
                "Hier gibt es keine Person mit den Namen",
                name,
                "die ich grüßen könnte.",
            )
            return
        print("Hallo, du!")
        self.persons[name].say_hello()

    def ask_person(self, name):
        if name not in self.persons:
            print("Hier gibt es keinen", name, "den ich fragen könnte.")
            return
        print("Sag mal, wie bist du zur Software Entwicklung gekommen?")
        self.persons[name].tell_story()
