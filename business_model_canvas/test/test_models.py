from django.test import TestCase
from business_model_canvas.models import *
from save_deep import save_deep

class TestVersion(TestCase):

    def test_copy_normal_fields(self):
        bmc = save_deep(BusinessModelCanvas.example())
        new_version = bmc.create_new_version()
        self.assertEqual(new_version.one_sentence, bmc.one_sentence)
        self.assertEqual(new_version.key_partners, bmc.key_partners)
        self.assertEqual(new_version.key_activies, bmc.key_activies)
        self.assertEqual(new_version.key_resources, bmc.key_resources)
        self.assertEqual(new_version.value_propositions, bmc.value_propositions)
        self.assertEqual(new_version.customer_relationships, bmc.customer_relationships)
        self.assertEqual(new_version.channels, bmc.channels)
        self.assertEqual(new_version.customer_segments, bmc.customer_segments)
        self.assertEqual(new_version.cost_structure, bmc.cost_structure)
        self.assertEqual(new_version.revenue_streams, bmc.revenue_streams)

    def test_copy_details(self):
        bmc = save_deep(BusinessModelCanvas.example())
        new_version = bmc.create_new_version()
        
        self.assertNotEqual(bmc, new_version)
        self.assertNotEqual(id(bmc), id(new_version))
        self.assertNotEqual(bmc.created_at, new_version.created_at)

        self.assertEqual(bmc.version + 1, new_version.version)

        self.assertTrue(new_version.pk)
        self.assertNotEqual(bmc.pk, new_version.pk)

    def test_setting_previous(self):
        bmc = save_deep(BusinessModelCanvas.example())
        new_version = bmc.create_new_version()
        self.assertEqual(new_version.previous, bmc)

