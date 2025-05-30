from django.db import models

class BaseModel(models.Model):
    """
    모든 모델의 기본이 되는 추상 모델
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 