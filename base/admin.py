# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from base.models import System


# Register your models here.
@admin.register(System)
class SystemAdmin(admin.ModelAdmin):
    list_display = ("sql_id", "enname", "cnname")
