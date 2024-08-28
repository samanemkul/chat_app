from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=50, default=0)
    def __str__(self):
        return self.room_name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default=0)
    sender = models.CharField(max_length=50,  default=0)
    message = models.TextField()
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.room)} - {self.sender}"
