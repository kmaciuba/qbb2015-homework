#!/usr/bin/env python

from __future__ import division

import sys
import chrombitsHOMEWORK



arr = chrombitsHOMEWORK.ChromosomeLocationBitArrays( fname=sys.argv[1] )

ctcf = arr.copy()
beaf = arr.copy()

ctcf.set_bits_from_file( sys.argv[2] )
beaf.set_bits_from_file( sys.argv[3] )

new = beaf.intersect( ctcf.complement() )

############
############


x=new.homework()


print  x
