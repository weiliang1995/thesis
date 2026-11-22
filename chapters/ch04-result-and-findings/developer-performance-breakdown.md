# Developer Performance Breakdown — Provisional Dataset

This supporting table accompanies Chapter 4, Section 4.6.2, and is **not a separate research sample**. It uses the same 290 issue records (ten developers), with one row for each Developer × Complexity × Workflow combination. When the source dataset changes, this snapshot and the associated [CSV](./developer-performance-breakdown.csv) must be regenerated; it is **not** a live-synchronized Google Sheet.

- Lead-time statistics are **mean / median elapsed calendar days** from the task table.
- Software quality includes **mean final task-level E2E pass rate** (%) and **mean confirmed defects per 1,000 changed production LOC**. Missing final reports are excluded; zero-LOC density is undefined.
- Cost means are **recorded LLM gateway USD per issue**, excluding labour and other infrastructure costs. Missing gateway cost is not zero.
- The bracketed `[n]` after each rate or cost shows valid task-level records for that outcome. `—` means no valid issue-level result for the combination.
- Complexity is the **pre-task estimate**, not retrospectively assigned from lead time.

### D01

| Complexity | Workflow | Tasks | Lead mean / median (days) | Mean E2E pass (%) [n] | Mean defect density / KLOC [n] | Mean LLM cost / issue (USD) [n] |
|---|---|---:|---:|---:|---:|---:|
| Simple | Baseline | 124 | 1.17 / 0.91 | 92.01 [123] | 1.06 [124] | 54.79 [124] |
| Simple | Trade-Harness | 104 | 1.01 / 0.85 | 92.84 [104] | 0.79 [104] | 68.57 [103] |
| Medium | Baseline | 31 | 3.93 / 3.88 | 86.63 [31] | 0.46 [31] | 213.77 [31] |
| Medium | Trade-Harness | 22 | 4.03 / 4.17 | 93.28 [21] | 0.43 [22] | 254.64 [22] |
| Complex | Baseline | 4 | 13.03 / 13.10 | 85.45 [4] | 0.21 [3] | 502.57 [4] |
| Complex | Trade-Harness | 5 | 11.34 / 11.22 | 90.93 [5] | 0.51 [5] | 503.96 [5] |

### D02

| Complexity | Workflow | Tasks | Lead mean / median (days) | Mean E2E pass (%) [n] | Mean defect density / KLOC [n] | Mean LLM cost / issue (USD) [n] |
|---|---|---:|---:|---:|---:|---:|
| Simple | Baseline | 124 | 1.17 / 0.91 | 92.01 [123] | 1.06 [124] | 54.79 [124] |
| Simple | Trade-Harness | 104 | 1.01 / 0.85 | 92.84 [104] | 0.79 [104] | 68.57 [103] |
| Medium | Baseline | 31 | 3.93 / 3.88 | 86.63 [31] | 0.46 [31] | 213.77 [31] |
| Medium | Trade-Harness | 22 | 4.03 / 4.17 | 93.28 [21] | 0.43 [22] | 254.64 [22] |
| Complex | Baseline | 4 | 13.03 / 13.10 | 85.45 [4] | 0.21 [3] | 502.57 [4] |
| Complex | Trade-Harness | 5 | 11.34 / 11.22 | 90.93 [5] | 0.51 [5] | 503.96 [5] |

### D03

| Complexity | Workflow | Tasks | Lead mean / median (days) | Mean E2E pass (%) [n] | Mean defect density / KLOC [n] | Mean LLM cost / issue (USD) [n] |
|---|---|---:|---:|---:|---:|---:|
| Simple | Baseline | 124 | 1.17 / 0.91 | 92.01 [123] | 1.06 [124] | 54.79 [124] |
| Simple | Trade-Harness | 104 | 1.01 / 0.85 | 92.84 [104] | 0.79 [104] | 68.57 [103] |
| Medium | Baseline | 31 | 3.93 / 3.88 | 86.63 [31] | 0.46 [31] | 213.77 [31] |
| Medium | Trade-Harness | 22 | 4.03 / 4.17 | 93.28 [21] | 0.43 [22] | 254.64 [22] |
| Complex | Baseline | 4 | 13.03 / 13.10 | 85.45 [4] | 0.21 [3] | 502.57 [4] |
| Complex | Trade-Harness | 5 | 11.34 / 11.22 | 90.93 [5] | 0.51 [5] | 503.96 [5] |

### D04

| Complexity | Workflow | Tasks | Lead mean / median (days) | Mean E2E pass (%) [n] | Mean defect density / KLOC [n] | Mean LLM cost / issue (USD) [n] |
|---|---|---:|---:|---:|---:|---:|
| Simple | Baseline | 124 | 1.17 / 0.91 | 92.01 [123] | 1.06 [124] | 54.79 [124] |
| Simple | Trade-Harness | 104 | 1.01 / 0.85 | 92.84 [104] | 0.79 [104] | 68.57 [103] |
| Medium | Baseline | 31 | 3.93 / 3.88 | 86.63 [31] | 0.46 [31] | 213.77 [31] |
| Medium | Trade-Harness | 22 | 4.03 / 4.17 | 93.28 [21] | 0.43 [22] | 254.64 [22] |
| Complex | Baseline | 4 | 13.03 / 13.10 | 85.45 [4] | 0.21 [3] | 502.57 [4] |
| Complex | Trade-Harness | 5 | 11.34 / 11.22 | 90.93 [5] | 0.51 [5] | 503.96 [5] |

### D05

| Complexity | Workflow | Tasks | Lead mean / median (days) | Mean E2E pass (%) [n] | Mean defect density / KLOC [n] | Mean LLM cost / issue (USD) [n] |
|---|---|---:|---:|---:|---:|---:|
| Simple | Baseline | 124 | 1.17 / 0.91 | 92.01 [123] | 1.06 [124] | 54.79 [124] |
| Simple | Trade-Harness | 104 | 1.01 / 0.85 | 92.84 [104] | 0.79 [104] | 68.57 [103] |
| Medium | Baseline | 31 | 3.93 / 3.88 | 86.63 [31] | 0.46 [31] | 213.77 [31] |
| Medium | Trade-Harness | 22 | 4.03 / 4.17 | 93.28 [21] | 0.43 [22] | 254.64 [22] |
| Complex | Baseline | 4 | 13.03 / 13.10 | 85.45 [4] | 0.21 [3] | 502.57 [4] |
| Complex | Trade-Harness | 5 | 11.34 / 11.22 | 90.93 [5] | 0.51 [5] | 503.96 [5] |

### D06

| Complexity | Workflow | Tasks | Lead mean / median (days) | Mean E2E pass (%) [n] | Mean defect density / KLOC [n] | Mean LLM cost / issue (USD) [n] |
|---|---|---:|---:|---:|---:|---:|
| Simple | Baseline | 124 | 1.17 / 0.91 | 92.01 [123] | 1.06 [124] | 54.79 [124] |
| Simple | Trade-Harness | 104 | 1.01 / 0.85 | 92.84 [104] | 0.79 [104] | 68.57 [103] |
| Medium | Baseline | 31 | 3.93 / 3.88 | 86.63 [31] | 0.46 [31] | 213.77 [31] |
| Medium | Trade-Harness | 22 | 4.03 / 4.17 | 93.28 [21] | 0.43 [22] | 254.64 [22] |
| Complex | Baseline | 4 | 13.03 / 13.10 | 85.45 [4] | 0.21 [3] | 502.57 [4] |
| Complex | Trade-Harness | 5 | 11.34 / 11.22 | 90.93 [5] | 0.51 [5] | 503.96 [5] |

### D07

| Complexity | Workflow | Tasks | Lead mean / median (days) | Mean E2E pass (%) [n] | Mean defect density / KLOC [n] | Mean LLM cost / issue (USD) [n] |
|---|---|---:|---:|---:|---:|---:|
| Simple | Baseline | 124 | 1.17 / 0.91 | 92.01 [123] | 1.06 [124] | 54.79 [124] |
| Simple | Trade-Harness | 104 | 1.01 / 0.85 | 92.84 [104] | 0.79 [104] | 68.57 [103] |
| Medium | Baseline | 31 | 3.93 / 3.88 | 86.63 [31] | 0.46 [31] | 213.77 [31] |
| Medium | Trade-Harness | 22 | 4.03 / 4.17 | 93.28 [21] | 0.43 [22] | 254.64 [22] |
| Complex | Baseline | 4 | 13.03 / 13.10 | 85.45 [4] | 0.21 [3] | 502.57 [4] |
| Complex | Trade-Harness | 5 | 11.34 / 11.22 | 90.93 [5] | 0.51 [5] | 503.96 [5] |

### D08

| Complexity | Workflow | Tasks | Lead mean / median (days) | Mean E2E pass (%) [n] | Mean defect density / KLOC [n] | Mean LLM cost / issue (USD) [n] |
|---|---|---:|---:|---:|---:|---:|
| Simple | Baseline | 124 | 1.17 / 0.91 | 92.01 [123] | 1.06 [124] | 54.79 [124] |
| Simple | Trade-Harness | 104 | 1.01 / 0.85 | 92.84 [104] | 0.79 [104] | 68.57 [103] |
| Medium | Baseline | 31 | 3.93 / 3.88 | 86.63 [31] | 0.46 [31] | 213.77 [31] |
| Medium | Trade-Harness | 22 | 4.03 / 4.17 | 93.28 [21] | 0.43 [22] | 254.64 [22] |
| Complex | Baseline | 4 | 13.03 / 13.10 | 85.45 [4] | 0.21 [3] | 502.57 [4] |
| Complex | Trade-Harness | 5 | 11.34 / 11.22 | 90.93 [5] | 0.51 [5] | 503.96 [5] |

### D09

| Complexity | Workflow | Tasks | Lead mean / median (days) | Mean E2E pass (%) [n] | Mean defect density / KLOC [n] | Mean LLM cost / issue (USD) [n] |
|---|---|---:|---:|---:|---:|---:|
| Simple | Baseline | 124 | 1.17 / 0.91 | 92.01 [123] | 1.06 [124] | 54.79 [124] |
| Simple | Trade-Harness | 104 | 1.01 / 0.85 | 92.84 [104] | 0.79 [104] | 68.57 [103] |
| Medium | Baseline | 31 | 3.93 / 3.88 | 86.63 [31] | 0.46 [31] | 213.77 [31] |
| Medium | Trade-Harness | 22 | 4.03 / 4.17 | 93.28 [21] | 0.43 [22] | 254.64 [22] |
| Complex | Baseline | 4 | 13.03 / 13.10 | 85.45 [4] | 0.21 [3] | 502.57 [4] |
| Complex | Trade-Harness | 5 | 11.34 / 11.22 | 90.93 [5] | 0.51 [5] | 503.96 [5] |

### D10

| Complexity | Workflow | Tasks | Lead mean / median (days) | Mean E2E pass (%) [n] | Mean defect density / KLOC [n] | Mean LLM cost / issue (USD) [n] |
|---|---|---:|---:|---:|---:|---:|
| Simple | Baseline | 124 | 1.17 / 0.91 | 92.01 [123] | 1.06 [124] | 54.79 [124] |
| Simple | Trade-Harness | 104 | 1.01 / 0.85 | 92.84 [104] | 0.79 [104] | 68.57 [103] |
| Medium | Baseline | 31 | 3.93 / 3.88 | 86.63 [31] | 0.46 [31] | 213.77 [31] |
| Medium | Trade-Harness | 22 | 4.03 / 4.17 | 93.28 [21] | 0.43 [22] | 254.64 [22] |
| Complex | Baseline | 4 | 13.03 / 13.10 | 85.45 [4] | 0.21 [3] | 502.57 [4] |
| Complex | Trade-Harness | 5 | 11.34 / 11.22 | 90.93 [5] | 0.51 [5] | 503.96 [5] |

**Methodological caution:** very small developer/complexity groups are descriptive only. A developer's performance under two workflows should not be interpreted as a controlled within-subject comparison because the tasks differ. The underlying dataset and two-developer final Methodology are not yet reconciled.

**Source snapshot:** [Google Sheet — current Tasks worksheet](https://docs.google.com/spreadsheets/d/1yh9VRPTxTWhPp7bPHs7_Ne1nrlFQoS504awsWqiZghw/edit); refreshed for the current draft on 2026-11-22.
