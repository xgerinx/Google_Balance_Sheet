from django.core.management.base import BaseCommand
from apps.balance_sheet.models import BalanceSheet

from lxml import html
import requests
import numpy
import pandas


class Command(BaseCommand):

    def handle(self, *args, **options):
        """
        This scrap Balance Sheet from Yahoo Finance and put it to database
        """

        symbol = 'GOOG'
        url = 'https://finance.yahoo.com/quote/' + symbol + '/balance-sheet?p=' + symbol
        page = requests.get(url)
        tree = html.fromstring(page.content)
        table_rows = tree.xpath("//div[contains(@class, 'D(tbr)')]")
        assert len(table_rows) > 0

        parsed_rows = []
        for i in table_rows:
            parsed_row = []
            el = i.xpath("./div")

            none_count = 0
            for i in el:
                try:
                    (text,) = i.xpath('.//span/text()[1]')
                    parsed_row.append(text)
                except ValueError:
                    parsed_row.append(numpy.NaN)
                    none_count += 1

            if (none_count < 4):
                parsed_rows.append(parsed_row)

            df = pandas.DataFrame(parsed_rows)

            numeric_columns = list(df.columns)[1::]
            for i in numeric_columns:
                df[i] = df[i].str.replace(',', '')

        return (
            BalanceSheet.objects.create(
                breakdown=pandas.to_datetime(df[1][0]),
                total_assets=int(df[1][1]),
                total_liabilities=int(df[1][2]),
                total_equity=int(df[1][3]),
                total_capitalization=int(df[1][4]),
                common_stock=int(df[1][5]),
                capital_lease=int(df[1][6]),
                net_tangible=int(df[1][7]),
                working_capital=int(df[1][8]),
                invested_capital=int(df[1][9]),
                tangible_book=int(df[1][10]),
                total_debt=int(df[1][11]),
                share_issued=int(df[1][12]),
                ordinary_shares=int(df[1][13])
            ),
            BalanceSheet.objects.create(
                breakdown=pandas.to_datetime(df[2][0]),
                total_assets=int(df[2][1]),
                total_liabilities=int(df[2][2]),
                total_equity=int(df[2][3]),
                total_capitalization=int(df[2][4]),
                common_stock=int(df[2][5]),
                capital_lease=int(df[2][6]),
                net_tangible=int(df[2][7]),
                working_capital=int(df[2][8]),
                invested_capital=int(df[2][9]),
                tangible_book=int(df[2][10]),
                total_debt=int(df[2][11]),
                share_issued=int(df[2][12]),
                ordinary_shares=int(df[2][13])
            ),
            BalanceSheet.objects.create(
                breakdown=pandas.to_datetime(df[3][0]),
                total_assets=int(df[3][1]),
                total_liabilities=int(df[3][2]),
                total_equity=int(df[3][3]),
                total_capitalization=int(df[3][4]),
                common_stock=int(df[3][5]),
                capital_lease=int(df[3][6]),
                net_tangible=int(df[3][7]),
                working_capital=int(df[3][8]),
                invested_capital=int(df[3][9]),
                tangible_book=int(df[3][10]),
                total_debt=int(df[3][11]),
                share_issued=int(df[3][12]),
                ordinary_shares=int(df[3][13])
            ),
            BalanceSheet.objects.create(
                breakdown=pandas.to_datetime(df[4][0]),
                total_assets=int(df[4][1]),
                total_liabilities=int(df[4][2]),
                total_equity=int(df[4][3]),
                total_capitalization=int(df[4][4]),
                common_stock=int(df[4][5]),
                capital_lease=int(df[4][6]),
                net_tangible=int(df[4][7]),
                working_capital=int(df[4][8]),
                invested_capital=int(df[4][9]),
                tangible_book=int(df[4][10]),
                total_debt=int(df[4][11]),
                share_issued=int(df[4][12]),
                ordinary_shares=int(df[4][13])
            )
        )
