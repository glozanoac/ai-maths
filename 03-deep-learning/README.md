# Phase 03 -- Deep Learning Foundations

Mathematical foundations of deep learning: neural network architectures, backpropagation through time, recurrent models, and optimization methods for training. This phase is independent of Phase 02 (Core RL) and can be studied in parallel.

## Reference Textbooks

- **Neural Networks:** Bach Ch.1-14; Goodfellow, Bengio & Courville
- **Optimization for DL:** Bach Ch.9-14

## Documents

| File | Directory | Topic | Status |
|------|-----------|-------|--------|
| `rnn` | `01-neural-networks/` | BPTT, vanishing/exploding gradients, sequence modeling | **exists** |
| `lstm` | `01-neural-networks/` | Gating mechanisms, cell state dynamics, GRU | **exists** |
| -- | `02-optimization-for-dl/` | SGD analysis, Adam, learning rate schedules, batch normalization | planned |

## Prerequisites

- **Phase 01** (measure theory and probability foundations) -- required for all documents in this phase

## Internal Reading Order

```
rnn -> lstm
optimization-for-dl (planned, independent of rnn/lstm)
```
