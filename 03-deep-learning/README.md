# Phase 03 -- Deep Learning Foundations

Mathematical foundations of deep learning: neural network approximation theory, recurrent architectures, and optimization methods for training. This phase is independent of Phase 02 (Core RL) and can be studied in parallel.

## Reference Textbooks

- **Approximation Theory:** Bach Ch.1-3, 6-7; Pinkus 1999; Cybenko 1989; Hornik et al. 1989
- **Neural Networks:** Goodfellow, Bengio & Courville
- **Optimization for DL:** Bottou et al. 2018, Kingma & Ba 2015, Reddi et al. 2018

## Documents

| File | Directory | Topic | Status |
|------|-----------|-------|--------|
| `01-approximation-theory` | `01-neural-networks/` | Universal approximation (Cybenko, Hornik), Barron's theorem, approximation rates, Rademacher complexity, NTK perspective | planned |
| `rnn` | `01-neural-networks/` | BPTT, vanishing/exploding gradients, sequence modeling | **exists** |
| `lstm` | `01-neural-networks/` | Gating mechanisms, cell state dynamics, GRU | **exists** |
| `01-sgd-and-adaptive-methods` | `02-optimization-for-dl/` | SGD convergence (convex/non-convex), variance reduction, AdaGrad, RMSprop, Adam, loss landscape geometry, batch normalization | planned |

## Prerequisites

- **Phase 01** (measure theory and probability foundations) -- required for all documents in this phase

## Internal Reading Order

```
01-approximation-theory (planned)
rnn -> lstm
01-sgd-and-adaptive-methods (planned, independent of rnn/lstm)
```
