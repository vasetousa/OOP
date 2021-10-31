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
            current_room.take_room(people)

    def free_room(self, room_number):
        current_room = [r for r in self.rooms if r.number == room_number][0]
        if current_room:
            current_room.free_room()

    def status(self):
        free_rooms = [r1.number for r1 in self.rooms if not r1.is_taken]
        taken_rooms = [r1.number for r1 in self.rooms if r1.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(map(str, free_rooms))}\n" \
               f"Taken rooms: {', '.join(map(str, taken_rooms))}"


