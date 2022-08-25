#
# Copyright © 2012–2022 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
"""Localization kwargs quality check example."""

import re
import json
import collections

from django.utils.translation import gettext_lazy as _
from weblate.checks.base import TargetCheck


"""check json has duplicate keys"""
def detect_duplicate_keys(list_of_pairs):
    key_count = collections.Counter(k for k,v in list_of_pairs)
    duplicate_keys = ', '.join(k for k,v in key_count.items() if v>1)

    if len(duplicate_keys) != 0:
        raise ValueError('Duplicate key(s) found: {}'.format(duplicate_keys))

def validate_data(list_of_pairs):
    detect_duplicate_keys(list_of_pairs)
    return dict(list_of_pairs)


class KwargsCheckA(TargetCheck):
    """Check kwargs"""

    # Used as identifier for check, should be unique
    # Has to be shorter than 50 chars
    check_id = "eve_localization_format_kwargs_check_a"

    # Short name used to display failing check
    name = _("Format kwargs 语法检查")

    # Description for failing check
    description = _("Format kwargs 语法检查")

    def check_single(self, source, target, unit):
        """Real check code."""
        SEPERATOR = "\n!====FORMAT-KWARGS====!\n"
        if SEPERATOR in target:
            ### step 1: check zh
            split = target.split(SEPERATOR)
            if len(split) == 2:
                # check if it is valid json string            
                try:
                    kwargs = json.loads(split[1], object_pairs_hook=validate_data)
                except Exception as e:
                    print(e)
                    return True
                # check if target kwargs match source
                ph_in_text = list(set(re.findall(r"{.*?}", split[0])))
                json_keys = list(kwargs.keys())
                ph_in_text.sort()
                json_keys.sort()
                if ph_in_text == json_keys:
                    # all good
                    return False
            ### todo: step 2: compare with en
            
            return True
        return False
