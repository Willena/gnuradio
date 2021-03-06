#
# Copyright 2012-2013 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
#

'''
Blocks for channel models and related functions.
'''
from __future__ import absolute_import
from __future__ import unicode_literals

import os

try:
    from .channels_swig import channels_swig
except ImportError:
    dirname, filename = os.path.split(os.path.abspath(__file__))
    __path__.append(os.path.join(dirname, "..", "..", "swig"))
    from .channels_swig import *

# Blocks for Hardware Impairments
from .amp_bal import amp_bal
from .conj_fs_iqcorr import conj_fs_iqcorr
from .distortion_2_gen import distortion_2_gen
from .distortion_3_gen import distortion_3_gen
from .impairments import impairments
from .iqbal_gen import iqbal_gen
from .phase_bal import phase_bal
from .phase_noise_gen import phase_noise_gen
from .quantizer import quantizer
