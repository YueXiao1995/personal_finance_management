"""
** Author: Xiao Yue
** Date: 2020-08-23
"""

import data
import illestration
import statistic
import plan

current_month = '2020-09'

# Load Data
# ----------------------------------------------------------------------------------------------------------------------
data_manager = data.DataManager()

daily_spend_sum = data_manager.get_daily_spend_sum()
monthly_spend_sum = data_manager.get_monthly_spend_sum()
spend_by_category = data_manager.get_spend_by_category_by_month(current_month)
income = data_manager.get_monthly_income_by_month(current_month)

# Load Plan
# ----------------------------------------------------------------------------------------------------------------------
plan_manager = plan.PlanManager()

income_arrangement_plan = plan_manager.get_income_arrangement_plan()
investment_plan = plan_manager.get_investment_plan()
total_asset_arrangement_plan = plan_manager.get_total_asset_arrangement_plan()

# Display Figure
# ----------------------------------------------------------------------------------------------------------------------
illestrator = illestration.Illestrator()
illestrator.spendByCategory(spend_by_category)
illestrator.draw_trend(monthly_spend_sum, daily_spend_sum)

# Show Statistic Result
# ----------------------------------------------------------------------------------------------------------------------

def print_monthly_bill_of_each_category(spend_by_category):
    print("************************** bills by category of " + current_month + " *****************************")
    for category in spend_by_category:
        print(category + ": " + str(round(sum(spend_by_category[category]), 2)))

def print_income_arrangement_plan(income_arrangement_plan, income):
    print("*********************** income arrangement plan of " + current_month + " **************************")
    income = sum(income)
    for category in income_arrangement_plan['固定开支']:
        income -= round(income_arrangement_plan['固定开支'][category], 2)
        print(category + ": " + str(round(income_arrangement_plan['固定开支'][category], 2)))

    for category in income_arrangement_plan['非固定开支']:
        print(category + ": " + str(round(income_arrangement_plan['非固定开支'][category] * income, 2)))

def print_investment_plan(investment_plan, amount):
    print("**************************** investment plan of " + current_month + " *****************************")
    for category in investment_plan:
        print(category + ": " + str(round(investment_plan[category] * amount, 2)))

print("****************************** total spend of " + current_month + " *******************************")
print(round(monthly_spend_sum[current_month], 2))

print_monthly_bill_of_each_category(spend_by_category)

print_income_arrangement_plan(income_arrangement_plan, income)

print_investment_plan(investment_plan, plan_manager.get_investment_amount(income))

print("**************************** statistic result of " + current_month + " ****************************")
statistican = statistic.Statistician()
print('恩格尔系数：' + str(statistican.engel_coefficient(spend_by_category, monthly_spend_sum[current_month])))

"""
import plotly.express as px
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig = px.pie(df, values='pop', names='country', title='Population of European continent')
fig.show()
"""
