# Light Influence on Neural Network Image Classification

> Yalu Ouyang, Yin Lei

The trained models can be located at the following Huggingface repos:

1. SeaSponge/glow-vit
2. SeaSponge/glow-vit-dark
3. SeaSponge/glow-vit-illuminate

The dataset used can also be found at the following Huggingface repos:



## Testing results:

### Respective datasets

```
***** glow-vit | testing on SeaSponge/wildme10_classify  metrics *****
  eval_loss                   =     0.1246
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:02:57.29
  eval_samples_per_second     =      20.48
  eval_steps_per_second       =       1.28
```

```
***** glow-vit-dark | testing on yin30lei/wildlife_very_dark metrics *****
  eval_loss                   =     0.5614
  eval_model_preparation_time =      0.002
  eval_runtime                = 0:00:09.52
  eval_samples_per_second     =     73.675
  eval_steps_per_second       =      4.618
```

```
***** glow-vit-illuminate | testing on yin30lei/wildlife_well_illuminated metrics *****
  eval_loss                   =     0.1064
  eval_model_preparation_time =     0.0022
  eval_runtime                = 0:02:03.81
  eval_samples_per_second     =     18.842
  eval_steps_per_second       =      1.179
```

```
***** glow-vit-mix | testing on yin30lei/wildlife_mixed  metrics *****
  eval_loss                   =     0.1449
  eval_model_preparation_time =     0.0023
  eval_runtime                = 0:03:20.46
  eval_samples_per_second     =     19.744
  eval_steps_per_second       =      1.237
```

### The various low-exposure datasets