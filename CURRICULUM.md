# Lesson-by-Lesson Curriculum

This curriculum breaks the six-phase learning path into **114 individual lessons**, each
representing a focused study session of roughly 2--3 hours. It is derived from
`curriculum.pdf` and maps every lesson to its corresponding repository document.

**Guiding principle:** Read for *understanding*, not coverage. Work through proofs,
verify claims, solve exercises. A single chapter deeply understood is worth more than
ten chapters skimmed.

**Estimated total duration:** 14--20 months.

**How to read the lesson specifications.** Each lesson lists the document sections to
study, the definitions to learn, and the key results to master. Results in **bold** are
the most important -- you should be able to state and prove these from memory.

---

## Phase 01: Mathematical Foundations (~38 lessons, 4--6 months)

### 1.1 Measure Theory and Probability (Lessons 1--14)

**Primary text:** Durrett, R. *Probability: Theory and Examples* (5th ed., 2019)
**Supplementary:** Billingsley, P. *Probability and Measure* (3rd ed.)

#### Lesson 1: sigma-Algebras and the pi-lambda Theorem

> [lesson-01](01-math-foundations/01-measure-theory/lesson-01-sigma-algebras.pdf)

- **Definitions:** 2.1 sigma-algebra, 3.2 generated sigma-algebra, 3.4 Borel sigma-algebra, 4.1 pi-system, 4.2 lambda-system
- **Key results:** Prop 2.3 basic properties of sigma-algebras, Lem 3.1 intersection of sigma-algebras, Prop 3.5 equivalent generators of Borel(R), Lem 4.4 pi + lambda = sigma, **Thm 4.5 pi-lambda theorem (Dynkin)**, **Cor 5.1 uniqueness of probability measures**
- **Examples:** 2.4 extreme sigma-algebras, 2.5 partition-generated sigma-algebra

#### Lesson 2: Measures and the Caratheodory Extension

> [lesson-02](01-math-foundations/01-measure-theory/lesson-02-measures-caratheodory.pdf)

- **Definitions:** 2.1 measure, 2.4 null set / complete measure, 3.1 algebra of sets, 3.4 pre-measure, 4.1 outer measure, 4.3 Caratheodory measurability
- **Key results:** Thm 2.3 properties of measures (monotonicity, countable subadditivity, continuity), Prop 2.5 completion, Prop 4.2 pre-measure induces outer measure, **Thm 4.5 Caratheodory extension theorem**, Thm 5.1 existence of Lebesgue measure, Thm 6.1 Vitali non-measurable sets

#### Lesson 3: Measurable Functions and Simple Approximation

> [lesson-03](01-math-foundations/01-measure-theory/lesson-03-measurable-functions.pdf)

- **Definitions:** 2.1 measurable function, 5.1 simple function, 6.1 sigma(X)
- **Key results:** Thm 2.3 generator criterion for measurability, Cor 2.4 standard criterion for real-valued measurability, Thm 3.1 closure under algebraic operations, Thm 4.1 closure under pointwise limits, **Thm 5.4 simple function approximation theorem**, **Thm 7.1 Doob--Dynkin lemma**

#### Lesson 4: From Measures to Probability Spaces

> [lesson-04](01-math-foundations/01-measure-theory/lesson-04-probability-spaces.pdf)

- **Definitions:** 2.1 probability space, 3.1 random variable, 4.1 distribution (pushforward measure), 5.1 CDF
- **Key results:** Thm 2.3 basic properties of probability, Thm 2.4 continuity of probability, Prop 5.2 properties of CDF, Prop 5.3 CDF determines distribution, Ex 6.1 probability space for a finite MDP
- **Exercises:** 8.1--8.7 (including Ex 8.7: MDP filtration)

#### Lesson 5: Probability Spaces, Random Variables, and Expectation

> [lesson-05](01-math-foundations/01-measure-theory/lesson-05-random-variables-expectation.pdf)

- **Definitions:** 3.1 conditional probability, 4.5 expectation, 6.1 Bernoulli, 6.3 categorical, 6.5 geometric, 7.1 joint distribution, 7.2 marginal distribution
- **Key results:** Thm 3.3 chain rule, **Thm 3.4 law of total probability**, **Thm 3.5 Bayes' theorem**, **Thm 5.1 linearity of expectation**, Cor 5.2 linearity for finite sums

#### Lesson 6: Conditional Expectation and the Tower Property

> [lesson-06](01-math-foundations/01-measure-theory/lesson-06-conditional-expectation-tower.pdf)

- **Definitions:** 2.1 conditional expectation given an event, 3.1 conditional expectation given a random variable, 3.3 conditional expectation given a sigma-algebra
- **Key results:** Thm 4.1 linearity of conditional expectation, **Thm 4.2 pull-out property**, **Thm 5.1 law of total expectation (tower property)**, Thm 5.3 generalized tower property, Thm 6.1 MDP expectation expansion, **Cor 6.2 Bellman expectation equation**

#### Lesson 7: Variance, Covariance, and Independence

> [lesson-07](01-math-foundations/01-measure-theory/lesson-07-variance-independence.pdf)

- **Definitions:** 2.1 variance, 3.1 covariance, 4.1 conditional variance, 5.1 independent events, 5.3 independent random variables, 7.1 conditional independence of events, 7.2 conditional independence of random variables
- **Key results:** **Thm 2.3 computational formula Var(X) = E[X^2] - (E[X])^2**, **Thm 4.2 law of total variance**, Thm 6.1 E[XY] = E[X]E[Y] for independent RVs, Cor 6.4 Var(X+Y) = Var(X) + Var(Y) for independent RVs
- **Examples:** 5.4 pairwise but not mutual independence

#### Lesson 8: Filtrations and Martingale Difference Sequences

> [lesson-08](01-math-foundations/01-measure-theory/lesson-08-filtrations-martingale-diff.pdf)

- **Definitions:** 2.1 filtration, 3.1 natural filtration of an MDP, 5.1 martingale, 5.5 supermartingale and submartingale, 6.1 martingale difference sequence (MDS)
- **Key results:** Prop 3.3 conditioning on F_t refines conditioning on S_t, Thm 7.1 MDS has zero unconditional mean, **Thm 7.2 MDS partial sums form a martingale**, Thm 7.3 uncorrelated increments of an MDS

#### Lesson 9: Probability Inequalities

> [lesson-09](01-math-foundations/01-measure-theory/lesson-09-probability-inequalities.pdf)

- **Definitions:** 6.1 convex function
- **Key results:** **Thm 2.1 Markov's inequality**, **Thm 2.4 Chebyshev's inequality**, Thm 3.1 Cauchy--Schwarz inequality, Cor 3.2 covariance bound, Lem 4.1 Hoeffding's lemma, **Thm 4.2 Hoeffding's inequality**, **Thm 5.1 Azuma--Hoeffding inequality** (for martingale differences), Lem 6.3 supporting hyperplane, **Thm 6.4 Jensen's inequality**, Thm 6.5 conditional Jensen's inequality

#### Lesson 10: Modes of Convergence and Borel--Cantelli

> [lesson-10](01-math-foundations/01-measure-theory/lesson-10-convergence-borel-cantelli.pdf)

- **Definitions:** 3.1 almost sure convergence, 3.2 convergence in probability, 3.3 L^p convergence, 3.4 convergence in distribution, 3.6 limsup of events
- **Key results:** **Thm 4.1 hierarchy of convergence modes** (a.s. => prob => dist, L^p => prob), Thm 4.2 L^p => prob, Thm 4.3 a.s. => prob, Thm 4.4 prob => dist, Thm 4.5 a.s. and L^p are incomparable, **Thm 5.1 first Borel--Cantelli lemma**, **Thm 5.3 second Borel--Cantelli lemma**, Thm 6.1 BC characterization of a.s. convergence, Cor 6.2 sufficient condition for a.s. convergence

#### Lesson 11: Limit Theorems

> [lesson-11](01-math-foundations/01-measure-theory/lesson-11-limit-theorems.pdf)

- **Key results:** **Thm 3.1 Monotone Convergence Theorem**, Thm 3.3 Fatou's lemma, **Thm 3.5 Dominated Convergence Theorem (Lebesgue)**, Thm 4.1 Weak Law of Large Numbers, **Thm 4.2 Strong Law of Large Numbers (Kolmogorov)**, **Thm 5.1 Central Limit Theorem**

#### Lesson 12: Markov Chains

> [lesson-12](01-math-foundations/01-measure-theory/lesson-12-markov-chains.pdf)

- **Definitions:** 3.1 Markov chain, 3.2 time-homogeneous transition matrix, 4.1 accessibility / communication, 4.3 irreducible chain, 4.4 recurrence / transience, 5.1 stationary distribution, 5.2 aperiodic chain, 5.4 positive recurrence, 6.1 ergodic chain, 7.1 detailed balance / reversibility
- **Key results:** **Thm 3.4 Chapman--Kolmogorov equation**, Thm 4.5 recurrence criterion, Prop 4.6 recurrence is a class property, **Thm 5.5 stationary distribution existence** (for irreducible positive-recurrent chains), **Thm 6.2 ergodic theorem for finite Markov chains**, Prop 7.2 detailed balance implies stationarity

#### Lesson 13: Martingale Convergence Theory

> [lesson-13](01-math-foundations/01-measure-theory/lesson-13-martingale-convergence.pdf)

- **Definitions:** 3.1 submartingale / supermartingale, 5.1 upcrossings
- **Key results:** Prop 4.1 convex functions of martingales are submartingales, Cor 4.2 squared martingale is a submartingale, **Thm 5.3 Doob's upcrossing inequality**, **Thm 6.1 Doob's forward convergence theorem**, **Thm 7.1 Robbins--Siegmund theorem** (essential for SA convergence proofs)

#### Lesson 14: Stochastic Approximation Noise Decomposition

> [lesson-14](01-math-foundations/01-measure-theory/lesson-14-sa-noise-decomposition.pdf)

- **Key results:** **Thm 5.1 TD noise decomposition** (noise in TD update is an MDS), Prop 6.1 Q-learning noise decomposition, Thm 7.1 convergence of TD(0)
- **Review:** Sec 8 summary table of all key results from Lessons 1--14; exercises in Sec 9

### 1.2 Functional Analysis (Lessons 15--22)

**Primary text:** Kreyszig, E. *Introductory Functional Analysis with Applications*
**Alternative:** Conway, J.B. *A Course in Functional Analysis*

#### Lesson 15: Metric Spaces

> [lesson-15](01-math-foundations/02-functional-analysis/lesson-15-metric-spaces.pdf)

- **Definitions:** 2.1 metric space, 2.8 open ball, 2.9 open / closed set, 2.11 interior / closure / boundary, 3.1 convergence, 3.3 Cauchy sequence, 3.5 complete metric space, 3.8 dense subset / separable space
- **Key results:** Prop 2.10 properties of open/closed sets, Prop 2.12 closure characterization, Prop 3.2 uniqueness of limits, Prop 3.4 convergent => Cauchy, Thm 3.6 completeness of R, Thm 3.7 completeness of R^n, **Thm 4.1 completion of a metric space**
- **Examples:** 2.3 Euclidean metric, 2.4 p-metrics on R^n, 2.5 discrete metric, 2.6 C[a,b] with sup norm, 2.7 sequence spaces ell^p

#### Lesson 16: Normed Spaces and Banach Spaces

> [lesson-16](01-math-foundations/02-functional-analysis/lesson-16-normed-banach-spaces.pdf)

- **Definitions:** 1.1 normed space, 3.1 equivalent norms, 4.1 Banach space, 5.1 absolute convergence, 6.1 Schauder basis
- **Key results:** Prop 1.3 norm induces metric, Lem 2.1 Young's inequality, Prop 2.2 Holder's inequality, Prop 2.3 Minkowski's inequality, **Thm 3.3 all norms on R^n are equivalent**, Cor 3.4 every finite-dimensional normed space is complete, Thm 4.2 ell^p is Banach, Thm 4.3 C[a,b] is Banach under sup norm, **Thm 5.3 Banach space characterization via absolute convergence of series**

#### Lesson 17: Bounded Linear Operators and Dual Spaces

> [lesson-17](01-math-foundations/02-functional-analysis/lesson-17-bounded-operators-duals.pdf)

- **Definitions:** 1.1 linear operator, 2.1 bounded linear operator, 4.1 space B(X,Y), 7.1 dual space
- **Key results:** Prop 2.2 equivalent formulations of operator norm, **Thm 3.1 bounded iff continuous**, Thm 4.2 B(X,Y) is a normed space, **Thm 4.4 B(X,Y) is Banach when Y is Banach**, Prop 5.1 all linear operators on finite-dimensional spaces are bounded, Cor 7.2 dual space is always Banach
- **Examples:** 6.1 matrix operators, 6.2 integral operator, 6.3 right shift operator, 7.6 dual of ell^p

#### Lesson 18: Compactness and the Baire Category Theorem

> [lesson-18](01-math-foundations/02-functional-analysis/lesson-18-compactness-baire.pdf)

- **Definitions:** 2.1 compact set, 2.2 sequential compactness, 3.1 totally bounded, 6.1 equicontinuity, 7.1 compact operator, 8.1 nowhere dense, 8.3 first / second category
- **Key results:** Prop 3.2 totally bounded => bounded, **Thm 3.4 compactness equivalence in metric spaces** (compact <=> seq. compact <=> complete + totally bounded), **Cor 4.1 Heine--Borel for R^n**, Lem 5.1 Riesz's lemma, **Thm 5.3 compact unit ball iff finite dimension** (Riesz), **Thm 6.3 Arzela--Ascoli theorem**, **Thm 8.5 Baire Category Theorem**

#### Lesson 19: Inner Product Spaces and Hilbert Spaces

> [lesson-19](01-math-foundations/02-functional-analysis/lesson-19-inner-product-hilbert.pdf)

- **Definitions:** 2.1 inner product, 5.1 Hilbert space, 6.1 orthogonality, 6.4 orthogonal complement
- **Key results:** **Thm 3.1 Cauchy--Schwarz inequality**, Cor 3.2 triangle inequality, Thm 4.1 parallelogram law, Prop 4.4 polarization identity, Prop 5.2 continuity of inner product, **Thm 6.2 Pythagorean theorem**, Prop 6.5 properties of orthogonal complements
- **Examples:** 2.5 Euclidean space R^n, 2.7 sequence space ell^2, 2.8 function space L^2

#### Lesson 20: Projections, Orthonormal Bases, and Riesz Representation

> [lesson-20](01-math-foundations/02-functional-analysis/lesson-20-projections-riesz.pdf)

- **Definitions:** 3.3 orthogonal projection, 4.1 orthonormal set, 4.2 Fourier coefficients, 5.1 orthonormal basis (Hilbert basis)
- **Key results:** **Thm 3.1 best approximation in closed convex sets**, **Thm 3.2 projection theorem** (H = M + M^perp), Prop 3.4 properties of orthogonal projections, Thm 4.3 Gram--Schmidt process, **Thm 4.4 Bessel's inequality**, **Thm 5.2 Parseval's identity and Fourier expansion**, Prop 6.1 separability and orthonormal bases, **Thm 7.1 Riesz representation theorem** (H* isomorphic to H)

#### Lesson 21: Fundamental Theorems of Functional Analysis

> [lesson-21](01-math-foundations/02-functional-analysis/lesson-21-fundamental-theorems.pdf)

- **Definitions:** 3.1 sublinear functional, 6.1 closed graph
- **Key results:** **Thm 3.2 Hahn--Banach theorem** (real case), Cor 3.3 extension of bounded linear functionals, Cor 3.4 norming functional existence, Thm 4.1 Baire Category (review), **Thm 4.2 Uniform Boundedness Principle (Banach--Steinhaus)**, **Thm 5.1 Open Mapping Theorem**, Cor 5.2 Bounded Inverse Theorem, **Thm 6.3 Closed Graph Theorem**

#### Lesson 22: Fixed Point Theorems

> [lesson-22](01-math-foundations/02-functional-analysis/lesson-22-fixed-point-theorems.pdf)

- **Definitions:** 3.1 contraction, 5.1 compact operator, 6.1 set-valued map / correspondence, 6.2 upper hemicontinuity
- **Key results:** **Thm 3.3 Banach Contraction Mapping Theorem** (value iteration convergence), **Thm 4.1 Brouwer Fixed Point Theorem**, **Thm 5.3 Schauder Fixed Point Theorem**, **Thm 6.4 Kakutani Fixed Point Theorem** (Nash equilibrium existence)
- **Exercises:** 8.1--8.7 (including Ex 8.1: Bellman operator is a contraction)

### 1.3 Optimization Theory (Lessons 23--32)

**Stage 1:** Boyd, S. & Vandenberghe, L. *Convex Optimization* (free online)
**Stage 2:** Nesterov, Y. *Introductory Lectures on Convex Optimization* (2004)
**Stage 3:** Borkar, V.S. *Stochastic Approximation: A Dynamical Systems Viewpoint* (2008)

#### Lesson 23: Convex Sets

> [lesson-23](01-math-foundations/03-optimization/lesson-23-convex-sets.pdf)

- **Definitions:** 2.2 affine set, 2.4 convex set, 2.6 convex combination / convex hull, 2.8 cone
- **Key results:** Prop 2.7 convex hull is smallest convex superset, Prop 4.1 intersection preserves convexity, Prop 4.3 affine image/preimage preserves convexity, Prop 4.5 perspective function preserves convexity, **Thm 5.1 separating hyperplane theorem**, **Thm 5.2 supporting hyperplane theorem**
- **Examples:** 3.1 hyperplanes / halfspaces, 3.2 balls / ellipsoids, 3.3 polyhedra, 3.4 positive semidefinite cone

#### Lesson 24: Convex Functions, Conjugates, and Quasiconvexity

> [lesson-24](01-math-foundations/03-optimization/lesson-24-convex-functions-conjugates.pdf)

- **Definitions:** 2.1 convex function, 2.2 epigraph, 6.1 Fenchel conjugate, 7.1 sublevel set, 7.3 quasiconvex function, 7.5 log-concave / log-convex function
- **Key results:** Prop 2.3 epigraph characterization (f convex <=> epi(f) convex), Prop 2.4 line restriction, **Thm 3.1 first-order condition for convexity**, Thm 3.2 second-order condition, **Thm 4.1 Jensen's inequality**, Prop 5.1--5.6 operations preserving convexity (sums, affine composition, pointwise max/sup, scalar composition, partial minimization, perspective), Prop 6.2 conjugate is always convex, **Thm 6.4 Fenchel's inequality**, **Thm 6.5 biconjugate theorem**
- **Exercises:** 8.1--8.8

#### Lesson 25: Convex Optimization Problems

> [lesson-25](01-math-foundations/03-optimization/lesson-25-convex-optimization-problems.pdf)

- **Definitions:** 2.1 convex optimization problem (standard form), 2.3 feasible set / optimal value, 4.1 LP, 5.1 QP, 6.2 SOCP, 7.2 SDP
- **Key results:** **Thm 3.1 local optimality implies global optimality** for convex problems, Thm 8.1 inclusion hierarchy LP < QP < SOCP < SDP

#### Lesson 26: Lagrangian Duality and KKT Conditions

> [lesson-26](01-math-foundations/03-optimization/lesson-26-lagrangian-duality-kkt.pdf)

- **Definitions:** 2.1 Lagrangian, 2.3 Lagrange dual function, 3.1 dual problem, 4.1 strong duality, 4.2 Slater's condition, 5.1 KKT conditions
- **Key results:** Prop 2.4 dual function is concave, **Thm 3.2 weak duality**, **Thm 4.4 Slater's condition implies strong duality**, **Thm 5.3 KKT necessary conditions** (under strong duality), **Thm 5.4 KKT sufficient conditions** (for convex problems)

#### Lesson 27: Gradient Descent and Convergence Rates

> [lesson-27](01-math-foundations/03-optimization/lesson-27-gradient-descent.pdf)

- **Definitions:** 2.1 L-smoothness, 6.1 mu-strong convexity
- **Key results:** **Thm 3.1 descent lemma** (quadratic upper bound), **Thm 5.1 O(1/k) convergence for convex L-smooth functions**, **Thm 7.1 linear convergence for mu-strongly convex L-smooth functions** (rate (kappa-1)/(kappa+1))

#### Lesson 28: Nesterov Acceleration

> [lesson-28](01-math-foundations/03-optimization/lesson-28-nesterov-acceleration.pdf)

- **Definitions:** 4.1 Nesterov's accelerated gradient method (momentum iteration)
- **Key results:** Thm 3.1 Nesterov's lower bound for smooth convex optimization, **Thm 6.2 O(1/k^2) convergence of Nesterov's method**, Thm 7.2 accelerated linear convergence for strongly convex functions

#### Lesson 29: Proximal Methods

> [lesson-29](01-math-foundations/03-optimization/lesson-29-proximal-methods.pdf)

- **Definitions:** 3.1 proximal operator, 5.1 proximal gradient method, 7.1 FISTA
- **Key results:** Prop 3.2 proximal operator is well-defined, **Thm 6.2 convergence of proximal gradient method**, **Thm 7.3 FISTA O(1/k^2) convergence**
- **Examples:** 4.1 soft thresholding (l1 proximal), 4.2 projection onto constraint set

#### Lesson 30: Interior-Point Methods

> [lesson-30](01-math-foundations/03-optimization/lesson-30-interior-point-methods.pdf)

- **Definitions:** 3.2 logarithmic barrier, 4.3 central path, 5.1 barrier method
- **Key results:** Prop 3.4 barrier is convex, **Thm 4.5 central path optimality bound**, **Thm 6.5 O(sqrt(m) log(1/epsilon)) complexity of barrier method**
- **Exercises:** 9.1--9.8 (including Ex 9.6: duality gap in constrained MDP)

#### Lesson 31: Robbins--Monro and the ODE Method

> [lesson-31](01-math-foundations/03-optimization/lesson-31-robbins-monro-ode.pdf)

- **Definitions:** 3.1 step-size sequence (Robbins--Monro conditions), 3.3 Robbins--Monro iteration, 3.4 standing assumptions, 4.1 associated ODE, 4.2 interpolated trajectory, 4.3 ODE method assumptions, 5.1 Borkar--Meyn assumptions
- **Key results:** Thm 3.6 Robbins--Siegmund, **Thm 3.7 Robbins--Monro convergence**, Lem 4.5 noise term vanishes asymptotically, **Thm 4.6 convergence via the ODE method**, **Thm 5.3 Borkar--Meyn stability theorem**
- **Examples:** 6.1 mean estimation, 6.2 quantile estimation, 6.3 Q-learning update as SA

#### Lesson 32: Convergence Rates, Two-Timescale SA, and RL Applications

> [lesson-32](01-math-foundations/03-optimization/lesson-32-two-timescale-sa.pdf)

- **Definitions:** 4.1 two-timescale SA, 4.3 two-timescale assumptions, 5.1 linear SA
- **Key results:** **Thm 3.3 CLT for stochastic approximation**, **Thm 3.5 Polyak--Ruppert averaging**, **Thm 4.4 two-timescale convergence (Borkar)**, Prop 6.1 lock-in to attractors, Thm 5.2 convergence of linear SA, Cor 5.3 automatic stability for linear SA, Thm 5.4 complete convergence for linear SA
- **RL connections:** Sec 7 -- TD(0) as SA, Q-learning as asynchronous SA, REINFORCE as SA on gradient ascent ODE, actor-critic as two-timescale SA
- **Exercises:** 8.1--8.7 (including Ex 8.5: deadly triad, Ex 8.6: GTD2)

### 1.4 Game Theory (Lessons 33--38)

**Primary text:** Fudenberg, D. & Tirole, J. *Game Theory* (1991)
**Alternative:** Osborne, M.J. & Rubinstein, A. *A Course in Game Theory*

#### Lesson 33: Normal-Form Games and Pure Nash Equilibrium

> [lesson-33](01-math-foundations/04-game-theory/lesson-33-normal-form-games-nash.pdf)

- **Definitions:** 2.1 normal-form game, 2.3 bimatrix game, 3.1 dominance (strict/weak), 3.4 IESDS, 4.1 best response, 4.3 rationalizable strategies, 5.1 pure strategy Nash equilibrium
- **Key results:** Prop 3.3 dominated strategies are never best responses, **Thm 3.7 order independence of IESDS**, Prop 4.5 IESDS and rationalizability coincide in two-player games, Prop 5.2 NE as mutual best response, Prop 6.5 Matching Pennies has no pure NE
- **Examples:** 2.4 Prisoner's Dilemma, 2.5 Battle of the Sexes, 2.6 Matching Pennies, 2.7 Stag Hunt

#### Lesson 34: Mixed Strategies, Nash Existence, and the Minimax Theorem

> [lesson-34](01-math-foundations/04-game-theory/lesson-34-mixed-strategies-minimax.pdf)

- **Definitions:** 1.1 mixed strategy, 1.2 support, 1.3 mixed extension, 1.5 mixed NE, 2.1 upper hemicontinuity, 3.1 zero-sum game, 3.2 maximin / minimax values, 4.1 correlated equilibrium
- **Key results:** **Thm 1.6 indifference principle**, Thm 2.2 Kakutani's FPT (review from Lesson 22), **Thm 2.3 Nash's existence theorem** (every finite game has a mixed NE), Lem 3.3 maximin <= minimax, **Thm 3.4 von Neumann minimax theorem**, Cor 3.5 NE characterization in zero-sum games, Prop 3.6 solving zero-sum games via LP, **Thm 4.2 every NE is a correlated equilibrium**, Prop 4.3 CE as a linear program

#### Lesson 35: Extensive-Form Games and Subgame Perfection

> [lesson-35](01-math-foundations/04-game-theory/lesson-35-extensive-form-spe.pdf)

- **Definitions:** 1.1 extensive-form game, 1.2 perfect information, 1.3 perfect recall, 1.6 pure strategy in extensive form, 1.8 behavioral strategy, 3.2 subgame, 3.4 subgame perfect equilibrium (SPE), 3.7 backward induction
- **Key results:** Prop 1.9 normal-form representation, **Thm 2.1 Kuhn's theorem** (behavioral <=> mixed under perfect recall), Prop 3.5 SPE refines NE, **Thm 3.8 backward induction yields SPE**, **Thm 4.1 Zermelo's theorem** (perfect-information finite games have pure SPE), Cor 4.2 chess has a determined outcome
- **Exercises:** 6.1--6.8

#### Lesson 36: Repeated Games and Folk Theorems

> [lesson-36](01-math-foundations/04-game-theory/lesson-36-repeated-games-folk.pdf)

- **Definitions:** 2.1 finitely repeated game, 2.3 SPE for repeated games, 4.1 infinitely repeated game (discounted), 5.1 feasible payoff set, 5.3 minimax value / individually rational payoffs, 6.2 grim trigger strategy, 7.1 tit-for-tat, 5.5 full dimensionality condition
- **Key results:** **Thm 2.4 unraveling** (unique stage-game NE => unique SPE in finitely repeated game), Prop 3.1 repetition enables new equilibria with multiple stage-game NE, Prop 5.4 NE payoff lower bound, **Thm 8.1 Nash folk theorem**, **Thm 9.1 subgame perfect folk theorem (Fudenberg--Maskin)**
- **Examples:** 6.1 cooperation in repeated Prisoner's Dilemma

#### Lesson 37: Learning in Games and Bayesian Games

> [lesson-37](01-math-foundations/04-game-theory/lesson-37-learning-bayesian-games.pdf)

- **Definitions:** 3.1 fictitious play, 4.1 external regret, 4.2 multiplicative weights update (MWU), 6.1 Bayesian game, 6.3 Bayesian Nash equilibrium (BNE)
- **Key results:** Thm 3.3 FP convergence in 2x2 zero-sum games, **Thm 3.4 Robinson's theorem** (FP converges in all zero-sum games), **Thm 4.4 MWU regret bound** O(sqrt(T log K)), **Thm 5.1 no-regret learning implies NE in zero-sum games**, **Thm 6.5 existence of BNE** (in finite Bayesian games)
- **Examples:** 7.1 Cournot duopoly with unknown costs, 7.2 first-price sealed-bid auction

#### Lesson 38: Signaling, Perfect Bayesian Equilibrium, and Potential Games

> [lesson-38](01-math-foundations/04-game-theory/lesson-38-signaling-potential-games.pdf)

- **Definitions:** 3.1 system of beliefs, 3.2 perfect Bayesian equilibrium (PBE), 4.1 signaling game, 4.2 equilibrium types (separating / pooling / semi-separating), 5.1 exact potential game, 5.2 ordinal potential game, 6.1 best-response dynamics, 7.1 congestion game
- **Key results:** Prop 4.4 PBE existence in finite signaling games, **Thm 5.4 potential games have pure NE**, **Thm 6.2 finite improvement property**, Cor 6.3 better-response dynamics converge, **Thm 7.2 Rosenthal's theorem** (congestion games are exact potential games), Cor 7.3 congestion games have pure NE
- **RL connections:** Sec 9 -- independent learners in repeated games, self-play and fictitious play, opponent modeling as Bayesian inference, potential-based reward shaping
- **Examples:** 4.3 Spence's job market signaling, 7.5 network routing, 7.6 resource allocation
- **Exercises:** 9.1--9.7

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
