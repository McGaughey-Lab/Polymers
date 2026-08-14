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

The directory contains VDOS data for **single-chain (`sc`)** and **crystalline (`cryst`)** polypropylene and polystyrene systems at 300 K, including:

```text id="czj2kz"
vdos_300K_sc_sPP.dat
vdos_300K_sc_iPP.dat
vdos_300K_sc_sPS.dat
vdos_300K_sc_iPS.dat

vdos_300K_cryst_sPP.dat
vdos_300K_cryst_iPP.dat
vdos_300K_cryst_sPS.dat
vdos_300K_cryst_iPS.dat
```

Additional VDOS datasets corresponding to different system sizes and dimensionalities are also provided.

The directory contains:

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

