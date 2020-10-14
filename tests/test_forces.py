#!/usr/bin/env python
# coding: utf-8

r"""Tests for the core.force.py module"""

import pytest

from ydeos_forces.forces import Force, SystemOfForces

force_x_plus_at_0_m1_0 = Force((1., 0., 10.), (0., -1., 0.))
force_x_minus_at_0_1_0 = Force((-1., 0., 10.), (0., 1., 0.))

force_y_plus_at_m1_0_0 = Force((0., 1., 10.), (-1., 0., 0.))
force_y_minus_at_1_0_0 = Force((0., -1., -30.), (1., 0., 0.))


def test_system_of_forces_ref_at_0_0_0():
    r"""Reference is at the origin."""
    sf = SystemOfForces(moments_point_of_reference=(0., 0., 0.))
    sf.add_force(force_x_plus_at_0_m1_0)
    sf.add_force(force_x_minus_at_0_1_0)
    sf.add_force(force_y_plus_at_m1_0_0)
    sf.add_force(force_y_minus_at_1_0_0)
    assert (sf.force == [0., 0., 0.]).all()
    assert (sf.moment == [0., 40., 0.]).all()

    sf = SystemOfForces(moments_point_of_reference=None)
    sf.add_force(force_x_plus_at_0_m1_0)
    sf.add_force(force_x_minus_at_0_1_0)
    sf.add_force(force_y_plus_at_m1_0_0)
    sf.add_force(force_y_minus_at_1_0_0)
    assert (sf.force == [0., 0., 0.]).all()
    assert (sf.moment == [0., 40., 0.]).all()
    assert sf.x == 0.
    assert sf.y == 0.
    assert sf.z == 0.
    assert sf.mx == 0.
    assert sf.my == 40.
    assert sf.mz == 0.


def test_system_of_forces_ref_somewhere_else():
    r"""Reference is at an arbitrary point."""
    sf_2 = SystemOfForces(moments_point_of_reference=(10., 22., 3800.))
    sf_2.add_force(force_x_plus_at_0_m1_0)
    sf_2.add_force(force_x_minus_at_0_1_0)
    sf_2.add_force(force_y_plus_at_m1_0_0)
    sf_2.add_force(force_y_minus_at_1_0_0)
    assert (sf_2.force == [0., 0., 0.]).all()
    assert (sf_2.moment == [0., 40., 0.]).all()


def test_none_input():
    r"""Force and point are None."""
    f = Force(None, None)
    assert f.x == 0
    assert f.y == 0
    assert f.z == 0
    assert f.px == 0
    assert f.py == 0
    assert f.pz == 0


def test_good_input():
    r"""Force and point are OK."""
    f = Force((1., 2., 3.), (1., 2., 3.))
    assert f.x == 1.
    assert f.y == 2.
    assert f.z == 3.
    assert f.px == 1.
    assert f.py == 2.
    assert f.pz == 3.


def test_wrong_input():
    r"""The inputs are wrong."""
    with pytest.raises(ValueError):
        Force((1., 2., 3., 4.), None)

    with pytest.raises(ValueError):
        Force(None, (1., 2., 3., 4.))

    with pytest.raises(ValueError):
        Force(('a', 2., 3.), (1., 2., 3.))

    with pytest.raises(ValueError):
        Force((1., 2., 3.), (1., 'a', 3.))


def test_representation():
    r"""str and repr tests"""
    f = Force((1., 2., 3.), (1., 2., 3.))
    assert str(f) == "F:(1.0, 2.0, 3.0)@(1.0, 2.0, 3.0)-name: no_name"

    f = Force((1., 2., 3.), (1., 2., 3.), name="The Force")
    assert str(f) == "F:(1.0, 2.0, 3.0)@(1.0, 2.0, 3.0)-name: The Force"
    assert repr(f) == "F:(1.0, 2.0, 3.0)@(1.0, 2.0, 3.0)-name: The Force"
