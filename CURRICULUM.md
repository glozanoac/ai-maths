# Lesson-by-Lesson Curriculum

This curriculum breaks the seven-phase learning path into **126 individual lessons**, each
representing a focused study session of roughly 2--3 hours. It is derived from
`curriculum.pdf` and maps every lesson to its corresponding repository document.

**Guiding principle:** Read for *understanding*, not coverage. Work through proofs,
verify claims, solve exercises. A single chapter deeply understood is worth more than
ten chapters skimmed.

**Estimated total duration:** 15--22 months.

**How to read the lesson specifications.** Each lesson lists the document sections to
study, the definitions to learn, and the key results to master. Results in **bold** are
the most important -- you should be able to state and prove these from memory.

---

## Phase 00: Prerequisites Review (12 lessons, 1--2 months)

### 0.1 Real Analysis (Lessons 1--4)

**Primary text:** Rudin, W. *Principles of Mathematical Analysis* (3rd ed., 1976)
**Supplementary:** Abbott, S. *Understanding Analysis* (2nd ed., 2015)

#### Lesson 1: Real Numbers, Sequences, and Series

> [lesson-01](00-prerequisites/01-real-analysis/lesson-01-real-numbers-sequences-series.pdf)

- **Definitions:** 3.1 ordered field, 3.3 supremum/infimum, 3.7 Archimedean property, 4.1 convergence, 4.6 Cauchy sequence, 5.1 series convergence
- **Key results:** **Thm 3.4 completeness of R**, **Thm 4.4 Monotone Convergence Theorem**, **Thm 4.5 Bolzano-Weierstrass theorem**, Thm 4.8 Cauchy completeness, **Thm 5.3 comparison test**, Thm 5.5 ratio test, Thm 5.6 root test

#### Lesson 2: Topology and Continuity

> [lesson-02](00-prerequisites/01-real-analysis/lesson-02-topology-and-continuity.pdf)

- **Definitions:** 2.1 open/closed sets, 3.1 compact set, 4.1 continuity, 4.6 uniform continuity
- **Key results:** **Thm 3.2 Heine-Borel theorem**, **Thm 3.4 Bolzano-Weierstrass (compact sets)**, **Thm 4.3 Intermediate Value Theorem**, **Thm 4.4 Extreme Value Theorem**, Thm 4.7 uniform continuity on compact sets

#### Lesson 3: Differentiation and Integration

> [lesson-03](00-prerequisites/01-real-analysis/lesson-03-differentiation-and-integration.pdf)

- **Definitions:** 2.1 derivative, 4.1 Riemann integral, 4.3 integrability
- **Key results:** Thm 2.3 chain rule, **Thm 3.1 Mean Value Theorem**, **Thm 3.3 Taylor's theorem**, **Thm 4.5 Fundamental Theorem of Calculus** (parts I and II)

#### Lesson 4: Function Sequences and Metric Spaces (Capstone)

> [lesson-04](00-prerequisites/01-real-analysis/lesson-04-function-sequences-and-metric-spaces.pdf)

- **Definitions:** 2.1 pointwise convergence, 2.2 uniform convergence, 4.1 metric space, 4.5 completeness
- **Key results:** **Thm 2.4 uniform limit of continuous functions is continuous**, Thm 3.1 Weierstrass M-test, **Thm 5.1 Banach fixed-point theorem**
- **Review:** Capstone summary table of Lessons 1--4

### 0.2 Linear Algebra (Lessons 5--8)

**Primary text:** Axler, S. *Linear Algebra Done Right* (3rd ed., 2015)
**Supplementary:** Strang, G. *Introduction to Linear Algebra* (5th ed., 2016)

#### Lesson 5: Vector Spaces and Linear Maps

> [lesson-05](00-prerequisites/02-linear-algebra/lesson-05-vector-spaces-and-linear-maps.pdf)

- **Definitions:** 2.1 vector space, 2.5 subspace, 3.1 linear independence, 3.4 basis, 3.6 dimension, 4.1 linear map, 4.3 null space, 4.4 range
- **Key results:** Thm 3.3 every spanning set contains a basis, **Thm 4.5 Rank-Nullity theorem**, Thm 5.1 matrix representation of linear maps

#### Lesson 6: Determinants and Eigenvalues

> [lesson-06](00-prerequisites/02-linear-algebra/lesson-06-determinants-and-eigenvalues.pdf)

- **Definitions:** 2.1 determinant, 3.1 eigenvalue, 3.2 eigenvector, 3.4 characteristic polynomial, 4.1 diagonalizable matrix
- **Key results:** Thm 2.4 cofactor expansion, Thm 2.6 multiplicativity of determinants, **Thm 4.3 diagonalizability criterion** (n distinct eigenvalues), **Thm 5.1 Cayley-Hamilton theorem**

#### Lesson 7: Inner Products and Spectral Theory

> [lesson-07](00-prerequisites/02-linear-algebra/lesson-07-inner-products-and-spectral-theory.pdf)

- **Definitions:** 2.1 inner product, 3.3 orthogonal projection, 4.1 orthonormal basis
- **Key results:** **Thm 2.3 Cauchy-Schwarz inequality**, Thm 4.2 Gram-Schmidt process, **Thm 5.1 Real Spectral Theorem** (symmetric matrices are orthogonally diagonalizable), Thm 6.1 positive definiteness criteria

#### Lesson 8: SVD, Norms, and Matrix Calculus (Capstone)

> [lesson-08](00-prerequisites/02-linear-algebra/lesson-08-svd-norms-and-matrix-calculus.pdf)

- **Definitions:** 3.1 singular value decomposition, 4.1 matrix norm, 5.1 matrix exponential, 6.1 matrix gradient, 6.3 Jacobian, 6.4 Hessian
- **Key results:** **Thm 3.2 SVD existence**, **Thm 3.4 Eckart-Young theorem** (best low-rank approximation), Thm 5.2 matrix exponential properties, Thm 6.5 chain rule for matrix calculus
- **Review:** Capstone summary table of Lessons 5--8

### 0.3 Probability (Lessons 9--12)

**Primary text:** Ross, S.M. *A First Course in Probability* (10th ed., 2019)
**Supplementary:** Blitzstein, J.K. & Hwang, J. *Introduction to Probability* (2nd ed., 2019)

#### Lesson 9: Probability Spaces and Conditioning

> [lesson-09](00-prerequisites/03-probability/lesson-09-probability-spaces-and-conditioning.pdf)

- **Definitions:** 2.1 sample space, 2.3 sigma-algebra, 2.5 probability measure (Kolmogorov axioms), 3.1 conditional probability, 4.1 independence
- **Key results:** Thm 2.6 inclusion-exclusion, Thm 2.7 continuity of probability, **Thm 3.3 law of total probability**, **Thm 3.4 Bayes' theorem**

#### Lesson 10: Random Variables and Distributions

> [lesson-10](00-prerequisites/03-probability/lesson-10-random-variables-and-distributions.pdf)

- **Definitions:** 2.1 random variable, 2.2 PMF, 2.3 CDF, 3.1 PDF, discrete distributions (Bernoulli, binomial, geometric, Poisson), continuous distributions (uniform, exponential, normal)
- **Key results:** Thm 2.7 Poisson limit theorem, **Thm 3.5 memoryless property of exponential**, Thm 3.8 Gaussian integral evaluation

#### Lesson 11: Expectation, Variance, and Joint Distributions

> [lesson-11](00-prerequisites/03-probability/lesson-11-expectation-variance-joint-distributions.pdf)

- **Definitions:** 2.1 expectation, 3.1 variance, 3.3 covariance, 4.1 joint distribution, 5.1 conditional expectation
- **Key results:** **Thm 2.3 LOTUS**, **Thm 2.4 linearity of expectation**, Thm 3.2 computational formula for variance, **Thm 5.3 law of total expectation (tower property)**, Thm 5.5 law of total variance

#### Lesson 12: Inequalities and Limit Theorems (Capstone)

> [lesson-12](00-prerequisites/03-probability/lesson-12-inequalities-and-limit-theorems.pdf)

- **Definitions:** 2.1 moment-generating function, 5.1 convergence in probability, 5.2 almost sure convergence, 5.3 convergence in distribution
- **Key results:** **Thm 3.1 Markov's inequality**, **Thm 3.3 Chebyshev's inequality**, **Thm 4.1 Hoeffding's inequality**, **Thm 5.4 Weak Law of Large Numbers**, Thm 5.5 Strong Law of Large Numbers, **Thm 5.6 Central Limit Theorem**, Cor 6.2 sample complexity bound
- **Review:** Capstone summary table of Lessons 9--12

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

#### Lesson 39: MDP Model and Policies

> [lesson-39](02-core-rl/01-mdp/lesson-39-mdp-model-and-policies.pdf)

- **Definitions:** 3.1 Markov decision process, 3.2 Markov property, 4.1 history, 4.2 history-dependent policy, 4.3 Markov policy, 4.4 stationary policy, 4.5 deterministic policy, 5.1 discounted return, 5.2 state-value function, 5.3 action-value function, 5.4 advantage function, 7.1 optimal value functions, 7.2 optimal policy
- **Key results:** Prop 5.1 return is well-defined and bounded, Prop 5.5 value-action value relationship, **Thm 6.1 Bellman expectation equation for V^pi**, **Thm 6.2 Bellman expectation equation for Q^pi**, Thm 7.3 existence of deterministic stationary optimal policy
- **Examples:** 3.3 grid world MDP, 4.6 inventory management MDP, 6.3 two-state MDP, 7.4 optimal policy for two-state MDP
- **Exercises:** 39.1--39.5

#### Lesson 40: Finite-Horizon MDPs

> [lesson-40](02-core-rl/01-mdp/lesson-40-finite-horizon-mdp.pdf)

- **Definitions:** 3.1 finite-horizon MDP, 3.2 finite-horizon return, 3.3 time-dependent Markov policy, 3.4 finite-horizon value functions, 5.1 backward induction algorithm
- **Key results:** Thm 4.1 principle of optimality, **Thm 4.2 finite-horizon Bellman optimality equations**, Thm 5.2 existence of deterministic Markov optimal policy, Prop 5.3 complexity of backward induction O(S^2 A T), Thm 7.1 finite-horizon Bellman expectation equations
- **Examples:** 6.1 shortest path on a grid, 6.2 optimal stopping problem (increasing threshold rule)
- **Exercises:** 40.1--40.6

#### Lesson 41: Discounted Reward and Bellman Equations

> [lesson-41](02-core-rl/01-mdp/lesson-41-discounted-reward-bellman-equations.pdf)

- **Definitions:** 4.1 Bellman expectation operator, 5.1 Bellman optimality operator, 6.1 greedy policy, 7.1 policy ordering, 8.1 Bellman optimality operator for Q
- **Key results:** Thm 4.2 T^pi is a gamma-contraction, Thm 4.3 V^pi is the unique fixed point of T^pi, Lem 5.2 max-norm inequality for max operator, Thm 5.3 T* is a gamma-contraction, **Thm 5.4 Bellman optimality equations characterize V***, Thm 6.2 greedy policy w.r.t. V* is optimal, **Thm 7.3 policy improvement theorem**, Prop 8.2 T*_Q is a contraction with fixed point Q*
- **Examples:** 4.4 policy evaluation via iteration, 8.3 solving Bellman optimality equation for two-state MDP, 8.4 gambling problem
- **Exercises:** 41.1--41.5

#### Lesson 42: Contraction and Value Iteration

> [lesson-42](02-core-rl/01-mdp/lesson-42-contraction-and-value-iteration.pdf)

- **Definitions:** 3.1 value iteration, 6.1 Q-value iteration, 7.1 policy iteration, 8.3 shift property of T*
- **Key results:** **Thm 4.1 value iteration converges geometrically**, **Thm 4.2 a priori error bound for VI**, Thm 4.4 a posteriori error bound, **Thm 5.1 approximate policy extraction** (2gamma*epsilon/(1-gamma)-optimality), Prop 6.2 convergence of Q-value iteration, Thm 7.3 finite convergence of policy iteration, Prop 8.1 monotonicity of T*, Prop 8.2 shift property of T*
- **Examples:** 4.3 iteration count for common parameters, 5.3 value iteration on two-state MDP, 7.4 policy iteration on two-state MDP
- **Exercises:** 42.1--42.5

#### Lesson 43: VI Error Bounds and Monotonicity

> [lesson-43](02-core-rl/01-mdp/lesson-43-vi-error-bounds-and-monotonicity.pdf)

- **Definitions:** 3.1 span seminorm, 6.1 greedy policy sequence
- **Key results:** Prop 3.2 properties of the span, **Thm 3.3 span contraction of T***, **Thm 4.1 span-based a posteriori bound**, Thm 5.1 monotone convergence from below, Cor 5.2 standard initialization v^(0)=0, Thm 5.3 monotone convergence from above, **Thm 6.2 eventual policy stability**, Thm 7.1 Bellman residual bound, Cor 7.2 two-sided bound from Bellman residual
- **Examples:** 4.3 span vs. sup-norm stopping, 5.5 monotone VI on three-state MDP, 6.5 early policy convergence
- **Exercises:** 43.1--43.6

#### Lesson 44: Average Reward MDPs

> [lesson-44](02-core-rl/01-mdp/lesson-44-average-reward-mdp.pdf)

- **Definitions:** 3.1 induced Markov chain, 3.2 communication classes, 3.3 chain types (irreducible/unichain/multichain), 4.1 average reward / gain, 4.3 optimal gain, 5.1 bias / relative value function, 6.2 average reward greedy policy, 8.1 relative value iteration, 9.1 Blackwell optimality
- **Key results:** Prop 3.4 stationary distribution for unichain policies, **Thm 4.2 gain of a unichain policy**, **Thm 5.2 gain-bias equations (Poisson equations)**, Thm 6.1 average reward Bellman optimality equations, Thm 6.3 optimality of the greedy policy, **Thm 7.1 discount-to-average limit**, Thm 8.2 convergence of relative value iteration, **Thm 9.2 Blackwell's theorem**
- **Examples:** 3.4 unichain vs. multichain, 4.4 average reward of a simple MDP, 5.4 computing gain and bias, 7.2 discounted to average reward, 8.3 relative value iteration, 9.4 Blackwell optimality in a two-action MDP
- **Exercises:** 44.1--44.6

#### Lesson 45: Policy Iteration

> [lesson-45](02-core-rl/01-mdp/lesson-45-policy-iteration.pdf)

- **Definitions:** 3.1 policy evaluation problem, 5.1 policy iteration, 7.1 modified policy iteration, 8.1 iteration complexity
- **Key results:** Thm 3.2 policy evaluation via matrix inversion, **Thm 4.1 policy improvement theorem**, Prop 4.3 algebraic proof of policy improvement, **Thm 6.1 finite convergence of policy iteration** (at most A^S iterations), Thm 6.2 strict monotonicity of value sequence, **Thm 6.3 Howard's improvement principle**, Prop 7.2 extremes of modified PI, Thm 7.3 convergence of modified policy iteration, Prop 8.2 VI iteration complexity, Prop 8.3 PI iteration complexity
- **Examples:** 3.5 policy evaluation on three-state MDP, 4.4 policy improvement step, 6.5 complete policy iteration trace, 8.5 computational comparison
- **Exercises:** 45.1--45.6

#### Lesson 46: LP Formulation and Occupancy Measures

> [lesson-46](02-core-rl/01-mdp/lesson-46-lp-formulation-and-occupancy.pdf)

- **Definitions:** 3.1 Bellman feasibility (superharmonic), 3.3 primal LP for discounted MDPs, 4.2 occupancy measure, 5.1 occupancy polytope, 7.1 feature expectations, 8.1 constrained MDP
- **Key results:** Lem 3.2 V* is the smallest Bellman superharmonic vector, **Thm 3.4 primal LP solves the MDP**, Thm 4.1 dual LP for discounted MDPs, Prop 4.3 occupancy measures as dual feasible points, Prop 4.4 dual objective equals policy value, **Thm 5.1 characterization of the occupancy polytope**, Prop 5.3 deterministic policies are vertices, **Thm 6.1 strong duality for the MDP LP**, **Thm 7.2 LP formulation of CMDPs**, Prop 8.2 linear reward and feature expectations
- **Examples:** 3.6 primal LP for two-state MDP, 5.4 occupancy measures for two-state MDP, 7.4 constrained two-state MDP, 8.4 feature matching in IRL
- **Exercises:** 46.1--46.6
- **Review:** Sec 10 summary table of all key results from Lessons 39--46

### 2.2 Reinforcement Learning Algorithms (Lessons 47--53)

**For intuition:** Sutton, R.S. & Barto, A.G. *Reinforcement Learning* (2nd ed., 2018, free online)
**For rigor:** Bertsekas, D.P. & Tsitsiklis, J.N. *Neuro-Dynamic Programming* (1996)

#### Lesson 47: TD(0) and n-Step TD

> [lesson-47](02-core-rl/02-rl-algorithms/lesson-47-td0-and-nstep-td.pdf)

- **Definitions:** 3.1 Monte Carlo update, 4.1 TD error, 4.2 TD(0) update rule, 4.3 TD(0) convergence conditions (assumption), 6.1 n-step return, 6.2 n-step TD update
- **Key results:** Prop 3.1 convergence of MC prediction, Lem 3.2 variance of MC return, Lem 4.1 unbiasedness of TD error (martingale difference), **Lem 4.2 return as telescoping sum of TD errors**, **Thm 4.3 convergence of TD(0)**, Prop 5.1 bias of TD(0) target, Prop 5.2 variance reduction by TD(0), Lem 6.1 n-step return as telescoping sum, Thm 6.2 convergence of n-step TD
- **Examples:** 4.1 two-state MDP, 5.1 variance comparison (chain with gamma=0.99), 6.1 n-step returns in a chain, 6.2 contraction rate vs variance
- **Exercises:** 47.1--47.6

#### Lesson 48: TD(lambda) and Eligibility Traces

> [lesson-48](02-core-rl/02-rl-algorithms/lesson-48-td-lambda-eligibility-traces.pdf)

- **Definitions:** 3.1 lambda-return, 5.1 accumulating eligibility trace, 5.2 TD(lambda) backward view update, 7.1 replacing traces, 7.2 Dutch traces
- **Key results:** Prop 3.1 special cases of the lambda-return, **Thm 4.1 lambda-return decomposition**, Lem 5.1 explicit form of eligibility trace, **Thm 6.1 forward-backward equivalence**, Cor 7.1 convergence of TD(lambda)
- **Examples:** 3.1 lambda-return interpolation, 4.1 finite episode decomposition, 5.1 trace evolution, 6.1 forward-backward equivalence verification
- **Exercises:** 48.1--48.6

#### Lesson 49: SARSA -- On-Policy TD Control

> [lesson-49](02-core-rl/02-rl-algorithms/lesson-49-sarsa.pdf)

- **Definitions:** 3.1 generalized policy iteration (GPI), 3.2 action-value Bellman expectation operator, 3.3 Bellman optimality operator on Q-values, 4.1 epsilon-greedy policy, 4.2 GLIE condition, 5.1 SARSA update rule, 6.1 SARSA convergence conditions (assumption)
- **Key results:** Lem 3.1 contraction of action-value Bellman operators, Prop 4.1 epsilon-greedy policy improvement, **Thm 6.1 convergence of SARSA**, Prop 7.1 SARSA with fixed epsilon converges to Q^{pi_epsilon}
- **Examples:** 4.1 standard GLIE schedule, 5.1 SARSA updates on a grid, 6.1 verifying the perturbation bound, 7.1 on-policy vs off-policy in a stochastic grid
- **Exercises:** 49.1--49.6

#### Lesson 50: Q-Learning and the Unified View of TD Control

> [lesson-50](02-core-rl/02-rl-algorithms/lesson-50-q-learning.pdf)

- **Definitions:** 3.1 Q-learning update rule, 5.1 Double Q-learning, 6.1 Expected SARSA update rule
- **Key results:** **Thm 4.1 convergence of Q-learning**, Prop 5.1 maximization bias, Prop 5.2 Double Q-learning removes maximization bias, **Prop 6.1 Expected SARSA has lower variance than SARSA**, Thm 6.2 convergence of Expected SARSA, Prop 7.1 relationships between TD control targets
- **Examples:** 3.1 Q-learning update, 4.1 off-policy data collection, 5.1 maximization bias in a simple MDP, 6.1 variance comparison (SARSA vs Expected SARSA), 7.1 unified view on a two-action MDP, 8.1 algorithm comparison on cliff-walking
- **Exercises:** 50.1--50.6

#### Lesson 51: Function Approximation in TD Learning

> [lesson-51](02-core-rl/02-rl-algorithms/lesson-51-function-approximation.pdf)

- **Definitions:** 3.1 feature vector and feature matrix, 3.2 linear value function approximation, 3.3 full column rank assumption, 4.1 stationary distribution, 4.2 mean squared value error (MSVE), 4.3 projection operator, 5.1 semi-gradient TD(0) update
- **Key results:** Prop 4.1 properties of the projection operator (Pythagorean theorem), Lem 5.1 expected semi-gradient TD(0) update, Lem 6.1 contraction of P_pi in d^pi-norm, Thm 6.1 negative definiteness of A, **Thm 6.2 convergence of semi-gradient TD(0) with linear FA**, **Thm 7.1 TD(lambda) error bound with factor (1-gamma*lambda)/(1-gamma)**
- **Examples:** 3.1 tabular features, 3.2 polynomial features on a grid, 4.1 projection in two-state case, 6.1 error bound for gamma=0.99, 7.1 comparing bounds for different lambda
- **Exercises:** 51.1--51.6

#### Lesson 52: Approximate Policy Iteration

> [lesson-52](02-core-rl/02-rl-algorithms/lesson-52-approximate-policy-iteration.pdf)

- **Definitions:** 3.1 policy iteration, 4.1 approximate policy evaluation, 4.2 approximate policy improvement, 4.3 approximate policy iteration, 6.1 LSTD algorithm, 7.1 LSTDQ (LSTD for action values), 7.2 LSPI algorithm, 8.1 fitted value iteration (FVI)
- **Key results:** Prop 3.1 monotone improvement and convergence of exact PI, Lem 5.1 one-step error bound, **Thm 5.1 error propagation bound for approximate PI: O(epsilon/(1-gamma)^2)**, Cor 5.1 required accuracy for epsilon-optimality, Thm 6.1 consistency of LSTD, Prop 7.1 LSPI as approximate PI, Prop 8.1 FVI error bound epsilon/(1-gamma)
- **Examples:** 5.1 accuracy requirement for long horizons, 6.1 LSTD on a small MDP, 7.1 LSPI for cart-pole
- **Exercises:** 52.1--52.5

#### Lesson 53: The Deadly Triad and Gradient-TD Methods

> [lesson-53](02-core-rl/02-rl-algorithms/lesson-53-deadly-triad.pdf)

- **Definitions:** 3.1 the deadly triad, 4.1 Baird's star MDP, 4.2 feature representation for Baird's MDP, 6.1 mean squared projected Bellman error (MSPBE), 6.2 GTD2 update rules, 7.1 GTD2 convergence conditions (assumption)
- **Key results:** **Thm 3.1 safety of pairs (any two triad elements are safe)**, Lem 4.1 off-policy matrix for Baird's MDP, **Thm 4.1 divergence of semi-gradient TD(0) on Baird's MDP**, Prop 5.1 removing FA restores convergence, Prop 5.2 removing bootstrapping restores convergence, Prop 5.3 removing off-policy restores convergence, Prop 6.1 quadratic form of MSPBE, **Thm 7.1 convergence of GTD2**, Prop 8.1 target networks stabilize semi-gradient TD
- **Examples:** 4.1 feature vectors explicitly, 4.2 numerical divergence trace, 7.1 GTD2 on Baird's MDP
- **Exercises:** 53.1--53.5
- **Review:** Sec 10 subdomain summary table reviewing Lessons 47--53 arc (tabular prediction to control, FA, deadly triad)

### 2.3 Policy Gradient Theory (Lessons 54--58)

**Primary sources:** Sutton et al. (2000), Kakade (2002), Schulman et al. (2015, 2017)

#### Lesson 54: Policy Gradient Theorem

> [lesson-54](02-core-rl/03-policy-gradient/lesson-54-policy-gradient-theorem.pdf)

- **Definitions:** 3.1 parameterized policy, 3.2 performance objective (start-state), 3.3 discounted state visitation distribution, 3.5 average-reward objective, 6.1 differential value function, 8.1 compatible features
- **Key results:** Lem 4.1 score function identity, Lem 4.2 score function has zero mean, **Thm 5.1 policy gradient theorem (episodic)**, Thm 6.3 policy gradient theorem (average-reward), Prop 7.1 baseline invariance, **Thm 8.2 compatible function approximation**
- **Examples:** 3.6 softmax policy, 3.7 Gaussian policy, 4.3 score function for softmax policy, 4.4 score function for Gaussian policy
- **Exercises:** 54.1--54.5

#### Lesson 55: REINFORCE and Baselines

> [lesson-55](02-core-rl/03-policy-gradient/lesson-55-reinforce-and-baselines.pdf)

- **Definitions:** 3.1 trajectory and return, 4.1 baseline, 4.3 advantage function, 5.1 per-step gradient estimator, 6.1 REINFORCE update rule, 6.2 REINFORCE with baseline update rule
- **Key results:** Lem 3.2 return as unbiased estimate of Q, **Thm 3.3 unbiasedness of REINFORCE**, Prop 4.2 unbiasedness with baseline, Prop 4.5 policy gradient via advantages, Lem 5.3 variance decomposition, **Thm 5.4 optimal baseline (scalar case)**, **Thm 5.5 optimal baseline (total variance)**, **Thm 7.3 convergence of REINFORCE**
- **Examples:** 3.6 REINFORCE on a single-state bandit, 5.7 optimal baseline for a bandit, 8.1 two-state MDP
- **Exercises:** 55.1--55.6

#### Lesson 56: Natural Policy Gradient

> [lesson-56](02-core-rl/03-policy-gradient/lesson-56-natural-policy-gradient.pdf)

- **Definitions:** 3.1 reparameterization, 4.1 Fisher information matrix, 5.1 steepest ascent under a metric, 8.1 natural policy gradient algorithm
- **Key results:** Prop 3.2 non-covariance of the vanilla gradient, Prop 4.2 properties of the Fisher information matrix, **Thm 4.3 Fisher information as KL Hessian**, **Thm 5.2 natural gradient**, **Thm 6.1 covariance under reparameterization**, **Thm 7.1 natural gradient via compatible features**, Thm 9.1 policy improvement under natural gradient
- **Examples:** 3.3 scaling reparameterization, 4.4 Fisher information for softmax policy, 4.5 Fisher information for Gaussian policy, 6.2 covariance verification for scaling, 7.3 natural gradient for Gaussian policy, 10.1 comparing vanilla and natural gradients
- **Exercises:** 56.1--56.5

#### Lesson 57: Actor-Critic and Generalized Advantage Estimation

> [lesson-57](02-core-rl/03-policy-gradient/lesson-57-actor-critic-and-gae.pdf)

- **Definitions:** 3.1 actor-critic components, 3.2 one-step actor-critic update, 4.1 temporal difference error, 5.1 n-step advantage estimator, 6.1 generalized advantage estimation (GAE), 8.1 GAE policy gradient estimator
- **Key results:** **Thm 4.2 TD error as unbiased advantage estimate**, Prop 4.4 bias from value function approximation, Prop 5.2 n-step estimator via TD errors, Thm 5.3 bias-variance of n-step estimators, **Thm 6.2 GAE as discounted sum of TD errors**, **Thm 7.1 bias of GAE**, Cor 7.2 unbiasedness at lambda=1, **Thm 7.3 variance of GAE**, Prop 8.2 bias of GAE policy gradient, **Thm 9.2 two-timescale convergence**
- **Examples:** 5.4 comparing 1-step and infinity-step, 8.3 GAE computation on a simple trajectory, 10.1 effect of lambda on credit assignment
- **Exercises:** 57.1--57.5

#### Lesson 58: Policy Gradient Synthesis

> [lesson-58](02-core-rl/03-policy-gradient/lesson-58-policy-gradient-synthesis.pdf)

- **Definitions:** 3.1 general policy gradient signal, 3.2 signal choices, 4.1 variance of a policy gradient estimator, 5.1 convergence rate classes, 6.4 surrogate objective, 7.1 entropy-regularized objective, 7.2 soft value functions
- **Key results:** **Thm 3.3 unbiasedness of signal choices**, Prop 3.4 bias of approximate signals, **Thm 4.2 variance ordering of signal choices**, **Thm 5.2 convergence rate of vanilla policy gradient**, **Thm 5.3 convergence rate of natural policy gradient**, Thm 5.4 local vs. global optimality, **Thm 6.1 performance difference lemma**, **Thm 6.5 conservative policy improvement bound**, **Thm 7.3 soft policy gradient theorem**
- **Examples:** 4.3 combining all variance reduction techniques
- **Exercises:** 58.1--58.6
- **Review:** Sec 10 Phase 02 grand summary table reviewing all 20 lessons across the three subdomains

---

## Phase 03: Deep Learning Foundations (~14 lessons, 2--3 months)

### 3.1 Neural Network Theory (Lessons 59--66)

**Primary text:** Bach, F. *Learning Theory from First Principles* (2024, free online)
**Supplementary:** Pinkus, A. *Approximation Theory of the MLP Model* (1999, Acta Numerica)

#### Lesson 59: Empirical Risk Minimization and Generalization

> [lesson-59](03-deep-learning/01-neural-networks/lesson-59-erm-and-generalization.pdf)

- **Definitions:** 3.1 Supervised Learning Setup, 3.2 Population Risk and Empirical Risk, 3.4 Bayes Risk and Best-in-Class Risk, 3.5 Empirical Risk Minimizer, 3.6 Excess Risk Decomposition, 5.1 Restriction and Shattering, 5.2 Growth Function, 5.3 VC Dimension, 6.1 Uniform Convergence of Empirical Risk, 6.4 PAC Learnability
- **Key results:** 4.1 Assumption (Bounded Loss), 4.2 Lemma (Pointwise Concentration), **4.3 Thm (Finite Class Generalization Bound)**, **5.7 Thm (Sauer's Lemma)**, **5.10 Thm (VC Bound)**, 6.2 Thm (ERM Generalizes Under Uniform Convergence), **6.5 Thm (Fundamental Theorem of Statistical Learning)**
- **Examples:** 3.7 Linear Classifiers, 3.8 Polynomial Regression, 4.4 Threshold Classifiers, 5.5 VC Dimension of Intervals, 5.6 VC Dimension of Halfspaces, 5.7 VC Dimension of Finite Classes, 5.11 VC Bound for Halfspaces
- **Exercises:** 59.1--59.5

#### Lesson 60: Bias-Variance Tradeoff and Model Selection

> [lesson-60](03-deep-learning/01-neural-networks/lesson-60-bias-variance-and-model-selection.pdf)

- **Definitions:** 3.1 Regression Function and Noise, 3.3 Best-in-Class Function, 4.1 Nested Hypothesis Classes, 4.5 Structural Risk Minimization, 5.1 Penalized Risk Minimization, 5.4 AIC and BIC, 6.1 K-Fold Cross-Validation, 6.2 Leave-One-Out Cross-Validation
- **Key results:** 3.2 Prop (Bayes Risk for Squared Loss), **3.4 Thm (Bias-Variance Decomposition)**, 4.2 Prop (Monotonicity of Approximation and Estimation Errors), **4.3 Thm (Oracle Inequality for ERM)**, **5.2 Thm (Oracle Inequality for Penalized Selection)**, **6.3 Thm (LOOCV Approximately Unbiased)**, 6.6 Prop (K-Fold Bias-Variance Tradeoff)
- **Examples:** 3.6 Polynomial Regression, 3.7 Nearest Neighbor, 4.4 Optimal Polynomial Degree, 5.3 VC-Based Penalty, 5.6 AIC vs BIC for Polynomial Selection, 6.5 LOOCV for Polynomial Selection, 6.7 Selecting Polynomial Degree via 5-Fold CV
- **Exercises:** 60.1--60.5

#### Lesson 61: Kernel Methods

> [lesson-61](03-deep-learning/01-neural-networks/lesson-61-kernel-methods.pdf)

- **Definitions:** 3.1 Feature Map, 3.2 Kernel Function, 4.1 Positive Definite Kernel, 5.1 Assumption (Mercer Setting), 5.2 Integral Operator
- **Key results:** 3.5 Prop (Kernelization Criterion), **4.3 Thm (Inner-Product Kernels are PD)**, **4.4 Thm (Closure Properties of PD Kernels)**, 5.3 Lemma (Properties of Integral Operator), **5.4 Thm (Mercer's Theorem)**, 6.2 Prop (General Polynomial Kernel), **6.3 Thm (Positive Definiteness of Gaussian Kernel)**, 6.5 Prop (Laplacian Kernel), 6.6 Prop (Additional Closure Operations)
- **Examples:** 3.3 Polynomial Kernel, 3.4 Kernelized Ridge Regression, 4.5 Linear Kernel, 4.6 Polynomial Kernel (PD), 4.7 Gaussian RBF Kernel, 5.5 Eigenexpansion of Gaussian on [0,1], 6.1 Bag-of-Words Kernel, 6.7 Constructing Kernels by Composition
- **Exercises:** 61.1--61.6

#### Lesson 62: RKHS and the Representer Theorem

> [lesson-62](03-deep-learning/01-neural-networks/lesson-62-rkhs-and-representer-theorem.pdf)

- **Definitions:** 3.1 Reproducing Kernel Hilbert Space, 3.3 Reproducing Kernel, 6.1 Kernel Ridge Regression, 6.5 Excess Risk
- **Key results:** **3.5 Thm (RKHS Construction / Aronszajn's Theorem)**, **4.1 Thm (Pointwise Bound)**, 4.3 Corollary (Uniform Pointwise Bound), 4.4 Prop (RKHS Convergence Implies Pointwise), 4.5 Thm (RKHS Inclusion), **4.6 Thm (Mercer Characterization)**, **5.1 Thm (Representer Theorem)**, **6.2 Thm (KRR Solution)**, 6.4 Assumption (Statistical Setting), **6.6 Thm (Excess Risk Bound for KRR)**, 6.7 Corollary (Optimal Regularization)
- **Examples:** 3.6 RKHS of the Linear Kernel, 3.7 RKHS of the Polynomial Kernel, 4.7 RKHS of the Gaussian Kernel, 5.2 Representer Theorem for Squared Loss, 5.3 Representer Theorem for SVM, 6.3 KRR with the Gaussian Kernel, 6.8 KRR with Sobolev Kernel
- **Exercises:** 62.1--62.6

#### Lesson 63: Universal Approximation

> [lesson-63](03-deep-learning/01-neural-networks/lesson-63-universal-approximation.pdf)

- **Definitions:** 3.1 Single-Hidden-Layer Network, 3.3 Universal Approximation Property, 4.1 Sigmoidal Function, 4.3 Discriminatory Function, 5.1 Non-Polynomial Activation
- **Key results:** 4.4 Lemma (Sigmoidal Implies Discriminatory), **4.5 Thm (Cybenko, 1989)**, 5.3 Lemma (Non-Polynomial Implies Discriminatory), **5.4 Thm (Hornik, 1989)**, 6.1 Prop (Lower Bound for Generic Functions)
- **Examples:** 3.4 Common Activations, 3.5 Simple Network on [0,1], 4.2 Sigmoidal Functions, 4.6 Approximating a Step Function, 4.7 Constructive Illustration in 1D, 5.5 ReLU Is a Universal Approximator, 5.6 Verification for tanh, 6.2 Dimension Scaling, 6.4 Overfitting with Universal Approximators
- **Exercises:** 63.1--63.6

#### Lesson 64: Barron's Theorem and Approximation Rates

> [lesson-64](03-deep-learning/01-neural-networks/lesson-64-barron-theorem-and-approximation-rates.pdf)

- **Definitions:** 3.1 Fourier Transform, 3.2 Barron Norm, 3.4 Barron Class, 5.5 Variation Norm, 6.1 Integral Representation of Neural Networks
- **Key results:** 4.1 Lemma (Fourier Representation of Barron Functions), 4.3 Prop (Expectation Representation), **4.4 Thm (Barron, 1993)**, 5.1 Prop (Classical Approximation Rates), 5.4 Prop (Sample Complexity for Barron Class), 6.3 Prop (Barron Norm as Total Variation)
- **Examples:** 3.6 Gaussian Function, 3.7 Logistic Function, 3.8 Indicator Functions Not in Barron Class, 4.5 Approximating a Gaussian, 4.6 Linear Combination of Sigmoids, 5.2 Dimension Dependence (Sobolev vs Barron), 6.4 Integral Representation of a Gaussian, 6.5 Integral Representation of a Two-Layer Network
- **Exercises:** 64.1--64.6

#### Lesson 65: Depth-Width Tradeoffs

> [lesson-65](03-deep-learning/01-neural-networks/lesson-65-depth-width-tradeoffs.pdf)

- **Definitions:** 3.1 L-Layer Neural Network, 3.2 Width and Depth, 3.3 Deep Network Function Class, 4.1 Tent Map, 4.3 Sawtooth Function, 5.4 Linear Region, 6.1 Sobolev Space, 6.5 Compositional Function
- **Key results:** 4.2 Lemma (ReLU Representation of Tent Map), 4.4 Lemma (Properties of Sawtooth), 4.6 Prop (Sawtooth as Deep Network), 4.7 Lemma (Linear Pieces of Shallow ReLU Networks), 4.8 Lemma (Oscillation Lower Bound), **4.9 Thm (Telgarsky Depth Separation)**, **5.1 Thm (Lu et al. Width Sufficiency)**, **5.2 Thm (Hanin Minimal Width)**, **5.5 Thm (Linear Region Bounds)**, 6.2 Prop (Classical Minimax Rates), **6.3 Thm (Yarotsky, 2017)**, **6.6 Thm (Depth Advantage for Compositional Functions)**
- **Examples:** 3.4 Parameter Count (Shallow vs Deep), 4.5 Sawtooth Functions for Small L, 4.10 Depth-2 vs Depth-20, 4.11 Depth Separation in Higher Dimensions, 5.3 Minimal Width in One Dimension, 5.6 Linear Regions (Depth vs Width), 6.7 Vision-Like Compositional Structure
- **Exercises:** 65.1--65.6

#### Lesson 66: Neural Tangent Kernel and Rademacher Complexity

> [lesson-66](03-deep-learning/01-neural-networks/lesson-66-ntk-and-rademacher-complexity.pdf)

- **Definitions:** 3.1 Rademacher Random Variables, 3.2 Empirical Rademacher Complexity, 3.3 Rademacher Complexity, 5.1 Neural Tangent Kernel
- **Key results:** **3.6 Thm (Rademacher Generalization Bound)**, 4.1 Lemma (Contraction / Ledoux-Talagrand), **4.3 Thm (Bartlett-Foster-Telgarsky Spectrally-Normalized Bound)**, 5.4 Prop (Gradient Descent in Function Space), **5.6 Thm (NTK Convergence at Initialization)**, **5.8 Thm (Lazy Training Regime)**, 6.1 Prop (NTK Generalization via Kernel Theory), 6.4 Prop (NTK Limitations)
- **Examples:** 3.5 Rademacher Complexity of Linear Classifiers, 3.7 Rademacher vs VC for Halfspaces, 4.4 Parameter-Free Bound for a DQN, 5.3 NTK for a Two-Layer Network, 5.7 NTK for Two-Layer ReLU, 6.2 NTK Generalization for Overparameterized Networks
- **Exercises:** 66.1--66.6
- **Review:** Capstone summary table (Lessons 59--66) covering the Neural Network Theory subdomain arc from statistical learning foundations through kernel methods to NTK and Rademacher complexity

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
