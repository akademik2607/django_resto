from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from multiselectfield import MultiSelectField

from config.settings import ROLES
from .managers import UserManager

STATUSES = (
    ('פעיל', 'active'),
    ('לא פעיל', 'off'),
    ('בחופשה', 'on_leave'),
    ('נא לבחור', 'choose')
)

# MultiSelectField()


class CustomMultiSelectField(MultiSelectField):
    def _get_flatchoices(self):
        flat_choices = super(models.CharField, self).flatchoices

        class MSFFlatchoices(list):
            # Used to trick django.contrib.admin.utils.display_for_field into not treating the list of values as a
            # dictionary key (which errors out)
            def __bool__(self):
                return False

            __nonzero__ = __bool__

        return MSFFlatchoices(flat_choices)

    flatchoices = property(_get_flatchoices)


class User(AbstractBaseUser, PermissionsMixin):
    status = models.CharField('status', choices=STATUSES, max_length=30, blank=False, default=STATUSES[3][0])
    role = CustomMultiSelectField('roles', choices=ROLES, max_length=250, blank=True)
    email = models.EmailField('email', unique=True)
    first_name = models.CharField('first_name', max_length=50, blank=True)
    last_name = models.CharField('first_name', max_length=50, blank=True)
    date_joined = models.DateTimeField('registered', auto_now_add=True)
    is_active = models.BooleanField('is_active', default=True)
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        '''
        Возвращает first_name и last_name с пробелом между ними.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Возвращает сокращенное имя пользователя.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Отправляет электронное письмо этому пользователю.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
