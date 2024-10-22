import justpy as jp
import os
from charts import avg_day_rating, avg_week_rating, avg_month_rating, num_ratings_month, num_ratings


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Udemy Courses Data",
                 classes="text-h1 q-pa-md text-center")

    wp.add_component(avg_day_rating)
    wp.add_component(avg_week_rating)
    wp.add_component(avg_month_rating)
    wp.add_component(num_ratings_month)
    wp.add_component(num_ratings)
    return wp


port = int(os.environ.get("PORT", 8000))
jp.justpy(app, host='0.0.0.0', port=port)
