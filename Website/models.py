from django.db import models
from django.urls import reverse

# Create your models here.
class Categories(models.Model):
    Title = models.CharField(max_length=100)

    non_responsive_website = "Website: Non-Responsive"
    responsive_website = "Website: Responsive"
    program_non_gui = "Program: Non-GUI"
    program_gui = "Program: GUI"
    category_choices = [
        ("empty", "EMPTY"),
        (non_responsive_website, "Website: Non-Responsive"),
        (responsive_website,"Website: Responsive"),
        (program_non_gui,"Program: Non-GUI"),
        (program_gui,"Program: GUI"),
    ]
    category = models.CharField(
        max_length = 50,
        choices = category_choices,
        default = "empty",
        blank = False, #makes it a required field
    )
    language_framework = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    URL = models.URLField(max_length=200)

    def __str__(self):
        return '%s %s %s' % (self.Title, self.language_framework, self.category)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'pk': self.pk})