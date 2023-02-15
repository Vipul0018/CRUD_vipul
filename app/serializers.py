from rest_framework import serializers
from .models import Blog
from django.contrib.auth.models import User

class BlogSerializers(serializers.ModelSerializer):
     # USER = serializers.CharField(source='Owner_Name.username')
     Owner_Staff_Name= serializers.ReadOnlyField(source='Owner_ID.username')

     class Meta:
          model = Blog
          fields = ['id','Owner_Staff_Name','Owner_ID','Title','Content','is_public','like']
     




