# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from objects.models import Objects, ObjectTypes, PropertiesTypes
from company.models import Teams, MachinesTypes


# Данные о работах на объектах
class WorksTypes(models.Model):
    work_type_name = models.CharField(max_length=45, verbose_name="Наименование работы")
    object_type_id = models.ForeignKey(ObjectTypes, verbose_name="Тип строительного объекта")

    class Meta:
        db_table = "works_types"
        verbose_name = "Данные о работах на объектах"
        verbose_name_plural = "Данные о работах на объектах"

    def __str__(self):
        return self.work_type_name


# Данные о фактических работах, проводимых при возведении объектов
class Works(models.Model):
    object_id = models.ForeignKey(Objects, verbose_name="Строительный объект")
    works_types_id = models.ForeignKey(PropertiesTypes, verbose_name="Тип работы, необходимый для постройки")
    teams_id = models.ForeignKey(Teams, verbose_name="Назначенная бригада")
    start_date = models.DateField(verbose_name="Дата начала работы")
    plan_date = models.DateField(verbose_name="Планируемая дата завершения работы")
    end_date = models.DateField(verbose_name="Фактическая дата завершения работы")

    class Meta:
        db_table = "works"
        verbose_name = "Данные о фактических работах, проводимых при возведении объектов"
        verbose_name_plural = "Данные о фактических работах, проводимых при возведении объектов"


# Необходимые ресурсы
class ResoursesTypes(models.Model):
    resourse_name = models.CharField(max_length=45, verbose_name="Наименование ресурса")
    work_type_id = models.ForeignKey(WorksTypes, verbose_name="Тип работы")

    class Meta:
        db_table = "resourses_types"
        verbose_name = "Данные о работах на объектах"
        verbose_name_plural = "Данные о работах на объектах"

    def __str__(self):
        return self.resourse_name


# Необходимые типы техники для проведения работ
class WorksTypesMachinesTypes(models.Model):
    machine_type_id = models.ForeignKey(MachinesTypes, verbose_name="Необходимый тип техники")
    work_type_id = models.ForeignKey(WorksTypes, verbose_name="Тип работы")

    class Meta:
        db_table = "works_types_machines_types"
        verbose_name = "Необходимые типы техники для проведения работ"
        verbose_name_plural = "Необходимые типы техники для проведения работ"


# Фактически использованные ресурсы
class Resourses(models.Model):
    work_id = models.ForeignKey(Works, verbose_name="Фактически производимая работа")
    resourse_type_id = models.ForeignKey(ResoursesTypes, verbose_name="Ресурс")
    required_amount = models.CharField(max_length=45, verbose_name="Планируемое кол-во ресурса для использования")
    real_amount = models.CharField(max_length=45, verbose_name="Фактически затраченное количество ресурса")

    class Meta:
        db_table = "resourses"
        verbose_name = "Фактически использованные ресурсы"
        verbose_name_plural = "Фактически использованные ресурсы"
