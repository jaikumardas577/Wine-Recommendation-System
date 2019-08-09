import sys, os 
import pandas as pd
import datetime


os.environ.setdefault("DJANGO_SETTINGS_MODULE","ml_with_Django.settings")

import django
django.setup()

from django.contrib.auth.models import User
from wine_recommender.models import Review, Wine 
# from django.contrib.auth

def save_user_from_row(user_row):
    user = User()
    user.id = user_row[0]+1
    user.username = user_row[1]
    # review.wine = Wine.objects.get(id=review_row[2])
    # review.rating = review_row[3]
    # review.pub_date = datetime.datetime.now()
    # review.comment = review_row[4]
    user.save()
    
    
if __name__ == "__main__":
    
    if len(sys.argv) == 2:
        print ("Reading from file " + str(sys.argv[1]))
        users_df = pd.read_csv(sys.argv[1])
        print (users_df)

        users_df.apply(
            save_user_from_row,
            axis=1
        )

        print ("There are {} reviews in DB".format(User.objects.count()))
        
    else:
        print ("Please, provide User file path")