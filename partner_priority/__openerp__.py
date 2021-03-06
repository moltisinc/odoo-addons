# -*- coding:utf-8 -*-
#
#
#    Copyright (C) 2016 Sucros Clear Information Technologies PLC.
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify it
#    under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#

{
    'name': 'Partner Priority',
    'summary': 'Set a priority on partners',
    'description': """
This module adds a 'priority' field to partner records. The priority applies
only to companies. Partner contacts inherit the priority of the parent
company.
    """,
    'author': 'Sucros Clear Information Technologies PLC',
    'website': 'http://www.clearict.com',
    'version': '1.0',
    'category': 'Base',
    'depends': [
        'base',
    ],
    'data': [
        'views/res_partner.xml',
    ],
    'test': [
    ],
    'demo_xml': [
    ],
    'installable': True,
    'active': False,
}
