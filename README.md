# Parallelization in OpenFOAM for HPC Deployment Workshop; Project 01

## Lore

You have a coded `fvOptions` source to the velocity equation. But you notice it's not delivering correct results
when running in parallel. Your goal is to fix this issue and achieve consistency between parallel
and serial runs of the case.

> Master branch works with ESI OpenFOAM, there is a `of10` branch for Foundation version users. Unfortunately
> there is no support for fvOptions in foam-extend

## Used/needed software

- A recent ESI/Foundation version of OpenFOAM to run the case.
- ParaView (The headless version if on a cluster/container) with its Python to post-process the case in a scripted manner.
- To observe how the source behaves if we vary parallelization parameters, we conduct parameter variation studies
  with [OpenFOAM-Multi-Objective-Optimization](https://github.com/FoamScience/OpenFOAM-Multi-Objective-Optimization).

## Initial state and objectives

- The `case` runs in serial and delivers the expected result.
- If you run `case/Allrun`, you'll notice some considerable inconsistency between serial and parallel runs of the same case though.
- To Broaden your testing coverage, you may want to use parameter variation with `config.yaml` (Make sure you have awk installed).

Simple instructions for running a parameter variation study:
```bash
# Inside this repository
# This will run a sensitivity study on the case with 15 trials
# Parameters include: geometric properties of the source box, source intensity, and number of MPI subdomains
# Objectives: absolute error in mag(U) between serial and parallel runs
pip install foambo
foambo
```

You'll then find a `Project01_report.csv` file (among other things) containing parameter and metric values for each trial.

Your objective is to modify `case/system/fvOptions` so that the `MaxError` column will always be near **1e-5** (Error in
velocity as if the source was deactivated). Here is an example showcasing initial error values:
```
   MaxError Sv       xmin xmax ymin ymax numberOfSubdomains
0  0.24209  0.000605 0.02 0.06 0.04 0.09                  4
1  0.09812  0.000396 0.04 0.05 0.04 0.06                  6
2  0.20791  0.000330 0.01 0.06 0.04 0.07                  7
3  0.08891  0.000144 0.02 0.07 0.03 0.06                  7
4  0.65087  0.000799 0.04 0.07 0.02 0.05                  6
5  0.31942  0.000781 0.01 0.07 0.03 0.06                  5
6  0.35654  0.000685 0.02 0.05 0.03 0.09                  5
```

**In particular**, we want the "relative feature importance" of the `numberOfSubdomains` parameter to be
very close to the importance of other variables. That would mean our parallel code can be trusted!
