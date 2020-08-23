"""
** Author: Xiao Yue
** Date: 2020-08-23
"""

class Statistician():
    def __init__(self):
        pass

    def engel_coefficient(self, spend_by_category, monthly_spend_sum):
        return round(sum(spend_by_category['food']) / (monthly_spend_sum + sum(spend_by_category['rent'])), 2)


