from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from blog.models import Post
from django.contrib.auth.models import User


class PostAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.other_user = User.objects.create_user(
            username='otheruser',
            password='otherpass123'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.post_data = {
            'titulo': 'Test Post',
            'contenido': 'Contenido de prueba'
        }
        self.post = Post.objects.create(
            titulo='Test Post',
            contenido='Contenido de prueba',
            autor=self.user
        )

    def test_crear_post(self):
        url = reverse('post-list')
        response = self.client.post(url, self.post_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
        self.assertEqual(response.data['autor'], 'testuser')

    def test_listar_posts(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['titulo'], 'Test Post')

    def test_obtener_post(self):
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], 'Test Post')
        self.assertEqual(response.data['autor'], 'testuser')

    def test_actualizar_post(self):
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        updated_data = {'titulo': 'Post Actualizado'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.post.refresh_from_db()
        self.assertEqual(self.post.titulo, 'Post Actualizado')

    def test_eliminar_post(self):
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)

    def test_no_eliminar_post_otro_autor(self):
        other_post = Post.objects.create(
            titulo='Otro Post',
            contenido='Contenido',
            autor=self.other_user
        )
        url = reverse('post-detail', kwargs={'pk': other_post.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Post.objects.count(), 2)

    def test_no_actualizar_post_otro_autor(self):
        other_post = Post.objects.create(
            titulo='Otro Post',
            contenido='Contenido',
            autor=self.other_user
        )
        url = reverse('post-detail', kwargs={'pk': other_post.pk})
        updated_data = {'titulo': 'Intento de modificación'}
        response = self.client.patch(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        other_post.refresh_from_db()
        self.assertEqual(other_post.titulo, 'Otro Post')