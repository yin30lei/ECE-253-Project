# Light Influence on Neural Network Image Classification

> Yalu Ouyang, Yin Lei

The trained models can be located at the following Huggingface repos:

1. SeaSponge/glow-vit
2. SeaSponge/glow-vit-dark
3. SeaSponge/glow-vit-illuminate

The dataset used can also be found at the following Huggingface repos:



## Testing results:

> Overview

|eval_loss| original | very dark | illuminate | mixed | very dark test | grayscale | less saturated | underexposed |
|--|---------|------------|------------|-------|----------------|-----------|----------------|----|
|Glow-ViT|0.1246|4.5018|0.0225|0.5657|4.3495|0.2021|0.176|0.351|
|Glow-ViT-Dark|0.2078|0.5554|0.1712|0.2502|0.4528|0.2992 |0.3231      |0.2702|
|Glow-ViT-Illuminate|0.1177|2.1939|0.1064|0.4042|2.2027|0.3929     |0.4334          |0.5756|
|Glow-ViT-Mix|0.0744|0.3715|0.0243|0.1449|0.1396       | 0.0776   | 0.0707 |0.0472|



|eval_samples_per_second| original | very dark | illuminate | mixed | very dark test | grayscale | less saturated | underexposed |
|--|---------|------------|------------|-------|----------------|-----------|----------------|----|
|Glow-ViT|13.22|13.087|13.589|12.81|21.118|13.231|20.086|20.162|
|Glow-ViT-Dark|13.027|13.189|13.249|12.587|19.035|12.997                |21.418|21.862|
|Glow-ViT-Illuminate|12.809|12.857|13.223|11.938|19.711             |12.803            |19.972|20.094|
|Glow-ViT-Mix|14.038|13.294 |13.956|12.778|21.091       | 13.254   | 21.135 |20.766|


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