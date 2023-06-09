from django.contrib.auth.models import User
from .models import Store, OpeningHours
from rest_framework import status
from rest_framework.test import APITestCase


class StoreListCreateViewTests(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            username="test_user", email="test@test.com", password="testpassword"
        )

    def test_unauthenticated_user_cannot_list_stores(self):
        Store.objects.create(store_name="A Test Store", store_address="1 Test Street")
        response = self.client.get("/api/v1/stores/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_list_stores(self):
        self.client.force_login(self.test_user)
        Store.objects.create(store_name="A Test Store", store_address="1 Test Street")
        response = self.client.get("/api/v1/stores/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_create_stores(self):
        self.client.force_login(self.test_user)
        self.assertEqual(len(Store.objects.all()), 0)
        response = self.client.post(
            "/api/v1/stores/",
            {"store_name": "Test Store 2", "store_address": "2 Test Street"},
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(Store.objects.all()), 1)


class StoreDetailViewTests(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            username="test_user", email="test@test.com", password="testpassword"
        )
        self.test_store = Store.objects.create(
            store_name="A Test Store", store_address="1 Test Street"
        )

    def test_unauthorised_user_cannot_retrieve_stores_with_id(self):
        response = self.client.get("/api/v1/stores/1/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_retrieve_store_with_valid_id(self):
        self.client.force_login(self.test_user)
        response = self.client.get("/api/v1/stores/1/")
        self.assertEqual(response.data["store_name"], "A Test Store")
        self.assertEqual(response.data["store_address"], "1 Test Street")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_store_with_invalid_id(self):
        self.client.force_login(self.test_user)
        response = self.client.get("/api/v1/stores/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_store_can_be_updated(self):
        self.client.force_login(self.test_user)
        response = self.client.put(
            "/api/v1/stores/1/",
            {"store_name": "Another Store", "store_address": "2 Test Street"},
        )
        store = Store.objects.get(pk=1)
        self.assertEqual(store.store_name, "Another Store")
        self.assertEqual(store.store_address, "2 Test Street")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_store_can_be_deleted(self):
        self.client.force_login(self.test_user)
        self.assertEqual(len(Store.objects.all()), 1)
        response = self.client.delete(
            "/api/v1/stores/1/",
            {"store_name": "Another Store", "store_address": "2 Test Street"},
        )
        self.assertEqual(len(Store.objects.all()), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class OpeningHoursListCreateViewTests(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            username="test_user", email="test@test.com", password="testpassword"
        )
        test_store = Store.objects.create(
            store_name="A Test Store", store_address="1 Test Street"
        )
        OpeningHours.objects.create(
            store_id=test_store,
            day_of_week="mon",
            opening_time="09:00:00",
            closing_time="12:00:00",
        )

    def test_unauthorised_user_cannot_view_opening_hours(self):
        response = self.client.get("/api/v1/times/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_opening_hours_list_view(self):
        self.client.force_login(self.test_user)
        response = self.client.get("/api/v1/times/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_create_opening_times(self):
        self.client.force_login(self.test_user)
        self.assertEqual(len(OpeningHours.objects.all()), 1)
        response = self.client.post(
            "/api/v1/times/",
            {
                "store_id": 1,
                "day_of_week": "tues",
                "opening_time": "09:00:00",
                "closing_time": "12:00:00",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        store = OpeningHours.objects.get(pk=2)
        self.assertEqual(store.day_of_week, "tues")
        self.assertEqual(len(OpeningHours.objects.all()), 2)

    def test_closing_time_cannot_be_same_as_opening_time(self):
        self.client.force_login(self.test_user)
        response = self.client.post(
            "/api/v1/times/",
            {
                "store_id": 1,
                "day_of_week": "weds",
                "opening_time": "09:00:00",
                "closing_time": "09:00:00",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json()["non_field_errors"][0],
            "Opening and closing times must be different",
        )

    def test_closing_time_cannot_be_earlier_than_opening_time(self):
        self.client.force_login(self.test_user)
        response = self.client.post(
            "/api/v1/times/",
            {
                "store_id": 1,
                "day_of_week": "weds",
                "opening_time": "12:00:00",
                "closing_time": "09:00:00",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json()["non_field_errors"][0],
            "A store cannot close before it has opened!",
        )


class OpeningHoursDetailViewTests(APITestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            username="test_user", email="test@test.com", password="testpassword"
        )
        test_store = Store.objects.create(
            store_name="A Test Store", store_address="1 Test Street"
        )
        OpeningHours.objects.create(
            store_id=test_store,
            day_of_week="mon",
            opening_time="09:00:00",
            closing_time="12:00:00",
        )

    def test_unauthorised_user_cannot_retrieve_opening_times_with_id(self):
        response = self.client.get("/api/v1/times/1/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_can_retrieve_opening_times_with_valid_id(self):
        self.client.force_login(self.test_user)
        response = self.client.get("/api/v1/times/1/")
        self.assertEqual(response.data["store_id"], 1)
        self.assertEqual(response.data["day_of_week"], "mon")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_opening_times_with_invalid_id(self):
        self.client.force_login(self.test_user)
        response = self.client.get("/api/v1/times/999/")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_opening_times_can_be_updated(self):
        self.client.force_login(self.test_user)
        response = self.client.put(
            "/api/v1/times/1/",
            {
                "store_id": 1,
                "day_of_week": "tues",
                "opening_time": "09:00:00",
                "closing_time": "12:00:00",
            },
        )
        store = OpeningHours.objects.get(pk=1)
        self.assertEqual(store.day_of_week, "tues")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_opening_hours_can_be_deleted(self):
        self.client.force_login(self.test_user)
        self.assertEqual(len(OpeningHours.objects.all()), 1)
        response = self.client.delete(
            "/api/v1/times/1/",
            {
                "store_id": 1,
                "day_of_week": "mon",
                "opening_time": "09:00:00",
                "closing_time": "12:00:00",
            },
        )
        self.assertEqual(len(OpeningHours.objects.all()), 0)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
