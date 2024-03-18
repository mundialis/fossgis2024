#!/usr/bin/env python3
"""
############################################################################
#
# MODULE:      t.fossgis.fortune
# AUTHOR(S):   Carmen Tawalika
#
# PURPOSE:     Prints fortune cookie sayings
# COPYRIGHT:   (C) 2024 by mundialis GmbH & Co. KG and the GRASS Development
#              Team
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#############################################################################
"""
# %Module
# % description: Prints fortune cookie sayings.
# % keyword: general
# % keyword: fortune
# %end

# %option G_OPT_V_INPUT
# % key: input
# % required: no
# % description: Polygon to generate saying for
# %end

# %option
# % key: box
# % description: Width and height
# % type: double
# % answer: 10,10
# % required: no
# %end

# %flag
# % key: v
# % description: Print fortune version and exit
# %end


import grass.script as grass

try:
    from fortune import fortune
except:
    grass.fatal(_("No fortune"))

def main():
    grass.message(_(fortune()))


if __name__ == "__main__":
    options, flags = grass.parser()
    main()
