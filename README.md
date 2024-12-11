# Light Influence on Neural Network Image Classification

> Yalu Ouyang, Yin Lei

The trained models can be located at the following Huggingface repos:

1. SeaSponge/glow-vit
2. SeaSponge/glow-vit-dark
3. SeaSponge/glow-vit-illuminate

The dataset used can also be found at the following Huggingface repos:



## Testing results:

### Respective datasets

> Glow-ViT

```
***** glow-vit | testing on SeaSponge/wildme10_classify  metrics *****
  eval_loss                   =     0.1246
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:02:57.29
  eval_samples_per_second     =      20.48
  eval_steps_per_second       =       1.28
```

> Glow-ViT-dark

```
***** glow-vit-dark | testing on yin30lei/wildlife_very_dark metrics *****
  eval_loss                   =     0.5614
  eval_model_preparation_time =      0.002
  eval_runtime                = 0:00:09.52
  eval_samples_per_second     =     73.675
  eval_steps_per_second       =      4.618
```

> Glow-ViT-illuminate

```
***** glow-vit-illuminate | testing on yin30lei/wildlife_well_illuminated metrics *****
  eval_loss                   =     0.1064
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:02:03.81
  eval_samples_per_second     =     18.842
  eval_steps_per_second       =      1.179
```

> Glow-ViT-mix

```
***** glow-vit-mix | testing on yin30lei/wildlife_mixed  metrics *****
  eval_loss                   =     0.1449
  eval_model_preparation_time =     0.0023
  eval_runtime                = 0:03:20.46
  eval_samples_per_second     =     19.744
  eval_steps_per_second       =      1.237
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
  eval_loss                   =      0.561
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:01:06.04
  eval_samples_per_second     =     19.956
  eval_steps_per_second       =      1.257
***** glow-vit-dark | testing on yin30lei/wildlife_grayscale  metrics *****
  eval_loss                   =     0.8321
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:02:23.75
  eval_samples_per_second     =     12.695
  eval_steps_per_second       =        0.8
***** glow-vit-dark | testing on yin30lei/wildlife_less_saturated  metrics *****
  eval_loss                   =     1.0754
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:00:56.26
  eval_samples_per_second     =     20.207
  eval_steps_per_second       =       1.28
***** glow-vit-dark | testing on yin30lei/wildlife_underexposed  metrics *****
  eval_loss                   =     0.9486
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:00:54.61
  eval_samples_per_second     =     20.819
  eval_steps_per_second       =      1.318
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