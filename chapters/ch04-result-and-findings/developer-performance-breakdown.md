# Developer Performance Breakdown — Provisional Dataset

This supporting table is generated from the `Copy of Tasks` worksheet in the current [Google Sheet](https://docs.google.com/spreadsheets/d/1yh9VRPTxTWhPp7bPHs7_Ne1nrlFQoS504awsWqiZghw/edit), using **strict filters on developer, workflow, and pre-task complexity**. It complements [Chapter 4, Section 4.6.2](./4.6-complexity-and-developer-comparison.md).

The source currently contains **290 tasks across 10 developers** (159 baseline; 131 Trade-Harness). The summary below contains all **60 possible Developer × Complexity × Workflow combinations**; groups with no assigned tasks are displayed with zero task count and unavailable metrics. Rows are a snapshot, **not** automatically synchronized with the Google Sheet.

For each row, Task count represents issues belonging to that specific developer, workflow and complexity. Feature/Enhancement shows the two task-type counts. Lead time is issue-level **mean / median elapsed days**; E2E means the **mean final task-level pass percentage**; defect density is **mean confirmed defects per 1,000 changed production LOC**; token cost is **mean gateway-recorded USD per issue**. A number in square brackets `[n]` is the valid sample size for that metric, which may differ from the Task count. The [CSV breakdown](./developer-performance-breakdown.csv) additionally includes valid sample sizes, means and medians for each relevant metric, changed LOC per million tokens, and test-script correction loops.

Missing E2E and gateway records are not treated as zero. Defect density is undefined for a task with zero changed production LOC. A dash (—) means the subgroup has no usable observation for that metric. Results have not been adjusted for developer ability, business domain, or differences in task allocation; the ten-developer sample is provisional pending final study-design confirmation.

### D01 — 12 tasks (5 baseline / 7 Trade-Harness)

| Complexity | Workflow | Tasks | Feature/Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Defect density mean / KLOC [n] | Token cost mean USD / issue [n] |
|---|---|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 1 | 0/1 | 0.89 / 0.89 | 100.00 [1] | 0.00 [1] | 79.34 [1] |
| Simple | Trade-Harness | 1 | 1/0 | 0.18 / 0.18 | 100.00 [1] | 0.00 [1] | 81.02 [1] |
| Medium | Baseline | 3 | 2/1 | 2.49 / 1.33 | 91.11 [3] | 0.93 [3] | 262.31 [3] |
| Medium | Trade-Harness | 4 | 4/0 | 3.84 / 4.17 | 96.43 [4] | 0.84 [4] | 352.51 [4] |
| Complex | Baseline | 1 | 0/1 | 5.95 / 5.95 | 85.00 [1] | 0.17 [1] | 414.32 [1] |
| Complex | Trade-Harness | 2 | 2/0 | 10.89 / 10.89 | 97.73 [2] | 0.71 [2] | 687.25 [2] |

### D02 — 43 tasks (23 baseline / 20 Trade-Harness)

| Complexity | Workflow | Tasks | Feature/Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Defect density mean / KLOC [n] | Token cost mean USD / issue [n] |
|---|---|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 21 | 13/8 | 1.45 / 0.96 | 91.50 [20] | 0.78 [21] | 64.35 [21] |
| Simple | Trade-Harness | 18 | 14/4 | 0.98 / 0.91 | 90.37 [18] | 1.03 [18] | 87.29 [18] |
| Medium | Baseline | 2 | 2/0 | 5.48 / 5.48 | 100.00 [2] | 1.46 [2] | 317.31 [2] |
| Medium | Trade-Harness | 2 | 1/1 | 4.51 / 4.51 | 85.42 [2] | 0.23 [2] | 171.10 [2] |
| Complex | Baseline | 0 | 0/0 | — | — | — | — |
| Complex | Trade-Harness | 0 | 0/0 | — | — | — | — |

### D03 — 33 tasks (18 baseline / 15 Trade-Harness)

| Complexity | Workflow | Tasks | Feature/Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Defect density mean / KLOC [n] | Token cost mean USD / issue [n] |
|---|---|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 15 | 8/7 | 1.15 / 1.03 | 89.44 [15] | 0.77 [15] | 117.74 [15] |
| Simple | Trade-Harness | 13 | 7/6 | 1.16 / 0.88 | 91.67 [13] | 0.90 [13] | 119.94 [13] |
| Medium | Baseline | 3 | 1/2 | 4.08 / 3.96 | 82.14 [3] | 0.54 [3] | 295.93 [3] |
| Medium | Trade-Harness | 2 | 2/0 | 5.48 / 5.48 | 93.75 [2] | 0.17 [2] | 679.48 [2] |
| Complex | Baseline | 0 | 0/0 | — | — | — | — |
| Complex | Trade-Harness | 0 | 0/0 | — | — | — | — |

### D04 — 17 tasks (8 baseline / 9 Trade-Harness)

| Complexity | Workflow | Tasks | Feature/Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Defect density mean / KLOC [n] | Token cost mean USD / issue [n] |
|---|---|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 3 | 2/1 | 1.86 / 1.81 | 85.00 [3] | 0.00 [3] | 48.95 [3] |
| Simple | Trade-Harness | 7 | 3/4 | 1.24 / 0.93 | 90.48 [7] | 1.24 [7] | 75.13 [7] |
| Medium | Baseline | 4 | 3/1 | 3.30 / 3.67 | 75.84 [4] | 0.41 [4] | 167.08 [4] |
| Medium | Trade-Harness | 2 | 1/1 | 3.47 / 3.47 | 95.45 [2] | 0.09 [2] | 136.55 [2] |
| Complex | Baseline | 1 | 1/0 | 19.97 / 19.97 | 89.47 [1] | — | 576.54 [1] |
| Complex | Trade-Harness | 0 | 0/0 | — | — | — | — |

### D05 — 23 tasks (14 baseline / 9 Trade-Harness)

| Complexity | Workflow | Tasks | Feature/Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Defect density mean / KLOC [n] | Token cost mean USD / issue [n] |
|---|---|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 12 | 10/2 | 1.85 / 1.07 | 95.14 [12] | 0.71 [12] | 14.49 [12] |
| Simple | Trade-Harness | 6 | 5/1 | 0.63 / 0.77 | 91.11 [6] | 0.86 [6] | 12.36 [6] |
| Medium | Baseline | 2 | 1/1 | 5.45 / 5.45 | 84.52 [2] | 0.28 [2] | 86.87 [2] |
| Medium | Trade-Harness | 2 | 2/0 | 5.84 / 5.84 | 94.44 [2] | 0.06 [2] | 98.70 [2] |
| Complex | Baseline | 0 | 0/0 | — | — | — | — |
| Complex | Trade-Harness | 1 | 1/0 | 11.22 / 11.22 | 91.67 [1] | 0.48 [1] | 183.50 [1] |

### D06 — 40 tasks (24 baseline / 16 Trade-Harness)

| Complexity | Workflow | Tasks | Feature/Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Defect density mean / KLOC [n] | Token cost mean USD / issue [n] |
|---|---|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 19 | 12/7 | 0.97 / 0.81 | 91.67 [19] | 0.93 [19] | 57.34 [19] |
| Simple | Trade-Harness | 15 | 7/8 | 0.95 / 0.87 | 90.56 [15] | 0.71 [15] | 70.24 [15] |
| Medium | Baseline | 5 | 3/2 | 4.13 / 4.92 | 91.11 [5] | 0.25 [5] | 250.00 [5] |
| Medium | Trade-Harness | 1 | 1/0 | 4.02 / 4.02 | 90.00 [1] | 1.19 [1] | 215.30 [1] |
| Complex | Baseline | 0 | 0/0 | — | — | — | — |
| Complex | Trade-Harness | 0 | 0/0 | — | — | — | — |

### D07 — 26 tasks (13 baseline / 13 Trade-Harness)

| Complexity | Workflow | Tasks | Feature/Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Defect density mean / KLOC [n] | Token cost mean USD / issue [n] |
|---|---|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 9 | 7/2 | 0.97 / 0.88 | 90.74 [9] | 1.12 [9] | 44.78 [9] |
| Simple | Trade-Harness | 9 | 6/3 | 0.78 / 0.81 | 98.15 [9] | 0.32 [9] | 47.22 [8] |
| Medium | Baseline | 3 | 2/1 | 3.35 / 3.15 | 78.41 [3] | 0.35 [3] | 132.51 [3] |
| Medium | Trade-Harness | 2 | 2/0 | 3.14 / 3.14 | 95.00 [2] | 0.41 [2] | 216.00 [2] |
| Complex | Baseline | 1 | 1/0 | 13.27 / 13.27 | 75.00 [1] | 0.24 [1] | 672.03 [1] |
| Complex | Trade-Harness | 2 | 2/0 | 11.85 / 11.85 | 83.77 [2] | 0.32 [2] | 480.90 [2] |

### D08 — 22 tasks (12 baseline / 10 Trade-Harness)

| Complexity | Workflow | Tasks | Feature/Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Defect density mean / KLOC [n] | Token cost mean USD / issue [n] |
|---|---|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 9 | 6/3 | 0.82 / 0.73 | 100.00 [9] | 0.46 [9] | 22.96 [9] |
| Simple | Trade-Harness | 7 | 4/3 | 0.71 / 0.87 | 89.52 [7] | 0.00 [7] | 44.01 [7] |
| Medium | Baseline | 2 | 1/1 | 2.00 / 2.00 | 74.24 [2] | 0.08 [2] | 100.60 [2] |
| Medium | Trade-Harness | 3 | 3/0 | 4.45 / 5.24 | 92.86 [2] | 0.21 [3] | 143.15 [3] |
| Complex | Baseline | 1 | 0/1 | 12.93 / 12.93 | 92.31 [1] | 0.21 [1] | 347.38 [1] |
| Complex | Trade-Harness | 0 | 0/0 | — | — | — | — |

### D09 — 39 tasks (21 baseline / 18 Trade-Harness)

| Complexity | Workflow | Tasks | Feature/Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Defect density mean / KLOC [n] | Token cost mean USD / issue [n] |
|---|---|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 15 | 11/4 | 1.09 / 0.89 | 91.11 [15] | 0.35 [15] | 51.68 [15] |
| Simple | Trade-Harness | 15 | 9/6 | 1.27 / 0.84 | 96.11 [15] | 0.18 [15] | 58.05 [15] |
| Medium | Baseline | 6 | 4/2 | 4.61 / 3.50 | 94.44 [6] | 0.27 [6] | 243.03 [6] |
| Medium | Trade-Harness | 3 | 3/0 | 1.75 / 1.21 | 92.80 [3] | 0.37 [3] | 183.47 [3] |
| Complex | Baseline | 0 | 0/0 | — | — | — | — |
| Complex | Trade-Harness | 0 | 0/0 | — | — | — | — |

### D10 — 35 tasks (21 baseline / 14 Trade-Harness)

| Complexity | Workflow | Tasks | Feature/Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Defect density mean / KLOC [n] | Token cost mean USD / issue [n] |
|---|---|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 20 | 7/13 | 0.92 / 0.86 | 91.17 [20] | 2.91 [20] | 40.08 [20] |
| Simple | Trade-Harness | 13 | 7/6 | 1.10 / 0.83 | 95.90 [13] | 1.68 [13] | 49.32 [13] |
| Medium | Baseline | 1 | 0/1 | 4.69 / 4.69 | 87.50 [1] | 0.66 [1] | 168.70 [1] |
| Medium | Trade-Harness | 1 | 1/0 | 5.91 / 5.91 | 90.91 [1] | 1.38 [1] | 393.31 [1] |
| Complex | Baseline | 0 | 0/0 | — | — | — | — |
| Complex | Trade-Harness | 0 | 0/0 | — | — | — | — |

## Reconciliation checks

- **290 tasks** appear in exactly one developer/workflow/complexity subgroup.
- **159 baseline and 131 Trade-Harness** task assignments are retained.
- For each developer, subgroup task counts sum to that developer’s total task count in the original sheet.
- Feature and enhancement counts within each subgroup add up to its task count.
- All metric sample counts are at most the subgroup task count.
- No task without a matching developer, workflow, or complexity has been silently imputed.
