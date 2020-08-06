from django.db import models


class BalanceSheet(models.Model):
    breakdown = models.DateField(auto_now=False)
    total_assets = models.IntegerField(null=True)
    total_liabilities = models.IntegerField(null=True)
    total_equity = models.IntegerField(null=True)
    total_capitalization = models.IntegerField(null=True)
    common_stock = models.IntegerField(null=True)
    capital_lease = models.IntegerField(null=True)
    net_tangible = models.IntegerField(null=True)
    working_capital = models.IntegerField(null=True)
    invested_capital = models.IntegerField(null=True)
    tangible_book = models.IntegerField(null=True)
    total_debt = models.IntegerField(null=True)
    share_issued = models.IntegerField(null=True)
    ordinary_shares = models.IntegerField(null=True)
