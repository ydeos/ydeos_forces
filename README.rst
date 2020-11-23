ydeos_forces
============

.. image:: https://travis-ci.org/ydeos/ydeos_forces.svg?branch=main
    :target: https://travis-ci.org/ydeos/ydeos_forces

.. image:: https://app.codacy.com/project/badge/Grade/07c4cb669a7f415bafa66b6cb91ea0bf
    :target: https://www.codacy.com/gh/ydeos/ydeos_forces/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ydeos/ydeos_forces&amp;utm_campaign=Badge_Grade

.. image:: https://coveralls.io/repos/github/ydeos/ydeos_forces/badge.svg?branch=main
    :target: https://coveralls.io/github/ydeos/ydeos_forces?branch=main


**ydeos_forces** is a force / system of forces model library in Python 3.

A force is a 3D vector applied at a 3D point.

A system of forces is a list of forces.

The resulting moment created by a force / system of forces relative to an arbitrary 3D point can be computed. It is a torque if the sum of forces is zero but the moment is not zero: a torque is independent from the 3D point of reference.

For instance, the force / system of forces model can be used to balance the forces in a sailing yacht VPP.

Install
-------

.. code-block:: shell

   git clone https://github.com/ydeos/ydeos_forces
   cd ydeos_forces
   python setup.py install


Examples
--------

See the examples_ folder.


.. _examples: https://github.com/ydeos/ydeos_forces/tree/main/examples


Contribute
----------

Please open an issue if you find a bug or if you come up with ideas about how to improve the project.

Then: fork, feature branch and open a pull request. Feel free to contribute!
