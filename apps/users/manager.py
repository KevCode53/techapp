from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
  def _create_user(self, email, username, nip, password, is_staff, is_superuser, **extra_fields):
    ''' Creates and saves a User with the given username, email, and password. '''
    
    # Validate username
    if not username:
      raise ValueError('The given username must be set')
    # validate email
    if not email:
      raise ValueError('The given email must be set')
    
    # Create a new user
    user = self.model(
      email=self.normalize_email(email),
      username=username,
      nip=nip,
      password=password,
      is_staff=is_staff,
      is_superuser=is_superuser,
      **extra_fields
    )
    
    # Set password
    user.set_password(password)
    # Save user in db
    user.save(using=self._db)
    
    return user

  def create_user(self, email, username, nip, password=None, **extra_fields):
    ''' Creates and saves a User with the given username, email, no password. '''
    return self._create_user(email, username, nip, password, False, False, **extra_fields)

  def create_superuser(self, email, username, nip, password, **extra_fields):
    ''' Creates and saves a superuser with the given username, email and password. '''
    return self._create_user(email, username, nip, password, True, True, **extra_fields)
  # def create_superuser(self, username, email, name, last_name, password, **extra_fields):
  #   ''' Creates and saves a Superuser with the given username, email, no password. '''
  #   return self._create_user(username, email, name, last_name, password, True, True, **extra_fields)