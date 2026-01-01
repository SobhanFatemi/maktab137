class Team:
    def __init__(self, name, players=None):
        if players is None:
            players = []
        self.name = name
        self.players = players

    def __len__(self):
        return len(self.players)
    
    def __add__(self, other):
        if not isinstance(other, Team):
            raise ValueError("Value must be a Team!")
        
        return Team(f"{self.name} & {other.name}", self.players + other.players)
    
    def __str__(self):
        return f"Team name: {self.name}\nPlayers: {', '.join(player for player in self.players)}"
    
    def __del__(self):
        print(f"'{self.name}' was deleted from memory!")


t1 = Team("Lions", ["Alice", "Bob"])
t2 = Team("Tigers", ["Charlie", "Dave"])

print(t1)

print(len(t2))  

t3 = t1 + t2
print(t3)