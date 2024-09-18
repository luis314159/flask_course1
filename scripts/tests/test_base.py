from flask_testing import TestCase
from flask import current_app, url_for
from main import app

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLE'] = False
        return app
    
    #verificar la aplicación
    def test_app_exits(self):
        self.assertIsNotNone(current_app)

    #verificar que la app está en test
    def test_app_in_test(self):
        self.assertTrue(current_app.config['TESTING'], True)
    
    #verificar que "/" redirige a /index
    def test_home_redirect(self):
        response = self.client.get(url_for('home'))
        # Normaliza la comparación quitando el dominio y comparando solo la parte relativa
        self.assertEqual(response.location.split('//')[-1], url_for('index'))

    #verificar respuesta 200
    def test_index_get(self):
        response = self.client.get(url_for('index'))

        self.assert200(response)
    
    #verificar post
    def test_index_post(self):
        fake_form = {
            'user_name': 'fake',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('index'), data = fake_form)
        self.assert200(response)

    def test_auth_plueprint_exits(self):
        self.assertIn('auth', self.app.blueprints)

    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))

        self.assert200(response)
        
    def test_auth_login_template(self):
        self.client.get(url_for('auth.login'))

        self.assertTemplateUsed('login.html')