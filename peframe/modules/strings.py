#!/usr/bin/env python

# ----------------------------------------------------------------------
# This file is part of PEframe.
#
# PEframe is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# PEframe is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PEframe. If not, see <http://www.gnu.org/licenses/>.
# ----------------------------------------------------------------------

import re


def get_process(content, min_length=6):
    # regex from cuckoo project
    strings = tuple(found.strip() for found in
                    re.findall('[\x1f-\x7e]{%s,}' %
                               min_length, content))
    strings += tuple(str(ws.decode("utf-16le")).strip()
                     for ws in re.findall('(?:[\x1f-\x7e][\x00]){%s,}'
                                          % min_length, content))
    return strings


def get(filename):
    with open(filename, 'rb') as f:
        return get_process(f.read())
