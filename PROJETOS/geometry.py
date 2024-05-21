from __future__ import annotations

import math
from dataclasses import dataclass, field
from types import NoneType
from typing import Self

# Building block classes


@dataclass
class Angle:
    """
    An Angle in degrees (unit of measurement)

    >>> Angle()
    Angle(degrees=90)
    >>> Angle(45.5)
    Angle(degrees=45.5)
    >>> Angle(-1)
    Traceback (most recent call last):
        ...
    TypeError: degrees must be a numeric value between 0 and 360.
    >>> Angle(361)
    Traceback (most recent call
