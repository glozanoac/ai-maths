# Phase 03 -- Deep Learning Foundations

Mathematical foundations of deep learning: neural network approximation theory, recurrent architectures, and optimization methods for training. 14 lessons organized into 3 subdomains.

## Reference Textbooks

- **Neural Network Theory:** Bach, *Learning Theory from First Principles* (2024); Pinkus 1999; Cybenko 1989; Hornik et al. 1989
- **Recurrent Networks:** Goodfellow, Bengio & Courville
- **Optimization for DL:** Bottou et al. 2018, Kingma & Ba 2015, Reddi et al. 2018

## Lessons

### 3.1 Neural Network Theory (Lessons 59-66)

| Lesson | File | Topic | Pages |
|--------|------|-------|-------|
| 59 | `01-neural-networks/lesson-59-erm-and-generalization` | ERM, hypothesis classes, VC dimension, Sauer's lemma, uniform convergence | 12 |
| 60 | `01-neural-networks/lesson-60-bias-variance-and-model-selection` | Bias-variance decomposition, approximation-estimation tradeoff, cross-validation | 12 |
| 61 | `01-neural-networks/lesson-61-kernel-methods` | Kernel trick, positive definite kernels, Mercer's theorem, kernel construction | 13 |
| 62 | `01-neural-networks/lesson-62-rkhs-and-representer-theorem` | RKHS construction, reproducing property, representer theorem, kernel ridge regression | 13 |
| 63 | `01-neural-networks/lesson-63-universal-approximation` | Cybenko's theorem, Hornik's generalization, density arguments, limitations | 12 |
| 64 | `01-neural-networks/lesson-64-barron-theorem-and-approximation-rates` | Barron's theorem, dimension-free rates, Fourier analysis, integral representation | 14 |
| 65 | `01-neural-networks/lesson-65-depth-width-tradeoffs` | Depth separation (Telgarsky), width sufficiency, Sobolev approximation rates | 13 |
| 66 | `01-neural-networks/lesson-66-ntk-and-rademacher-complexity` | Neural tangent kernel, lazy training, Rademacher complexity, generalization | 15 |

### 3.2 Recurrent Neural Networks (Lessons 67-69)

| Lesson | File | Topic | Pages |
|--------|------|-------|-------|
| 67 | `01-neural-networks/lesson-67-rnn-and-bptt` | Vanilla RNN, BPTT derivation, vanishing/exploding gradient theorems, gradient clipping | 12 |
| 68 | `01-neural-networks/lesson-68-lstm-and-gating` | LSTM cell, forget/input/output gates, cell state gradient highway, LSTM variants | 11 |
| 69 | `01-neural-networks/lesson-69-gru-and-sequence-architectures` | GRU, bidirectional RNNs, stacked RNNs, encoder-decoder framework | 11 |

### 3.3 Optimization for Deep Learning (Lessons 70-72)

| Lesson | File | Topic | Pages |
|--------|------|-------|-------|
| 70 | `02-optimization-for-dl/01-sgd-and-adaptive-methods` | SGD convergence (convex/non-convex), learning rate schedules | planned |
| 71 | `02-optimization-for-dl/01-sgd-and-adaptive-methods` | SVRG, SAGA, AdaGrad, RMSprop | planned |
| 72 | `02-optimization-for-dl/01-sgd-and-adaptive-methods` | Adam, AMSGrad, convergence issues and fixes | planned |

## Prerequisites

- **Phase 01** measure theory, probability, functional analysis, optimization
- **Phase 00** probability (Hoeffding's inequality from Lesson 12)

## Internal Reading Order

```
NN Theory: 59 -> 60 -> 61 -> 62 -> 63 -> 64 -> 65 -> 66
RNN:       67 -> 68 -> 69
OPT:       01-sgd-and-adaptive-methods (independent of above)
```

Lesson 66 (NTK/Rademacher) leads into Phase 04 (deep RL value-based methods).
