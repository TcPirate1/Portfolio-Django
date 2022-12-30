from django.db import models

# Create your models here.
class Categories(models.model):
    Title = models.CharField(max_length=100)

    Non_responsive_website = "Website: Non-Responsive"
    responsive_website = "Website: Responsive"
    program_non_gui = "Program: Non-GUI"
    program_gui = "Program: GUI"
    category_choices = [
        ("empty", "EMPTY"),
        (Non_responsive_website, "Website: Non-Responsive"),
        (responsive_website,"Website: Responsive"),
        (program_gui,"Program: Non-GUI"),
        (program_gui,"Program: GUI"),
    ]
    category = models.CharField(
        choices = category_choices,
        default = "empty",
        blank = False, #makes it a required field
    )

    URL = models.URLField(max_length=200)
    language_framework = models.CharField(max_length=30)