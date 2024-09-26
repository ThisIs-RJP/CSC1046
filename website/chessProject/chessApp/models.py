from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Player model: person playing the game
# Game model: to track game session and link the two players, maage turns and track game status
# Board model: stores state of the chessboard
# Piece model: rep individual chess piece on the board
# Move model: Store history of moves


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField('Email', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

class Game(model.Model):
    id = models.AutoField(primary_key=True)
    white_player = models.ForeignKey(User, related_name='white_player', on_delete=models.CASCADE)
    black_player = models.ForeignKey(User, related_name='black_player', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('ONGOING', 'Ongoing'), ('FINISHED', 'Finished')], default='ONGOING')
    winner = models.ForeignKey(User, related_name='winner', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.white_player} vs {self.black_player} - {self.status}"

class Piece(models.Model):
    id = models.AutoField(primary_key=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    color = models.CharField(max_length=5)
    position = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.color} {self.type} at {self.position}"

class Move(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, related_name='moves', on_delete=models.CASCADE)
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    start_position = models.CharField(max_length=2)
    end_position = models.CharField(max_length=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.piece} moved from {self.start_position} to {self.end_position}"

class Board(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    state = models.JSONField() 

    def __str__(self):
        return f"Board for Game {self.game.id}"
