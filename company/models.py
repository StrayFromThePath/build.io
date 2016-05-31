# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Строительные управления
class Felials(models.Model):
    felial_name = models.CharField(max_length=45, verbose_name="Название строительного управления")

    class Meta:
        db_table = "felials"
        verbose_name = "Строительное управление"
        verbose_name_plural = "Строительные управления"

    def __str__(self):
        return self.felial_name


# Строительные участки
class Spots(models.Model):
    spot_name = models.CharField(max_length=45, verbose_name="Название строительного участка")
    spot_address = models.CharField(max_length=100, verbose_name="Адрес")
    felial_id = models.ForeignKey(Felials, verbose_name="Строительное управление")

    class Meta:
        db_table = "spots"
        verbose_name = "Строительный участок"
        verbose_name_plural = "Строительные участки"

    def __str__(self):
        return self.spot_name


# Типы строительной техники
class MachinesTypes(models.Model):
    machine_type_name = models.CharField(max_length=45, verbose_name="Наименование типа техники")

    class Meta:
        db_table = "machines_types"
        verbose_name = "Тип техники"
        verbose_name_plural = "Типы техники"

    def __str__(self):
        return self.machine_type_name


# Строительная техника
class Machines(models.Model):
    machine_number = models.CharField(max_length=45, verbose_name="Автомобильный номер")
    machine_type_id = models.ForeignKey(MachinesTypes, verbose_name="Тип строительной техники")
    felial_id = models.ForeignKey(Felials, verbose_name="Строительное управление")
    spot_id = models.ForeignKey(Spots, verbose_name="Строительный участок")

    class Meta:
        db_table = "machines"
        verbose_name = "Строительная техника"
        verbose_name_plural = "Строительная техника"

    def __str__(self):
        return self.machine_number


# Бригады
class Teams(models.Model):
    team_name = models.CharField(max_length=45, verbose_name="Название бригады")
    felial_id = models.ForeignKey(Felials, verbose_name="Строительное управление")
    spot_id = models.ForeignKey(Spots, verbose_name="Строительный участок")

    class Meta:
        db_table = "teams"
        verbose_name = "Бригада"
        verbose_name_plural = "Бригады"

    def __str__(self):
        return self.team_name

