# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Books ( models.Model ):
    book_name = models.CharField( max_length = 255 )
    book_price = models.DecimalField( max_digits = 5, decimal_places = 2 )
    book_time = models.DateTimeField( '保存日期', auto_now_add = True )