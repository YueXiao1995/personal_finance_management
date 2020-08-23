"""
** Author: Xiao Yue
** Date: 2020-08-23
"""

import matplotlib.pyplot as plt
import data
import illestration
import statistic

"""
Load data
"""
data_manager = data.DataManager()

daily_spend_sum = data_manager.get_daily_spend_sum()
monthly_spend_sum = data_manager.get_monthly_spend_sum()
spend_by_category_in_Auguest = data_manager.get_spend_by_category_by_month('2020-08')

"""
Display
"""
illestrator = illestration.Illestrator()
illestrator.spendByCategory(spend_by_category_in_Auguest)
illestrator.draw_figures(monthly_spend_sum, daily_spend_sum)

statistican = statistic.Statistician()
print('恩格尔系数：' + str(statistican.engel_coefficient(spend_by_category_in_Auguest, monthly_spend_sum['2020-08'])))

"""
import plotly.express as px
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
fig.show()
"""

def get_monthly_bill_of_each_category(spend_by_category):

    for category in spend_by_category:
        print(category + ": " + str(round(sum(spend_by_category[category]), 2)))

print(get_monthly_bill_of_each_category(spend_by_category_in_Auguest))
print(round(monthly_spend_sum['2020-08'], 2))
