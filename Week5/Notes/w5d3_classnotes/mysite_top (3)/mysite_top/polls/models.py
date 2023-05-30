from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    author = models.ForeignKey('Person', on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField('Category')

class Category(models.Model):
    name = models.CharField(max_length=20)

# python manage.py makemigrations
# python manage.py migrate






# python manage.py makemigrations - commit changes 
# python manage.py migrate - push changes


# -------------SINGLE INSTANCE-------------
# from polls.models import Post
# post1 = Post(title='First Post', content='test content', author='Joe')
# post1.save()
# post1.title = '1st Post'
# post1.delete()

# -------------Multiple INSTANCES-------------
# Post.objects.all() - returns all rows/objects
# Post.objects.last() - returns the last object
# Post.objects.first() - returns the first object

# Post.objects.all().order_by('author')

# get
# Post.objects.get(author='Adam') - returns single object

# filter
# Post.objects.filter(author='Joe') - returns multiple objects

# --------------Related model creation-----------
# category_science = Category(name='Science')
# category_science.save()
# post_science = Post(title='Mars', content='bla bla', author='Ben', category=category_science)
# post_science.save()