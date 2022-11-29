Unobtrusive test models creation for django

**Current development of the package happens in https://github.com/ivelum/django-whatever.**

django-whatever is a friendly fork of ``django-any`` package written by Mikhail Podgurskiy (kmmbvnr)
The purpose of the fork is to fix most annoying bugs and add `some features <http://django-whatever.readthedocs.org/en/latest/changelog.html>`_
To remain compatible with original package ``django-whatever`` retains same namespace: ``django_any``.

``django-whatever`` is explicit replacement for old-style, big and error-prone
implicit fixture files.

``django-whatever`` allows you to specify only fields important for tests
and fills the rest randomly with acceptable values.

It makes tests clean and easy to understand, without reading fixture files.::

    from django_any import any_model

    class TestMyShop(TestCase):
        def test_order_updates_user_account(self):
            account = any_model(Account, amount=25, user__is_active=True)
            order = any_model(Order, user=account.user, amount=10)
            order.proceed()

            account = Account.objects.get(pk=account.pk)
            self.assertEquals(15, account.amount)

Read more at the docs: http://django-whatever.readthedocs.org/
