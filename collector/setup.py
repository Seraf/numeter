#!/usr/bin/env python
#
# $Id: setup.py,v 1.32 2010-10-17 15:47:21 gaelL Exp $
#
#    Copyright (C) 2010-2013  Gaël Lambert (gaelL) <gael@gael-lambert.org>
#
#    This file is part of numeter
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

if __name__ == '__main__':

    setup(name='redmon-collector',
        version='0.9.15.1',
        description='Numeter Collector',
        long_description="""Limited Shell (numeter) is lets you restrict the \
environment of any user. It provides an easily configurable shell: just \
choose a list of allowed commands for every limited account.""",
        author='Gaël Lambert (gaelL)',
        author_email='gael@gael-lambert.org',
        maintainer='Gaël Lambert (gaelL)',
        maintainer_email='gael@gael-lambert.org',
        keywords=['limited','shell','security','python'],
        url='https://github.com/enovance/numeter',
        license='GPL',
        platforms='UNIX',
        scripts = ['collector/numeter-collector'],
        packages = [''],
        package_dir = {'':'collector/module'},
        #package_data={'': ['collector/numeter_collector.py']},
        #              ('/etc/logrotate.d', ['etc/logrotate.d/numeter']),
        #              ('share/doc/numeter',['README', 'COPYING', 'CHANGES']),
        #              ('share/man/man1/', ['man/numeter.1']) ],
        data_files = [('/etc/numeter', ['collector/numeter_collector.cfg','collector/poller-list']),
                      ('/var/log/numeter', ''),
                      ('/etc/cron.d', ['collector/numeter-collector-cron']) ],
        classifiers=[
                'Development Status :: 4 - Beta',
                'Environment :: Console'
                'Intended Audience :: Advanced End Users',
                'Intended Audience :: System Administrators',
                'License :: OSI Approved :: GNU General Public License v3',
                'Operating System :: POSIX',
                'Programming Language :: Python',
                'Topic :: Security',
                'Topic :: System Shells',
                'Topic :: Terminals'
                ],
    )
