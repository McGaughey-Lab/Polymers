# Polymers

This repository contains structure-generation tools and molecular dynamics analysis data for studying the structural and vibrational properties of polymers. The current datasets primarily focus on polypropylene (PP) and polystyrene (PS) with different tacticities and structural configurations.

## Repository Contents

### `STRUCTURES/`

Scripts and example files for constructing polymer structures for LAMMPS molecular dynamics simulations.

The workflow progresses from a polymer chain generated using **RadonPy** to periodic structures of increasing dimensionality:

```text id="fxejm6"
Polymer chain → 1D periodic chain → 2D crystal → 3D bulk structure
```

The initial polymer chain is generated from a SMILES representation with a specified degree of polymerization and tacticity. Subsequent scripts construct the periodic single-chain, crystalline, and bulk simulation structures.

See [`STRUCTURES/README.md`](STRUCTURES/README.md) for the complete structure-generation workflow, required inputs, dependencies, and example commands.

---

### `DIHEDRALS/`

Dihedral-angle distributions obtained from molecular dynamics trajectories of polypropylene and polystyrene with different tacticities.

The available datasets include:

```text id="nvbrgu"
sPP
aPP_0.25
aPP
aPP_0.75

sPS
aPS_0.25
aPS
aPS_0.75
```

The corresponding data files follow the convention:

```text id="gr05b7"
dihedrals_<system>.dat
```

The directory also contains:

* `get_dihedral_distribution.py` — calculates dihedral-angle distributions from trajectory data.
* `plotdihs.py` — plots and compares the resulting distributions.

---
### `VDOS/`

Vibrational density of states (VDOS) data obtained from velocity autocorrelation functions calculated from molecular dynamics trajectories.

The datasets are named according to temperature, system configuration, chain length, and polymer/tacticity:

`vdos_300K_<configuration><chain_length>_<polymer>.dat`

The available configurations include:

* `1c` — single-chain systems
* `2c` — two-chain systems
* `2d` — two-dimensional systems
* `3d` — three-dimensional systems

For syndiotactic polypropylene (`sPP`), VDOS data are provided for chain lengths of 40, 80, and 120 repeat units across the available configurations.

Additional 40-repeat-unit datasets are provided for isotactic polypropylene (`iPP`), syndiotactic polystyrene (`sPS`), and isotactic polystyrene (`iPS`).

Example files include:

* `vdos_300K_1c40_sPP.dat`
* `vdos_300K_1c80_sPP.dat`
* `vdos_300K_1c120_sPP.dat`
* `vdos_300K_2c40_sPP.dat`
* `vdos_300K_2d40_sPP.dat`
* `vdos_300K_3d40_sPP.dat`
* `vdos_300K_1c40_iPP.dat`
* `vdos_300K_1c40_sPS.dat`
* `vdos_300K_1c40_iPS.dat`

The directory also contains:

* `get_vacf.py` — calculates the velocity autocorrelation function and VDOS.
* `compare_vacf.py` — compares VDOS results between different systems.


## Polymer Notation

| Notation | Description                    |
| -------- | ------------------------------ |
| `PP`     | Polypropylene                  |
| `PS`     | Polystyrene                    |
| `s`      | Syndiotactic                   |
| `a`      | Atactic/intermediate tacticity |
| `i`      | Isotactic                      |
| `sc`     | Single chain                   |
| `cryst`  | Crystal                        |

For the dihedral datasets, the tacticity is characterized by the meso-diad probability, (p_m):

| System                 | (p_m) |
| ---------------------- | ----: |
| `sPP`, `sPS`           |     0 |
| `aPP_0.25`, `aPS_0.25` |  0.25 |
| `aPP`, `aPS`           |  0.50 |
| `aPP_0.75`, `aPS_0.75` |  0.75 |
| `iPP`, `iPS`           |     1 |

## Simulation and Analysis

The molecular dynamics simulations associated with these datasets were performed using **LAMMPS**. The included Python scripts provide tools for structure generation and post-processing of molecular dynamics trajectories, including analysis of polymer conformations through dihedral-angle distributions and vibrational properties through velocity autocorrelation functions and VDOS.

