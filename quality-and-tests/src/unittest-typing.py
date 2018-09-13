from dataclasses import dataclass
from datetime import date, datetime, timezone
from typing import Optional
from unittest import TestCase


@dataclass
class Astronaut:
    name: str
    agency: str = 'NASA'
    date_of_birth: Optional[date] = None
    first_step: Optional[datetime] = None

    def __post_init__(self):
        if self.first_step and self.first_step.tzinfo != timezone.utc:
            raise ValueError('Timezone must by UTC')


class AstronautTest(TestCase):
    def test_recruiting_new_astronaut(self):
        jose = Astronaut(name='Jose Jimenez')
        self.assertEqual(jose.name, 'Jose Jimenez')

    def test_default_agency(self):
        jose = Astronaut(name='Jose Jimenez')
        self.assertEqual(jose.agency, 'NASA')

    def test_date_of_birth(self):
        jose = Astronaut(name='Jose Jimenez', date_of_birth=date(1961, 4, 12))
        self.assertEqual(jose.date_of_birth, date(1961, 4, 12))

    def test_first_step_in_utc(self):
        step = datetime(1969, 7, 21, 14, tzinfo=timezone.utc)
        jose = Astronaut(name='Jose Jimenez', first_step=step)
        self.assertEqual(jose.first_step.tzinfo, timezone.utc)

    def test_first_step_not_in_utc(self):
        step = datetime(1969, 7, 21, 14)

        with self.assertRaises(ValueError):
            Astronaut(name='Jose Jimenez', first_step=step)
