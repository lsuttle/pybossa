# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2013 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.

from default import Test, assert_not_raises
from pybossa.auth import require
from nose.tools import assert_raises
from werkzeug.exceptions import Forbidden, Unauthorized
from mock import patch
from test_authorization import mock_current_user



class TestTokenAuthorization(Test):

    auth_providers = ('twitter', 'facebook', 'google')
    mock_anonymous = mock_current_user()
    mock_authenticated = mock_current_user(anonymous=False, admin=False, id=2)


    @patch('pybossa.auth.current_user', new=mock_anonymous)
    def test_anonymous_user_delete(self):
        """Test anonymous user is not allowed to delete an oauth token"""
        for token in self.auth_providers:
            assert_raises(Unauthorized,
                      require.ensure_authorized, 'delete', 'token', token=token)


    @patch('pybossa.auth.current_user', new=mock_authenticated)
    def test_authenticated_user_delete(self):
        """Test authenticated user is not allowed to delete an oauth token"""
        for token in self.auth_providers:
            assert_raises(Forbidden,
                      require.ensure_authorized, 'delete', 'token', token=token)


    @patch('pybossa.auth.current_user', new=mock_anonymous)
    def test_anonymous_user_create(self):
        """Test anonymous user is not allowed to create an oauth token"""
        for token in self.auth_providers:
            assert_raises(Unauthorized,
                      require.ensure_authorized, 'create', 'token', token=token)


    @patch('pybossa.auth.current_user', new=mock_authenticated)
    def test_authenticated_user_create(self):
        """Test authenticated user is not allowed to create an oauth token"""
        for token in self.auth_providers:
            assert_raises(Forbidden,
                      require.ensure_authorized, 'create', 'token', token=token)


    @patch('pybossa.auth.current_user', new=mock_anonymous)
    def test_anonymous_user_update(self):
        """Test anonymous user is not allowed to update an oauth token"""
        for token in self.auth_providers:
            assert_raises(Unauthorized,
                      require.ensure_authorized, 'update', 'token', token=token)


    @patch('pybossa.auth.current_user', new=mock_authenticated)
    def test_authenticated_user_update(self):
        """Test authenticated user is not allowed to update an oauth token"""
        for token in self.auth_providers:
            assert_raises(Forbidden,
                      require.ensure_authorized, 'update', 'token', token=token)


    @patch('pybossa.auth.current_user', new=mock_anonymous)
    def test_anonymous_user_read(self):
        """Test anonymous user is not allowed to read an oauth token"""
        for token in self.auth_providers:
            assert_raises(Unauthorized,
                      require.ensure_authorized, 'read', 'token', token=token)


    @patch('pybossa.auth.current_user', new=mock_authenticated)
    def test_authenticated_user_read(self):
        """Test authenticated user is allowed to read his own oauth tokens"""
        for token in self.auth_providers:
            assert_not_raises(Exception,
                      require.ensure_authorized, 'read', 'token', token=token)
