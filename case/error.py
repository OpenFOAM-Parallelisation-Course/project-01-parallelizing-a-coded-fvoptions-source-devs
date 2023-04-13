#!/usr/bin/env pvpython

# trace generated using paraview version 5.10.0
# Run with: pvpython error.py
# Depends on: 0.5/USerial (moved from serial run) and 0.5/U (reconstructed from parallel run)

#### import the simple module from the paraview
from paraview.simple import *
import paraview.servermanager as sm
import os
root = os.getcwd()

# create a new 'OpenFOAMReader'
casefoam = OpenFOAMReader(registrationName='case.foam', FileName=f"{root}/case.foam")
casefoam.MeshRegions = ['internalMesh']
UpdatePipeline(time=0.5, proxy=casefoam)
casefoam.CellArrays = ['USerial', 'U']

# calculate error
error = Calculator(registrationName='Calculator1', Input=casefoam)
error.Function = 'abs(U-USerial)'
error.AttributeType = 'Cell Data'
error.ResultArrayName = 'Error'

# Display error range
data = sm.Fetch(error)
(min, max) = data.GetBlock(0).GetCellData().GetArray('Error').GetRange()
(minU, maxU) = data.GetBlock(0).GetCellData().GetArray('USerial').GetRange()
print(f"Max mag(U_serial - U_parallel) = {max:.4e}, max(U) = {maxU}")
print(f"Min mag(U_serial - U_parallel) = {min:.4e}, min(U) = {minU}")
