class customer:
    def __init__(self,customername, tier):
        self.customername = customername
        self.tier = tier

    def set_customername(self,customername):
        self.customername=customername

    def get_customername(self):
        return self.customername

    def set_tier(self,tier):
        self.tier=tier

    def get_tier(self):
        return self.tier