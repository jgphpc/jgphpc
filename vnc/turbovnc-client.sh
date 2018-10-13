#!/bin/bash

if [ `uname -n` = "banco" ] ; then
        export PATH=/apps/java/jre1.8.0_71/bin:$PATH
        export PATH=/opt/TurboVNC/bin:$PATH
fi
