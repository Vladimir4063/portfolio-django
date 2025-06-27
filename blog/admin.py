from django.contrib import admin
from .models import Post

admin.site.register(Post)  # Assuming Post is the model you want to register, import it from models.py
