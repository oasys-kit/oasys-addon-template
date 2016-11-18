#! /usr/bin/env python3

import imp
import os
import sys
import subprocess

NAME = 'oasys-addon-template'

VERSION = '1.0'
ISRELEASED = False

DESCRIPTION = 'oasys-addon-template: Template for creating an oasys addon'
README_FILE = os.path.join(os.path.dirname(__file__), 'README.txt')
LONG_DESCRIPTION = open(README_FILE).read()
AUTHOR = 'Manuel Sanchez del Rio'
AUTHOR_EMAIL = 'srio@esrf.eu'
URL = 'http://orange.biolab.si/'
DOWNLOAD_URL = 'http://github.com/srio/oasys-addon-template'
LICENSE = 'MIT'

KEYWORDS = (
    'Oasys',
    'Orange',
    'Template',
    'addon',
)

CLASSIFIERS = (
    'Development Status :: 4 - Beta',
    'Environment :: X11 Applications :: Qt',
    'Environment :: Console',
    'Environment :: Plugins',
    'Programming Language :: Cython',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Intended Audience :: Science/Research',
)


SETUP_REQUIRES = (
                  'setuptools',
                  )

INSTALL_REQUIRES = (
                    'setuptools',
                   )

if len({'develop', 'release', 'bdist_egg', 'bdist_rpm', 'bdist_wininst',
        'install_egg_info', 'build_sphinx', 'egg_info', 'easy_install',
        'upload', 'test'}.intersection(sys.argv)) > 0:
    import setuptools
    extra_setuptools_args = dict(
        zip_safe=False,  # the package can run out of an .egg file
        include_package_data=True,
        install_requires=INSTALL_REQUIRES
    )
else:
    extra_setuptools_args = dict()

from setuptools import find_packages, setup

PACKAGES = find_packages(
                         exclude = ('*.tests', '*.tests.*', 'tests.*', 'tests'),
                         )

PACKAGE_DATA = {"orangecontrib.oasys-addon-template.widgets.widgets1D":["icons/*.png", "icons/*.jpg"],
                "orangecontrib.oasys-addon-template.widgets.plotTools":["icons/*.png", "icons/*.jpg"],
}


NAMESPACE_PACAKGES =
["orangecontrib","orangecontrib.oasys-addon-template",
"orangecontrib.oasys-addon-template.widgets"]


ENTRY_POINTS = {
    'oasys.addons' : ("oasys-addon-template = orangecontrib.oasys-addon-template", ),
    'oasys.widgets' : (
        "oasys-addon-template widgets1D = orangecontrib.oasys-addon-templates.widgets.widgets1D",
        "oasys-addon-template plotTools = orangecontrib.oasys-addon-templates.widgets.plotTools",
    ),
}

if __name__ == '__main__':
    setup(
          name = NAME,
          version = VERSION,
          description = DESCRIPTION,
          long_description = LONG_DESCRIPTION,
          author = AUTHOR,
          author_email = AUTHOR_EMAIL,
          url = URL,
          download_url = DOWNLOAD_URL,
          license = LICENSE,
          keywords = KEYWORDS,
          classifiers = CLASSIFIERS,
          packages = PACKAGES,
          package_data = PACKAGE_DATA,
          setup_requires = SETUP_REQUIRES,
          install_requires = INSTALL_REQUIRES,
          entry_points = ENTRY_POINTS,
          namespace_packages=NAMESPACE_PACAKGES,
          include_package_data = True,
          zip_safe = False,
          )
