# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a collection of rigorous mathematical treatment documents (PDFs) covering AI/ML topics. Each document provides formal proofs, complete derivations, and theoretical foundations -- not implementations or code.

## Document Catalog

Documents are organized across 7 phases (Phase 00 prerequisites + Phases 01-06 aligned with curriculum.pdf -- 102 sessions). Each phase directory has its own `README.md` with full details.

**Total: 70 documents** (54 exist, 16 planned)

### Phase 00 -- Prerequisites (12 lessons)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 1 | `00-prerequisites/01-real-analysis/lesson-01-real-numbers-sequences-series` | Ordered fields, supremum/infimum, Archimedean property, sequences, convergence, Bolzano-Weierstrass, series, convergence tests | **exists** |
| 2 | `00-prerequisites/01-real-analysis/lesson-02-topology-and-continuity` | Open/closed sets, compactness, Heine-Borel, continuity, IVT, EVT, uniform continuity | **exists** |
| 3 | `00-prerequisites/01-real-analysis/lesson-03-differentiation-and-integration` | Derivatives, chain rule, MVT, Taylor's theorem, Riemann integral, FTC | **exists** |
| 4 | `00-prerequisites/01-real-analysis/lesson-04-function-sequences-and-metric-spaces` | Pointwise/uniform convergence, interchange theorems, metric spaces, completeness, Banach fixed-point theorem | **exists** |
| 5 | `00-prerequisites/02-linear-algebra/lesson-05-vector-spaces-and-linear-maps` | Vector spaces, subspaces, bases, dimension, linear maps, rank-nullity, matrix representation | **exists** |
| 6 | `00-prerequisites/02-linear-algebra/lesson-06-determinants-and-eigenvalues` | Determinants, cofactor expansion, eigenvalues, characteristic polynomial, diagonalization, Cayley-Hamilton | **exists** |
| 7 | `00-prerequisites/02-linear-algebra/lesson-07-inner-products-and-spectral-theory` | Inner product spaces, Cauchy-Schwarz, Gram-Schmidt, orthogonal projections, spectral theorem, positive definiteness | **exists** |
| 8 | `00-prerequisites/02-linear-algebra/lesson-08-svd-norms-and-matrix-calculus` | Quadratic forms, SVD, Eckart-Young, matrix norms, condition number, matrix exponential, gradient, Jacobian, Hessian | **exists** |
| 9 | `00-prerequisites/03-probability/lesson-09-probability-spaces-and-conditioning` | Probability spaces, Kolmogorov axioms, inclusion-exclusion, conditional probability, Bayes' theorem, independence | **exists** |
| 10 | `00-prerequisites/03-probability/lesson-10-random-variables-and-distributions` | Discrete RVs (Bernoulli, binomial, geometric, Poisson), continuous RVs (uniform, exponential, normal), CDFs, PDFs | **exists** |
| 11 | `00-prerequisites/03-probability/lesson-11-expectation-variance-joint-distributions` | Expectation, LOTUS, variance, covariance, correlation, joint distributions, conditional expectation, tower property | **exists** |
| 12 | `00-prerequisites/03-probability/lesson-12-inequalities-and-limit-theorems` | MGFs, Markov/Chebyshev/Hoeffding inequalities, WLLN, SLLN, CLT, sample complexity | **exists** |

### Phase 01 -- Mathematical Foundations (9 docs)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 13 | `01-math-foundations/01-measure-theory/01-measure-spaces` | sigma-algebras, measures, Caratheodory extension, measurable functions, pi-lambda theorem | **exists** |
| 14 | `01-math-foundations/01-measure-theory/probability-foundations` | Expectation, conditional expectation, tower property, variance, convergence modes, inequalities, Borel-Cantelli, LLN, CLT, Markov chains, martingales | **exists** |
| 15 | `01-math-foundations/02-functional-analysis/01-metric-and-normed-spaces` | Metric spaces, normed spaces, Banach spaces, completeness, compactness in normed spaces | **exists** |
| 16 | `01-math-foundations/02-functional-analysis/02-hilbert-spaces-and-operators` | Inner product spaces, Hilbert spaces, orthogonal projections, Riesz representation, Hahn-Banach, uniform boundedness, fixed point theorems (Banach, Brouwer, Schauder, Kakutani) | **exists** |
| 17 | `01-math-foundations/03-optimization/01-convex-analysis` | Convex sets, convex functions, operations preserving convexity, conjugate functions, separation theorems | **exists** |
| 18 | `01-math-foundations/03-optimization/02-convex-optimization-and-duality` | Convex optimization problems, Lagrangian duality, KKT conditions, gradient descent, accelerated methods, proximal methods, interior point methods | **exists** |
| 19 | `01-math-foundations/03-optimization/03-stochastic-approximation` | Robbins-Monro, ODE method, convergence analysis, two-timescale SA | **exists** |
| 20 | `01-math-foundations/04-game-theory/01-static-and-extensive-form-games` | Normal-form games, Nash equilibrium, minimax theorem, correlated equilibrium, extensive-form games, subgame perfection | **exists** |
| 21 | `01-math-foundations/04-game-theory/02-repeated-games-and-incomplete-info` | Repeated games, folk theorems, fictitious play, no-regret learning, Bayesian games, PBE, signaling games, potential games | **exists** |

### Phase 02 -- Core Reinforcement Learning (20 lessons)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 22 | `02-core-rl/01-mdp/lesson-39-mdp-model-and-policies` | MDP components (S, A, P, R), policies, histories, Markov property, value functions, Bellman expectation equations | **exists** |
| 23 | `02-core-rl/01-mdp/lesson-40-finite-horizon-mdp` | Finite-horizon optimality equations, backward induction | **exists** |
| 24 | `02-core-rl/01-mdp/lesson-41-discounted-reward-bellman-equations` | Discounted reward criterion, Bellman optimality equation, Bellman operators | **exists** |
| 25 | `02-core-rl/01-mdp/lesson-42-contraction-and-value-iteration` | Banach fixed-point on Bellman operator, value iteration convergence, a priori/a posteriori error bounds | **exists** |
| 26 | `02-core-rl/01-mdp/lesson-43-vi-error-bounds-and-monotonicity` | Span seminorm, span-based error bounds, monotone convergence, policy convergence | **exists** |
| 27 | `02-core-rl/01-mdp/lesson-44-average-reward-mdp` | Average reward criterion, gain-bias equations, Poisson equations, relative VI, Blackwell optimality | **exists** |
| 28 | `02-core-rl/01-mdp/lesson-45-policy-iteration` | Policy improvement theorem, policy iteration, finite convergence, modified PI | **exists** |
| 29 | `02-core-rl/01-mdp/lesson-46-lp-formulation-and-occupancy` | LP formulation of MDPs, occupancy measures, duality, constrained MDPs | **exists** |
| 30 | `02-core-rl/02-rl-algorithms/lesson-47-td0-and-nstep-td` | TD(0) update, TD error properties, convergence via SA, bias-variance analysis, n-step returns | **exists** |
| 31 | `02-core-rl/02-rl-algorithms/lesson-48-td-lambda-eligibility-traces` | Lambda-return, forward/backward views, eligibility traces, forward-backward equivalence | **exists** |
| 32 | `02-core-rl/02-rl-algorithms/lesson-49-sarsa` | SARSA update, on-policy TD control, epsilon-greedy, GLIE, convergence via perturbed SA | **exists** |
| 33 | `02-core-rl/02-rl-algorithms/lesson-50-q-learning` | Q-learning, off-policy control, convergence proof, maximization bias, Double Q-learning, Expected SARSA | **exists** |
| 34 | `02-core-rl/02-rl-algorithms/lesson-51-function-approximation` | Linear FA, features, projection operators, MSVE, semi-gradient TD(0), convergence under linear FA | **exists** |
| 35 | `02-core-rl/02-rl-algorithms/lesson-52-approximate-policy-iteration` | Approximate PI, error propagation bounds, LSTD, fitted value iteration | **exists** |
| 36 | `02-core-rl/02-rl-algorithms/lesson-53-deadly-triad` | Deadly triad, Baird's counterexample, divergence, MSPBE, GTD2, Gradient-TD methods | **exists** |
| 37 | `02-core-rl/03-policy-gradient/lesson-54-policy-gradient-theorem` | Policy gradient theorem derivation, score function, compatible function approximation | **exists** |
| 38 | `02-core-rl/03-policy-gradient/lesson-55-reinforce-and-baselines` | REINFORCE algorithm, variance reduction via baselines, optimal baseline | **exists** |
| 39 | `02-core-rl/03-policy-gradient/lesson-56-natural-policy-gradient` | Natural gradient, Fisher information matrix, information geometry, covariance theorem | **exists** |
| 40 | `02-core-rl/03-policy-gradient/lesson-57-actor-critic-and-gae` | Actor-critic architecture, advantage functions, GAE, two-timescale convergence | **exists** |
| 41 | `02-core-rl/03-policy-gradient/lesson-58-policy-gradient-synthesis` | Unified PG framework, variance reduction taxonomy, convergence landscape, connections to TRPO/PPO/SAC | **exists** |

### Phase 03 -- Deep Learning (12 docs)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 42 | `03-deep-learning/01-neural-networks/lesson-59-erm-and-generalization` | ERM, hypothesis classes, VC dimension, Sauer's lemma, uniform convergence, fundamental theorem of statistical learning | **exists** |
| 43 | `03-deep-learning/01-neural-networks/lesson-60-bias-variance-and-model-selection` | Bias-variance decomposition, approximation-estimation tradeoff, structural risk minimization, AIC/BIC, cross-validation | **exists** |
| 44 | `03-deep-learning/01-neural-networks/lesson-61-kernel-methods` | Kernel trick, positive definite kernels, Mercer's theorem, kernel construction | **exists** |
| 45 | `03-deep-learning/01-neural-networks/lesson-62-rkhs-and-representer-theorem` | RKHS construction, reproducing property, representer theorem, kernel ridge regression | **exists** |
| 46 | `03-deep-learning/01-neural-networks/lesson-63-universal-approximation` | Cybenko's theorem, Hornik's universal approximation, density arguments, limitations | **exists** |
| 47 | `03-deep-learning/01-neural-networks/lesson-64-barron-theorem-and-approximation-rates` | Barron's theorem, dimension-free approximation rates, Fourier analysis, integral representation | **exists** |
| 48 | `03-deep-learning/01-neural-networks/lesson-65-depth-width-tradeoffs` | Depth separation (Telgarsky), width sufficiency, approximation rates for smooth functions | **exists** |
| 49 | `03-deep-learning/01-neural-networks/lesson-66-ntk-and-rademacher-complexity` | Neural tangent kernel, lazy training, Rademacher complexity bounds for NNs, generalization | **exists** |
| 50 | `03-deep-learning/01-neural-networks/lesson-67-rnn-and-bptt` | Vanilla RNN architecture, BPTT derivation, vanishing/exploding gradient theorems, gradient clipping | **exists** |
| 51 | `03-deep-learning/01-neural-networks/lesson-68-lstm-and-gating` | LSTM cell architecture, forget/input/output gates, cell state dynamics, BPTT through LSTM, gradient flow analysis | **exists** |
| 52 | `03-deep-learning/01-neural-networks/lesson-69-gru-and-sequence-architectures` | GRU, bidirectional RNNs, deep stacked RNNs, encoder-decoder framework | **exists** |
| 53 | `03-deep-learning/02-optimization-for-dl/01-sgd-and-adaptive-methods` | SGD convergence (convex/non-convex), variance reduction, AdaGrad, RMSprop, Adam, loss landscape geometry, batch normalization | planned |

### Phase 04 -- Deep Reinforcement Learning (7 docs)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 54 | `04-deep-rl/01-value-based/01-dqn-and-extensions` | DQN, experience replay, target networks, Double DQN, Dueling, overestimation bias | planned |
| 55 | `04-deep-rl/01-value-based/02-distributional-rl` | C51, quantile regression DQN, IQN, distributional Bellman equation | planned |
| 56 | `04-deep-rl/02-policy-based/01-trust-region-methods` | TRPO, natural policy gradient, KL-constrained optimization | **exists** |
| 57 | `04-deep-rl/02-policy-based/02-proximal-policy-optimization` | PPO, clipped surrogate objective, advantage estimation | **exists** |
| 58 | `04-deep-rl/02-policy-based/03-deterministic-policy-gradient` | Deterministic PG theorem, DDPG, TD3 | planned |
| 59 | `04-deep-rl/02-policy-based/04-maximum-entropy-rl` | Maximum entropy framework, SAC, two-timescale actor-critic analysis | planned |
| 60 | `04-deep-rl/03-model-based/01-model-based-rl` | Dyna, MuZero, Dreamer, world models, planning with learned models | planned |

### Phase 05 -- Multi-Agent RL (5 docs)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 61 | `05-marl/01-stochastic-games/01-stochastic-game-theory` | Stochastic game formalism, Markov perfect equilibrium, Shapley's theorem, existence via fixed points | planned |
| 62 | `05-marl/02-cooperative/01-cooperative-marl` | Dec-POMDP, CTDE, VDN, QMIX, QTRAN, MAPPO, IGM condition, credit assignment | planned |
| 63 | `05-marl/03-competitive/01-competitive-and-mixed-marl` | Minimax-Q, Nash-Q, MADDPG, LOLA, self-play, PSRO | planned |
| 64 | `05-marl/04-mean-field/01-mean-field-games` | Mean field game theory, McKean-Vlasov dynamics, forward-backward SDEs, mean field equilibria | planned |
| 65 | `05-marl/05-communication/01-communication-in-marl` | CommNet, DIAL, RIAL, TarMAC, emergent communication | planned |

### Phase 06 -- Aerospace Applications (5 docs)

| # | Path | Topic | Status |
|---|------|-------|--------|
| 66 | `06-aerospace/01-continuous-control/01-continuous-control` | High-dimensional action spaces, hierarchical RL, MPC+RL hybrids | planned |
| 67 | `06-aerospace/02-safety/01-safety-and-constraints` | Constrained MDPs, Lagrangian relaxation, CPO, Lyapunov stability, reachability | planned |
| 68 | `06-aerospace/03-partial-observability/01-pomdps` | POMDP formulation, belief states, structural results, approximate methods | planned |
| 69 | `06-aerospace/04-sim-to-real/01-sim-to-real-transfer` | Domain randomization, system identification, progressive nets | planned |
| 70 | `06-aerospace/05-multi-vehicle/01-multi-vehicle-coordination` | Formation control (graph Laplacian), collision avoidance, communication-aware coordination | planned |

## Dependency Tree / Reading Order

The dependency tree shows prerequisites for each document. Arrows (->) indicate "is required by".

```
Phase 00 -- Prerequisites (optional refresher)
  real-analysis -> linear-algebra -> probability -> [Phase 01]

Phase 01 -- Mathematical Foundations (requires: Phase 00 or equivalent background)
  01-measure-spaces -> probability-foundations -> [Phase 02, 03]
  01-metric-and-normed-spaces -> 02-hilbert-spaces-and-operators -> [Phase 02, 04]
  01-convex-analysis -> 02-convex-optimization-and-duality -> 03-stochastic-approximation -> [Phase 02]
  01-static-and-extensive-form-games -> 02-repeated-games-and-incomplete-info -> [Phase 05]

Phase 02 -- Core RL (requires: Phase 01 measure theory + optimization)
  MDP: lesson-39 -> lesson-40 -> lesson-41 -> lesson-42 -> lesson-43 -> lesson-44 -> lesson-45 -> lesson-46
  TD:  lesson-46 -> lesson-47 -> lesson-48 -> lesson-49 -> lesson-50 -> lesson-51 -> lesson-52 -> lesson-53
  PG:  lesson-53 -> lesson-54 -> lesson-55 -> lesson-56 -> lesson-57 -> lesson-58
  lesson-58 -> [Phase 04 policy-based]

Phase 03 -- Deep Learning (requires: Phase 01 measure theory; independent of Phase 02)
  NN Theory: lesson-59 -> lesson-60 -> lesson-61 -> lesson-62 -> lesson-63 -> lesson-64 -> lesson-65 -> lesson-66
  RNN: lesson-67 -> lesson-68 -> lesson-69
  Optimization: 01-sgd-and-adaptive-methods

Phase 04 -- Deep RL (requires: Phase 02 + Phase 03)
  01-dqn-and-extensions -> 02-distributional-rl
  01-trust-region-methods -> 02-proximal-policy-optimization
  03-deterministic-policy-gradient
  04-maximum-entropy-rl

Phase 05 -- MARL (requires: Phase 02 + Phase 01 game theory)
  01-stochastic-game-theory -> {cooperative, competitive, mean-field, communication}

Phase 06 -- Aerospace (requires: Phase 04 + Phase 05)
  {continuous-control, safety, partial-observability, sim-to-real, multi-vehicle}
```

**Inter-phase dependencies summary:**
- **00 -> 01** : Prerequisites review refreshes the background needed for measure theory
- **01 -> 02** : Measure theory and probability needed for RL foundations
- **01 -> 03** : Measure theory and probability needed for deep learning theory
- **02 + 03 -> 04** : Core RL + deep learning combine into deep RL
- **02 + 01/game-theory -> 05** : MARL requires RL theory and game theory
- **04 + 05 -> 06** : Aerospace applications integrate deep RL and multi-agent methods

## Conventions

- Documents are LaTeX-generated PDFs; source `.tex` files may be present for newer documents
- Commit messages reference the primary topic added
- After any modification compile and commit the changes with a meaningful commit message.
- When creating a new document, add it to the Document Catalog in this file and update the corresponding phase `README.md`.
- Only use ASCII characters to write documents.
- After creating the PDF document from tex file, clean the temporal files that were generated.

## Lesson Structure Standard

Lessons follow a structure based on **Gagne's Nine Events of Instruction** (Gagne, Briggs & Wager, *Principles of Instructional Design*, 5th ed., 2005), adapted for graduate-level mathematical writing. Each section maps to one or more of Gagne's events. Learning objectives use **Bloom's Revised Taxonomy** (Anderson & Krathwohl, 2001) action verbs.

### Mapping: Gagne's Events to Lesson Sections

| Gagne Event | Lesson Section | Purpose |
|---|---|---|
| 1. Gain attention | Motivation & Overview (opening problem) | Engage with a concrete RL/ML scenario |
| 2. Inform learners of objectives | Motivation & Overview (learning objectives) | State what the student will be able to do |
| 3. Stimulate recall of prior learning | Motivation & Overview (prerequisites) | Activate knowledge from earlier lessons |
| 4. Present the content | Core Content Sections (2 through N) | Definitions, theorems, proofs |
| 5. Provide learning guidance | Worked examples, `rlconnection`, `keyresult`, `warning` boxes | Connect abstract theory to applications |
| 6. Elicit performance | Exercises | Practice applying new knowledge |
| 7. Provide feedback | Exercise hints (optional) | Guide self-assessment |
| 8. Assess performance | Exercises (graded difficulty) | Evaluate mastery at multiple Bloom levels |
| 9. Enhance retention and transfer | Summary + Further Reading | Consolidate and connect forward |

### LaTeX File Template

```latex
\documentclass[11pt,a4paper]{article}
\input{../../lesson-preamble}   % relative path from subdomain dir
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\textsc{Lesson N: Title}}
\fancyhead[R]{\thepage}
\title{Lesson N: Title}
\author{AI/ML Mathematics}
\date{}
\begin{document}
\maketitle
\tableofcontents
\newpage
% --- Section 1: Motivation and Overview ---
% --- Sections 2..N: Core Content ---
% --- Section N+1: Exercises ---
% --- Section N+2: Summary ---
% --- Section N+3: Further Reading ---
\bibliography{subdomain-refs}
\end{document}
```

### Section Specifications

#### Section 1 -- Motivation and Overview

*Gagne Events 1-3: Gain attention, state objectives, recall prerequisites.*

This section has four subsections written as prose (no `\subsection` commands -- use paragraph breaks or `\paragraph{}`):

1. **Opening problem** (1-2 paragraphs): Present a concrete RL/ML problem or scenario that requires the mathematics developed in this lesson. Do not solve it -- just pose it to create intellectual need. End with a forward pointer: *"The tools developed in this lesson will let us..."*

2. **RL/ML connection box**: An `\begin{rlconnection}` environment listing 2-4 specific algorithms or results that depend on this lesson's material, with one-sentence explanations of how.

3. **Prerequisites**: A `\paragraph{Prerequisites.}` listing the specific definitions, theorems, or lessons the student must know, using textual cross-references (e.g., "Chebyshev's inequality (Lesson 9, Theorem 2.3)").

4. **Learning objectives**: A `\paragraph{Learning objectives.}` with a bulleted list (`\begin{itemize}`) of 3-6 measurable objectives using Bloom's Revised Taxonomy verbs:
   - **Remember/Understand**: *Define*, *State*, *Explain*, *Classify*
   - **Apply/Analyze**: *Compute*, *Derive*, *Prove*, *Compare*
   - **Evaluate/Create**: *Justify*, *Construct*, *Design*, *Critique*

   Each objective should be verifiable (a reader can confirm they achieved it).

#### Section 2 -- References

*Supports Gagne Event 4 (content presentation) with authoritative sources.*

A bulleted list of 3-6 primary references using `\citet{}` with specific chapter/section pointers. Format:

```latex
\begin{itemize}
  \item \citet[Chapter 4]{durrett2019} -- Detailed treatment of conditional expectation.
  \item \citet[Sections 7.1--7.3]{williams1991} -- Martingale convergence theorems.
\end{itemize}
```

#### Sections 3 through N -- Core Content

*Gagne Events 4-5: Present content and provide learning guidance.*

These sections develop the mathematical content. Guidelines:

- **Definitions first**: Every new concept gets a `\begin{definition}` environment before it is used. Never use a term before defining it.
- **Complete proofs**: Every theorem, lemma, and proposition must include a full proof (`\begin{proof}...\end{proof}`). No "see textbook" or "left to the reader" for main results. Minor technical lemmas may defer to exercises.
- **Worked examples**: Include at least 2-3 `\begin{example}` environments per content section showing concrete computations or applications.
- **Key result boxes**: Wrap the 1-3 most important results per lesson in `\begin{keyresult}` environments.
- **RL connection boxes**: Insert `\begin{rlconnection}` at natural connection points (aim for 2-4 per lesson) explaining how the current result applies in RL/ML.
- **Warning boxes**: Use `\begin{warning}` for common misconceptions or subtle pitfalls (0-2 per lesson, only when genuinely needed).
- **Custom box titles**: Override default titles when needed: `\begin{keyresult}[title={Bellman Optimality}]`.
- **Logical flow**: Each section should end with a brief transition sentence pointing to the next section.

#### Section N+1 -- Exercises

*Gagne Events 6-8: Elicit performance, provide feedback, assess mastery.*

Include 4-6 exercises spanning multiple Bloom levels. Format:

```latex
\section{Exercises}

\begin{exercise}[Descriptive Title] \textnormal{(\(*\))} \\
  Statement of the exercise.
\end{exercise}
```

Difficulty scoring (mandatory, placed after the title):
- `(*)` -- Direct application of a single definition or theorem (Bloom: Apply)
- `(**)` -- Requires combining 2-3 results or multi-step reasoning (Bloom: Analyze)
- `(***)` -- Proof construction, generalization, or open-ended exploration (Bloom: Evaluate/Create)

Distribution: aim for 1-2 exercises at each difficulty level. At least one exercise should have an explicit RL/ML application context.

Optional: include `\textit{Hint:}` at the end of harder exercises.

#### Section N+2 -- Summary

*Gagne Event 9 (first part): Enhance retention.*

A concise bulleted list (`\begin{itemize}`) of 5-10 key takeaways. Each item should be a complete, self-contained statement (not just a topic name). Example:

```latex
\begin{itemize}
  \item The Banach fixed-point theorem guarantees a unique fixed point for
        contraction mappings on complete metric spaces, which underpins
        the convergence of value iteration.
\end{itemize}
```

For capstone lessons (last lesson in a subdomain), include a summary table reviewing the full subdomain arc.

#### Section N+3 -- Further Reading

*Gagne Event 9 (second part): Enhance transfer.*

A bulleted list combining:
- **Forward pointers** to upcoming lessons that build on this material (textual, e.g., "Lesson 15 extends these results to...")
- **Deeper references** to advanced textbooks, monographs, or survey papers for students who want to go further
- **Historical notes** (optional) crediting original contributors

### Cross-Lesson Reference Conventions

- Each lesson compiles independently -- no `\ref{}` or `\label{}` across lessons.
- Reference results from other lessons textually: "By the Borel-Cantelli lemma (Lesson 9, Theorem 2.3)..."
- When using a prior result, briefly re-state it without proof and cite the lesson.
- Within a lesson, use standard `\label{}`/`\ref{}` freely.

### Target Length

- Standard lessons: 500-800 lines of LaTeX source
- Capstone or survey lessons: up to 1000 lines
- Each lesson should produce 10-20 pages of PDF output

### Shared Preamble and Bibliography

- All Phase 01 lessons use `\input{../../lesson-preamble}` (path: `01-math-foundations/lesson-preamble.tex`)
- Bibliography files are per-subdomain (e.g., `measure-theory-refs.bib`, `optimization-refs.bib`)
- Use `\citet{}` for textual citations and `\citep{}` for parenthetical citations
- Compile chain: `pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`, then clean temp files

### Available Environments (from `lesson-preamble.tex`)

**Theorem-like** (all share a single counter, numbered by section):
`theorem`, `lemma`, `proposition`, `corollary`, `definition`, `example`, `exercise`, `assumption`, `remark`

**Colored boxes** (tcolorbox, breakable):
- `keyresult` -- green, for central results
- `rlconnection` -- blue, for RL/ML connections
- `warning` -- red, for common mistakes or pitfalls

**Custom commands**: `\R`, `\N`, `\Q`, `\Z`, `\C` (number sets); `\E`, `\Prob`, `\Var`, `\Cov`, `\indicator` (probability); `\cas`, `\cprob`, `\clp{p}`, `\cdist` (convergence); `\dom`, `\epi`, `\conv`, `\argmin`, `\argmax`, `\prox` (operators); `\powerset`, `\Borel` (measure theory)
