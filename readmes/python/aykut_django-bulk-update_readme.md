django-bulk-update
==================================
[![Build Status](https://travis-ci.org/aykut/django-bulk-update.svg?branch=master)](https://travis-ci.org/aykut/django-bulk-update)
[![Coverage Status](https://coveralls.io/repos/aykut/django-bulk-update/badge.svg?branch=master)](https://coveralls.io/r/aykut/django-bulk-update?branch=master)

Simple bulk update over Django ORM or with helper function.

This project aims to bulk update given objects using **one query** over
**Django ORM**.

Installation
==================================
    pip install django-bulk-update

Usage
==================================
With manager:

```python
import random
from django_bulk_update.manager import BulkUpdateManager
from tests.models import Person

class Person(models.Model):
    ...
    objects = BulkUpdateManager()

random_names = ['Walter', 'The Dude', 'Donny', 'Jesus']
people = Person.objects.all()
for person in people:
  person.name = random.choice(random_names)

Person.objects.bulk_update(people, update_fields=['name'])  # updates only name column
Person.objects.bulk_update(people, exclude_fields=['username'])  # updates all columns except username
Person.objects.bulk_update(people)  # updates all columns
Person.objects.bulk_update(people, batch_size=50000)  # updates all columns by 50000 sized chunks
```


With helper:

```python
import random
from django_bulk_update.helper import bulk_update
from tests.models import Person

random_names = ['Walter', 'The Dude', 'Donny', 'Jesus']
people = Person.objects.all()
for person in people:
  person.name = random.choice(random_names)

bulk_update(people, update_fields=['name'])  # updates only name column
bulk_update(people, exclude_fields=['username'])  # updates all columns except username
bulk_update(people, using='someotherdb')  # updates all columns using the given db
bulk_update(people)  # updates all columns using the default db
bulk_update(people, batch_size=50000)  # updates all columns by 50000 sized chunks using the default db
```

Note: You can consider to use `.only('name')` when you only want to update `name`, so that Django will only retrieve name data from db.

And consider to use `.defer('username')` when you don't want to update `username`, so Django won't retrieve username from db.
These optimization can improve the performance even more.

Performance Tests:
==================================
Here we test the performance of the `bulk_update` function vs. simply calling
`.save()` on every object update (`dmmy_update`). The interesting metric is the speedup using
the `bulk_update` function more than the actual raw times.


```python
# Note: SQlite is unable to run the `timeit` tests
# due to the max number of sql variables
In [1]: import os
In [2]: import timeit
In [3]: import django

In [4]: os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.test_settings'
In [5]: django.setup()

In [6]: from tests.fixtures import create_fixtures

In [7]: django.db.connection.creation.create_test_db()
In [8]: create_fixtures(1000)

In [9]: setup='''
import random
from django_bulk_update import helper
from tests.models import Person
random_names = ['Walter', 'The Dude', 'Donny', 'Jesus']
ids = list(Person.objects.values_list('id', flat=True)[:1000])
people = Person.objects.filter(id__in=ids)
for p in people:
    name = random.choice(random_names)
    p.name = name
    p.email = '%s@example.com' % name
bu_update = lambda: helper.bulk_update(people, update_fields=['name', 'email'])
'''

In [10]: bu_perf = min(timeit.Timer('bu_update()', setup=setup).repeat(7, 100))

In [11]: setup='''
import random
from tests.models import Person
from django.db.models import F
random_names = ['Walter', 'The Dude', 'Donny', 'Jesus']
ids = list(Person.objects.values_list('id', flat=True)[:1000])
people = Person.objects.filter(id__in=ids)
def dmmy_update():
    for p in people:
        name = random.choice(random_names)
        p.name = name
        p.email = '%s@example.com' % name
        p.save(update_fields=['name', 'email'])
'''

In [12]: dmmy_perf = min(timeit.Timer('dmmy_update()', setup=setup).repeat(7, 100))
In [13]: print 'Bulk update performance: %.2f. Dummy update performance: %.2f. Speedup: %.2f.' % (bu_perf, dmmy_perf, dmmy_perf / bu_perf)
Bulk update performance: 7.05. Dummy update performance: 373.12. Speedup: 52.90.
```

Requirements
==================================
- Django 1.8+

Contributors
==================================
- [aykut](https://github.com/aykut)
- [daleobrien](https://github.com/daleobrien)
- [sruon](https://github.com/sruon)
- [HowerHell](https://github.com/HoverHell)
- [c-nichols](https://github.com/c-nichols)
- [towr](https://github.com/towr)
- [joshblum](https://github.com/joshblum)
- [luzfcb](https://github.com/luzfcb)
- [torchingloom](https://github.com/torchingloom)
- [cihann](https://github.com/cihann)
- [wetneb](https://github.com/wetneb)
- [tatterdemalion](https://github.com/tatterdemalion)
- [gabriel-laet](https://github.com/gabriel-laet)
- [arnau126](https://github.com/arnau126)

TODO
==================================
- Geometry Fields support

License
==================================
django-bulk-update is released under the MIT License. See the LICENSE file for more details.
