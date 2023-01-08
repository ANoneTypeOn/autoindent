#      StrIndent. A tool to automatically indent your strings.
#      Copyright (C) 2023 Avester
#
#      This program is free software: you can redistribute it and/or modify
#      it under the terms of the GNU General Public License as published by
#      the Free Software Foundation, either version 3 of the License, or
#      (at your option) any later version.
#
#      This program is distributed in the hope that it will be useful,
#      but WITHOUT ANY WARRANTY; without even the implied warranty of
#      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#      GNU General Public License for more details.
#
#      You should have received a copy of the GNU General Public License
#      along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import unittest

from autoindent import Indent

indenter = Indent()


class MyTestCase(unittest.TestCase):
    def test_string_adding(self):
        right = '  Who am I?\n    Nobody'

        indenter.add("Who am I?", 1)
        indenter.add("Nobody", 2)

        output = indenter.get_output()

        if output == right:
            pass
        else:
            self.fail("Results don't matching")


if __name__ == '__main__':
    unittest.main()
