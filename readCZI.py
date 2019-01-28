from __future__ import absolute_import, print_function, unicode_literals

import czifile
import os
import javabridge
import bioformats
from bioformats import log4j
import sys

javabridge.start_vm(class_path=bioformats.JARS,
                    run_headless=True)
try:
    log4j.basic_config()

    image_path = "FKO X10 0.5_sox2, pax6, map2-OME TIFF-Export-01.ome.tiff"
    image, scale = bioformats.load_image(image_path, rescale=False,
                                         wants_max_intensity=True)
    try:
        import pylab
        import matplotlib.pyplot as plt

        #pylab.imshow(image)
        plt.imshow(image[50])
        #pylab.gca().set_title(image_path)
        #pylab.show()
    except:
        print(image.shape)
finally:
    javabridge.kill_vm()
