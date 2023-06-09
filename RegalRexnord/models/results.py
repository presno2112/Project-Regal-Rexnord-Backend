from django.db import models
from ..models.user import User
from ..models.game import Game

class Results(models.Model): # asi se hace relacional como en el diagrama? es muchos a muchos models.ManyToManyField
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING) # models.ManyToManyField
    game = models.ForeignKey(Game, related_name="results" , on_delete=models.DO_NOTHING)
    time = models.FloatField(default=0.0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.first_name)