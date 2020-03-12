# -*- coding: utf-8 -*-
""" 
    :author: Toti Cavalcanti
    :url: https://toticavalcanti.gitlab.io/profile/
    :copyright: © 2020 Toti Cavalcanti <https://toticavalcanti.gitlab.io/profile/>
    :license: MIT, see LICENSE for more details.
"""
from flask import url_for

from tests.base import BaseTestCase
from fluentchat.extensions import db
from fluentchat.models import User


class AdminTestCase(BaseTestCase):

    def setUp(self):
        super(AdminTestCase, self).setUp()
        admin = User(email='admin@flask.com', nickname='Admin User')
        admin.set_password('123')
        db.session.add(admin)
        db.session.commit()

    def test_admin_permission(self):
        response = self.client.delete(url_for('admin.block_user', user_id=1))
        self.assertEqual(response.status_code, 403)

        self.login()
        response = self.client.delete(url_for('admin.block_user', user_id=1))
        self.assertEqual(response.status_code, 403)

    def test_block_admin(self):
        self.login(email='admin@helloflask.com', password='123')
        response = self.client.delete(url_for('admin.block_user', user_id=2))
        self.assertEqual(response.status_code, 400)

    def test_block_user(self):
        self.login(email='admin@helloflask.com', password='123')
        response = self.client.delete(url_for('admin.block_user', user_id=1))
        self.assertEqual(response.status_code, 204)
        self.assertIsNone(User.query.get(1))
