from django.contrib.auth.models import AbstractUser
from django.db import models
from django import forms

class User(AbstractUser):
    location = models.CharField(max_length=100, blank=True, null=True)
    business_name = models.CharField(max_length=200, blank=True, null=True)
    


    def __repr__(self):
        return f"<User username={self.username} pk={self.pk}>"

    def __str__(self):
        return self.username


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    recipe = models.TextField()
    ingredients = models.TextField()
    chef = models.ForeignKey('User', on_delete=models.CASCADE, related_name='chef', max_length=255) 
    recipe_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipe} by {self.chef}"


class Test(models.Model):
    title = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='tests', max_length = 255)
#temporarily set to charfield in order to research how to sequential number entries
    version_number = models.CharField(max_length=3)
    ingredients = models.TextField(max_length=500)
    recipe = models.TextField(max_length=800)  
    image = models.ImageField(blank=True, null=True)
    outside_notes = models.CharField(max_length=400, blank=True, null=True)
    final_notes = models.CharField(max_length=400, blank=True, null=True)
    adjustments = models.CharField(max_length=455, blank=True, null=True)
    feedback_link = models.URLField(max_length=255, )
#temporarily set to CharField, researching how to connect with tags component from react FE repo
    tags = models.CharField(max_length=255, blank=True, null=True)
    chef = models.ForeignKey('User', on_delete=models.CASCADE, related_name='tests', max_length = 255)
    variation_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    successful_variation = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}: Test #{self.version_number} "


class TasterFeedback(models.Model):
    ONE = '1' 
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'

    RADIO = [ 
        (ONE , '1'), 
        (TWO , '2'), 
        (THREE , '3'), 
        (FOUR , '4'), 
        (FIVE , '5'), 
        ]

    TOO_LITTLE = 'Too Little'
    JUST_RIGHT = 'Just Right'
    TOO_MUCH = 'Too Much'

    SCALE = [ 
        (TOO_LITTLE , 'Too Little'), 
        (JUST_RIGHT , 'Just Right'),
        (TOO_MUCH , 'Too Much'), 
        ]
    
    YES = 'Yes'
    NO = 'No'

    CHOICE = [ 
        (YES , 'Yes'), 
        (NO , 'No'), 
        ]
    
    rating = models.CharField(max_length=6, choices=RADIO, default=THREE,)
    saltiness = models.CharField(max_length= 11, choices=SCALE, default=JUST_RIGHT,)
    sweetness = models.CharField(max_length= 11, choices=SCALE, default=JUST_RIGHT,)
    portion = models.CharField(max_length= 11, choices=SCALE, default=JUST_RIGHT,)
    texture = models.CharField(max_length= 5, choices=CHOICE, default=YES,)
    additional_comment = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    version_number = models.ForeignKey('Test', on_delete=models.CASCADE, related_name='taster_feedback', max_length = 3)
    tester = models.ForeignKey('User', on_delete=models.CASCADE, related_name='taster_feedback', max_length=50)

    def __str__(self):
        return f"Feedback for {self.version_number}"