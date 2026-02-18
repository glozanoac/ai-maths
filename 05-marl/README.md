# Phase 05 -- Multi-Agent Reinforcement Learning

Extends RL to multi-agent settings: stochastic games as the foundational framework, cooperative and competitive paradigms, mean-field approximations for large populations, and emergent communication between agents.

## Reference Textbooks

- **Stochastic Games:** Shoham & Leyton-Brown Ch.3-4, 6-7; Filar & Vrieze Ch.1-5
- **Cooperative:** Bernstein et al. 2002 (Dec-POMDP), Rashid et al. 2018 (QMIX), Yu et al. 2022 (MAPPO)
- **Competitive:** Littman 1994 (Minimax-Q), Lowe et al. 2017 (MADDPG), Lanctot et al. 2017 (PSRO)
- **Mean-Field:** Carmona & Delarue Vol.I; Yang et al. 2018
- **Communication:** Sukhbaatar et al. 2016 (CommNet), Foerster et al. 2016 (DIAL/RIAL), Das et al. 2019 (TarMAC)

## Documents

| File | Directory | Topic | Status |
|------|-----------|-------|--------|
| `01-stochastic-game-theory` | `01-stochastic-games/` | Stochastic game formalism, Markov perfect equilibrium, Shapley's theorem, existence via fixed points | **exists** |
| `01-cooperative-marl` | `02-cooperative/` | Dec-POMDP, CTDE, VDN, QMIX, QTRAN, MAPPO, IGM condition, credit assignment | **exists** |
| `01-competitive-and-mixed-marl` | `03-competitive/` | Minimax-Q, Nash-Q, MADDPG, LOLA, self-play, PSRO | **exists** |
| `01-mean-field-games` | `04-mean-field/` | Mean field game theory, McKean-Vlasov dynamics, forward-backward SDEs, mean field equilibria | **exists** |
| `01-communication-in-marl` | `05-communication/` | CommNet, DIAL, RIAL, TarMAC, emergent communication | **exists** |

## Prerequisites

- **Phase 02** (core RL theory) -- required for all documents
- **Phase 01 / 04-game-theory** -- game-theoretic foundations required for stochastic games and equilibrium concepts

## Internal Reading Order

```
01-stochastic-game-theory -> {cooperative, competitive, mean-field, communication}
```

Stochastic games provide the multi-agent framework; all other documents build on it and can be read in any order.
