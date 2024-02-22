# Generated by Django 4.2.9 on 2024-02-22 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_alter_studentextra_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('education', 'Education'), ('entertainment', 'Entertainment'), ('comics', 'Comics'), ('biography', 'Biography'), ('history', 'History')], default='education', max_length=30),
        ),
        migrations.CreateModel(
            name='ReturnedBookDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=30)),
                ('issuedate', models.DateField()),
                ('returned_dated', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.studentextra')),
            ],
        ),
    ]
