from django.contrib.auth.models import User
from .models import Store, OpeningHours
from rest_framework import status
from rest_framework.test import APITestCase


class StoreListCreateViewTests(APITestCase):
    def test_can_list_stores(self):
        Store.objects.create(store_name="A Test Store", store_address="1 Test Street")
        response = self.client.get("/api/v1/stores/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_create_stores(self):
        self.assertEqual(len(Store.objects.all()), 0)
        response = self.client.post(
            "/api/v1/stores/",
            {"store_name": "Test Store 2", "store_address": "2 Test Street"},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(Store.objects.all()), 1)


class StoreDetailViewTests(APITestCase):
    def setUp(self):
        test_store = Store.objects.create(
            store_name="A Test Store", store_address="1 Test Street"
        )

    def test_can_retrieve_store_with_valid_id(self):
        response = self.client.get("/api/v1/stores/1/")
        self.assertEqual(response.data["store_name"], "A Test Store")
        self.assertEqual(response.get(store_name="store_name"), "A Test Store")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_store_with_invalid_id(self):
        response = self.client.get("/api/v1/stores/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_store_can_be_updated(self):
        response = self.client.put(
            "/api/v1/stores/1/",
            {"store_name": "Another Store", "store_address": "2 Test Street"},
        )
        store = Store.objects.get(pk=1)
        self.assertEqual(store.store_name, "Another Store")
        self.assertEqual(store.store_address, "2 Test Street")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_store_can_be_deleted(self):
        self.assertEqual(len(Store.objects.all()), 1)
        response = self.client.delete(
            "/api/v1/stores/1/",
            {"store_name": "Another Store", "store_address": "2 Test Street"},
        )
        self.assertEqual(len(Store.objects.all()), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
