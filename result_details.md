# Details results

This file contains more detailed analysis of models' performance on the various datasets we employed.

### Respective datasets

> Glow-ViT

```
***** glow-vit | testing on SeaSponge/wildme10_classify  metrics *****
  eval_loss                   =     0.1246
  eval_model_preparation_time =      0.006
  eval_runtime                = 0:04:34.66
  eval_samples_per_second     =      13.22
  eval_steps_per_second       =      0.826
***** glow-vit | testing on yin30lei/wildlife_very_dark  metrics *****
  eval_loss                   =     4.5018
  eval_model_preparation_time =      0.006
  eval_runtime                = 0:00:53.63
  eval_samples_per_second     =     13.087
  eval_steps_per_second       =       0.82
***** glow-vit | testing on yin30lei/wildlife_well_illuminated  metrics *****
  eval_loss                   =     0.0225
  eval_model_preparation_time =      0.006
  eval_runtime                = 0:02:51.68
  eval_samples_per_second     =     13.589
  eval_steps_per_second       =       0.85
***** glow-vit | testing on yin30lei/wildlife_mixed  metrics *****
  eval_loss                   =     0.5657
  eval_model_preparation_time =     0.0057
  eval_runtime                = 0:05:08.96
  eval_samples_per_second     =      12.81
  eval_steps_per_second       =      0.803  
```

> Glow-ViT-dark

```
***** glow-vit-dark | testing on SeaSponge/wildme10_classify  metrics *****
  eval_loss                   =     0.2078
  eval_model_preparation_time =     0.0058
  eval_runtime                = 0:04:38.73
  eval_samples_per_second     =     13.027
  eval_steps_per_second       =      0.814
***** glow-vit-dark | testing on yin30lei/wildlife_very_dark  metrics *****
  eval_loss                   =     0.5554
  eval_model_preparation_time =     0.0058
  eval_runtime                = 0:00:53.22
  eval_samples_per_second     =     13.189
  eval_steps_per_second       =      0.827
***** glow-vit-dark | testing on yin30lei/wildlife_well_illuminated  metrics *****
  eval_loss                   =     0.1712
  eval_model_preparation_time =     0.0058
  eval_runtime                = 0:02:56.09
  eval_samples_per_second     =     13.249
  eval_steps_per_second       =      0.829
***** glow-vit-dark | testing on yin30lei/wildlife_mixed  metrics *****
  eval_loss                   =     0.2502
  eval_model_preparation_time =     0.0058
  eval_runtime                = 0:05:14.45
  eval_samples_per_second     =     12.587
  eval_steps_per_second       =      0.789
```

> Glow-ViT-illuminate

```
***** glow-vit-illuminate | testing on SeaSponge/wildme10_classify  metrics *****
  eval_loss                   =     0.1177
  eval_model_preparation_time =     0.0035
  eval_runtime                = 0:04:43.47
  eval_samples_per_second     =     12.809
  eval_steps_per_second       =      0.801
***** glow-vit-illuminate | testing on yin30lei/wildlife_very_dark  metrics *****
  eval_loss                   =     2.1939
  eval_model_preparation_time =     0.0035
  eval_runtime                = 0:00:54.60
  eval_samples_per_second     =     12.857
  eval_steps_per_second       =      0.806
***** glow-vit-illuminate | testing on yin30lei/wildlife_well_illuminated  metrics *****
  eval_loss                   =     0.1064
  eval_model_preparation_time =     0.0035
  eval_runtime                = 0:02:56.43
  eval_samples_per_second     =     13.223
  eval_steps_per_second       =      0.827
***** glow-vit-illuminate | testing on yin30lei/wildlife_mixed  metrics *****
  eval_loss                   =     0.4042
  eval_model_preparation_time =     0.0035
  eval_runtime                = 0:05:31.54
  eval_samples_per_second     =     11.938
  eval_steps_per_second       =      0.748
```

> Glow-ViT-mix

```
***** glow-vit-mix | testing on SeaSponge/wildme10_classify  metrics *****
  eval_loss                   =     0.0744
  eval_model_preparation_time =     0.0061
  eval_runtime                = 0:04:18.65
  eval_samples_per_second     =     14.038
  eval_steps_per_second       =      0.878
***** glow-vit-mix | testing on yin30lei/wildlife_very_dark  metrics *****
  eval_loss                   =     0.3715
  eval_model_preparation_time =     0.0061
  eval_runtime                = 0:00:52.80
  eval_samples_per_second     =     13.294
  eval_steps_per_second       =      0.833
***** glow-vit-mix | testing on yin30lei/wildlife_well_illuminated  metrics *****
  eval_loss                   =     0.0243
  eval_model_preparation_time =     0.0061
  eval_runtime                = 0:02:47.16
  eval_samples_per_second     =     13.956
  eval_steps_per_second       =      0.873
***** glow-vit-mix | testing on yin30lei/wildlife_mixed  metrics *****
  eval_loss                   =     0.1449
  eval_model_preparation_time =     0.0061
  eval_runtime                = 0:05:09.75
  eval_samples_per_second     =     12.778
  eval_steps_per_second       =      0.801
```

### The various low-exposure datasets

> Glow-ViT

```
***** glow-vit | testing on yin30lei/wildlife_very_dark_test  metrics *****
  eval_loss                   =     4.3495
  eval_model_preparation_time =     0.0024
  eval_runtime                = 0:01:02.41
  eval_samples_per_second     =     21.118
  eval_steps_per_second       =       1.33
***** glow-vit | testing on yin30lei/wildlife_grayscale  metrics *****
  eval_loss                   =     0.2021
  eval_model_preparation_time =     0.0024
  eval_runtime                = 0:02:17.93
  eval_samples_per_second     =     13.231
  eval_steps_per_second       =      0.834
***** glow-vit | testing on yin30lei/wildlife_less_saturated  metrics *****
  eval_loss                   =      0.176
  eval_model_preparation_time =     0.0024
  eval_runtime                = 0:00:56.60
  eval_samples_per_second     =     20.086
  eval_steps_per_second       =      1.272
***** glow-vit | testing on yin30lei/wildlife_underexposed  metrics *****
  eval_loss                   =      0.351
  eval_model_preparation_time =     0.0024
  eval_runtime                = 0:00:56.39
  eval_samples_per_second     =     20.162
  eval_steps_per_second       =      1.277
```

> Glow-ViT-dark

```
***** glow-vit-dark | testing on yin30lei/wildlife_very_dark_test  metrics *****
  eval_loss                   =     0.4528
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:01:09.23
  eval_samples_per_second     =     19.035
  eval_steps_per_second       =      1.199
***** glow-vit-dark | testing on yin30lei/wildlife_grayscale  metrics *****
  eval_loss                   =     0.2992
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:02:20.41
  eval_samples_per_second     =     12.997
  eval_steps_per_second       =      0.819
***** glow-vit-dark | testing on yin30lei/wildlife_less_saturated  metrics *****
  eval_loss                   =     0.3231
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:00:53.08
  eval_samples_per_second     =     21.418
  eval_steps_per_second       =      1.356
***** glow-vit-dark | testing on yin30lei/wildlife_underexposed  metrics *****
  eval_loss                   =     0.2702
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:00:52.00
  eval_samples_per_second     =     21.862
  eval_steps_per_second       =      1.384
```

> Glow-ViT_illuminate

```
***** glow-vit-illuminate | testing on yin30lei/wildlife_very_dark_test  metrics *****
  eval_loss                   =     2.2027
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:01:06.86
  eval_samples_per_second     =     19.711
  eval_steps_per_second       =      1.241
***** glow-vit-illuminate | testing on yin30lei/wildlife_grayscale  metrics *****
  eval_loss                   =     0.3929
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:02:22.54
  eval_samples_per_second     =     12.803
  eval_steps_per_second       =      0.807
***** glow-vit-illuminate | testing on yin30lei/wildlife_less_saturated  metrics *****
  eval_loss                   =     0.4334
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:00:56.92
  eval_samples_per_second     =     19.972
  eval_steps_per_second       =      1.265
***** glow-vit-illuminate | testing on yin30lei/wildlife_underexposed  metrics *****
  eval_loss                   =     0.5756
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:00:56.58
  eval_samples_per_second     =     20.094
  eval_steps_per_second       =      1.272
```


> Glow-ViT-mix

```
***** glow-vit-mix | testing on yin30lei/wildlife_very_dark_test  metrics *****
  eval_loss                   =     0.1396
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:01:02.49
  eval_samples_per_second     =     21.091
  eval_steps_per_second       =      1.328
***** glow-vit-mix | testing on yin30lei/wildlife_grayscale  metrics *****
  eval_loss                   =     0.0776
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:02:17.69
  eval_samples_per_second     =     13.254
  eval_steps_per_second       =      0.835
***** glow-vit-mix | testing on yin30lei/wildlife_less_saturated  metrics *****
  eval_loss                   =     0.0707
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:00:53.79
  eval_samples_per_second     =     21.135
  eval_steps_per_second       =      1.338  
***** glow-vit-mix | testing on yin30lei/wildlife_underexposed  metrics *****
  eval_loss                   =     0.0472
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:00:54.75
  eval_samples_per_second     =     20.766
  eval_steps_per_second       =      1.315
```


### Filtered dataset:

#### very_dark

> Glow-ViT

```
***** glow-vit | testing on yin30lei/wildlife_verydark_clahe  metrics *****
  eval_loss                   =      0.075
  eval_model_preparation_time =     0.0028
  eval_runtime                = 0:01:10.11
  eval_samples_per_second     =     18.797
  eval_steps_per_second       =      1.184
***** glow-vit | testing on yin30lei/wildlife_verydark_he  metrics *****
  eval_loss                   =     0.1791
  eval_model_preparation_time =     0.0028
  eval_runtime                = 0:01:12.74
  eval_samples_per_second     =     18.119
  eval_steps_per_second       =      1.141
***** glow-vit | testing on yin30lei/wildlife_verydark_afifi  metrics *****
  eval_loss                   =     0.4517
  eval_model_preparation_time =     0.0028
  eval_runtime                = 0:01:08.64
  eval_samples_per_second     =     19.199
  eval_steps_per_second       =      1.209
```

> Glow-ViT-dark

```
***** glow-vit-dark | testing on yin30lei/wildlife_verydark_clahe  metrics *****
  eval_loss                   =     0.2089
  eval_model_preparation_time =     0.0033
  eval_runtime                = 0:01:10.19
  eval_samples_per_second     =     18.775
  eval_steps_per_second       =      1.182
***** glow-vit-dark | testing on yin30lei/wildlife_verydark_he  metrics *****
  eval_loss                   =     0.2324
  eval_model_preparation_time =     0.0033
  eval_runtime                = 0:01:09.88
  eval_samples_per_second     =      18.86
  eval_steps_per_second       =      1.188
***** glow-vit-dark | testing on yin30lei/wildlife_verydark_afifi  metrics *****
  eval_loss                   =     0.3838
  eval_model_preparation_time =     0.0033
  eval_runtime                = 0:01:10.25
  eval_samples_per_second     =     18.761
  eval_steps_per_second       =      1.181
```

> Glow-ViT-illuminate

```
***** glow-vit-illuminate | testing on yin30lei/wildlife_verydark_clahe  metrics *****
  eval_loss                   =     0.3039
  eval_model_preparation_time =     0.0032
  eval_runtime                = 0:01:09.24
  eval_samples_per_second     =     19.033
  eval_steps_per_second       =      1.199
***** glow-vit-illuminate | testing on yin30lei/wildlife_verydark_he  metrics *****
  eval_loss                   =      0.419
  eval_model_preparation_time =     0.0032
  eval_runtime                = 0:01:03.51
  eval_samples_per_second     =     20.752
  eval_steps_per_second       =      1.307
***** glow-vit-illuminate | testing on yin30lei/wildlife_verydark_afifi  metrics *****
  eval_loss                   =     0.6543
  eval_model_preparation_time =     0.0032
  eval_runtime                = 0:01:04.05
  eval_samples_per_second     =     20.576
  eval_steps_per_second       =      1.296
```

> Glow-ViT-mix

```

***** glow-vit-mix | testing on yin30lei/wildlife_verydark_clahe  metrics *****
  eval_loss                   =     0.1768
  eval_model_preparation_time =     0.0024
  eval_runtime                = 0:01:13.95
  eval_samples_per_second     =     17.821
  eval_steps_per_second       =      1.122
***** glow-vit-mix | testing on yin30lei/wildlife_verydark_he  metrics *****
  eval_loss                   =     0.1925
  eval_model_preparation_time =     0.0024
  eval_runtime                = 0:01:09.50
  eval_samples_per_second     =     18.962
  eval_steps_per_second       =      1.194
***** glow-vit-mix | testing on yin30lei/wildlife_verydark_afifi  metrics *****
  eval_loss                   =     0.1952
  eval_model_preparation_time =     0.0024
  eval_runtime                = 0:01:10.62
  eval_samples_per_second     =     18.662
  eval_steps_per_second       =      1.175

```


#### less-saturated

> Glow-ViT

```
***** glow-vit | testing on yin30lei/wildlife_less_saturated_clahe  metrics *****
  eval_loss                   =     0.4322
  eval_model_preparation_time =      0.003
  eval_runtime                = 0:00:59.21
  eval_samples_per_second     =     19.202
  eval_steps_per_second       =      1.216
README.md: 100%
 459/459 [00:00<00:00, 24.5kB/s]
Generating train split: 100%
 1137/1137 [00:00<00:00, 3084.09 examples/s]
***** glow-vit | testing on yin30lei/wildlife_less_saturated_he  metrics *****
  eval_loss                   =     0.1722
  eval_model_preparation_time =      0.003
  eval_runtime                = 0:00:54.37
  eval_samples_per_second     =     20.912
  eval_steps_per_second       =      1.324
README.md: 100%
 461/461 [00:00<00:00, 22.2kB/s]
Generating train split: 100%
 1137/1137 [00:00<00:00, 2149.82 examples/s]
***** glow-vit | testing on yin30lei/wildlife_less_saturated_afifi  metrics *****
  eval_loss                   =     0.1746
  eval_model_preparation_time =      0.003
  eval_runtime                = 0:00:52.28
  eval_samples_per_second     =     21.745
  eval_steps_per_second       =      1.377
```

> Glow-ViT-dark

```
***** glow-vit-dark | testing on yin30lei/wildlife_less_saturated_clahe  metrics *****
  eval_loss                   =     0.5156
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:00:54.74
  eval_samples_per_second     =      20.77
  eval_steps_per_second       =      1.315
***** glow-vit-dark | testing on yin30lei/wildlife_less_saturated_he  metrics *****
  eval_loss                   =     0.2069
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:00:51.13
  eval_samples_per_second     =     22.236
  eval_steps_per_second       =      1.408
***** glow-vit-dark | testing on yin30lei/wildlife_less_saturated_afifi  metrics *****
  eval_loss                   =     0.3232
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:00:53.64
  eval_samples_per_second     =     21.194
  eval_steps_per_second       =      1.342
```

> Glow-ViT-illuminate

```
***** glow-vit-illuminate | testing on yin30lei/wildlife_less_saturated_clahe  metrics *****
  eval_loss                   =     0.6073
  eval_model_preparation_time =     0.0024
  eval_runtime                = 0:00:55.73
  eval_samples_per_second     =     20.399
  eval_steps_per_second       =      1.292
***** glow-vit-illuminate | testing on yin30lei/wildlife_less_saturated_he  metrics *****
  eval_loss                   =     0.3827
  eval_model_preparation_time =     0.0024
  eval_runtime                = 0:00:54.40
  eval_samples_per_second     =       20.9
  eval_steps_per_second       =      1.324
***** glow-vit-illuminate | testing on yin30lei/wildlife_less_saturated_afifi  metrics *****
  eval_loss                   =     0.3601
  eval_model_preparation_time =     0.0024
  eval_runtime                = 0:00:51.80
  eval_samples_per_second     =     21.946
  eval_steps_per_second       =       1.39
```

> Glow-ViT-mix

```
***** glow-vit-mix | testing on yin30lei/wildlife_less_saturated_clahe  metrics *****
  eval_loss                   =      0.207
  eval_model_preparation_time =     0.0029
  eval_runtime                = 0:00:59.91
  eval_samples_per_second     =     18.978
  eval_steps_per_second       =      1.202
***** glow-vit-mix | testing on yin30lei/wildlife_less_saturated_he  metrics *****
  eval_loss                   =     0.1004
  eval_model_preparation_time =     0.0029
  eval_runtime                = 0:00:52.45
  eval_samples_per_second     =     21.674
  eval_steps_per_second       =      1.373
***** glow-vit-mix | testing on yin30lei/wildlife_less_saturated_afifi  metrics *****
  eval_loss                   =     0.0977
  eval_model_preparation_time =     0.0029
  eval_runtime                = 0:00:52.51
  eval_samples_per_second     =     21.653
  eval_steps_per_second       =      1.371
```

#### underexposed

> Glow-ViT

```
***** glow-vit | testing on yin30lei/wildlife_underexposed_clahe  metrics *****
  eval_loss                   =     0.0688
  eval_model_preparation_time =     0.0023
  eval_runtime                = 0:01:00.30
  eval_samples_per_second     =     18.855
  eval_steps_per_second       =      1.194
***** glow-vit | testing on yin30lei/wildlife_underexposed_he  metrics *****
  eval_loss                   =     0.1119
  eval_model_preparation_time =     0.0023
  eval_runtime                = 0:00:56.81
  eval_samples_per_second     =     20.013
  eval_steps_per_second       =      1.267
***** glow-vit | testing on yin30lei/wildlife_underexposed_afifi  metrics *****
  eval_loss                   =     0.0692
  eval_model_preparation_time =     0.0023
  eval_runtime                = 0:00:58.17
  eval_samples_per_second     =     19.543
  eval_steps_per_second       =      1.238
```


> Glow-ViT-Dark

```
***** glow-vit-dark | testing on yin30lei/wildlife_underexposed_clahe  metrics *****
  eval_loss                   =     0.2596
  eval_model_preparation_time =     0.0027
  eval_runtime                = 0:01:03.22
  eval_samples_per_second     =     17.982
  eval_steps_per_second       =      1.139
README.md: 100%
 461/461 [00:00<00:00, 22.5kB/s]
Generating train split: 100%
 1137/1137 [00:00<00:00, 1566.71 examples/s]
***** glow-vit-dark | testing on yin30lei/wildlife_underexposed_he  metrics *****
  eval_loss                   =     0.2636
  eval_model_preparation_time =     0.0027
  eval_runtime                = 0:00:58.08
  eval_samples_per_second     =     19.576
  eval_steps_per_second       =       1.24
README.md: 100%
 461/461 [00:00<00:00, 25.2kB/s]
Generating train split: 100%
 1137/1137 [00:00<00:00, 3154.83 examples/s]
***** glow-vit-dark | testing on yin30lei/wildlife_underexposed_afifi  metrics *****
  eval_loss                   =      0.245
  eval_model_preparation_time =     0.0027
  eval_runtime                = 0:00:55.07
  eval_samples_per_second     =     20.645
  eval_steps_per_second       =      1.307
```

> Glow-ViT-illuminate

```
***** glow-vit-illuminate | testing on yin30lei/wildlife_underexposed_clahe  metrics *****
  eval_loss                   =     0.2424
  eval_model_preparation_time =     0.0025
  eval_runtime                = 0:01:02.28
  eval_samples_per_second     =     18.255
  eval_steps_per_second       =      1.156
***** glow-vit-illuminate | testing on yin30lei/wildlife_underexposed_he  metrics *****
  eval_loss                   =      0.255
  eval_model_preparation_time =     0.0025
  eval_runtime                = 0:00:54.62
  eval_samples_per_second     =     20.814
  eval_steps_per_second       =      1.318
***** glow-vit-illuminate | testing on yin30lei/wildlife_underexposed_afifi  metrics *****
  eval_loss                   =     0.2446
  eval_model_preparation_time =     0.0025
  eval_runtime                = 0:00:54.77
  eval_samples_per_second     =     20.759
  eval_steps_per_second       =      1.315
```

> Glow-Vit-mix

```
***** glow-vit-mix | testing on yin30lei/wildlife_underexposed_clahe  metrics *****
  eval_loss                   =     0.0577
  eval_model_preparation_time =     0.0027
  eval_runtime                = 0:00:58.96
  eval_samples_per_second     =     19.283
  eval_steps_per_second       =      1.221
***** glow-vit-mix | testing on yin30lei/wildlife_underexposed_he  metrics *****
  eval_loss                   =     0.0917
  eval_model_preparation_time =     0.0027
  eval_runtime                = 0:00:54.53
  eval_samples_per_second     =     20.847
  eval_steps_per_second       =       1.32
***** glow-vit-mix | testing on yin30lei/wildlife_underexposed_afifi  metrics *****
  eval_loss                   =      0.061
  eval_model_preparation_time =     0.0027
  eval_runtime                = 0:00:56.55
  eval_samples_per_second     =     20.104
  eval_steps_per_second       =      1.273
```


### Extra details:

> Glow-ViT

```
***** glow-vit | testing on yin30lei/wildlife_very_dark_test  metrics *****
  eval_accuracy               =     0.2193
  eval_f1_weighted            =     0.1204
  eval_loss                   =     4.3495
  eval_model_preparation_time =     0.0023
  eval_precision_weighted     =     0.5146
  eval_recall_weighted        =     0.2193
  eval_runtime                = 0:01:08.37
  eval_samples_per_second     =     19.277
  eval_steps_per_second       =      1.214
***** glow-vit | testing on yin30lei/wildlife_grayscale  metrics *****
  eval_accuracy               =     0.9474
  eval_f1_weighted            =      0.947
  eval_loss                   =     0.2021
  eval_model_preparation_time =     0.0023
  eval_precision_weighted     =     0.9583
  eval_recall_weighted        =     0.9474
  eval_runtime                = 0:02:08.26
  eval_samples_per_second     =     14.228
  eval_steps_per_second       =      0.897



***** glow-vit | testing on yin30lei/wildlife_less_saturated  metrics *****
  eval_accuracy               =     0.9551
  eval_f1_weighted            =     0.9571
  eval_loss                   =      0.176
  eval_model_preparation_time =     0.0023
  eval_precision_weighted     =     0.9612
  eval_recall_weighted        =     0.9551
  eval_runtime                = 0:00:51.20
  eval_samples_per_second     =     22.204
  eval_steps_per_second       =      1.406
***** glow-vit | testing on yin30lei/wildlife_underexposed  metrics *****
  eval_accuracy               =     0.9244
  eval_f1_weighted            =     0.9393
  eval_loss                   =      0.351
  eval_model_preparation_time =     0.0023
  eval_precision_weighted     =     0.9573
  eval_recall_weighted        =     0.9244
  eval_runtime                = 0:00:59.22
  eval_samples_per_second     =     19.199
  eval_steps_per_second       =      1.216
***** glow-vit | testing on yin30lei/wildlife_verydark_clahe  metrics *****
  eval_accuracy               =     0.9848
  eval_f1_weighted            =     0.9849
  eval_loss                   =      0.075
  eval_model_preparation_time =     0.0023
  eval_precision_weighted     =     0.9851
  eval_recall_weighted        =     0.9848
  eval_runtime                = 0:01:06.77
  eval_samples_per_second     =     19.738
  eval_steps_per_second       =      1.243
***** glow-vit | testing on yin30lei/wildlife_verydark_he  metrics *****
  eval_accuracy               =     0.9537
  eval_f1_weighted            =     0.9538
  eval_loss                   =     0.1791
  eval_model_preparation_time =     0.0023
  eval_precision_weighted     =     0.9551
  eval_recall_weighted        =     0.9537
  eval_runtime                = 0:01:04.56
  eval_samples_per_second     =     20.413
  eval_steps_per_second       =      1.285
***** glow-vit | testing on yin30lei/wildlife_verydark_afifi  metrics *****
  eval_accuracy               =     0.8953
  eval_f1_weighted            =     0.8959
  eval_loss                   =     0.4517
  eval_model_preparation_time =     0.0023
  eval_precision_weighted     =     0.9021
  eval_recall_weighted        =     0.8953
  eval_runtime                = 0:01:08.96
  eval_samples_per_second     =      19.11
  eval_steps_per_second       =      1.203
***** glow-vit | testing on yin30lei/wildlife_less_saturated_clahe  metrics *****
  eval_accuracy               =     0.9015
  eval_f1_weighted            =     0.9003
  eval_loss                   =     0.4322
  eval_model_preparation_time =     0.0023
  eval_precision_weighted     =     0.9157
  eval_recall_weighted        =     0.9015
  eval_runtime                = 0:00:55.43
  eval_samples_per_second     =     20.511
  eval_steps_per_second       =      1.299



***** glow-vit | testing on yin30lei/wildlife_less_saturated_he  metrics *****
  eval_accuracy               =     0.9587
  eval_f1_weighted            =      0.959
  eval_loss                   =     0.1722
  eval_model_preparation_time =     0.0023
  eval_precision_weighted     =     0.9606
  eval_recall_weighted        =     0.9587
  eval_runtime                = 0:00:52.94
  eval_samples_per_second     =     21.477
  eval_steps_per_second       =       1.36
***** glow-vit | testing on yin30lei/wildlife_less_saturated_afifi  metrics *****
  eval_accuracy               =     0.9507
  eval_f1_weighted            =      0.952
  eval_loss                   =     0.1746
  eval_model_preparation_time =     0.0023
  eval_precision_weighted     =     0.9547
  eval_recall_weighted        =     0.9507
  eval_runtime                = 0:01:01.18
  eval_samples_per_second     =     18.582
  eval_steps_per_second       =      1.177
***** glow-vit | testing on yin30lei/wildlife_underexposed_clahe  metrics *****
  eval_accuracy               =     0.9859
  eval_f1_weighted            =     0.9864
  eval_loss                   =     0.0688
  eval_model_preparation_time =     0.0023
  eval_precision_weighted     =      0.987
  eval_recall_weighted        =     0.9859
  eval_runtime                = 0:00:58.50
  eval_samples_per_second     =     19.435
  eval_steps_per_second       =      1.231



***** glow-vit | testing on yin30lei/wildlife_underexposed_he  metrics *****
  eval_accuracy               =     0.9745
  eval_f1_weighted            =     0.9753
  eval_loss                   =     0.1119
  eval_model_preparation_time =     0.0023
  eval_precision_weighted     =     0.9768
  eval_recall_weighted        =     0.9745
  eval_runtime                = 0:00:53.75
  eval_samples_per_second     =     21.153
  eval_steps_per_second       =      1.339
***** glow-vit | testing on yin30lei/wildlife_underexposed_afifi  metrics *****
  eval_accuracy               =     0.9798
  eval_f1_weighted            =     0.9802
  eval_loss                   =     0.0692
  eval_model_preparation_time =     0.0023
  eval_precision_weighted     =      0.981
  eval_recall_weighted        =     0.9798
  eval_runtime                = 0:01:04.33
  eval_samples_per_second     =     17.673
  eval_steps_per_second       =      1.119      
```


> Glow-ViT-Dark

```
***** glow-vit-dark | testing on yin30lei/wildlife_very_dark_test  metrics *****
  eval_accuracy               =     0.9082
  eval_f1_weighted            =     0.9082
  eval_loss                   =     0.4528
  eval_model_preparation_time =     0.0025
  eval_precision_weighted     =     0.9108
  eval_recall_weighted        =     0.9082
  eval_runtime                = 0:01:13.59
  eval_samples_per_second     =     17.909
  eval_steps_per_second       =      1.128
***** glow-vit-dark | testing on yin30lei/wildlife_grayscale  metrics *****
  eval_accuracy               =     0.9304
  eval_f1_weighted            =     0.9298
  eval_loss                   =     0.2992
  eval_model_preparation_time =     0.0025
  eval_precision_weighted     =     0.9327
  eval_recall_weighted        =     0.9304
  eval_runtime                = 0:02:07.43
  eval_samples_per_second     =     14.321
  eval_steps_per_second       =      0.902



***** glow-vit-dark | testing on yin30lei/wildlife_less_saturated  metrics *****
  eval_accuracy               =     0.9226
  eval_f1_weighted            =     0.9363
  eval_loss                   =     0.3231
  eval_model_preparation_time =     0.0025
  eval_precision_weighted     =     0.9529
  eval_recall_weighted        =     0.9226
  eval_runtime                = 0:00:47.82
  eval_samples_per_second     =     23.774
  eval_steps_per_second       =      1.505
***** glow-vit-dark | testing on yin30lei/wildlife_underexposed  metrics *****
  eval_accuracy               =     0.9376
  eval_f1_weighted            =     0.9427
  eval_loss                   =     0.2702
  eval_model_preparation_time =     0.0025
  eval_precision_weighted     =     0.9506
  eval_recall_weighted        =     0.9376
  eval_runtime                = 0:00:45.57
  eval_samples_per_second     =     24.945
  eval_steps_per_second       =       1.58
***** glow-vit-dark | testing on yin30lei/wildlife_verydark_clahe  metrics *****
  eval_accuracy               =     0.9446
  eval_f1_weighted            =     0.9439
  eval_loss                   =     0.2089
  eval_model_preparation_time =     0.0025
  eval_precision_weighted     =     0.9457
  eval_recall_weighted        =     0.9446
  eval_runtime                = 0:00:56.69
  eval_samples_per_second     =     23.247
  eval_steps_per_second       =      1.464
***** glow-vit-dark | testing on yin30lei/wildlife_verydark_he  metrics *****
  eval_accuracy               =     0.9431
  eval_f1_weighted            =      0.943
  eval_loss                   =     0.2324
  eval_model_preparation_time =     0.0025
  eval_precision_weighted     =     0.9452
  eval_recall_weighted        =     0.9431
  eval_runtime                = 0:00:53.99
  eval_samples_per_second     =     24.409
  eval_steps_per_second       =      1.537
***** glow-vit-dark | testing on yin30lei/wildlife_verydark_afifi  metrics *****
  eval_accuracy               =      0.915
  eval_f1_weighted            =     0.9144
  eval_loss                   =     0.3838
  eval_model_preparation_time =     0.0025
  eval_precision_weighted     =     0.9217
  eval_recall_weighted        =      0.915
  eval_runtime                = 0:00:55.68
  eval_samples_per_second     =     23.667
  eval_steps_per_second       =       1.49
***** glow-vit-dark | testing on yin30lei/wildlife_less_saturated_clahe  metrics *****
  eval_accuracy               =     0.8698
  eval_f1_weighted            =     0.8816
  eval_loss                   =     0.5156
  eval_model_preparation_time =     0.0025
  eval_precision_weighted     =     0.9154
  eval_recall_weighted        =     0.8698
  eval_runtime                = 0:00:54.27
  eval_samples_per_second     =      20.95
  eval_steps_per_second       =      1.327



***** glow-vit-dark | testing on yin30lei/wildlife_less_saturated_he  metrics *****
  eval_accuracy               =     0.9437
  eval_f1_weighted            =      0.945
  eval_loss                   =     0.2069
  eval_model_preparation_time =     0.0025
  eval_precision_weighted     =     0.9476
  eval_recall_weighted        =     0.9437
  eval_runtime                = 0:00:52.53
  eval_samples_per_second     =     21.644
  eval_steps_per_second       =      1.371
***** glow-vit-dark | testing on yin30lei/wildlife_less_saturated_afifi  metrics *****
  eval_accuracy               =     0.9129
  eval_f1_weighted            =     0.9233
  eval_loss                   =     0.3232
  eval_model_preparation_time =     0.0025
  eval_precision_weighted     =     0.9378
  eval_recall_weighted        =     0.9129
  eval_runtime                = 0:00:56.49
  eval_samples_per_second     =     20.127
  eval_steps_per_second       =      1.275
***** glow-vit-dark | testing on yin30lei/wildlife_underexposed_clahe  metrics *****
  eval_accuracy               =     0.9393
  eval_f1_weighted            =     0.9436
  eval_loss                   =     0.2596
  eval_model_preparation_time =     0.0025
  eval_precision_weighted     =     0.9504
  eval_recall_weighted        =     0.9393
  eval_runtime                = 0:00:44.65
  eval_samples_per_second     =     25.462
  eval_steps_per_second       =      1.612



***** glow-vit-dark | testing on yin30lei/wildlife_underexposed_he  metrics *****
  eval_accuracy               =     0.9446
  eval_f1_weighted            =     0.9459
  eval_loss                   =     0.2636
  eval_model_preparation_time =     0.0025
  eval_precision_weighted     =     0.9494
  eval_recall_weighted        =     0.9446
  eval_runtime                = 0:00:53.93
  eval_samples_per_second     =     21.081
  eval_steps_per_second       =      1.335
***** glow-vit-dark | testing on yin30lei/wildlife_underexposed_afifi  metrics *****
  eval_accuracy               =     0.9437
  eval_f1_weighted            =     0.9461
  eval_loss                   =      0.245
  eval_model_preparation_time =     0.0025
  eval_precision_weighted     =     0.9503
  eval_recall_weighted        =     0.9437
  eval_runtime                = 0:00:45.14
  eval_samples_per_second     =     25.185
  eval_steps_per_second       =      1.595  
```

> Glow-ViT-Illuminate

```
***** glow-vit-illuminate | testing on yin30lei/wildlife_very_dark_test  metrics *****
  eval_accuracy               =     0.2079
  eval_f1_weighted            =     0.1767
  eval_loss                   =     2.2027
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.2792
  eval_recall_weighted        =     0.2079
  eval_runtime                = 0:01:04.32
  eval_samples_per_second     =     20.488
  eval_steps_per_second       =       1.29
***** glow-vit-illuminate | testing on yin30lei/wildlife_grayscale  metrics *****
  eval_accuracy               =     0.9063
  eval_f1_weighted            =     0.9077
  eval_loss                   =     0.3929
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.9237
  eval_recall_weighted        =     0.9063
  eval_runtime                = 0:02:07.00
  eval_samples_per_second     =      14.37
  eval_steps_per_second       =      0.905



***** glow-vit-illuminate | testing on yin30lei/wildlife_less_saturated  metrics *****
  eval_accuracy               =     0.9033
  eval_f1_weighted            =     0.9044
  eval_loss                   =     0.4334
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =      0.912
  eval_recall_weighted        =     0.9033
  eval_runtime                = 0:00:46.58
  eval_samples_per_second     =     24.408
  eval_steps_per_second       =      1.546
***** glow-vit-illuminate | testing on yin30lei/wildlife_underexposed  metrics *****
  eval_accuracy               =     0.8734
  eval_f1_weighted            =     0.8733
  eval_loss                   =     0.5756
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =       0.88
  eval_recall_weighted        =     0.8734
  eval_runtime                = 0:00:46.35
  eval_samples_per_second     =      24.53
  eval_steps_per_second       =      1.553
***** glow-vit-illuminate | testing on yin30lei/wildlife_verydark_clahe  metrics *****
  eval_accuracy               =      0.931
  eval_f1_weighted            =     0.9341
  eval_loss                   =     0.3039
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.9402
  eval_recall_weighted        =      0.931
  eval_runtime                = 0:00:55.12
  eval_samples_per_second     =     23.909
  eval_steps_per_second       =      1.506
***** glow-vit-illuminate | testing on yin30lei/wildlife_verydark_he  metrics *****
  eval_accuracy               =     0.8991
  eval_f1_weighted            =     0.9051
  eval_loss                   =      0.419
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.9185
  eval_recall_weighted        =     0.8991
  eval_runtime                = 0:00:58.57
  eval_samples_per_second     =     22.501
  eval_steps_per_second       =      1.417
***** glow-vit-illuminate | testing on yin30lei/wildlife_verydark_afifi  metrics *****
  eval_accuracy               =     0.8437
  eval_f1_weighted            =     0.8443
  eval_loss                   =     0.6543
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.8504
  eval_recall_weighted        =     0.8437
  eval_runtime                = 0:00:52.82
  eval_samples_per_second     =      24.95
  eval_steps_per_second       =      1.571
***** glow-vit-illuminate | testing on yin30lei/wildlife_less_saturated_clahe  metrics *****
  eval_accuracy               =      0.861
  eval_f1_weighted            =     0.8605
  eval_loss                   =     0.6073
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.8812
  eval_recall_weighted        =      0.861
  eval_runtime                = 0:00:47.41
  eval_samples_per_second     =     23.981
  eval_steps_per_second       =      1.519



***** glow-vit-illuminate | testing on yin30lei/wildlife_less_saturated_he  metrics *****
  eval_accuracy               =     0.9138
  eval_f1_weighted            =     0.9122
  eval_loss                   =     0.3827
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.9134
  eval_recall_weighted        =     0.9138
  eval_runtime                = 0:00:50.40
  eval_samples_per_second     =     22.555
  eval_steps_per_second       =      1.428
***** glow-vit-illuminate | testing on yin30lei/wildlife_less_saturated_afifi  metrics *****
  eval_accuracy               =     0.9217
  eval_f1_weighted            =     0.9199
  eval_loss                   =     0.3601
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.9218
  eval_recall_weighted        =     0.9217
  eval_runtime                = 0:00:43.59
  eval_samples_per_second     =     26.083
  eval_steps_per_second       =      1.652
***** glow-vit-illuminate | testing on yin30lei/wildlife_underexposed_clahe  metrics *****
  eval_accuracy               =     0.9393
  eval_f1_weighted            =     0.9397
  eval_loss                   =     0.2424
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.9431
  eval_recall_weighted        =     0.9393
  eval_runtime                = 0:00:46.92
  eval_samples_per_second     =     24.229
  eval_steps_per_second       =      1.534



***** glow-vit-illuminate | testing on yin30lei/wildlife_underexposed_he  metrics *****
  eval_accuracy               =      0.942
  eval_f1_weighted            =     0.9412
  eval_loss                   =      0.255
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.9448
  eval_recall_weighted        =      0.942
  eval_runtime                = 0:00:49.23
  eval_samples_per_second     =     23.095
  eval_steps_per_second       =      1.462
***** glow-vit-illuminate | testing on yin30lei/wildlife_underexposed_afifi  metrics *****
  eval_accuracy               =      0.949
  eval_f1_weighted            =      0.949
  eval_loss                   =     0.2446
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =      0.951
  eval_recall_weighted        =      0.949
  eval_runtime                = 0:00:57.17
  eval_samples_per_second     =     19.886
  eval_steps_per_second       =      1.259      
```

> Glow-ViT-Mix

```
***** glow-vit-mix | testing on yin30lei/wildlife_very_dark_test  metrics *****
  eval_accuracy               =     0.9643
  eval_f1_weighted            =     0.9645
  eval_precision_weighted     =     0.9653
  eval_recall_weighted        =     0.9643
  
  
***** glow-vit-mix | testing on yin30lei/wildlife_grayscale  metrics *****
  eval_accuracy               =      0.983
  eval_f1_weighted            =     0.9829
  eval_precision_weighted     =     0.9832
  eval_recall_weighted        =      0.983
  
  
***** glow-vit-mix | testing on yin30lei/wildlife_less_saturated  metrics *****
  eval_accuracy               =     0.9833
  eval_f1_weighted            =     0.9836
  eval_precision_weighted     =     0.9841
  eval_recall_weighted        =     0.9833
  

***** glow-vit-mix | testing on yin30lei/wildlife_underexposed  metrics *****
  eval_accuracy               =     0.9886
  eval_f1_weighted            =      0.989
  eval_precision_weighted     =     0.9895
  eval_recall_weighted        =     0.9886

***** glow-vit-mix | testing on yin30lei/wildlife_verydark_clahe  metrics *****
  eval_accuracy               =     0.9545
  eval_f1_weighted            =     0.9644
  eval_precision_weighted     =     0.9783
  eval_recall_weighted        =     0.9545
  
***** glow-vit-mix | testing on yin30lei/wildlife_verydark_he  metrics *****
  eval_accuracy               =      0.953
  eval_f1_weighted            =     0.9584
  eval_precision_weighted     =     0.9667
  eval_recall_weighted        =      0.953
  
***** glow-vit-mix | testing on yin30lei/wildlife_verydark_afifi  metrics *****
  eval_accuracy               =     0.9514
  eval_f1_weighted            =     0.9517
  eval_precision_weighted     =     0.9531
  eval_recall_weighted        =     0.9514

***** glow-vit-mix | testing on yin30lei/wildlife_less_saturated_clahe  metrics *****
  eval_accuracy               =     0.9499
  eval_f1_weighted            =     0.9509
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.9558
  eval_recall_weighted        =     0.9499
  
***** glow-vit-mix | testing on yin30lei/wildlife_less_saturated_he  metrics *****
  eval_accuracy               =     0.9771
  eval_f1_weighted            =      0.977
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.9771
  eval_recall_weighted        =     0.9771
  
***** glow-vit-mix | testing on yin30lei/wildlife_less_saturated_afifi  metrics *****
  eval_accuracy               =     0.9771
  eval_f1_weighted            =     0.9778
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.9788
  eval_recall_weighted        =     0.9771
  
  
***** glow-vit-mix | testing on yin30lei/wildlife_underexposed_clahe  metrics *****
  eval_accuracy               =      0.985
  eval_f1_weighted            =     0.9851
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.9851
  eval_recall_weighted        =      0.985
  
***** glow-vit-mix | testing on yin30lei/wildlife_underexposed_he  metrics *****
  eval_accuracy               =      0.978
  eval_f1_weighted            =      0.978
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.9781
  eval_recall_weighted        =      0.978
  
***** glow-vit-mix | testing on yin30lei/wildlife_underexposed_afifi  metrics *****
  eval_accuracy               =     0.9877
  eval_f1_weighted            =     0.9877
  eval_model_preparation_time =     0.0029
  eval_precision_weighted     =     0.9877
  eval_recall_weighted        =     0.9877  
```