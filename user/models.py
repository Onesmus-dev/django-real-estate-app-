from django.db import models

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager
class UserAccountManager(BaseUserManager):
    def create_user(self, email,name,password =None):
        if not email :
            raise ValueError ('USer must have an email address') #checks if the user as entered he/her email ##haha sorry two genders only
        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email = email,
            name = name

        )

        user.set_password(password)
        set.save(using =self._db)

        return user
    def create_realtor(self,email, name, password= None):
        user = self.create_user(email, name, password)

        user.is_realtor = True
        user.save(using= self._db)

        return user
    
    def create_superuser(self, email,name, password=None):
        user = self.create_user(email,name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)

        return user
        
class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length =255, unique= True)
    name = models.CharField(max_length= 255)
    is_active = models.BooleanField(default= True) #if we want them to verify email before activating account then it should be set False
    is_staff = models.BooleanField(default= False)

    is_realtor = models.BooleanField(default= False)
    objects = UserAccountManager()
    
    USERNAME_FIELD ='email'
    REQUIRED_FIELDS = ['name']