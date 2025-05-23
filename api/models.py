from django.db import models

# Create your models here.

# 부동산 데이터 모델
# 값들은 api에서 가져올 값 설정
class RealEstateData(models.Model):
    date = models.DateField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    area = models.DecimalField(max_digits=8, decimal_places=2)
    location = models.CharField(max_length=100)
    type = models.CharField(max_length=50)  # 아파트, 주택, 상가 등
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.location} - {self.date}"

