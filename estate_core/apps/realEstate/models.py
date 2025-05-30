from django.db import models
from django.conf import settings

class Property(models.Model):
    """
    부동산 매물 모델
    """
    REAL_ESTATE_PROPERTY_TYPES = [
        ('APARTMENT', '아파트'),
        ('HOUSE', '주택'),
        ('COMMERCIAL', '상가'),
        ('OFFICE', '사무실'),
    ]

    title = models.CharField(max_length=200, verbose_name='제목')
    description = models.TextField(verbose_name='설명')
    real_estate_property_type = models.CharField(max_length=20, choices=REAL_ESTATE_PROPERTY_TYPES)
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='가격')
    address = models.CharField(max_length=200, verbose_name='주소')
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='면적')
    rooms = models.IntegerField()
    bathrooms = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='properties',
        verbose_name='소유자'
    )

    class Meta:
        verbose_name = '부동산 매물'
        verbose_name_plural = '부동산 매물'
        ordering = ['-created_at']

    def __str__(self):
        return self.title 