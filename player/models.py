from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    forename = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.forename} {self.name}"

    @property
    def total_points(self):
        return sum(match.points for match in self.matches.all())

    @property
    def total_assists(self):
        return sum(match.assists for match in self.matches.all())

    @property
    def total_rebounds(self):
        return sum(match.rebounds for match in self.matches.all())
    @property
    def total_steals(self):
        return sum(match.steals for match in self.matches.all())

    @property
    def total_blocks(self):
        return sum(match.blocks for match in self.matches.all())

    @property
    def total_turnovers(self):
        return sum(match.turnover for match in self.matches.all())

    @property
    def total_efficiency(self):
        return sum(match.efficiency for match in self.matches.all())

    @property
    def total_minutes(self):
        return sum(match.time for match in self.matches.all())
    
    @property
    def total_threes(self):
        return sum(match.three for match in self.matches.all())

    @property
    def total_threes_made(self):
        return sum(match.three_made for match in self.matches.all())

    @property
    def total_twos(self):
        return sum(match.two for match in self.matches.all())

    @property
    def total_twos_made(self):
        return sum(match.two_made for match in self.matches.all())

    @property
    def total_ones(self):
        return sum(match.one for match in self.matches.all())

    @property
    def total_ones_made(self):
        return sum(match.one_made for match in self.matches.all())

    @property
    def total_more_one(self):
        return sum(match.more_one for match in self.matches.all())
    @property
    def average_points(self):
        return self.total_points / self.total_more_one if self.total_more_one > 0 else 0

    @property
    def average_assists(self):
        return self.total_assists / self.total_more_one if self.total_more_one > 0 else 0

    @property
    def average_rebounds(self):
        return self.total_rebounds / self.total_more_one if self.total_more_one > 0 else 0

    @property
    def average_steals(self):
        return self.total_steals / self.total_more_one if self.total_more_one > 0 else 0

    @property
    def average_blocks(self):
        return self.total_blocks / self.total_more_one if self.total_more_one > 0 else 0

    @property
    def average_turnovers(self):
        return self.total_turnovers / self.total_more_one if self.total_more_one > 0 else 0

    @property
    def average_efficiency(self):
        return self.total_efficiency / self.total_more_one if self.total_more_one > 0 else 0

    @property
    def average_minutes(self):
        return self.total_minutes / self.total_more_one if self.total_more_one > 0 else 0
    
    @property
    def average_threes(self):
        return (self.total_threes / self.total_threes_made) * 100 if self.total_more_one > 0 else 0

    @property
    def average_twos(self):
        return (self.total_twos / self.total_twos_made) * 100 if self.total_more_one > 0 else 0

    @property
    def average_ones(self):
        return (self.total_ones / self.total_ones_made) * 100 if self.total_more_one > 0 else 0



class Match(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="matches")
    points = models.IntegerField()
    assists = models.IntegerField()
    rebounds = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    turnover = models.IntegerField()
    three = models.IntegerField()
    three_made = models.IntegerField()
    two = models.IntegerField()
    two_made = models.IntegerField()
    one = models.IntegerField()
    one_made = models.IntegerField()
    efficiency = models.IntegerField()
    time = models.IntegerField(default=0)  # or another default value

    
    # Ajout des champs supplémentaires pour les types de matchs
    more_one = models.IntegerField()
    playoff = models.BooleanField(default=False)
    club = models.BooleanField(default=False)
    equipe = models.BooleanField(default=False)
    reguliere = models.BooleanField(default=True)
    ligue_2 = models.BooleanField(default=False)
    ligue_1 = models.BooleanField(default=False)

    def __str__(self):
        return f"Match de {self.player} - Points: {self.points}"

# vues
# player = Player.objects.get(id=1)
# total_points = player.total_points
# total_assists = player.total_assists

# templates
# <p>Total Points: {{ player.total_points }}</p>
# <p>Total Assists: {{ player.total_assists }}</p>
# <p>Total Rebounds: {{ player.total_rebounds }}</p>
