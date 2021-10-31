from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        if current_room:
            result = current_room.take_room(people)
            if not result:
                self.guests += people

    def free_room(self, room_number):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        self.guests -= current_room.guests
        current_room.free_room()

    def status(self):
        free_rooms = [r1.number for r1 in self.rooms if r1.is_taken == False]
        taken_rooms = [r1.number for r1 in self.rooms if r1.is_taken == True]
        return f"Hotel {self.name} has {self.guests} total guests\nFree rooms:" \
               f" {', '.join(map(str, free_rooms))}\nTaken rooms: {', '.join(map(str, taken_rooms))}"
