# Parallelization in OpenFOAM for HPC Deployment Workshop; Project 01

## Lore

You have a coded `fvOptions` source to the velocity equation. But you notice it's not delivering correct results
when running in parallel. Your goal is to fix this issue and achieve consistency between parallel
and serial runs of the case.

## Used/needed software

- A recent ESI/Foundation version of OpenFOAM to run the case.
- ParaView (The headless version if on a cluster/container) with its Python to post-process the case in a scripted manner.
- To observe how the source behaves if we vary parallelization parameters, we conduct parameter variation studies
  with [OpenFOAM-Multi-Objective-Optimization](https://github.com/FoamScience/OpenFOAM-Multi-Objective-Optimization).

## Initial state and objectives

- The `case` runs in serial and delivers the expected result.
- If you run `case/Allrun`, you'll notice inconsistency between serial and parallel runs of the same case though.
- To Broaden your testing coverage, you may want to use parameter variation with `config.yaml` (Make sure you have awk installed).
  You can find instructions on how to do that [here](https://github.com/FoamScience/OpenFOAM-Multi-Objective-Optimization)

Your objective is to modify `case/system/fvOptions` so that the `MaxError` column will always be near **1e-6** (Error in
velocity as if the source was deactivated). Here is an example showcasing initial error values:
```
   casename                                        Sv        xmin  xmax  ymin  ymax  numberOfProcesses  model  MaxError
0  Example_trial_c39946102f0dae57c9628ead95c394ad  0.000084  0.03  0.07  0.02  0.07                  4  Sobol  0.031354
1  Example_trial_fe6985404fe3e5006febccabfe54dd1b  0.000939  0.02  0.06  0.04  0.05                  4  Sobol  0.771100
2  Example_trial_a14a2bd374f8554f9bc196de443fc851  0.000992  0.04  0.09  0.03  0.09                  7  Sobol  0.376710
3  Example_trial_f9a95d53a6a9a204814c01e91da87246  0.000516  0.02  0.09  0.04  0.09                  6  Sobol  0.200970
4  Example_trial_d1635e5df435ba422452520d2aca21ab  0.000629  0.03  0.09  0.03  0.07                  6  Sobol  0.249320
5  Example_trial_c41216a9aa602cd5b13129faa5efefdd  0.000604  0.04  0.09  0.01  0.07                  5  Sobol  0.271220
6  Example_trial_69913960e598438e7d7a3c7b63d60c4b  0.000298  0.01  0.07  0.04  0.06                  6  Sobol  0.103060
7  Example_trial_1f575c6d607f466b5be8190eb8565d76  0.000362  0.01  0.09  0.03  0.09                  7  Sobol  0.139940
```
