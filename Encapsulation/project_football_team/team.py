from Encapsulation.project_football_team.player import Player


class Team:
    def __init__(self, name: str, rating: int):
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player):
        if player not in self.__players:
            self.__players.append(player)
            return f"Player {player.name} joined team {self.__name}"
        return f"Player {player.name} has already joined"

    def remove_player(self, player_name: str):
        if self.__players:
            for pl in self.__players:
                if player_name == pl.name:
                    self.__players.remove(pl)
                    return pl
                else:
                    return f"Player {player_name} not found"
        else:
            return f"Player {player_name} not found"