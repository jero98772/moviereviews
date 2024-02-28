from django.core.management.base import BaseCommand
from movie.models import Movie
import os
import json

class Command(BaseCommand):
    help = 'Load movies from movie_descriptions.json into the Movie model'

    def handle(self, *args, **kwargs):
        # Construct the full path to the JSON file
        #Recuerde que la consola está ubicada en la carpeta DjangoProjectBase.
        #El path del archivo movie_descriptions con respecto a DjangoProjectBase sería la carpeta anterior
        json_file_path = 'movie/management/commands/movies.json' 
        
        # Load data from the JSON file
        with open(json_file_path, 'r') as file:
            movies = json.load(file)
        
        # Add products to the database
        for i in range(100):
            movie = movies[i]
            exist = Movie.objects.filter(title = movie['title']).first() #Se asegura que la película no exista en la base de datos
            if not exist:              
                Movie.objects.create(title = movie['title'],
                                     image = 'movie/image/default.jpg',
                                     genre = movie['genre'],
                                     year = movie['year'])        
        
        #self.stdout.write(self.style.SUCCESS(f'Successfully added {cont} products to the database'))
                
                