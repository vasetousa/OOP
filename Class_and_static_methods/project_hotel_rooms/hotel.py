from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number: int, people: int):
        for room in self.rooms:
            if room.number == room_number:
                result = room.take_room(people)
                if not result:
                    self.guests += people

    def free_room(self, room_number):
        for rr in self.rooms:
            if rr == room_number:
                self.guests -= rr.guests
                rr.free_room()

    def status(self):
        nl = "\n"

        free_rooms = [r.number for r in self.rooms if r.is_taken==False]
        taken_rooms = [r.number for r in self.rooms if r.is_taken==True]
        string = f"Hotel {self.name} has {self.guests} total guests\n" \
                 f"Free rooms: {', '.join(map(str, free_rooms))}\n" \
                 f"Taken rooms: {', '.join(map(str, taken_rooms))}"

        return string

