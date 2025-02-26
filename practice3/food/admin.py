from django.contrib import admin
from .models import *

from .models import Food, Consume

admin.site.register(Food)
admin.site.register(Consume)
