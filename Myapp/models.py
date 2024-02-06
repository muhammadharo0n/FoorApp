from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.fields.related import ForeignKey , OneToOneField



# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, first_name , last_name, username, email, password=None): 
        if not email:
            raise ValueError('User not Valid')
        
        if not username: 
            raise ValueError('Enter User name')
        
        user = self.model(
            email= self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name ,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name , last_name, username, email, password=None):
        user= self.create_user(
            email= self.normalize_email(email),
            username = username,
            password=password,
            first_name = first_name,
            last_name = last_name 
             
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using = self._db)
        return user



class User(AbstractBaseUser):
    
    RESTURANT = 1
    COSTUMER = 2
    
    ROLE_CHOICES = ( 
        (RESTURANT ,'RESTURANT'),
        (COSTUMER ,'COSTUMER')
    )
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50,  unique=True)
    phone = models.CharField(max_length = 12 , blank =True)
    role = models.PositiveSmallIntegerField(choices = ROLE_CHOICES ,blank = True , null = True )


    date_joined  = models.DateTimeField(auto_now_add = True)
    last_login  = models.DateTimeField(auto_now_add = True)
    created_date  = models.DateTimeField(auto_now_add = True)
    modified_date  = models.DateTimeField(auto_now_add = True)
    is_admin = models.BooleanField(default =  False)
    is_active = models.BooleanField(default =  False)
    is_staff = models.BooleanField(default =  False)
    is_superadmin = models.BooleanField(default =  False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username' , 'first_name', 'last_name']
    objects = UserManager()

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

    def has_perm(self , perm, obj = None):
        return self.is_admin

    def has_module_perms (self , app_label) :
        return True
    

class UserProfile(models.Model):
    user = OneToOneField(User , on_delete=models.CASCADE , blank = True , null = True)
    profile_picture = models.ImageField(upload_to='user/profile_picture' , blank=True , null= True)
    cover_photo =  models.ImageField(upload_to='user/cover_photo' , blank=True , null= True)
    phone = models.CharField(max_length = 12 , blank =True)
    adress_line_1 = models.CharField(max_length=50 ,blank=True , null= True)
    adress_line_2 = models.CharField(max_length=50 ,blank=True , null= True)
    country = models.CharField(max_length=50 ,blank=True , null= True)
    state = models.CharField(max_length=50 ,blank=True , null= True)
    city = models.CharField(max_length=50 ,blank=True , null= True)
    pincode = models.CharField(max_length=50 ,blank=True , null= True)
    latiitude = models.CharField(max_length=50 ,blank=True , null= True)
    longitude = models.CharField(max_length=50 ,blank=True , null= True)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.user.email
    
