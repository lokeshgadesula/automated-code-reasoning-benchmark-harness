# Automated Code Reasoning & Benchmark Harness
Python evaluation framework for LLM-generated algorithmic code. It includes AST syntax validation, normalized execution observations, output diffs, edge-case pass rates, PEP-8-oriented style diagnostics, and a Docker sandbox adapter with network disabled plus memory/CPU/PID/read-only constraints.

The evaluator is unit-tested independently from the host runtime. Actual candidate execution requires Docker. “Efficiency” means measured execution timing on configured cases, not formal Big-O inference.
