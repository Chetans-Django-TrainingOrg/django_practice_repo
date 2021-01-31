import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE","django_06ModelForms.settings")
import django
django.setup()
# print(os.environ["DBNAME"])
# print(os.environ["DBUSER"])
# print(os.environ["DBPASS"])
# print(os.environ["PORT"])

import random,faker
from moviesApp.models import Movie
fake = faker.Faker()

for i in range(50):
    releaseDate = fake.date()
    movieName = fake.word()
    starMale = fake.first_name_male()
    starFemale = fake.first_name_female()
    rating = random.randint(1,5)
    data = Movie.objects.create(releaseDate=releaseDate,movieName=movieName,starMale=starMale,starFemale=starFemale,rating=rating)