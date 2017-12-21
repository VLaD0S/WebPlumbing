from __future__ import absolute_import, unicode_literals
import os
import django
import urllib.request

#model imports
from plumbing.models import Review


#Celery imports
from celery import task
from celery import shared_task


#Pulling reviews soup/wget imports
from bs4 import BeautifulSoup
import wget

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebPlumbing.settings')
django.setup()




''' 
***


The following methods are responsible for downloading the HTML page specified in the file URL,
navigating through it, extracting the relevant bits and populating the DB with the info.  


@SECURITY THREAT!!


***NEEDS UNIT TESTING - is highly dependant on the naming conventions used on the main site
in order to extract the data correctly.
  
'''


#getting reviews from MyBuilder
mybuilder_url = "https://www.mybuilder.com/profile/view/fgneacsu/feedback"
reviews_name = "reviews.html"


#creates a delicious soup
def createsoup(url):
    local_filename, headers = urllib.request.urlretrieve(url)
    reviews_html = open(local_filename)
    soup = BeautifulSoup(reviews_html, 'html.parser')
    refined_soup = soup.find_all("div", attrs={'itemprop':'review'})
    return refined_soup, local_filename


#creates a review in the database.
def reviewCreator(desc, auth, dt, rev_no):
    data = Review.objects.get_or_create(description=desc, author=auth, date=dt)[0]
    data.save()
    print("...saved review .no: " + str(rev_no))
    return data


#Deletes html grabbed by urllib
def tempdelete(file):
    print("Attempting to delete temporary file")
    try:
        os.remove(file)
        print("Temporary html file deleted successfully!")
    except FileNotFoundError:
        print("Failed to remove temporary html file!")

#logic populating the database with reviews
def populate():
    review_box, tempfile_name = createsoup(mybuilder_url)
    count = 0
    for review in review_box:

        review_text = review.find("span", attrs={'itemprop': 'description'})
        review_author = review.find("span", attrs={'itemprop': 'author'})
        review_date = review.find("em", attrs={'class': 'date'})

        description = str(review_text.get_text())
        author = str(review_author.get_text())
        date = str(review_date.get_text())

        reviewCreator(description, author, date, count)

        count = count + 1

    tempdelete(tempfile_name)


@shared_task(name="populate_reviews")
def populate_reviews():
    populate()
    print("Review Table update completed.")




