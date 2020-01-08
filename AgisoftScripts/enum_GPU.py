import os
import PhotoScan as ps
doc = ps.app.document
app = ps.Application
numGpu = ps.app.enumGPUDevices()
print(numGpu)