This is the second attempt to improve the data that is being generated after a succesfull pipeline is established

In this attempt epochs was set to 50

Did not complete, last messages:
{
1993              3759 -75.099998     0.0016       -0.0424  
1993              3759 -75.099998     0.0016       -0.0424  

[54861 rows x 8 columns]
A DataProcessor is not available for the TimeGAN.
Emddeding network training: 100%|██████████████████████████████████████| 50/50 [01:12<00:00,  1.44s/it]
Supervised network training: 100%|█████████████████████████████████████| 50/50 [01:11<00:00,  1.43s/it]
Joint networks training: 100%|█████████████████████████████████████████| 50/50 [04:31<00:00,  5.43s/it]
6 0
6 1
6 2
6 3
6 4
7
cd_counter_rollers_installation      0.0
ld_counter_rollers_installation      0.0
closing_device_failure             False
misalignment_cd_vs_ld                0.0
misalignment_cd_vs_ld_sill_gap       1.0
belt_tension                         0.0
pulley_is_touching_belt            False
zero_position                        0.0
Name: 7, dtype: object
     cmcouplerfriction  cmdoorfriction  cmelectronicage  cmvibration  \
268         143.199997      118.400002             0.89          0.7   
268         143.199997      118.400002             0.89          0.7   
268         143.199997      118.400002             0.89          0.7   
268         143.199997      118.400002             0.89          0.7   
268         143.199997      118.400002             0.89          0.7   
..                 ...             ...              ...          ...   
501         156.199997      124.800003             0.91          1.1   
501         156.199997      124.800003             0.91          1.1   
501         156.199997      124.800003             0.91          1.1   
501         156.199997      124.800003             0.91          1.1   
501         156.199997      124.800003             0.91          1.1   

     doorcyclecounter  doorforce  doorspeed  doorposition  
268              1440 -75.099998     0.0016       -0.0492  
268              1440 -75.099998     0.0016       -0.0492  
268              1440 -75.099998     0.0016       -0.0492  
268              1440 -93.400002     0.0016       -0.0492  
268              1440 -58.700001     0.0307       -0.0480  
..                ...        ...        ...           ...  
501              1673 -75.099998     0.0016       -0.0492  
501              1673 -75.099998     0.0016       -0.0492  
501              1673 -75.099998     0.0016       -0.0492  
501              1673 -75.099998     0.0016       -0.0492  
501              1673 -75.099998     0.0016       -0.0492  

[44124 rows x 8 columns]
A DataProcessor is not available for the TimeGAN.
Emddeding network training: 100%|██████████████████████████████████████| 50/50 [00:58<00:00,  1.17s/it]
Supervised network training: 100%|█████████████████████████████████████| 50/50 [00:57<00:00,  1.15s/it]
Joint networks training: 100%|█████████████████████████████████████████| 50/50 [03:53<00:00,  4.68s/it]
7 0
7 1
7 2
7 3
7 4
8
cd_counter_rollers_installation      0.0
ld_counter_rollers_installation      0.0
closing_device_failure             False
misalignment_cd_vs_ld                1.0
misalignment_cd_vs_ld_sill_gap       0.0
belt_tension                         0.0
pulley_is_touching_belt            False
zero_position                        0.0
Name: 8, dtype: object
    cmcouplerfriction  cmdoorfriction  cmelectronicage  cmvibration  \
0          154.899994      121.300003             0.86          0.9   
0          154.899994      121.300003             0.86          0.9   
0          154.899994      121.300003             0.86          0.9   
0          154.899994      121.300003             0.86          0.9   
0          154.899994      121.300003             0.86          0.9   
..                ...             ...              ...          ...   
17         146.500000      132.699997             0.93          1.1   
17         146.500000      132.699997             0.93          1.1   
17         146.500000      132.699997             0.93          1.1   
17         146.500000      132.699997             0.93          1.1   
17         146.500000      132.699997             0.93          1.1   

    doorcyclecounter  doorforce  doorspeed  doorposition  
0               1166 -75.099998     0.0016       -0.0492  
0               1166 -75.099998     0.0016       -0.0492  
0               1166 -92.800003     0.0016       -0.0492  
0               1166 -73.500000     0.0016       -0.0492  
0               1166 -51.900002     0.0531       -0.0451  
..               ...        ...        ...           ...  
17              1185 -75.099998     0.0016       -0.0492  
17              1185 -75.099998     0.0016       -0.0492  
17              1185 -75.099998     0.0016       -0.0492  
17              1185 -75.099998     0.0016       -0.0492  
17              1185 -75.099998     0.0016       -0.0492  

[3410 rows x 8 columns]
A DataProcessor is not available for the TimeGAN.
Emddeding network training: 100%|██████████████████████████████████████| 50/50 [00:09<00:00,  5.10it/s]
Supervised network training: 100%|█████████████████████████████████████| 50/50 [00:35<00:00,  1.40it/s]
Joint networks training:   0%|                                                  | 0/50 [00:00<?, ?it/s]Killed
}