# Phase 05 -- Multi-Agent Reinforcement Learning

Extends RL to multi-agent settings: stochastic games as the foundational framework, cooperative and competitive paradigms, mean-field approximations for large populations, and emergent communication between agents.

## Reference Textbooks

- **Stochastic Games:** Shoham & Leyton-Brown; Filar & Vrieze
- **Cooperative:** Rashid et al. (QMIX), Yu et al. (MAPPO)
- **Competitive:** Littman (minimax-Q), Lanctot et al. (PSRO)
- **Mean-Field:** Carmona & Delarue
- **Communication:** Sukhbaatar et al. (CommNet), Das et al. (TarMAC)

## Documents

| File | Directory | Topic | Status |
|------|-----------|-------|--------|
| -- | `01-stochastic-games/` | Stochastic games, Shapley value, Nash-Q | planned |
| -- | `02-cooperative/` | CTDE, QMIX, MAPPO | planned |
| -- | `03-competitive/` | Minimax MARL, policy-space response oracles | planned |
| -- | `04-mean-field/` | Mean-field games, McKean-Vlasov dynamics | planned |
| -- | `05-communication/` | CommNet, TarMAC, emergent communication | planned |

## Prerequisites

- **Phase 02** (core RL theory) -- required for all documents
- **Phase 01 / 04-game-theory** -- game-theoretic foundations required for stochastic games and equilibrium concepts

## Internal Reading Order

```
stochastic-games -> cooperative -> competitive -> mean-field -> communication
```

Stochastic games provide the multi-agent framework; cooperative and competitive methods build on it; mean-field and communication are more specialized extensions.
