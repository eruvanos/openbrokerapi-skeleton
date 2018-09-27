from unittest import TestCase

from broker.broker import Broker


class CatalogTest(TestCase):
    def test_returns_default_catalog(self):
        subject = Broker()

        catalog = subject.catalog()

        self.assertIsNotNone(catalog)


class ProvisioningTest(TestCase):
    def test_returns_spec_with_dashboard_id(self):
        pass

    def test_saves_space_and_org_guids(self):
        pass


class BindTest(TestCase):
    def test_returns_api_url_with_credentials(self):
        pass

    def test_saves_binding_with_apikey_in_db(self):
        pass


class UnbindTest(TestCase):
    def test_successfully_unbind(self):
        pass

    def test_deletes_binding(self):
        pass


class DeprovisionTest(TestCase):
    def test_successfully_deprovision(self):
        pass

    def test_deletes_entry(self):
        pass
