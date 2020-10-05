from django.db import models
from django.core import validators
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin



class UserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)

    user_or_owner = models.BooleanField(
        _('user_or_owner'),
        default=False,
    )

    is_staff = models.BooleanField(
        _('staff status'),
        default=True,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_superuser = models.BooleanField(
        _('superuser'),
        default=True,
    )

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
          

class Info(models.Model):

    SEX_CHOICES = (
        (1, 'S/S'),
        (2, 'A/W'),
    )

    name = models.CharField(
        verbose_name='info name',
        max_length=200,
    )
    # image = models.ImageField(upload_to='info/', default='defo')

    season = models.IntegerField(
        verbose_name='season',
        choices=SEX_CHOICES,
        default=1
    )

    info = models.TextField(
        verbose_name='information',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='registlation date',
        auto_now_add=True
    )


class Item(models.Model):

    SEX_CHOICES = (
        (1, 'man'),
        (2, 'woman'),
        (3, 'child'),
    )

    name = models.CharField(
        verbose_name='product name',
        max_length=200,
    )
    age = models.IntegerField(
        verbose_name='price',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
    sex = models.IntegerField(
        verbose_name='gender',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='add information',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='registlation date',
        auto_now_add=True
    )
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='documents/', default='defo')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'item'
