# Value Decomposition Network (VDN)

## The Core Idea

VDN addresses the multi-agent credit assignment problem with a simple but powerful idea:

**The team's Q-value is the sum of individual agent Q-values.**

```
Q_total(s, a1, a2) = Q_1(o1, a1) + Q_2(o2, a2)
```

This decomposition means:
- Each agent has its own Q-network that takes only its local observation
- During training, we optimize the sum (team Q-value) against the team reward
- During execution, each agent independently picks its best action (argmax of its own Q)

## Centralized Training, Decentralized Execution (CTDE)

VDN follows the CTDE paradigm:

- **Centralized Training**: The loss function uses the joint team reward and updates all agent networks together through the sum. The replay buffer stores joint transitions.
- **Decentralized Execution**: At test time, each agent only needs its own observation and its own Q-network. No communication required.

## Why Summation Works

The additive decomposition `Q_total = sum(Q_i)` ensures that:
```
argmax_{a1,a2} Q_total = (argmax_a1 Q_1, argmax_a2 Q_2)
```

This is the **Individual-Global-Max (IGM)** property — the globally optimal joint action can be found by each agent independently maximizing its own Q-value. This is what makes decentralized execution possible.

## Architecture

```
Predator 0 obs (6D) -> [Linear(64) -> ReLU -> Linear(64) -> ReLU -> Linear(5)] -> Q_0 (5 values)
Predator 1 obs (6D) -> [Linear(64) -> ReLU -> Linear(64) -> ReLU -> Linear(5)] -> Q_1 (5 values)

Q_total = Q_0[a0] + Q_1[a1]    (scalar, used for loss computation)
```

### Training Details
- **Replay buffer**: 50,000 joint transitions, warmup 1,000 steps
- **Target networks**: Soft update with tau=0.005
- **Optimizer**: Adam, lr=0.001
- **Batch size**: 32
- **Epsilon decay**: 1.0 -> 0.05 over 5,000 episodes

## VDN vs IQL

| Aspect | IQL | VDN |
|--------|-----|-----|
| Training | Independent | Centralized (shared loss) |
| Reward | Individual | Team reward |
| Credit assignment | None | Through Q_total decomposition |
| Coordination | Emergent (unlikely) | Explicitly learned |
| Non-stationarity | Severe | Mitigated (joint training) |

## Limitations

VDN's additive decomposition is restrictive — it can't represent all possible value decompositions. QMIX (a natural extension) uses a monotonic mixing network that is strictly more expressive. But for our predator-prey task, VDN's simplicity is sufficient and easier to understand.

## Expected Results

- VDN should outperform IQL (60-90% capture rate)
- Higher cooperative capture rate (both predators adjacent at capture)
- Agents learn surrounding/pincer strategies rather than just independent chasing
