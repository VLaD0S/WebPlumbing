from __future__ import absolute_import, unicode_literals
import os
import django

#model imports
from plumbing.models import Review
import string

#Celery imports
from celery import task
from celery import shared_task
from celery import Celery

#Pulling reviews soup/wget imports
from bs4 import BeautifulSoup
import wget

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebPlumbin.settings')
django.setup()


##getting reviews from MyBuilder
file_url = "https://www.mybuilder.com/profile/view/fgneacsu/feedback"
reviews_name = "reviews.html"

''' The following methods are responsible for downloading the HTML page specified in the file URL,
navigating through it, extracting the relevant bits and populating the DB with the info.    
'''

#Creates soup. returns it
def createSoup(url, file):
    file_name = wget.download(url, file)
    html_content = open(file, "r")
    return BeautifulSoup(html_content, 'html.parser')

#calls createSoup to pull reviews. Returns them in a review_box
def pullReviews():
    try:
        os.remove(reviews_name)
        print("New reviews loaded...")
    except FileNotFoundError:
        print("No Old reviews loaded. Pulling data...")

    review_box = createSoup(file_url, reviews_name).find_all("div", attrs={'itemprop':'review'})
    print("Data successfully pulled")
    return review_box
    

#creates a review, given the params.
def reviewCreator(desc, auth, dt):
    data = Review.objects.get_or_create(description=desc, author=auth, date=dt)[0]
    print("Saving Review")
    data.save()
    return data
    
def populate():
    review_box = pullReviews()
    count = 0
    for review in review_box:

        review_text = review.find("span", attrs={'itemprop': 'description'})
        review_author = review.find("span", attrs={'itemprop': 'author'})
        review_date = review.find("em", attrs={'class': 'date'})

        description = str(review_text.get_text())
        author = str(review_author.get_text())
        date = str(review_date.get_text())


        reviewCreator(description, author, date)       
        count = count + 1
        print(count)


@shared_task(name="populate_reviews")
def populate_reviews():
    populate()
    print("population complete")

