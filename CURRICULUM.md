# Lesson-by-Lesson Curriculum

This curriculum breaks the six-phase learning path into **114 individual lessons**, each
representing a focused study session of roughly 2--3 hours. It is derived from
`curriculum.pdf` and maps every lesson to its corresponding repository document.

**Guiding principle:** Read for *understanding*, not coverage. Work through proofs,
verify claims, solve exercises. A single chapter deeply understood is worth more than
ten chapters skimmed.

**Estimated total duration:** 14--20 months.

---

## Phase 01: Mathematical Foundations (~38 lessons, 4--6 months)

### 1.1 Measure Theory and Probability (Lessons 1--14)

**Primary text:** Durrett, R. *Probability: Theory and Examples* (5th ed., 2019)
**Supplementary:** Billingsley, P. *Probability and Measure* (3rd ed.)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 1 | Durrett Ch.1.1--1.3: sigma-algebras, measures | Caratheodory extension theorem, pi-lambda theorem | [01-measure-spaces](01-math-foundations/01-measure-theory/01-measure-spaces.pdf) |
| 2 | Durrett Ch.1.4--1.7: measurable functions, integration | Construction of Lebesgue integral, simple function approximation | [01-measure-spaces](01-math-foundations/01-measure-theory/01-measure-spaces.pdf) |
| 3 | Durrett Ch.1.6--1.7: convergence theorems | Monotone Convergence Theorem, Fatou's Lemma, Dominated Convergence Theorem | [01-measure-spaces](01-math-foundations/01-measure-theory/01-measure-spaces.pdf) |
| 4 | Durrett Ch.2: product measures, Fubini | Product sigma-algebras, Fubini-Tonelli theorem | [01-measure-spaces](01-math-foundations/01-measure-theory/01-measure-spaces.pdf) |
| 5 | Durrett Ch.3.1--3.3: independence, WLLN | Independence of sigma-algebras, Weak Law of Large Numbers | [probability-foundations](01-math-foundations/01-measure-theory/probability-foundations.pdf) |
| 6 | Durrett Ch.3.4--3.6: SLLN, Borel-Cantelli | Strong Law of Large Numbers, Borel-Cantelli Lemmas (both directions) | [probability-foundations](01-math-foundations/01-measure-theory/probability-foundations.pdf) |
| 7 | Durrett Ch.4.1--4.3: characteristic functions | Levy continuity theorem, inversion formula | [probability-foundations](01-math-foundations/01-measure-theory/probability-foundations.pdf) |
| 8 | Durrett Ch.4.4--4.5: Central Limit Theorem | CLT (Lindeberg-Feller), Berry-Esseen bound | [probability-foundations](01-math-foundations/01-measure-theory/probability-foundations.pdf) |
| 9 | Durrett Ch.5.1--5.2: conditional expectation | Conditional expectation as projection, tower property | [probability-foundations](01-math-foundations/01-measure-theory/probability-foundations.pdf) |
| 10 | Durrett Ch.5.3--5.4: martingales | Martingale definitions, submartingale, supermartingale, Doob decomposition | [probability-foundations](01-math-foundations/01-measure-theory/probability-foundations.pdf) |
| 11 | Durrett Ch.5.5--5.6: martingale convergence | Martingale Convergence Theorem, Doob's Maximal Inequality | [probability-foundations](01-math-foundations/01-measure-theory/probability-foundations.pdf) |
| 12 | Durrett Ch.5.7: optional stopping | Optional Stopping Theorem, uniform integrability | [probability-foundations](01-math-foundations/01-measure-theory/probability-foundations.pdf) |
| 13 | Durrett Ch.6.1--6.3: Markov chains | Transition matrices, classification of states, stationary distributions | [probability-foundations](01-math-foundations/01-measure-theory/probability-foundations.pdf) |
| 14 | Durrett Ch.6.4--6.6: ergodic theory | Ergodic theorem, convergence to stationarity, coupling arguments | [probability-foundations](01-math-foundations/01-measure-theory/probability-foundations.pdf) |

### 1.2 Functional Analysis (Lessons 15--22)

**Primary text:** Kreyszig, E. *Introductory Functional Analysis with Applications*
**Alternative:** Conway, J.B. *A Course in Functional Analysis*

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 15 | Kreyszig Ch.1.1--1.4: metric spaces | Metric space axioms, open/closed sets, convergence, completeness | [01-metric-and-normed-spaces](01-math-foundations/02-functional-analysis/01-metric-and-normed-spaces.pdf) |
| 16 | Kreyszig Ch.1.5--1.6: completeness, compactness | Baire Category Theorem, sequential compactness, total boundedness | [01-metric-and-normed-spaces](01-math-foundations/02-functional-analysis/01-metric-and-normed-spaces.pdf) |
| 17 | Kreyszig Ch.2.1--2.4: normed spaces | Normed spaces, equivalence of norms in finite dimensions, Banach spaces | [01-metric-and-normed-spaces](01-math-foundations/02-functional-analysis/01-metric-and-normed-spaces.pdf) |
| 18 | Kreyszig Ch.2.5--2.8: bounded operators | Bounded linear operators, operator norm, dual spaces | [01-metric-and-normed-spaces](01-math-foundations/02-functional-analysis/01-metric-and-normed-spaces.pdf) |
| 19 | Kreyszig Ch.3.1--3.4: inner product spaces | Inner product axioms, Cauchy-Schwarz, Hilbert spaces, orthogonal complements | [02-hilbert-spaces-and-operators](01-math-foundations/02-functional-analysis/02-hilbert-spaces-and-operators.pdf) |
| 20 | Kreyszig Ch.3.5--3.8: projections, Riesz | Orthogonal projections, Riesz Representation Theorem | [02-hilbert-spaces-and-operators](01-math-foundations/02-functional-analysis/02-hilbert-spaces-and-operators.pdf) |
| 21 | Kreyszig Ch.4.1--4.3: fundamental theorems | Hahn-Banach Theorem, Uniform Boundedness Principle, Open Mapping Theorem | [02-hilbert-spaces-and-operators](01-math-foundations/02-functional-analysis/02-hilbert-spaces-and-operators.pdf) |
| 22 | Kreyszig Ch.5.1--5.4: fixed point theorems | Banach (Contraction Mapping), Brouwer, Schauder, Kakutani FPTs | [02-hilbert-spaces-and-operators](01-math-foundations/02-functional-analysis/02-hilbert-spaces-and-operators.pdf) |

### 1.3 Optimization Theory (Lessons 23--32)

**Stage 1:** Boyd, S. & Vandenberghe, L. *Convex Optimization* (free online)
**Stage 2:** Nesterov, Y. *Introductory Lectures on Convex Optimization* (2004)
**Stage 3:** Borkar, V.S. *Stochastic Approximation: A Dynamical Systems Viewpoint* (2008)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 23 | Boyd Ch.2: convex sets | Convex sets, cones, hyperplanes, separation theorems | [01-convex-analysis](01-math-foundations/03-optimization/01-convex-analysis.pdf) |
| 24 | Boyd Ch.3: convex functions | Convex functions, operations preserving convexity, conjugate functions | [01-convex-analysis](01-math-foundations/03-optimization/01-convex-analysis.pdf) |
| 25 | Boyd Ch.4: convex optimization problems | LP, QP, SOCP, SDP formulations | [02-convex-optimization-and-duality](01-math-foundations/03-optimization/02-convex-optimization-and-duality.pdf) |
| 26 | Boyd Ch.5: Lagrangian duality | Lagrangian, dual problem, weak/strong duality, KKT conditions | [02-convex-optimization-and-duality](01-math-foundations/03-optimization/02-convex-optimization-and-duality.pdf) |
| 27 | Boyd Ch.9: unconstrained optimization | Gradient descent, steepest descent, convergence analysis | [02-convex-optimization-and-duality](01-math-foundations/03-optimization/02-convex-optimization-and-duality.pdf) |
| 28 | Boyd Ch.10--11: Newton, interior point | Newton's method, barrier method, interior point algorithms | [02-convex-optimization-and-duality](01-math-foundations/03-optimization/02-convex-optimization-and-duality.pdf) |
| 29 | Nesterov Ch.1--2: smooth optimization | L-Lipschitz gradient, mu-strong convexity, O(1/k) and O(rho^k) rates | [02-convex-optimization-and-duality](01-math-foundations/03-optimization/02-convex-optimization-and-duality.pdf) |
| 30 | Nesterov Ch.3--4: nonsmooth, proximal | Nesterov acceleration, proximal operators, proximal gradient methods | [02-convex-optimization-and-duality](01-math-foundations/03-optimization/02-convex-optimization-and-duality.pdf) |
| 31 | Borkar Ch.1--2: Robbins-Monro, ODE method | Stochastic approximation, Robbins-Monro algorithm, ODE characterization | [03-stochastic-approximation](01-math-foundations/03-optimization/03-stochastic-approximation.pdf) |
| 32 | Borkar Ch.3, 6: convergence, two-timescale | Convergence analysis via ODE, two-timescale stochastic approximation | [03-stochastic-approximation](01-math-foundations/03-optimization/03-stochastic-approximation.pdf) |

### 1.4 Game Theory (Lessons 33--38)

**Primary text:** Fudenberg, D. & Tirole, J. *Game Theory* (1991)
**Alternative:** Osborne, M.J. & Rubinstein, A. *A Course in Game Theory*

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 33 | F&T Ch.1: static games | Normal-form games, Nash equilibrium existence (via Kakutani/Brouwer), mixed strategies | [01-static-and-extensive-form-games](01-math-foundations/04-game-theory/01-static-and-extensive-form-games.pdf) |
| 34 | F&T Ch.2: iterated dominance | Iterated strict dominance, rationalizability, correlated equilibrium | [01-static-and-extensive-form-games](01-math-foundations/04-game-theory/01-static-and-extensive-form-games.pdf) |
| 35 | F&T Ch.3: extensive-form games | Game trees, information sets, subgame perfect equilibrium, backward induction | [01-static-and-extensive-form-games](01-math-foundations/04-game-theory/01-static-and-extensive-form-games.pdf) |
| 36 | F&T Ch.6: repeated games | Infinitely repeated games, folk theorems, discount factor and cooperation | [02-repeated-games-and-incomplete-info](01-math-foundations/04-game-theory/02-repeated-games-and-incomplete-info.pdf) |
| 37 | F&T Ch.12: Bayesian games | Incomplete information, Bayesian Nash equilibrium, type spaces | [02-repeated-games-and-incomplete-info](01-math-foundations/04-game-theory/02-repeated-games-and-incomplete-info.pdf) |
| 38 | F&T Ch.13: signaling games | Signaling, Perfect Bayesian Equilibrium (PBE), potential games | [02-repeated-games-and-incomplete-info](01-math-foundations/04-game-theory/02-repeated-games-and-incomplete-info.pdf) |

---

## Phase 02: Core Reinforcement Learning (~20 lessons, 3--4 months)

### 2.1 Markov Decision Processes (Lessons 39--46)

**Primary text:** Puterman, M.L. *Markov Decision Processes* (2014)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 39 | Puterman Ch.2: model formulation | MDP components (S, A, P, R), policies, histories | [01-mdp-formulation-and-finite-horizon](02-core-rl/01-mdp/01-mdp-formulation-and-finite-horizon.pdf) |
| 40 | Puterman Ch.3: finite-horizon MDPs | Backward induction, finite-horizon optimality equations | [01-mdp-formulation-and-finite-horizon](02-core-rl/01-mdp/01-mdp-formulation-and-finite-horizon.pdf) |
| 41 | Puterman Ch.4: infinite-horizon, discounted | Bellman optimality equation, discounted reward criterion | [02-infinite-horizon-and-dynamic-programming](02-core-rl/01-mdp/02-infinite-horizon-and-dynamic-programming.pdf) |
| 42 | Puterman Ch.5.1--5.3: contraction, value iteration | Contraction property of Bellman operator (sup-norm), value iteration convergence | [02-infinite-horizon-and-dynamic-programming](02-core-rl/01-mdp/02-infinite-horizon-and-dynamic-programming.pdf) |
| 43 | Puterman Ch.5.4--5.6: value iteration (cont.) | Error bounds, stopping criteria, monotonicity | [02-infinite-horizon-and-dynamic-programming](02-core-rl/01-mdp/02-infinite-horizon-and-dynamic-programming.pdf) |
| 44 | Puterman Ch.6: average reward | Average reward criterion, gain-bias equations, Blackwell optimality | [02-infinite-horizon-and-dynamic-programming](02-core-rl/01-mdp/02-infinite-horizon-and-dynamic-programming.pdf) |
| 45 | Puterman Ch.8.1--8.4: policy iteration | Policy improvement theorem, policy iteration convergence | [02-infinite-horizon-and-dynamic-programming](02-core-rl/01-mdp/02-infinite-horizon-and-dynamic-programming.pdf) |
| 46 | Puterman Ch.8.5--8.8: LP formulation | Linear programming formulation of MDPs, occupancy measures | [02-infinite-horizon-and-dynamic-programming](02-core-rl/01-mdp/02-infinite-horizon-and-dynamic-programming.pdf) |

### 2.2 Reinforcement Learning Algorithms (Lessons 47--53)

**For intuition:** Sutton, R.S. & Barto, A.G. *Reinforcement Learning* (2nd ed., 2018, free online)
**For rigor:** Bertsekas, D.P. & Tsitsiklis, J.N. *Neuro-Dynamic Programming* (1996)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 47 | S&B Ch.6--7 + B&T Ch.4: TD(0), n-step TD | TD(0) update rule, n-step returns, bias-variance tradeoff | [temporal-difference-learning](02-core-rl/02-rl-algorithms/temporal-difference-learning.pdf) |
| 48 | B&T Ch.4: TD(lambda), eligibility traces | TD(lambda), forward/backward views, eligibility trace mechanism | [temporal-difference-learning](02-core-rl/02-rl-algorithms/temporal-difference-learning.pdf) |
| 49 | S&B Ch.6 + B&T Ch.4: SARSA | SARSA update, on-policy TD control, convergence conditions | [temporal-difference-learning](02-core-rl/02-rl-algorithms/temporal-difference-learning.pdf) |
| 50 | S&B Ch.6 + B&T Ch.6: Q-learning | Q-learning update, off-policy control, convergence proof (Jaakkola, Jordan, Singh 1994) | [temporal-difference-learning](02-core-rl/02-rl-algorithms/temporal-difference-learning.pdf) |
| 51 | B&T Ch.2: function approximation | Linear function approximation, feature construction, projection operators | [temporal-difference-learning](02-core-rl/02-rl-algorithms/temporal-difference-learning.pdf) |
| 52 | B&T Ch.3: approximate policy iteration | Approximate policy iteration, error propagation bounds | [temporal-difference-learning](02-core-rl/02-rl-algorithms/temporal-difference-learning.pdf) |
| 53 | S&B Ch.11 + B&T: the deadly triad | Deadly triad (function approx + bootstrapping + off-policy), Baird's counterexample, divergence | [temporal-difference-learning](02-core-rl/02-rl-algorithms/temporal-difference-learning.pdf) |

### 2.3 Policy Gradient Theory (Lessons 54--58)

**Primary sources:** Sutton et al. (2000), Kakade (2002), Schulman et al. (2015, 2017)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 54 | S&B Ch.13: policy gradient theorem | Policy gradient theorem derivation: nabla J = E[nabla log pi * Q^pi] | [policy-gradient-theorem](02-core-rl/03-policy-gradient/policy-gradient-theorem.pdf) |
| 55 | Sutton et al. (2000): REINFORCE | REINFORCE algorithm, variance reduction via baselines | [policy-gradient-theorem](02-core-rl/03-policy-gradient/policy-gradient-theorem.pdf) |
| 56 | Kakade (2002): natural gradient | Natural policy gradient, Fisher information matrix, information geometry | [policy-gradient-theorem](02-core-rl/03-policy-gradient/policy-gradient-theorem.pdf) |
| 57 | S&B Ch.13: actor-critic | Actor-critic architecture, advantage functions, GAE | [policy-gradient-theorem](02-core-rl/03-policy-gradient/policy-gradient-theorem.pdf) |
| 58 | Review + connections | Synthesis of policy gradient theory, connections to Phase 04 methods | [policy-gradient-theorem](02-core-rl/03-policy-gradient/policy-gradient-theorem.pdf) |

---

## Phase 03: Deep Learning Foundations (~14 lessons, 2--3 months)

### 3.1 Neural Network Theory (Lessons 59--66)

**Primary text:** Bach, F. *Learning Theory from First Principles* (2024, free online)
**Supplementary:** Pinkus, A. *Approximation Theory of the MLP Model* (1999, Acta Numerica)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 59 | Bach Ch.1--2: statistical learning | ERM, hypothesis classes, generalization bounds | [01-approximation-theory](03-deep-learning/01-neural-networks/01-approximation-theory.pdf) |
| 60 | Bach Ch.3: bias-variance | Bias-variance decomposition, model selection | [01-approximation-theory](03-deep-learning/01-neural-networks/01-approximation-theory.pdf) |
| 61 | Bach Ch.4: kernel methods | Kernel trick, Mercer's theorem, RKHS construction | [01-approximation-theory](03-deep-learning/01-neural-networks/01-approximation-theory.pdf) |
| 62 | Bach Ch.5: RKHS theory | Reproducing kernel Hilbert spaces, representer theorem | [01-approximation-theory](03-deep-learning/01-neural-networks/01-approximation-theory.pdf) |
| 63 | Bach Ch.6: NN approximation | Universal approximation theorems (Cybenko, Hornik et al.) | [01-approximation-theory](03-deep-learning/01-neural-networks/01-approximation-theory.pdf) |
| 64 | Bach Ch.7: NN optimization | Barron's theorem, dimension-free approximation rates | [01-approximation-theory](03-deep-learning/01-neural-networks/01-approximation-theory.pdf) |
| 65 | Pinkus (1999): approximation rates | Approximation rates for smooth functions, width vs depth tradeoffs | [01-approximation-theory](03-deep-learning/01-neural-networks/01-approximation-theory.pdf) |
| 66 | NTK perspective + complexity | Neural Tangent Kernel, Rademacher complexity bounds for NNs | [01-approximation-theory](03-deep-learning/01-neural-networks/01-approximation-theory.pdf) |

### 3.2 Recurrent Neural Networks (Lessons 67--69)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 67 | BPTT derivation | Backpropagation Through Time, vanishing/exploding gradient problem | [rnn](03-deep-learning/01-neural-networks/rnn.pdf) |
| 68 | LSTM architecture | Gating mechanisms (input, forget, output), cell state dynamics | [lstm](03-deep-learning/01-neural-networks/lstm.pdf) |
| 69 | GRU and variants | GRU simplification, sequence-to-sequence architectures | [lstm](03-deep-learning/01-neural-networks/lstm.pdf) |

### 3.3 Optimization for Deep Learning (Lessons 70--72)

**Key papers:** Bottou et al. (2018), Kingma & Ba (2015), Reddi et al. (2018)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 70 | Bottou et al. (2018): SGD convergence | SGD convergence (convex and non-convex), learning rate schedules | [01-sgd-and-adaptive-methods](03-deep-learning/02-optimization-for-dl/01-sgd-and-adaptive-methods.pdf) |
| 71 | Variance reduction + adaptive | SVRG, SAGA, AdaGrad, RMSprop | [01-sgd-and-adaptive-methods](03-deep-learning/02-optimization-for-dl/01-sgd-and-adaptive-methods.pdf) |
| 72 | Kingma & Ba (2015), Reddi (2018) | Adam optimizer, AMSGrad, convergence issues and fixes | [01-sgd-and-adaptive-methods](03-deep-learning/02-optimization-for-dl/01-sgd-and-adaptive-methods.pdf) |

---

## Phase 04: Deep Reinforcement Learning (~14 lessons, 2--3 months)

### 4.1 Value-Based Methods (Lessons 73--76)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 73 | Mnih et al. (2015): DQN | DQN architecture, experience replay, target networks, why they stabilize learning | [01-dqn-and-extensions](04-deep-rl/01-value-based/01-dqn-and-extensions.pdf) |
| 74 | Van Hasselt (2016), Wang (2016) | Double DQN (overestimation bias fix), Dueling architecture | [01-dqn-and-extensions](04-deep-rl/01-value-based/01-dqn-and-extensions.pdf) |
| 75 | Bellemare et al. (2017): C51 | Distributional Bellman equation, categorical projection | [02-distributional-rl](04-deep-rl/01-value-based/02-distributional-rl.pdf) |
| 76 | QR-DQN, IQN | Quantile regression for distributional RL, implicit quantile networks | [02-distributional-rl](04-deep-rl/01-value-based/02-distributional-rl.pdf) |

### 4.2 Policy-Based Methods (Lessons 77--84)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 77 | Schulman et al. (2015): TRPO | TRPO derivation, monotonic improvement guarantee, trust regions and why they help | [01-trust-region-methods](04-deep-rl/02-policy-based/01-trust-region-methods.pdf) |
| 78 | TRPO practical algorithm | Conjugate gradient for KL constraint, line search, practical implementation | [01-trust-region-methods](04-deep-rl/02-policy-based/01-trust-region-methods.pdf) |
| 79 | Schulman et al. (2017): PPO | PPO clipped surrogate objective, simplified trust region | [02-proximal-policy-optimization](04-deep-rl/02-policy-based/02-proximal-policy-optimization.pdf) |
| 80 | PPO + GAE details | Generalized Advantage Estimation, PPO implementation details | [02-proximal-policy-optimization](04-deep-rl/02-policy-based/02-proximal-policy-optimization.pdf) |
| 81 | Lillicrap et al. (2016): DDPG | Deterministic policy gradient theorem, DDPG algorithm | [03-deterministic-policy-gradient](04-deep-rl/02-policy-based/03-deterministic-policy-gradient.pdf) |
| 82 | Fujimoto et al. (2018): TD3 | Twin critics, delayed updates, target policy smoothing | [03-deterministic-policy-gradient](04-deep-rl/02-policy-based/03-deterministic-policy-gradient.pdf) |
| 83 | Haarnoja et al. (2018): SAC | Maximum entropy framework, soft Bellman equation, SAC algorithm | [04-maximum-entropy-rl](04-deep-rl/02-policy-based/04-maximum-entropy-rl.pdf) |
| 84 | SAC analysis | Two-timescale actor-critic analysis (connects to Borkar), entropy-regularized optimality | [04-maximum-entropy-rl](04-deep-rl/02-policy-based/04-maximum-entropy-rl.pdf) |

### 4.3 Model-Based Methods (Lessons 85--86)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 85 | Sutton (1991), Schrittwieser (2020) | Dyna architecture, MuZero (planning with learned models) | [01-model-based-rl](04-deep-rl/03-model-based/01-model-based-rl.pdf) |
| 86 | Hafner et al. (2020): Dreamer | World models, latent imagination, Dreamer algorithm | [01-model-based-rl](04-deep-rl/03-model-based/01-model-based-rl.pdf) |

---

## Phase 05: Multi-Agent Reinforcement Learning (~18 lessons, 3--4 months)

> *This is your target area. Build strong foundations in the previous phases before
> diving deep here.*

### 5.1 Stochastic Games (Lessons 87--92)

**Primary:** Shoham, Y. & Leyton-Brown, K. *Multiagent Systems* (2008, free online)
**Theoretical:** Filar, J. & Vrieze, K. *Competitive Markov Decision Processes* (1997)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 87 | Shoham & L-B Ch.3--4: game theory review | Normal-form games, Nash equilibria, mixed strategies (review from Phase 01) | [01-stochastic-game-theory](05-marl/01-stochastic-games/01-stochastic-game-theory.pdf) |
| 88 | Shoham & L-B Ch.6--7: learning in games | Repeated games, fictitious play, no-regret learning | [01-stochastic-game-theory](05-marl/01-stochastic-games/01-stochastic-game-theory.pdf) |
| 89 | Filar & Vrieze Ch.1--2: zero-sum stochastic games | Stochastic game formalism (N, S, {A_i}, P, {R_i}, gamma), zero-sum case | [01-stochastic-game-theory](05-marl/01-stochastic-games/01-stochastic-game-theory.pdf) |
| 90 | Filar & Vrieze Ch.3--4: general-sum | General-sum stochastic games, Markov perfect equilibrium | [01-stochastic-game-theory](05-marl/01-stochastic-games/01-stochastic-game-theory.pdf) |
| 91 | Filar & Vrieze Ch.5: equilibrium computation | Computation of equilibria, complexity results | [01-stochastic-game-theory](05-marl/01-stochastic-games/01-stochastic-game-theory.pdf) |
| 92 | Shapley's theorem, existence | Shapley's theorem for zero-sum games, existence via fixed point arguments | [01-stochastic-game-theory](05-marl/01-stochastic-games/01-stochastic-game-theory.pdf) |

### 5.2 Cooperative MARL (Lessons 93--95)

**Key papers:** Bernstein et al. (2002), Sunehag et al. (2018), Rashid et al. (2018), Son et al. (2019), Yu et al. (2022)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 93 | Bernstein et al. (2002) | Dec-POMDP formalism, NEXP-completeness, CTDE paradigm | [01-cooperative-marl](05-marl/02-cooperative/01-cooperative-marl.pdf) |
| 94 | Sunehag (2018), Rashid (2018) | VDN, QMIX, IGM condition, value decomposition | [01-cooperative-marl](05-marl/02-cooperative/01-cooperative-marl.pdf) |
| 95 | Son (2019), Yu (2022) | QTRAN, MAPPO, credit assignment problem | [01-cooperative-marl](05-marl/02-cooperative/01-cooperative-marl.pdf) |

### 5.3 Competitive and Mixed MARL (Lessons 96--98)

**Key papers:** Littman (1994), Hu & Wellman (2003), Lowe et al. (2017), Foerster et al. (2018), Silver et al. (2017), Lanctot et al. (2017)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 96 | Littman (1994), Hu & Wellman (2003) | Minimax-Q for zero-sum, Nash Q-Learning for general-sum | [01-competitive-and-mixed-marl](05-marl/03-competitive/01-competitive-and-mixed-marl.pdf) |
| 97 | Lowe et al. (2017), Foerster et al. (2018) | MADDPG (centralized critic), LOLA (opponent modeling) | [01-competitive-and-mixed-marl](05-marl/03-competitive/01-competitive-and-mixed-marl.pdf) |
| 98 | Silver et al. (2017), Lanctot et al. (2017) | AlphaGo Zero self-play, PSRO (population-based) | [01-competitive-and-mixed-marl](05-marl/03-competitive/01-competitive-and-mixed-marl.pdf) |

### 5.4 Mean-Field Games (Lessons 99--101)

**Primary:** Carmona, R. & Delarue, F. *Probabilistic Theory of Mean Field Games* (2018), Volume I
**Key paper:** Yang et al. (2018)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 99 | Carmona & Delarue I, Ch.1--2 | Mean-field game formulation, McKean-Vlasov dynamics, forward-backward SDEs | [01-mean-field-games](05-marl/04-mean-field/01-mean-field-games.pdf) |
| 100 | Carmona & Delarue I, Ch.3--5 | Mean-field equilibria, existence and uniqueness, fixed point characterization | [01-mean-field-games](05-marl/04-mean-field/01-mean-field-games.pdf) |
| 101 | Yang et al. (2018) | Mean Field Multi-Agent RL, mean-field Q-learning | [01-mean-field-games](05-marl/04-mean-field/01-mean-field-games.pdf) |

### 5.5 Communication in MARL (Lessons 102--104)

**Key papers:** Sukhbaatar et al. (2016), Foerster et al. (2016), Das et al. (2019)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 102 | Sukhbaatar (2016), Foerster (2016) | CommNet (continuous communication), DIAL/RIAL (discrete channels) | [01-communication-in-marl](05-marl/05-communication/01-communication-in-marl.pdf) |
| 103 | Das et al. (2019) | TarMAC (targeted multi-agent communication via attention) | [01-communication-in-marl](05-marl/05-communication/01-communication-in-marl.pdf) |
| 104 | Survey papers | Emergent communication, language grounding, survey of communication methods | [01-communication-in-marl](05-marl/05-communication/01-communication-in-marl.pdf) |

**Recommended surveys:**
- Busoniu et al. (2008) -- "A Comprehensive Survey of Multi-Agent Reinforcement Learning"
- Hernandez-Leal et al. (2019) -- "A Survey and Critique of Multiagent Deep Reinforcement Learning"
- Zhang et al. (2021) -- "Multi-Agent Reinforcement Learning: A Selective Overview of Theories and Algorithms"

---

## Phase 06: Aerospace Applications (~10 lessons, ongoing)

### 6.1 Continuous Control (Lessons 105--106)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 105 | High-dimensional action spaces | Hierarchical RL, option framework, action decomposition | [01-continuous-control](06-aerospace/01-continuous-control/01-continuous-control.pdf) |
| 106 | MPC+RL hybrids | Model predictive control integration, planning horizons | [01-continuous-control](06-aerospace/01-continuous-control/01-continuous-control.pdf) |

### 6.2 Safety and Constraints (Lessons 107--108)

**Key papers:** Altman (1999), Achiam et al. (2017), Chow et al. (2018), Berkenkamp et al. (2017)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 107 | Altman (1999), Achiam (2017) | Constrained MDPs, Lagrangian relaxation, CPO, primal-dual methods | [01-safety-and-constraints](06-aerospace/02-safety/01-safety-and-constraints.pdf) |
| 108 | Chow (2018), Berkenkamp (2017) | Lyapunov-based safe RL, reachability analysis, safe model-based RL | [01-safety-and-constraints](06-aerospace/02-safety/01-safety-and-constraints.pdf) |

### 6.3 Partial Observability (Lessons 109--110)

**Primary:** Krishnamurthy, V. *Partially Observed Markov Decision Processes* (2016)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 109 | Krishnamurthy Ch.1--3: POMDP formulation | POMDP model, belief states, belief MDP reduction | [01-pomdps](06-aerospace/03-partial-observability/01-pomdps.pdf) |
| 110 | Krishnamurthy Ch.4--5, 7--8: structural results | Structural results for optimal policies, approximate methods | [01-pomdps](06-aerospace/03-partial-observability/01-pomdps.pdf) |

### 6.4 Sim-to-Real Transfer (Lessons 111--112)

**Key papers:** Tobin et al. (2017), Peng et al. (2018), Akkaya et al. (2019)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 111 | Tobin (2017), Akkaya (2019) | Domain randomization, systematic perturbation of simulation parameters | [01-sim-to-real-transfer](06-aerospace/04-sim-to-real/01-sim-to-real-transfer.pdf) |
| 112 | Peng et al. (2018) | Progressive nets, system identification, bridging the sim-to-real gap | [01-sim-to-real-transfer](06-aerospace/04-sim-to-real/01-sim-to-real-transfer.pdf) |

### 6.5 Multi-Vehicle Coordination (Lessons 113--114)

**Key papers:** Sartoretti et al. (2019), Khan et al. (2020), Riviere et al. (2020)

| Lesson | Reading | Key Results | Document |
|--------|---------|-------------|----------|
| 113 | Sartoretti (2019), Khan (2020) | Formation control (graph Laplacian), graph policy gradients, collision avoidance | [01-multi-vehicle-coordination](06-aerospace/05-multi-vehicle/01-multi-vehicle-coordination.pdf) |
| 114 | Riviere (2020) + synthesis | GLAS, communication-aware coordination, heterogeneous agent teams | [01-multi-vehicle-coordination](06-aerospace/05-multi-vehicle/01-multi-vehicle-coordination.pdf) |

---

## Summary: The Critical Path

If time is constrained, here is the absolute minimum path through the curriculum:

| Topic | Essential Reading | Lessons |
|-------|-------------------|---------|
| Probability | Durrett, Chapters 1--5 | 1--12 |
| Optimization | Boyd Ch. 2--5, 9; Nesterov Ch. 2; Borkar Ch. 1--3, 6 | 23--32 |
| Game Theory | Fudenberg & Tirole Ch. 1, 3, 6 | 33, 35, 36 |
| MDPs | Puterman Ch. 4--6, 8 | 41--46 |
| RL Algorithms | Sutton & Barto (intuition); Bertsekas & Tsitsiklis Ch. 4--6 (rigor) | 47--53 |
| Deep RL | DQN, DDPG, PPO, SAC papers | 73, 79, 81, 83 |
| MARL Foundations | Shoham & Leyton-Brown Ch. 6--7; Filar & Vrieze Ch. 1--4 | 88--91 |
| MARL Algorithms | QMIX, MADDPG, MAPPO papers | 94, 97 |
| Safety | Altman (1999); CPO paper | 107 |

## Practical Advice

1. **Prove things yourself.** Close the book, state the theorem, and prove it.
2. **Implement from scratch.** After understanding the theory, implement TD-learning, Q-learning, policy gradients, QMIX without using existing libraries.
3. **Read original papers.** Textbooks synthesize, but papers show the original thinking and often contain insights lost in translation.
4. **Join the research community.** Follow proceedings of NeurIPS, ICML, ICLR, AAMAS, CoRL.
5. **Find open problems.** As you read, note gaps, limitations, open questions. These are your research opportunities.

*The goal is not to learn reinforcement learning. The goal is to advance it.*
