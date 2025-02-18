from django.db import models

class URLCheck(models.Model):
    url = models.URLField(max_length=2000)
    status_code = models.IntegerField()
    content_type = models.CharField(max_length=100)
    checked_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['checked_at']),
            models.Index(fields=['url']),
        ]
        
    def __str__(self):
        return f"{self.url} - {self.status_code} at {self.checked_at}"
