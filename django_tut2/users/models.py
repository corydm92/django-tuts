from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self):
    #     super().save()

    #When overwriting models .save() method you need to pass in kwargs or you get this error: TypeError at /register/ || save() got an unexpected keyword argument 'force_insert'

    def save(self, **kwargs):
        super().save()

        # Overwriting default image size if it exceeds 300px 
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
