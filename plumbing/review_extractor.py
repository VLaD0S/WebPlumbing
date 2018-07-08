
from bs4 import BeautifulSoup
import os
import wget

#Setup
file_url = "https://www.mybuilder.com/profile/view/fgneacsu/feedback"
reviews_name = "reviews.html"



def createSoup(url, file):
    file_name = wget.download(url, file)
    html_content = open(file, "r")
    return BeautifulSoup(html_content, 'html.parser')
#End Setup

"""
class GetReviews(self):
    try:
        os.remove(global.reviews_name)
        print("New reviews loaded...")
    except FileNotFoundError:
        print("No Old reviews loaded. Pulling data...")

    review_box = createSoup(global.file_url, global.reviews_name).find_all("div", attrs={'itemprop':'review'})

    

    def printer(self, review_box):
        for review in review_box:
            review_text = review.find("span", attrs={'itemprop': 'description'})
            review_author = review.find("span", attrs={'itemprop': 'author'})
            review_date = review.find("em", attrs={'class': 'date'})
            print("")
            print(review_text.get_text())
            print(review_author.get_text(), " ", review_date.get_text())

"""


    