# Generated by Django 4.1.7 on 2023-03-04 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название категории"),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="media/categories", verbose_name="Изображение"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="Slug"),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название компании"),
                ),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="Slug"),
                ),
            ],
            options={
                "verbose_name": "Компания",
                "verbose_name_plural": "Компании",
            },
        ),
        migrations.CreateModel(
            name="Material",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Навзание материала"),
                ),
                ("slug", models.SlugField(max_length=255, verbose_name="Slug")),
            ],
            options={
                "verbose_name": "Материал",
                "verbose_name_plural": "Материалы",
            },
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Название")),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "verbose_name": "Тип",
                "verbose_name_plural": "Типы инструментов",
            },
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=255, verbose_name="Название инструмента"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        help_text="Данное поле заполняется автоматически",
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "description",
                    models.TextField(verbose_name="Описание/характеристика"),
                ),
                (
                    "colors",
                    models.CharField(
                        choices=[("Белый", "Белый"), ("Черный", "Черный")],
                        max_length=255,
                        verbose_name="Цвет",
                    ),
                ),
                ("size", models.FloatField(verbose_name="Размер")),
                ("price", models.FloatField(verbose_name="Цена")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.category",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.company",
                        verbose_name="Компания",
                    ),
                ),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.material",
                        verbose_name="Материал",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="main.type",
                        verbose_name="Тип",
                    ),
                ),
            ],
            options={
                "verbose_name": "Инструмент",
                "verbose_name_plural": "Инструменты",
            },
        ),
        migrations.CreateModel(
            name="Images",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="media/instruments/",
                        verbose_name="Изображение инструмента",
                    ),
                ),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="item_images",
                        to="main.item",
                        verbose_name="Инструмент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Изображение",
                "verbose_name_plural": "Изображения",
            },
        ),
    ]
