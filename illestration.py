"""
** Author: Xiao Yue
** Date: 2020-08-23
"""

import matplotlib.pyplot as plt

class Illestrator():
    def __init__(self):
        pass

    def spendByCategory(self, spend_by_category):
        total_spend = 0
        for category in spend_by_category:
            total_spend += sum(spend_by_category[category])
        labels = []
        sizes = []
        for category in spend_by_category:
            labels.append(category)
            sizes.append(sum(spend_by_category[category]) / total_spend)

        explode = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')
        plt.show()

    def draw_figures(self, monthly_spend_sum, daily_spend_sum):
        plt.figure(figsize=(16, 8))
        plt.subplot(221)
        plt.bar(monthly_spend_sum.keys(), monthly_spend_sum.values())
        plt.title('Monthly Spend')

        plt.subplot(222)
        average_daily_spend = dict()
        for month in monthly_spend_sum:
            average_daily_spend[month] = monthly_spend_sum[month] / 30
        plt.plot(average_daily_spend.keys(), average_daily_spend.values())
        plt.title("Averget Daily Spend")

        plt.subplot(223)
        plt.plot(daily_spend_sum.values())
        plt.title("Daily Spend")

        # plt.subplot(224)
        # plt.plot(total_assets.keys(), total_assets.values())
        # plt.title("Total Asset")

        plt.show()
