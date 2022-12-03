# PVS-Compact-Model
simple virtual source compact model
# Versions 1.1 (22.12.3)
## Amendments
1. based on matlab programs, we use python to rewrite the programs, so we name the version 1.1
2. we complete the .csv file reading and processing parts
3. we add the TCAD data and PVS data comparation using id-vg and id-vd plots
4. 
## Problems
1. the fit para 'mu'(means mobility), in the optimise process, which would always hit the upper bound we set (based on physics), regardless of the up-bo' value.
2. lack of the iteration program -- to make the source(drain) resistance reasonable
3. we just describe the i-v charactersitic curve, without considering the q-v charactersitic, which is very important in a complete device compact model

## Notes
I will amend the problems soon.