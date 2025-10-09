
from django.db import models
from django.db.models import Q, Index

# Create your models here.
##Many-to-one relationships
class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline

    class Meta:
        ordering = ["headline"]




class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True)  # single-field index
    country = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    published_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=50, db_index=True)

    class Meta:
        indexes = [
            # Composite index: common filter pattern
            Index(fields=['author', 'genre']),
            # Index for frequent ordering by published date
            Index(fields=['published_date']),
        ]

    def __str__(self):
        return f"{self.title} ({self.author.name})"


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="orders")
    customer_name = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("completed", "Completed"),
            ("cancelled", "Cancelled"),
        ],
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            Index(fields=['created_at'], name='order_created_idx'),
            # ✅ Fixed: specify field + condition (PostgreSQL only)
            Index(fields=['status'], condition=Q(status='completed'), name='completed_orders_idx'),
        ]

    def __str__(self):
        return f"Order({self.book.title}, {self.status})"
