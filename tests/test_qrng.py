# Qoin provides random number generation using quantum computing.
# Copyright (C) 2024  Amir Ali Malekani Nezhad

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations

__all__ = ['TestQRNG']

from qoin.qrng import QRNG

qrng = QRNG()

class TestQRNG:
    """ `TestQRNG` class provides tests for the `QRNG` class.
    """
    def test_randint(self) -> None:
        """ Test the `randint` method of the `QRNG` class.
        """
        for _ in range(1000):
            random_int = qrng.randint(0, 10)
            assert isinstance(random_int, int)
            assert 0 <= random_int < 10

    def test_randbin(self) -> None:
        """ Test the `randbin` method of the `QRNG` class.
        """
        random_bin = qrng.randbin()
        assert isinstance(random_bin, bool)

    def test_random(self) -> None:
        """ Test the `random` method of the `QRNG` class.
        """
        for _ in range(1000):
            random_float = qrng.random(8)
            assert isinstance(random_float, float)
            assert 0 <= random_float < 1

    def test_choice(self) -> None:
        """ Test the `choice` method of the `QRNG` class.
        """
        items = ['a', 'b', 'c', 'd', 'e']
        random_item = qrng.choice(items)
        assert random_item in items

    def test_choices(self) -> None:
        """ Test the `choices` method of the `QRNG` class.
        """
        items = ['a', 'b', 'c', 'd', 'e']
        random_items = qrng.choices(items, 3)
        assert isinstance(random_items, list)
        assert all(item in items for item in random_items)

    def test_sample(self) -> None:
        """ Test the `sample` method of the `QRNG` class.
        """
        items = ['a', 'b', 'c', 'd', 'e']
        random_items = qrng.sample(items, len(items))
        assert sorted(random_items) == sorted(items)

    def test_shuffle(self) -> None:
        """ Test the `shuffle` method of the `QRNG` class.
        """
        items = ['a', 'b', 'c', 'd', 'e']
        shuffled_items = qrng.shuffle(items)
        assert sorted(shuffled_items) == sorted(items)