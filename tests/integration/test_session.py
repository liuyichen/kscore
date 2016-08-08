# Copyright 2014 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
# http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
from tests import unittest

import kscore.session


class TestCanChangeParsing(unittest.TestCase):
    def setUp(self):
        self.session = kscore.session.get_session()

    def test_maps_service_name_when_overriden(self):
        gametest = self.session.get_service_model('gametest')
        self.assertEqual(gametest.endpoint_prefix, 'gametest')
        # But we should map the service_name to be the same name
        # used when calling get_service_model which is different
        # than the endpoint_prefix.
        self.assertEqual(gametest.service_name, 'gametest')

    def test_maps_service_name_from_client(self):
        # Same thing as test_maps_service_name_from_client,
        # except through the client interface.
        client = self.session.create_client('gametest', region_name='cn-beijing-6')
        self.assertEqual(client.meta.service_model.service_name, 'gametest')
