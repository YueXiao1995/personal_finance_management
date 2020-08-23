"""
** Author: Xiao Yue
** Date: 2020-08-23
"""
class Plan():
    def __init__(self):
        self.income_arrangement_plan = {
                                        '房租': 0.25,
                                        '一般消费预算': 0.1, # 1200
                                        '恋爱基金': 0.05,   # 600
                                        '特别预算': 0.1,    # 1200
                                        "可用投资资金": 0.5, # 6000
                                        }

        self.investment_plan = {
                                        "指数基金": 0.65, # 3900 （165/天）
                                        "货币基金": 0.1,  # 600  （20/天）
                                        "股票": 0.1,     # 600  （20/天）
                                        "债券": 0.1,     # 1200
                                        "贵金属": 0.05   # 300
                                        }
        self.total_asset_arrangement_plan = None

    def set_income_arrangement_plan(self, plan):
        self.income_arrangement_plan = plan

    def set_investment_plan(self, plan):
        self.investment_plan = plan

    def set_total_asset_arrangement_plan(self, plan):
        self.total_asset_arrangement_plan = plan

    def get_income_arrangement_plan(self):
        return self.income_arrangement_plan

    def get_investment_plan(self):
        return self.investment_plan

    def get_total_asset_arrangement_plan(self):
        return self.total_asset_arrangement_plan

    def save_plan_as_file(self):
        pass
