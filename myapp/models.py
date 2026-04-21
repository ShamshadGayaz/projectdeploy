from django.db import models

class FrontPageImage(models.Model):
    title = models.CharField(max_length=200, help_text="Title for the image")
    image = models.ImageField(upload_to='frontpage/', help_text="Upload an image for the front page")
    is_active = models.BooleanField(default=True, help_text="Show this image on front page")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Front Page Image"
        verbose_name_plural = "Front Page Images"
