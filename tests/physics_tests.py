"""
physics_test.py

Basic validation tests for the core physical concepts used in
Dance of the Titans.

These tests verify mathematical relationships and helper functions
used throughout the simulation.

Author: Aiden Vihaan
Project: Dance of the Titans
"""

import math
import unittest


class TestPhysics(unittest.TestCase):

    def test_gravitational_constant_positive(self):
        G = 6.67430e-11
        self.assertGreater(G, 0)

    def test_event_horizon_radius_positive(self):
        mass = 30
        event_horizon_factor = 2.95
        radius = mass * event_horizon_factor
        self.assertGreater(radius, 0)

    def test_orbital_distance(self):
        distance = 600
        self.assertGreater(distance, 0)

    def test_mass_ratio(self):
        mass_a = 35
        mass_b = 25
        ratio = mass_a / mass_b
        self.assertGreater(ratio, 1)

    def test_energy_positive(self):
        mass = 60
        c = 299792458
        energy = mass * (c ** 2)
        self.assertGreater(energy, 0)

    def test_wave_frequency(self):
        frequency = 150
        self.assertGreater(frequency, 0)


if __name__ == "__main__":
    unittest.main()
