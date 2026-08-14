from django.db import models

#category model creation
class category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name



#tag model creation
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# lesson models creation.
class Lesson(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey('category', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)        #included thetags field in the lesson model
    description = models.TextField( blank=True, null=True  )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
#Quiz model creation
class Question(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='questions' ) #one lesson can have multiple questions
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.lesson.title}: {self.text}"  #returns the lesson title and question text for better readability in the admin interface   


#option model creation
class Option(models.Model): 
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options') #one question can have multiple options
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)  #indicates whether the option is correct or not  

    def __str__(self):
        return f"{self.text}"  #returns the option text for better readability in the admin interface




    