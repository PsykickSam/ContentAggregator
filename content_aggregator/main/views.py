from django.shortcuts import render
from background_task import background

from .scraper import scrap
from .database import database as db

import itertools

# Methods
# @background(schedule=0)
def run_on_homepage():
    yahoo_5 = dict(itertools.islice(scrap.scrap_yahoo_news().items(), 5))
    db.save_to_database(scrap.scrap_yahoo_news())

    print("\n\nData:\n", yahoo_5, "\nEnd\n\n")
    return yahoo_5
    
# Create your views here.
def homepage(request):
    yahoo_5 = run_on_homepage()

    return render(request, 'index.html', {
        'yahooNews': yahoo_5,  
    })  