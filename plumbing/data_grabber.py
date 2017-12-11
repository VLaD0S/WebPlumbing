from django_cron import CronJobBase, Schedule
from bs4 import BeautifulSoup
import os
import wget


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    code = "review_extractor"

    file_url = "https://www.mybuilder.com/profile/view/fgneacsu/feedback"
    reviews_name = "reviews.html"


    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'plumbing.data_grabber'

    try:
        os.remove(reviews_name)
        print("New reviews loaded...")
    except FileNotFoundError:
        print("No Old reviews loaded. Pulling data...")

    def createSoup(url, file):
        file_name = wget.download(url, file)
        html_content = open(file, "r")
        return BeautifulSoup(html_content, 'html.parser')

    review_box = createSoup(file_url, reviews_name).find_all("div", attrs={'itemprop':'review'})

    for review in review_box:
        review_text = review.find("span", attrs={'itemprop': 'description'})
        review_author = review.find("span", attrs={'itemprop': 'author'})
        review_date = review.find("em", attrs={'class': 'date'})
        print("")
        print(review_text.get_text())
        print(review_author.get_text(), " ", review_date.get_text())



    def do(self):

        print("Cron Job Done?")


        



            