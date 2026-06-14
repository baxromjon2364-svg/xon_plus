import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xon_plus.settings')
django.setup()

from django.contrib.auth import get_user_user_model

User = get_user_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('ahrorbek', 'admin@example.com', 'ahrorbek')
    print("Superuser muvaffaqiyatli yaratildi!")
else:
    print("Superuser allaqachon mavjud.")