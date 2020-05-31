"""Manager for User created using AbstractBaseUser.

    UserManager is created for User to attach the objects attribute/data
"""

#python imports

#django imports
from django.contrib.auth.models import BaseUserManager

#third-party imports

#inter-app imports

#local imports


class UserManager(BaseUserManager):
    """Custom User Manager For User.
    """
    use_in_migrations = True

    def _create_user(self, user_name, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """

        user = self.model(user_name = user_name,
                          **extra_fields,
                          )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, user_name, password=None, **extra_fields):
        """Create User with Default Access"""
        extra_fields.setdefault('is_staff', False)
        return self._create_user(user_name, password, **extra_fields)

    def create_superuser(self, user_name, password, **extra_fields):
        """Create User with Admin Accessibility"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(user_name, password, **extra_fields)
