from flask_testing import TestCase
from application import app, db
from application.models import Tasks
from flask import url_for

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY="ndjfijsdfksmkfk",
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        test = Tasks(description="Test")
        db.session.add(test)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

class testViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)