from django.shortcuts import render
from django.http import HttpResponse
from .models import UserProfile, Game

# Create your views here.
def home(request):
    return HttpResponse("this is home page of game. For creating User go to '/game/create_user',For deleting user go to '/game/delete_user',For update user go to '/game/update_user',Go to '/game/user_login' For User Login,")

def create_user(request):
    return HttpResponse("This will create User")

def delete_user(request,userid):
    return HttpResponse("this will delete user")

def update_user(reqest,user_id):
    return HttpResponse("thhis will update user_id")

def user_login(request,user_id):
    return HttpResponse("user loged in")

def start_game(request):
    game=Game()

def get_board(request, game_id):
    return 

def update_board(request, game_id):
    return 
    # get the game object using its id and then call the method to update the board 
