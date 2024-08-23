from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('can_add_book', 'Can add a new book'), ('can_change_book', 'Can change a book'), ('can_delete_book', 'Can delete a book')]},
        ),
    ]