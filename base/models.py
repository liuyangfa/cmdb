# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import sys

reload(sys)
sys.setdefaultencoding('utf8')

# Create your models here.

class System(models.Model):
    sql_id = models.CharField(verbose_name="序号", max_length=30)
    enname = models.CharField(verbose_name="英文名", max_length=30)
    cnname = models.CharField(verbose_name="中文名", max_length=30)

    def __str__(self):
        return "%s,%s,%s" % (self.sql_id, self.enname, self.cnname)

    class Meta:
        verbose_name = "system"
        verbose_name_plural = "system"
