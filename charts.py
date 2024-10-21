import pandas
import justpy as jp
from charts_definition import avg_rat_day_chart, avg_rat_week_chart, avg_rat_month_chart, num_ratings_month_crs_chart, num_ratings_course_chart

data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])

"""
Dataframe for average rating per day chart
"""
data["Day"] = data["Timestamp"].dt.date
day_average = data.groupby(["Day"])["Rating"].mean()

wp = jp.QuasarPage()
avg_day_rating = jp.HighCharts(a=wp, options=avg_rat_day_chart)

avg_day_rating.options.xAxis.categories = list(day_average.index)
avg_day_rating.options.series[0].data = list(day_average.values)

"""
Dataframe for average rating per week chart
"""
data["Week"] = data["Timestamp"].dt.strftime("%Y-%U")
week_average = data.groupby(["Week"])["Rating"].mean()

avg_week_rating = jp.HighCharts(a=wp, options=avg_rat_week_chart)

avg_week_rating.options.xAxis.categories = list(week_average.index)
avg_week_rating.options.series[0].data = list(week_average.values)

"""
Dataframe for average rating per month chart
"""
data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")
month_average = data.groupby(["Month"])["Rating"].mean()

avg_month_rating = jp.HighCharts(a=wp, options=avg_rat_month_chart)
avg_month_rating.options.xAxis.categories = list(month_average.index)
avg_month_rating.options.series[0].data = list(month_average.values)

"""
Dataframe for number of ratings per month for each course chart
"""
data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")
num_ratings_month_crs = data.groupby(["Month", "Course Name"])[
    "Rating"].count().unstack()

num_ratings_month = jp.HighCharts(a=wp, options=num_ratings_month_crs_chart)

num_ratings_month.options.xAxis.categories = list(num_ratings_month_crs.index)

chart_data = [{"name": name, "data": [v2 for v2 in num_ratings_month_crs[name]]}
              for name in num_ratings_month_crs.columns]
num_ratings_month.options.series = chart_data


"""
Dataframe for number of ratings of each course
"""
num_ratings_crs = data.groupby(["Course Name"])["Rating"].count()

num_ratings = jp.HighCharts(a=wp, options=num_ratings_course_chart)

chart_data = [{"name": name, "y": int(ratings)}
              for name, ratings in zip(num_ratings_crs.index, num_ratings_crs.values)]
num_ratings.options.series[0].data = chart_data
