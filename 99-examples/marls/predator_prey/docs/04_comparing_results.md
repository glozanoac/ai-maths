# Comparing Results

## What to Look For

### Training Curves

1. **Capture Rate**: The primary metric. Plot the rolling average (window=100) of whether the prey was captured each episode.
   - Random: ~5-15% (flat)
   - IQL: Rises to 40-70%, may plateau or oscillate
   - VDN: Rises to 60-90%, typically more stable

2. **Episode Length**: Shorter episodes generally mean faster captures.
   - Random: ~90-100 (mostly timeouts)
   - IQL: Decreases as agents learn to chase
   - VDN: Decreases further, especially for cooperative captures

3. **Cooperative Capture Rate**: Fraction of captures where both predators are adjacent to the prey.
   - Random/IQL: Low (accidental coordination only)
   - VDN: Should be noticeably higher (learned coordination)

### Key Differences

**Why VDN > IQL:**
- VDN agents learn complementary roles (e.g., one blocks escape while other chases)
- IQL agents both chase greedily, often approaching from the same direction
- The cooperative reward bonus (+25 vs +10) in VDN incentivizes surrounding

**Why IQL > Random:**
- IQL agents learn to move toward the prey (basic chasing)
- Random agents waste steps moving in unhelpful directions

## Running the Comparison

```bash
# Train all agents
pythontrain_random.py
pythontrain_iql.py
pythontrain_vdn.py

# Run evaluation
pythonevaluate.py

# Watch them play
pythonvisualize.py --agent random
pythonvisualize.py --agent iql
pythonvisualize.py --agent vdn
```

## Interpreting the Numbers

Don't expect exact numbers to match — RL training has high variance. Focus on:
- **Relative ordering**: VDN > IQL > Random for capture rate
- **Trends**: Curves should generally improve over training
- **Cooperative captures**: VDN should show meaningfully more

If IQL and VDN perform similarly, try:
- Increasing training episodes
- Adjusting the cooperative bonus magnitude
- Making the grid larger (coordination matters more in bigger spaces)
