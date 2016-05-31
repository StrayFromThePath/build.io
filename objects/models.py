# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from company.models import Spots


# Типы строительных объектов
class ObjectTypes(models.Model):
    object_type_name = models.CharField(max_length=45, verbose_name="Наименование типа строительного объекта")

    class Meta:
        db_table = "object_types"
        verbose_name = "Тип строительного объекта"
        verbose_name_plural = "Тип строительных объектов"

    def __str__(self):
        return self.object_type_name


# Свойства, относящиеся к определенным типам строительных объектов
class PropertiesTypes(models.Model):
    object_type_name = models.CharField(max_length=45, verbose_name="Наименование типа строительного объекта")
    object_type_id = models.ForeignKey(ObjectTypes, verbose_name="Тип строительного объекта")

    class Meta:
        db_table = "properties_types"
        verbose_name = "Свойство строительного объекта"
        verbose_name_plural = "Свойства строительных объектов"

    def __str__(self):
        return self.object_type_name


# Строительные объекты
class Objects(models.Model):
    object_name = models.CharField(max_length=45, verbose_name="Наименование объекта")
    spot_id = models.ForeignKey(Spots, verbose_name="Строительный участок")
    type_id = models.ForeignKey(ObjectTypes, verbose_name="Тип строительного объекта")
    customer_name = models.CharField(max_length=45, verbose_name="ФИО заказчика")
    object_address = models.CharField(max_length=45, verbose_name="Адрес объекта")
    start_date = models.DateField(verbose_name="Дата начала строительства")
    plan_date = models.DateField(verbose_name="Планируемая дата завершения строительства")
    end_date = models.DateField(verbose_name="Фактическая дата завершения строительства")

    class Meta:
        db_table = "objects"
        verbose_name = "Строительный объект"
        verbose_name_plural = "Строительные объекты"

    def __str__(self):
        return self.object_name


# Свойства объектов
class Properties(models.Model):
    property_value = models.CharField(max_length=45, verbose_name="Значение конкретного свойства")
    object_id = models.ForeignKey(Objects, verbose_name="Строительный объект")
    property_id = models.ForeignKey(PropertiesTypes, verbose_name="Тип свойства")

    class Meta:
        db_table = "properties"
        verbose_name = "Свойство строительного объекта"
        verbose_name_plural = "Свойства строительных объектов"

    def __str__(self):
        return self.property_value
