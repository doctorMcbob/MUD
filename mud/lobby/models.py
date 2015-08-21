from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.gis.db import models as models


@python_2_unicode_compatible
class Game(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    max_characters = models.PositiveIntegerField()
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return "Game: " + self.name


@python_2_unicode_compatible
class Character(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    clas = models.CharField(
        max_length=20,
        choices=(
            ('fighter', 'fighter'),
            ('wizard', 'wizard'),
            ('healer', 'healer'),
        ),
        default='fighter'
    )
    hp = models.IntegerField()
    st = models.IntegerField()
    df = models.IntegerField()
    game = models.ForeignKey(Game)

    def __str__(self):
        return "Character: " + self.name
