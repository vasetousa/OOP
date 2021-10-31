from Class_and_static_methods.project_hotel_rooms.room import Room


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

    def take_room(self, room_number, people):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        if current_room:
            if current_room.capacity >= people and current_room.is_taken == False:
                current_room.is_taken = True
                self.guests += people

    def free_room(self, room_number):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        if current_room:
            if current_room.is_taken:
                current_room.is_taken = False
                self.guests -= current_room.guests

    def status(self):
        free_rooms = [r1.number for r1 in self.rooms if r1.is_taken == False]
        taken_rooms = [r1.number for r1 in self.rooms if r1.is_taken == True]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(map(str, free_rooms))}\n" \
               f"Taken rooms: {', '.join(map(str, taken_rooms))}"


