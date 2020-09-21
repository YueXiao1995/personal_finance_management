"""
** Author: Xiao Yue
** Date: 2020-08-23
"""
class PlanManager():
    def __init__(self):
        self.income_arrangement_plan = {
                                        '固定开支': {
                                                    '房租': 3430
                                                    },
                                        '非固定开支': {
                                                    '一般消费预算': 0.15, # 1200
                                                    '恋爱基金': 0.1,  # 600
                                                    '特别预算': 0.15,  # 1200
                                                    "投资预算": 0.6,  # 6000
                                                    },
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

    def get_investment_amount(self, income):
        fixed_spend = sum(self.income_arrangement_plan['固定开支'].values())
        return self.income_arrangement_plan['非固定开支']['投资预算'] * (sum(income) - fixed_spend)
