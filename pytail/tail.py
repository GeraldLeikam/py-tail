# !/usr/bin/env python


# @author Gerald Leikam <gerald.leikam@aol.com>

# @copyright Copyright (c) 2023
# @license GPL-2.0
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


from os import access
from os import F_OK
from os import R_OK
from os.path import isdir
from sys import stdout
from time import sleep
from typing import BinaryIO


class Tail:

    def __init__(self, file: str = None, refresh: float = 0.5, encoding: str = 'utf-8') -> None:
        self.file = file
        if refresh == 0:
            refresh = 0.1
        self.refresh = refresh
        self.encoding = encoding
        self.callback = self.build_in_callback

    @property
    def callback(self):
        return self._callback

    @callback.setter
    def callback(self, value) -> None:
        self._callback = value

    @property
    def file(self) -> str:
        return self._file

    @file.setter
    def file(self, value: str | None) -> None:
        self._file = value

    @property
    def refresh(self) -> float:
        return self._refresh

    @refresh.setter
    def refresh(self, value: float) -> None:
        self._refresh = value

    @property
    def encoding(self) -> str:
        return self._encoding

    @encoding.setter
    def encoding(self, value: str):
        self._encoding = value

    def get_file_object(self, file: str = None) -> BinaryIO:
        file = (file or self.file)
        if self.check_file(file=file):
            return open(
                file=(file or self.file),
                mode='rb',
            )

    def lines(self, count: int = 20):
        file_object = self.get_file_object()
        result = self.lines_function(file_object=file_object, n=count)
        file_object.close()
        return result

    def follow(self):
        file_object = self.get_file_object()
        self.follow_function(file_object=file_object)
        file_object.close()

    def bytes(self, count: int = 0):
        file_object = self.get_file_object()
        result = self.bytes_function(file_object=file_object, count=count)
        file_object.close()
        return result

    def lines_function(self, file_object: BinaryIO, n: int = 20) -> list[str]:
        temporary_n = n + 1
        result = file_object.read().decode(self.encoding).split('\n')[-temporary_n:]
        if result[len(result) - 1] == '':
            del result[len(result) - 1]
        else:
            del result[0]
        return result

    def follow_function(self, file_object: BinaryIO) -> None:
        file_object.seek(0, 2)
        while True:
            current_position = file_object.tell()
            line = file_object.read()
            if not line:
                file_object.seek(current_position)
                sleep(self.refresh)
            else:
                if line.startswith(b'\n'):
                    line = line.replace(b'\n', b'', 1)
                if b'\n' in line:
                    for line in line.split(b'\n'):
                        if len(line) > 0:
                            self.callback(line)
                else:
                    self.callback(line)

    @staticmethod
    def bytes_function(file_object: BinaryIO, count: int = 0) -> bytes:
        return file_object.read()[-count:]

    def build_in_callback(self, line: any) -> None:
        if type(line) == bytes:
            if not line.endswith(b'\n'):
                line += b'\n'
            line = line.decode(encoding=self.encoding)
        stdout.writelines(line)

    @staticmethod
    def check_file(file: str) -> bool:
        if not isdir(file):
            if access(path=file, mode=F_OK):
                if access(path=file, mode=R_OK):
                    return True
                else:
                    raise FileNotReadableException(message=f'File "{file}" is not readable')
            else:
                raise NoFileException(message=f'File "{file}" does not exists. Please check filepath')
        else:
            raise FileIsDirectoryException(message=f'File "{file}" is a directory. Please check filepath')


class FileIsDirectoryException(Exception):

    def __init__(self, message) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return super().__str__()


class FileNotReadableException(Exception):

    def __init__(self, message):
        super().__init__(message)

    def __str__(self) -> str:
        return super().__str__()


class NoFileException(Exception):

    def __init__(self, message: str) -> None:
        super().__init__(message)

    def __str__(self) -> str:
        return super().__str__()
