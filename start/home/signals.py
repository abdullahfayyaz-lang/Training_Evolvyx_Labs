from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Student
##Signals let you “listen” for certain actions (like when a model is saved, deleted, etc.) and then automatically run custom code in response.
##send email to new students

# Why Use Signals?
# They help:
# Keep code clean and decoupled
# Avoid repeating logic in multiple places
# Automatically trigger tasks like:
# Sending emails on user registration
# Creating user profiles after user creation
# Logging or auditing actions

# Common Built-in Signals
# Signal	Triggered When	Typical Use
# pre_save	Before a model’s save()	Validate or modify data before saving
# post_save	After a model’s save()	Send notifications, create related objects
# pre_delete	Before a model’s delete()	Clean up files, cancel related objects
# post_delete	After a model’s delete()	Log deletions, adjust counters
# m2m_changed	When ManyToMany field is changed	Handle tagging, relations updates
# request_started / request_finished	On request start/end	Logging or timing middleware-like logic
# pre_migrate / post_migrate	Before/after migrations	Initial data setup

@receiver(post_save, sender=Student, dispatch_uid="send_welcome_email")
def send_welcome_email(sender, instance, created, **kwargs):
    print("signal fired")
    if created:
        send_mail(
            subject='Welcome!',
            message='Thanks for registering.',
            from_email='admin@django.com',
            recipient_list=['akbuddy8@gmail.com'],
            fail_silently=False,
        )
