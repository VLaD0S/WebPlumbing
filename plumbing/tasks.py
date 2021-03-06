from __future__ import absolute_import, unicode_literals
import os
import django
import urllib.request
from plumbing.models import review, contact, incrementer
from celery import shared_task
from bs4 import BeautifulSoup
from django.conf import settings
from django.core.mail import send_mail
from datetime import datetime


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebPlumbing.settings')
django.setup()


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
    data = review.objects.get_or_create(description=desc, author=auth, date=dt)[0]
    data.save()

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
    print('Fetching HTML page...', end="", flush=True)
    review_box, tempfile_name = createsoup(mybuilder_url)
    print('Done')
    print('Extracting reviews...')
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

        print('review: {} '.format(count), end='\r')

    tempdelete(tempfile_name)
    print("Done")



@shared_task(name="send_contact_email")
def send_contact_email(contact):
    subject = "No Reply: FGN Plumbing & Heating"
    from_email = settings.EMAIL_HOST_USER
    to_email = [contact.email]
    message = "Hi " + contact.name + "!\n"
    message += "Thank you for contacting me. I will reply at my earliest available time.\n Below is a copy of your message:\n \n"
    message += contact.message + "\n \n"
    message += "Please do not reply at this message. \n http://fgnplumbing.co.uk"
    send_mail(subject=subject, from_email=from_email, message=message, recipient_list=to_email, fail_silently=False)

def get_incrementer():
    if not incrementer.objects.filter(name='query_counter').exists():
       inc = incrementer(name='query_counter', value=0)
       inc.save()
    inc = incrementer.objects.get(name='query_counter')
    inc.value += 1
    query = inc.value
    inc.save()
    return query



@shared_task(name="send_self")
def send_self():
    email_logger = 0
    did = False
    for cont in contact.objects.all():
        if cont.initiate == False:
            did = True
            query_no = get_incrementer()
            subject = "Q:" + str(query_no) +". From:" +str(cont.name)
            from_email = settings.EMAIL_HOST_USER
            to_email = ['fgnplumbing@gmail.com']
            message = "Query Number: " + str(query_no) + "\n"
            message += "New message from: " + str(cont.name) + "\n"
            message += "email: " + str(cont.email) + "\n"
            message += "phone: " + str(cont.phone) + "\n"
            message += "Message: \n"
            message += str(cont.message)
            send_mail(subject=subject, from_email=from_email, message=message, recipient_list=to_email,
                      fail_silently=False)
            email_logger += 1
            cont.initiate = True
            cont.save()
    if did == True:
        print("Sent "+str(email_logger)+" new emails at " + str(datetime.now()))

@shared_task(name="populate_reviews")
def populate_reviews():
    populate()
    print("Review Table update completed.")

