from rest_framework.test import APITestCase
from django.urls import reverse
from twisted.scripts import trial

# Doğru veriler ile kayıt işlemi yap
# Şifre invalid olabilir
# Kullanıcı Adı kullanılmış olabilir
# Üye girişi yaptıysak o sayfa gözükmemeli.
# Token ile giriş yaptığımızda o sayfa gözükmemeli.(adminden giriş yapılırsa session olur)

class UserRegistrationTestCase(APITestCase):
    url = reverse("account:register")

    def test_user_registration(self):
        """
        Doğru Veriler ile kayıt işlemi
        """
        data = {
            "username": "tahsintest",
            "password": "deneme123",
        }

        response = self.client.post(self.url, data)
        self.assertEquals(201, response.status_code)


    def test_user_invalid_password(self):
        """
        invalid İşlemi ile kayıt işlemi
        """
        data = {
            "username": "tahsintest",
            "password": "1",
        }

        response = self.client.post(self.url, data)
        self.assertEquals(400, response.status_code)

    def test_unique_name(self):
        """
        Benzersiz isim ile kayıt işlemi
        """
        self.test_user_registration()
        data = {
            "username": "tahsintest",
            "password": "galapagos",
        }

        response = self.client.post(self.url, data)
        self.assertEquals(400, response.status_code)
