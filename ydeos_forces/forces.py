# coding: utf-8

r"""Force model."""

from typing import List, Tuple

import numpy as np


class Force:
    """Force model.

    A force represented by:
    - a vector (force parameter)
    - acting at a given position (position parameter)

    Parameters
    ----------
    force : Represents the x, y, z components of the force vector.
    position : Represents the x, y, z coordinates of the force point of application.
    name : A name given to the force.

    """

    def __init__(self,
                 force: Tuple[float, float, float] = None,
                 position: Tuple[float, float, float] = None,
                 name: str = None):
        if force is None:
            self.force = (0., 0., 0.)
        else:
            if len(force) != 3:
                msg = "A Force object vector should be initialized with a tuple of length == 3"
                raise ValueError(msg)
            # raises ValueError if cast impossible
            self.force = (float(force[0]), float(force[1]), float(force[2]))

        if position is None:
            self.position = (0., 0., 0.)
        else:
            if len(position) != 3:
                msg = "A Force object position should be initialized with a tuple of length == 3"
                raise ValueError(msg)
            self.position = (float(position[0]), float(position[1]), float(position[2]))

        self.name = name

    def moment(self,
               point_of_reference: Tuple[float, float, float]) -> np.ndarray:
        """Moment created by the force.

        Moment of the force about the origin of the frame of reference used
        to define 'position'.

        Parameters
        ----------
        point_of_reference : x, y, z coordinates of the point of reference

        """
        relative_position = (self.px - point_of_reference[0],
                             self.py - point_of_reference[1],
                             self.pz - point_of_reference[2])
        return np.cross(relative_position, self.force)

    @property
    def x(self) -> float:
        r"""X component of Force."""
        return self.force[0]

    @property
    def y(self) -> float:
        r"""Y component of Force."""
        return self.force[1]

    @property
    def z(self) -> float:
        r"""Z component of Force."""
        return self.force[2]

    @property
    def px(self) -> float:
        r"""X coordinate of the point of application."""
        return self.position[0]

    @property
    def py(self) -> float:
        r"""Y coordinate of the point of application."""
        return self.position[1]

    @property
    def pz(self) -> float:
        r"""Z coordinate of the point of application."""
        return self.position[2]

    def __repr__(self) -> str:
        """Readable representation of the Force."""
        name = 'no_name' if self.name is None else self.name
        return f"F:{str(self.force)}@{str(self.position)}-name: {str(name)}"

    def __str__(self) -> str:
        r"""User friendly representation of the Force."""
        return self.__repr__()


class SystemOfForces:
    """A system of forces made of n forces.

    Parameters
    ----------
    forces : list of Force object(s), optional (default : [])
        Represents all the Forces in the SystemOfForces
    moments_point_of_reference : list of 3 floats,
                                 optional (default : [0., 0., 0.])
        Represents the x, y, z coordinates of the point
        of reference for moments calculations.

    """

    def __init__(self,
                 forces: List[Force] = None,
                 moments_point_of_reference: Tuple[float, float, float] = None):
        self.forces = forces if forces is not None else []
        if moments_point_of_reference is None:
            self.moments_point_of_reference = (0., 0., 0.)
        else:
            self.moments_point_of_reference = moments_point_of_reference

    @property
    def moment(self) -> np.ndarray:
        """The moment vector coordinates [x,y,z] of the SystemOfForces."""
        # axis = 0 -> sum of each column
        return np.sum([f.moment(self.moments_point_of_reference) for f in self.forces], axis=0)

    @property
    def mx(self) -> float:
        r"""Moment around X axis."""
        return self.moment[0]

    @property
    def my(self) -> float:
        r"""Moment around Y axis."""
        return self.moment[1]

    @property
    def mz(self) -> float:
        r"""Moment around Z axis."""
        return self.moment[2]

    @property
    def force(self) -> np.ndarray:
        """The sum of all force vectors [x,y,z] of the SystemOfForces."""
        # axis = 0 -> sum of each column
        return np.sum([f.force for f in self.forces], axis=0)

    @property
    def x(self) -> float:
        r"""X component of the resulting force."""
        return self.force[0]

    @property
    def y(self) -> float:
        r"""Y component of the resulting force."""
        return self.force[1]

    @property
    def z(self) -> float:
        r"""Z component of the resulting force."""
        return self.force[2]

    def add_force(self, force: Force):
        """Add a Force object to the SystemOfForces object."""
        self.forces.append(force)
