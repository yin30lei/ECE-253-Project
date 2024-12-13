# Light Influence on Neural Network Image Classification

> Yalu Ouyang, Yin Lei

The trained models can be located at the following Huggingface repos:

1. SeaSponge/glow-vit
2. SeaSponge/glow-vit-dark
3. SeaSponge/glow-vit-illuminate

The dataset used can also be found at the following Huggingface repos:



## Testing results :

### Unfiltered Dataset

> Overview

|eval_loss            | original | very dark | illuminate | mixed | very dark test | grayscale | less saturated | underexposed |
|---------------------|----------|-----------|------------|-------|----------------|-----------|----------------|----|
|Glow-ViT             |0.1246    |4.5018     |0.0225      |0.5657 |4.3495          |0.2021     |0.176           |0.351|
|Glow-ViT-Dark        |0.2078    |0.5554     |0.1712      |0.2502 |0.4528          |0.2992     |0.3231          |0.2702|
|Glow-ViT-Illuminate  |0.1177    |2.1939     |0.1064      |0.4042 |2.2027          |0.3929     |0.4334          |0.5756|
|Glow-ViT-Mix         |0.0744    |0.3715     |0.0243      |0.1449 |0.1396          | 0.0776    | 0.0707         |0.0472|



|eval_samples_per_second| original | very dark | illuminate | mixed | very dark test | grayscale | less saturated | underexposed |
|--|---------|------------|------------|-------|----------------|-----------|----------------|----|
|Glow-ViT|13.22|13.087|13.589|12.81|21.118|13.231|20.086|20.162|
|Glow-ViT-Dark|13.027|13.189|13.249|12.587|19.035|12.997                |21.418|21.862|
|Glow-ViT-Illuminate|12.809|12.857|13.223|11.938|19.711             |12.803            |19.972|20.094|
|Glow-ViT-Mix|14.038|13.294 |13.956|12.778|21.091       | 13.254   | 21.135 |20.766|

### Filtered dataset

This section contains results of models' performance running on dataset that have been filtered using the blow methods:

- HE
- CLAHE
- AFIFI

The tables are sorted by datasets:

#### very-dark-test

| Model             | Dataset                              | Eval Loss | Eval Samples Per Second |
|--------------------|--------------------------------------|-----------|--------------------------|
| Glow-ViT          | CLAHE                                 | 0.075     | 18.797                   |
| Glow-ViT          | HE                                    | 0.1791    | 18.119                   |
| Glow-ViT          | AFIFI                                 | 0.4517    | 19.199                   |
| Glow-ViT-dark     | CLAHE                                 | 0.2089    | 18.775                   |
| Glow-ViT-dark     | HE                                    | 0.2324    | 18.86                    |
| Glow-ViT-dark     | AFIFI                                 | 0.3838    | 18.761                   |
| Glow-ViT-illuminate | CLAHE                               | 0.3039    | 19.033                   |
| Glow-ViT-illuminate | HE                                  | 0.419     | 20.752                   |
| Glow-ViT-illuminate | AFIFI                               | 0.6543    | 20.576                   |
| Glow-ViT-mix      | CLAHE                                 | 0.1768    | 17.821                   |
| Glow-ViT-mix      | HE                                    | 0.1925    | 18.962                   |
| Glow-ViT-mix      | AFIFI                                 | 0.1952    | 18.662                   |

#### less saturated

| Model              | Dataset                              | Eval Loss | Eval Samples Per Second |
|--------------------|--------------------------------------|-----------|--------------------------|
| Glow-ViT          | CLAHE                                 | 0.4322    | 19.202                   |
| Glow-ViT          | HE                                    | 0.1722    | 20.912                   |
| Glow-ViT          | AFIFI                                 | 0.1746    | 21.745                   |
| Glow-ViT-dark     | CLAHE                                 | 0.5156    | 20.770                   |
| Glow-ViT-dark     | HE                                    | 0.2069    | 22.236                   |
| Glow-ViT-dark     | AFIFI                                 | 0.3232    | 21.194                   |
| Glow-ViT-illuminate | CLAHE                               | 0.6073    | 20.399                   |
| Glow-ViT-illuminate | HE                                  | 0.3827    | 20.900                   |
| Glow-ViT-illuminate | AFIFI                               | 0.3601    | 21.946                   |
| Glow-ViT-mix      | CLAHE                                 | 0.2070    | 18.978                   |
| Glow-ViT-mix      | HE                                    | 0.1004    | 21.674                   |
| Glow-ViT-mix      | AFIFI                                 | 0.0977    | 21.653                   |

#### underexposed

| Model             | Dataset                              | Eval Loss | Eval Samples Per Second |
|--------------------|--------------------------------------|-----------|--------------------------|
| Glow-ViT          | CLAHE                                 | 0.0688    | 18.855                   |
| Glow-ViT          | HE                                    | 0.1119    | 20.013                   |
| Glow-ViT          | AFIFI                                 | 0.0692    | 19.543                   |
| Glow-ViT-Dark     | CLAHE                                 | 0.2596    | 17.982                   |
| Glow-ViT-Dark     | HE                                    | 0.2636    | 19.576                   |
| Glow-ViT-Dark     | AFIFI                                 | 0.2450    | 20.645                   |
| Glow-ViT-Illuminate | CLAHE                               | 0.2424    | 18.255                   |
| Glow-ViT-Illuminate | HE                                  | 0.2550    | 20.814                   |
| Glow-ViT-Illuminate | AFIFI                               | 0.2446    | 20.759                   |
| Glow-ViT-Mix      | CLAHE                                 | 0.0577    | 19.283                   |
| Glow-ViT-Mix      | HE                                    | 0.0917    | 20.847                   |
| Glow-ViT-Mix      | AFIFI                                 | 0.0610    | 20.104                   |