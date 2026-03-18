from tortoise import fields
from tortoise.models import Model

from stariodemo.DataStructsPkg.UserModule import User


class Tournament(Model):
    # Defining `id` field is optional, it will be defined automatically
    # if you haven't done it yourself
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)


class Event(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)
    # References to other models are defined in format
    # "{app_name}.{model_name}" - where {app_name} is defined in the tortoise config
    tournament = fields.ForeignKeyField("models.Tournament", related_name="events")
    participants = fields.ManyToManyField("models.Team", related_name="events", through="event_team")


class Team(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=255)


TortoiseDbUsers = [
    User(id="1u8dh29", username="gary", color="red"),
    User(id="0sgah72", username="thabo", color="blue"),
    User(id="77h8sho", username="fido", color="green"),
    User(id="8bcuyy6", username="sue", color="red"),
]
