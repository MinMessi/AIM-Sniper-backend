from django.db import models
from company_report.entity.company_data_total import CompanyDataTotal


class FinancialData(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.ForeignKey(CompanyDataTotal, on_delete=models.CASCADE)
    year = models.IntegerField()
    revenue = models.BigIntegerField()
    receivable_turnover = models.FloatField()
    operating_cash_flow = models.BigIntegerField()

    def __str__(self):
        return f"({self.year})"

    class Meta:
        db_table = 'company_finance'
        app_label = 'company_report'