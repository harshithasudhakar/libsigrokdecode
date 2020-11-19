##
## This file is part of the libsigrokdecode project.
##
## Copyright (C) 2020 Daniel Maslowski <info@orangecms.org>
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, see <http://www.gnu.org/licenses/>.
##

import sigrokdecode as srd

class Decoder(srd.Decoder):
    api_version = 3
    id = 'pslab'
    name = 'PSLab'
    longname = 'PSLab decoder'
    desc = 'PSLab...'
    license = 'gplv2+'
    inputs = ['logic']
    outputs = []
    tags = ['Embedded/industrial', 'PSLab']
    channels = (
        {'id': 'data', 'name': 'Data', 'desc': 'Data'},
    )
    annotations = (
        ('PSL', 'PSLab'),
    )

    def __init__(self):
        self.reset()

    def reset(self):
        # TODO: reset PSLab

    def start(self):
        # https://sigrok.org/wiki/Protocol_decoder_API#register-function
        self.out_id = self.register(srd.OUTPUT_PYTHON)
        # TODO: connect to PSLab

    # ss and es are short for startsample and endsample for convenience
    def decode(self, ss, es, data):
