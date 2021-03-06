# -*- coding: utf-8 -*-
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from colin.checks.abstract.filesystem import FileSystemCheck


class FileCopy(FileSystemCheck):

    def __init__(self):
        super().__init__(name="file_copy",
                         message="Package httpd has to be isntalled.",
                         description="To copy a file into image, use `COPY source destination`. Pro vkládání souborů do kontejnerového obrazu použij příkaz`COPY zdroj cíl`",
                         reference_url="https://docs.docker.com/engine/reference/builder/#copy",
                         files=['/var/www/html/index.html'],
                         tags=['filesystem', 'copy', 'openhouse'],
                         all_must_be_present=False)
