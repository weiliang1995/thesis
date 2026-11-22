# Developer Performance Breakdown — Provisional Dataset

This supporting analysis uses **548 distinct Jira tasks** from the [Google Sheet](https://docs.google.com/spreadsheets/d/1yh9VRPTxTWhPp7bPHs7_Ne1nrlFQoS504awsWqiZghw/edit), reviewed on 2026-11-22. It accompanies [Chapter 4, Section 4.6.2](./4.6-complexity-and-developer-comparison.md).

Each row is filtered by the **developer, task complexity and workflow** named in that row. Metrics are issue-level: development lead time (mean and median elapsed days), final E2E pass rate (mean task-level %), the total number of confirmed task-linked defects, the total changed production KLOC (1 KLOC = 1,000 changed LOC), confirmed defect density (mean of the individual tasks' defects per 1,000 changed production LOC), and recorded LLM gateway cost (mean USD per issue). **The subgroup's average defect density is not calculated by dividing its total defect count by its total changed KLOC.** The `[n]` beside a metric indicates its valid task count. Missing values are not treated as zero, and defect density is undefined for zero changed production LOC. `—` indicates no valid observation.

The [CSV version](./developer-performance-breakdown.csv) additionally gives each metric's valid count, changed LOC per million tokens, and correction-loop means. This is a static data snapshot, not a live-synced file.

### D01 — 19 tasks (Baseline 9, Trade-Harness 10)

| Complexity | Workflow | Tasks | Feature / Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Confirmed defects (total) | Changed KLOC (total) | Defect density mean / KLOC [n] | Token cost mean (USD) [n] |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 2 | 0 / 2 | 0.08 / 0.08 | 81.67 [2] | 2 | 1.175 | 2.53 [2] | 18.63 [2] |
| Simple | Trade-Harness | 3 | 3 / 0 | 0.13 / 0.11 | 100.00 [3] | 3 | 1.219 | 2.57 [3] | 23.69 [3] |
| Medium | Baseline | 6 | 5 / 1 | 3.42 / 2.82 | 88.19 [6] | 10 | 19.469 | 0.60 [6] | 189.96 [6] |
| Medium | Trade-Harness | 5 | 1 / 4 | 3.04 / 2.29 | 85.50 [5] | 6 | 7.839 | 1.14 [5] | 256.97 [5] |
| Complex | Baseline | 1 | 0 / 1 | 4.14 / 4.14 | 81.25 [1] | 4 | 5.750 | 0.70 [1] | 476.38 [1] |
| Complex | Trade-Harness | 2 | 2 / 0 | 9.16 / 9.16 | 87.01 [2] | 6 | 8.484 | 0.75 [2] | 568.46 [2] |

### D02 — 67 tasks (Baseline 35, Trade-Harness 32)

| Complexity | Workflow | Tasks | Feature / Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Confirmed defects (total) | Changed KLOC (total) | Defect density mean / KLOC [n] | Token cost mean (USD) [n] |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 29 | 20 / 9 | 1.27 / 0.84 | 94.05 [28] | 20 | 6.387 | 4.05 [28] | 32.80 [29] |
| Simple | Trade-Harness | 25 | 18 / 7 | 0.94 / 0.78 | 89.53 [25] | 14 | 6.120 | 3.36 [25] | 36.20 [25] |
| Medium | Baseline | 6 | 5 / 1 | 2.44 / 2.14 | 81.93 [6] | 17 | 13.045 | 1.67 [6] | 140.69 [6] |
| Medium | Trade-Harness | 6 | 4 / 2 | 3.66 / 3.44 | 92.78 [6] | 24 | 15.924 | 1.73 [6] | 154.98 [6] |
| Complex | Baseline | 0 | 0 / 0 | — | — | 0 | 0.000 | — | — |
| Complex | Trade-Harness | 1 | 1 / 0 | 3.26 / 3.26 | 86.36 [1] | 14 | 4.246 | 3.30 [1] | 269.27 [1] |

### D03 — 60 tasks (Baseline 34, Trade-Harness 26)

| Complexity | Workflow | Tasks | Feature / Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Confirmed defects (total) | Changed KLOC (total) | Defect density mean / KLOC [n] | Token cost mean (USD) [n] |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 30 | 15 / 15 | 0.92 / 0.48 | 92.44 [30] | 19 | 11.900 | 2.09 [30] | 48.96 [30] |
| Simple | Trade-Harness | 22 | 13 / 9 | 1.17 / 0.82 | 97.73 [22] | 10 | 8.515 | 1.34 [22] | 58.85 [22] |
| Medium | Baseline | 3 | 1 / 2 | 6.47 / 6.27 | 81.48 [3] | 5 | 13.593 | 0.43 [3] | 293.95 [3] |
| Medium | Trade-Harness | 4 | 4 / 0 | 3.25 / 3.43 | 91.29 [4] | 4 | 15.300 | 0.27 [4] | 358.06 [4] |
| Complex | Baseline | 1 | 0 / 1 | 7.91 / 7.91 | 75.00 [1] | 4 | 15.079 | 0.27 [1] | 494.45 [1] |
| Complex | Trade-Harness | 0 | 0 / 0 | — | — | 0 | 0.000 | — | — |

### D04 — 30 tasks (Baseline 18, Trade-Harness 12)

| Complexity | Workflow | Tasks | Feature / Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Confirmed defects (total) | Changed KLOC (total) | Defect density mean / KLOC [n] | Token cost mean (USD) [n] |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 10 | 7 / 3 | 0.78 / 0.17 | 92.17 [10] | 4 | 2.085 | 1.49 [10] | 23.59 [10] |
| Simple | Trade-Harness | 6 | 5 / 1 | 0.65 / 0.81 | 95.83 [6] | 1 | 1.229 | 0.86 [6] | 36.38 [6] |
| Medium | Baseline | 7 | 1 / 6 | 3.21 / 3.03 | 84.29 [6] | 9 | 7.744 | 1.54 [7] | 100.98 [7] |
| Medium | Trade-Harness | 6 | 6 / 0 | 3.23 / 1.97 | 89.58 [6] | 13 | 8.253 | 1.90 [6] | 124.88 [6] |
| Complex | Baseline | 1 | 1 / 0 | 11.10 / 11.10 | 82.61 [1] | 11 | 6.656 | 1.65 [1] | 280.36 [1] |
| Complex | Trade-Harness | 0 | 0 / 0 | — | — | 0 | 0.000 | — | — |

### D05 — 60 tasks (Baseline 32, Trade-Harness 28)

| Complexity | Workflow | Tasks | Feature / Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Confirmed defects (total) | Changed KLOC (total) | Defect density mean / KLOC [n] | Token cost mean (USD) [n] |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 25 | 13 / 12 | 0.78 / 0.26 | 92.07 [25] | 17 | 6.606 | 4.60 [25] | 6.25 [25] |
| Simple | Trade-Harness | 21 | 9 / 12 | 0.76 / 0.32 | 93.10 [21] | 12 | 5.751 | 2.34 [21] | 8.37 [21] |
| Medium | Baseline | 7 | 6 / 1 | 3.78 / 3.88 | 96.32 [7] | 15 | 11.330 | 1.46 [7] | 29.31 [7] |
| Medium | Trade-Harness | 6 | 4 / 2 | 2.86 / 1.97 | 96.94 [6] | 12 | 15.544 | 1.11 [6] | 33.84 [6] |
| Complex | Baseline | 0 | 0 / 0 | — | — | 0 | 0.000 | — | — |
| Complex | Trade-Harness | 1 | 1 / 0 | 7.98 / 7.98 | 84.21 [1] | 4 | 7.569 | 0.53 [1] | 62.36 [1] |

### D06 — 80 tasks (Baseline 44, Trade-Harness 36)

| Complexity | Workflow | Tasks | Feature / Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Confirmed defects (total) | Changed KLOC (total) | Defect density mean / KLOC [n] | Token cost mean (USD) [n] |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 37 | 28 / 9 | 0.78 / 0.81 | 95.36 [37] | 24 | 7.787 | 4.21 [37] | 27.14 [37] |
| Simple | Trade-Harness | 29 | 18 / 11 | 1.01 / 0.85 | 96.84 [29] | 18 | 5.897 | 3.52 [29] | 32.38 [29] |
| Medium | Baseline | 7 | 5 / 2 | 3.72 / 4.08 | 93.81 [7] | 19 | 16.757 | 2.21 [7] | 97.83 [7] |
| Medium | Trade-Harness | 7 | 4 / 3 | 3.36 / 2.88 | 89.46 [7] | 16 | 11.658 | 2.18 [7] | 140.06 [7] |
| Complex | Baseline | 0 | 0 / 0 | — | — | 0 | 0.000 | — | — |
| Complex | Trade-Harness | 0 | 0 / 0 | — | — | 0 | 0.000 | — | — |

### D07 — 47 tasks (Baseline 28, Trade-Harness 19)

| Complexity | Workflow | Tasks | Feature / Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Confirmed defects (total) | Changed KLOC (total) | Defect density mean / KLOC [n] | Token cost mean (USD) [n] |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 18 | 13 / 5 | 0.72 / 0.23 | 91.02 [18] | 14 | 10.682 | 1.91 [18] | 24.07 [18] |
| Simple | Trade-Harness | 16 | 9 / 7 | 1.01 / 0.80 | 93.02 [16] | 6 | 8.079 | 1.83 [16] | 25.48 [16] |
| Medium | Baseline | 8 | 5 / 3 | 4.01 / 3.03 | 86.46 [8] | 22 | 24.063 | 1.02 [8] | 151.41 [8] |
| Medium | Trade-Harness | 2 | 0 / 2 | 5.05 / 5.05 | 95.00 [2] | 3 | 4.857 | 0.62 [2] | 141.81 [2] |
| Complex | Baseline | 2 | 2 / 0 | 9.66 / 9.66 | 66.67 [2] | 20 | 21.275 | 0.95 [2] | 274.01 [2] |
| Complex | Trade-Harness | 1 | 1 / 0 | 9.79 / 9.79 | 85.00 [1] | 7 | 5.645 | 1.24 [1] | 360.31 [1] |

### D08 — 45 tasks (Baseline 23, Trade-Harness 22)

| Complexity | Workflow | Tasks | Feature / Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Confirmed defects (total) | Changed KLOC (total) | Defect density mean / KLOC [n] | Token cost mean (USD) [n] |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 14 | 6 / 8 | 0.56 / 0.21 | 92.62 [14] | 8 | 5.319 | 2.79 [14] | 9.91 [13] |
| Simple | Trade-Harness | 16 | 10 / 6 | 0.74 / 0.18 | 94.06 [16] | 6 | 6.328 | 0.88 [16] | 11.75 [16] |
| Medium | Baseline | 8 | 3 / 5 | 3.61 / 4.00 | 90.31 [8] | 18 | 27.659 | 1.23 [8] | 55.29 [8] |
| Medium | Trade-Harness | 5 | 2 / 3 | 2.67 / 1.87 | 89.00 [5] | 13 | 16.052 | 0.93 [5] | 61.14 [5] |
| Complex | Baseline | 1 | 1 / 0 | 10.09 / 10.09 | 91.67 [1] | 6 | 22.791 | 0.26 [1] | 139.16 [1] |
| Complex | Trade-Harness | 1 | 0 / 1 | 8.25 / 8.25 | 91.30 [1] | 4 | 9.251 | 0.43 [1] | 288.74 [1] |

### D09 — 65 tasks (Baseline 36, Trade-Harness 29)

| Complexity | Workflow | Tasks | Feature / Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Confirmed defects (total) | Changed KLOC (total) | Defect density mean / KLOC [n] | Token cost mean (USD) [n] |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 27 | 12 / 15 | 0.99 / 0.77 | 92.59 [27] | 17 | 10.736 | 1.37 [27] | 29.62 [27] |
| Simple | Trade-Harness | 23 | 13 / 10 | 0.97 / 0.27 | 92.68 [23] | 19 | 10.999 | 2.31 [23] | 32.64 [23] |
| Medium | Baseline | 9 | 2 / 7 | 3.74 / 4.13 | 82.48 [9] | 29 | 28.720 | 1.23 [9] | 128.22 [9] |
| Medium | Trade-Harness | 5 | 1 / 4 | 3.27 / 3.06 | 96.52 [5] | 17 | 13.421 | 1.36 [5] | 126.46 [5] |
| Complex | Baseline | 0 | 0 / 0 | — | — | 0 | 0.000 | — | — |
| Complex | Trade-Harness | 1 | 1 / 0 | 7.13 / 7.13 | 82.61 [1] | 7 | 14.042 | 0.50 [1] | 317.64 [1] |

### D10 — 75 tasks (Baseline 43, Trade-Harness 32)

| Complexity | Workflow | Tasks | Feature / Enhancement | Lead mean / median (days) | E2E mean (%) [n] | Confirmed defects (total) | Changed KLOC (total) | Defect density mean / KLOC [n] | Token cost mean (USD) [n] |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Simple | Baseline | 40 | 25 / 15 | 1.62 / 0.83 | 92.96 [40] | 34 | 7.257 | 6.06 [40] | 16.03 [40] |
| Simple | Trade-Harness | 28 | 14 / 14 | 1.50 / 0.96 | 93.81 [28] | 16 | 4.861 | 4.48 [28] | 20.04 [28] |
| Medium | Baseline | 3 | 1 / 2 | 3.09 / 3.09 | 89.68 [3] | 14 | 2.690 | 4.96 [3] | 83.87 [3] |
| Medium | Trade-Harness | 4 | 3 / 1 | 6.72 / 6.53 | 92.22 [4] | 17 | 2.892 | 5.87 [4] | 137.74 [4] |
| Complex | Baseline | 0 | 0 / 0 | — | — | 0 | 0.000 | — | — |
| Complex | Trade-Harness | 0 | 0 / 0 | — | — | 0 | 0.000 | — | — |

## Reconciliation

The 60 Developer × Workflow × Complexity rows account for **548 tasks**: **302 baseline and 246 Trade-Harness**, with each task counted once. Every developer subtotal matches the source task records. Feature and enhancement subtotals reconcile with each subgroup's task count.

Results remain provisional until the study sample and defect extraction date are confirmed. Small subgroups should not be interpreted as randomized, matched comparisons.
