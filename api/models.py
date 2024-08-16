from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Branch(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True, db_index=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name="branches")
    branch_name = models.CharField(max_length=100)
    address = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.branch_name} ({self.ifsc})"
