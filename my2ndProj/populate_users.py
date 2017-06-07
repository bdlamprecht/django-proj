import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'my2ndProj.settings')

import django
django.setup()

from my2ndApp.models import MyUser
from faker import Faker

fakegen = Faker()


def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        user = MyUser.objects.get_or_create(fName = fake_first_name,
                                            lName=fake_last_name,
                                            email=fake_email)[0]
if __name__ == '__main__':
    print("POPULATING")
    populate()
    print("COMPLETE")
