
from django.db import models
from django.utils.translation import gettext_lazy as _


class PersonManager(models.Manager):
    pass  # You can add custom query methods later


class Person(models.Model):
    ROLE_CHOICES = [
        ("A", _("Author")),
        ("E", _("Editor")),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    people = PersonManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_role_display()})"


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name


class StudentManagerBSCS(models.Manager):#Fixed section filter
    def get_queryset(self):
        return super().get_queryset().filter(degree="BSCS")

class StudentSectionManager(models.Manager):#Dynamic filtering
    def for_section(self, section_name):#here we didnt used the query_set bcz it does not accepts the 2nd arrgument so we have to create a custome one
        return self.get_queryset().filter(section=section_name)

class Student(models.Model):
    name=models.CharField(max_length=50)
    student_id=models.IntegerField()
    section=models.CharField(max_length=5)
    degree=models.CharField(max_length=4)

    objects=models.Manager()#default manager
    Bscs_objects=StudentManagerBSCS()## will only return students with degree bscs
    Section_objects=StudentSectionManager()#return all students of a specific section



class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3)
    birth_date = models.DateField(blank=True, null=True)


#For ORM
class Album(models.Model):
    title = models.CharField(max_length = 30)
    artist = models.CharField(max_length = 30)
    genre = models.CharField(max_length = 30)

    def __str__(self):
        return self.title

class Song(models.Model):
    name = models.CharField(max_length = 100)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)##Adding foreign key

    def __str__(self):
        return self.name

#Many-to-many relationships->
class Publication(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length=100)
    publications = models.ManyToManyField(Publication)

    class Meta:
        ordering = ["headline"]

    def __str__(self):
        return self.headline

#One-to-one relationships
class Place(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80)

    def __str__(self):
        return f"{self.name} the place"


class Restaurant(models.Model):
    place = models.OneToOneField(
        Place,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    def __str__(self):
        return "%s the restaurant" % self.place.name


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return "%s the waiter at %s" % (self.name, self.restaurant)


class PersonQuerySet(models.QuerySet):#Custom Querry sets
    def authors(self):
        return self.filter(role="A")

    def editors(self):
        return self.filter(role="E")


    def starts_with(self,letter):
        return self.filter(first_name__istartswith=letter)


class PersonManager(models.Manager):
    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)

    def authors(self):
        return self.get_queryset().authors()

    def editors(self):
        return self.get_queryset().editors()


class Person(models.Model):
    ROLE_CHOICES = [
        ("A", _("Author")),
        ("E", _("Editor")),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES)

    people = PersonManager()
    objects=models.Manager()#default manager

    