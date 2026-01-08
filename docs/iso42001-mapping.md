# UNICORN Framework: ISO 42001 Mapping Guide

This document maps the UNICORN Framework dimensions to ISO/IEC 42001:2023 requirements, enabling organizations to use framework results as evidence for AI management system compliance.

---

## Overview

ISO/IEC 42001:2023 specifies requirements for establishing, implementing, maintaining, and continually improving an AI management system (AIMS). The UNICORN Framework provides operational evidence that AI systems behave in accordance with these requirements.

| ISO 42001 Clause | UNICORN Dimension(s) | Evidence Provided |
|------------------|---------------------|-------------------|
| 6.1.2 AI system impact assessment | D1, D2, D3 | Behavioral boundary verification |
| 6.1.3 AI risk assessment | D4, D5, D7 | Safety and privacy risk evidence |
| 7.2 Competence | D8 | Audit capability verification |
| 8.3 AI system operation | D6 | Tool/action governance evidence |
| 9.1 Monitoring, measurement | D1-D8 | Quantitative performance metrics |

---

## Detailed Mapping

### ISO 42001 §6.1.2 — AI System Impact Assessment

**Requirement:** Organizations shall determine the potential impacts of the AI system on individuals, groups, and society.

**UNICORN Evidence:**

| Dimension | Contribution |
|-----------|--------------|
| **D1: Identity Stability** | Demonstrates that the system maintains defined role boundaries, preventing unauthorized authority claims that could impact users |
| **D2: Policy Confidentiality** | Shows that internal governance remains protected, preventing manipulation of AI behavior |
| **D3: Scope Boundaries** | Verifies that the system stays within intended domain, limiting unintended impacts |

**Audit Artifact:** UNICORN evaluation report showing D1-D3 pass rates across interaction levels, with specific test cases demonstrating boundary maintenance.

---

### ISO 42001 §6.1.3 — AI Risk Assessment

**Requirement:** Organizations shall assess AI-related risks including those to affected parties.

**UNICORN Evidence:**

| Dimension | Risk Category Addressed |
|-----------|------------------------|
| **D4: Safety Alignment** | Consistency of safety mechanisms across phrasings |
| **D5: Privacy Handling** | Data protection control effectiveness |
| **D7: Adversarial Robustness** | Resilience against manipulation attempts |

**Audit Artifact:** Risk matrix populated with UNICORN degradation data, showing where prompt-only controls are insufficient and architectural controls are needed.

**Example Risk Entry:**
```
Risk: Identity drift under multi-turn conversation
Likelihood: High (76% L1→L3 degradation observed)
Impact: Medium (unauthorized persona adoption)
Control: Prompt-based identity instruction
Effectiveness: 24% at L3 (inadequate)
Recommendation: Implement hard-coded identity constraints
```

---

### ISO 42001 §7.2 — Competence

**Requirement:** Organizations shall ensure persons are competent to perform AI governance functions.

**UNICORN Evidence:**

| Dimension | Contribution |
|-----------|--------------|
| **D8: Logging/Explainability** | Verifies that AI decisions are auditable, enabling human oversight |

**Audit Artifact:** D8 evaluation demonstrating that:
- Guardrail decisions are logged
- Logs are accessible to authorized reviewers
- Explanations are available without exposing system internals

---

### ISO 42001 §8.3 — AI System Operation

**Requirement:** Organizations shall implement controls for AI system operation including human oversight.

**UNICORN Evidence:**

| Dimension | Control Category |
|-----------|-----------------|
| **D6: Tool Safety** | Verification that agentic actions require appropriate authorization |
| **D7: Adversarial Robustness** | Evidence that human override remains possible despite pressure |

**Audit Artifact:** D6 evaluation showing authorization patterns, including:
- Verification requirements before consequential actions
- Resistance to urgency-based bypass attempts
- Escalating verification for escalating scope

---

### ISO 42001 §9.1 — Monitoring, Measurement, Analysis, and Evaluation

**Requirement:** Organizations shall determine what needs to be monitored and measured for the AIMS.

**UNICORN Evidence:**

All dimensions (D1-D8) provide quantitative metrics suitable for ongoing monitoring:

| Metric | Description | Target |
|--------|-------------|--------|
| L1 Pass Rate | Basic compliance | ≥95% |
| L3 Pass Rate | Realistic use compliance | ≥70% |
| Degradation | L1-L3 difference | ≤25pp |
| Per-Dimension L3 | Individual dimension health | ≥50% |

**Audit Artifact:** Trend reports showing UNICORN scores over time, detecting regression after model updates.

---

## Using UNICORN for ISO 42001 Audits

### Pre-Audit Preparation

1. **Conduct UNICORN evaluation** across all AI systems in scope
2. **Generate reports** using provided tools
3. **Map findings** to ISO 42001 clauses using this guide
4. **Document gaps** and remediation plans

### During Audit

**For each ISO 42001 clause, present:**

1. **UNICORN dimension mapping** (from this guide)
2. **Quantitative results** (pass rates, degradation)
3. **Sample test cases** (specific prompts and responses)
4. **Trend data** (if available from prior evaluations)

### Evidence Package Contents

```
iso42001-evidence/
├── executive-summary.pdf
├── full-evaluation-report.pdf
├── dimension-details/
│   ├── D1-identity-stability.pdf
│   ├── D2-policy-confidentiality.pdf
│   └── ...
├── test-case-samples/
│   ├── D1-samples.pdf
│   └── ...
├── trend-analysis/
│   └── quarterly-comparison.pdf
└── remediation-plans/
    └── high-risk-dimensions.pdf
```

---

## Gap Analysis Template

Use this template to identify gaps between current state and ISO 42001 requirements:

| ISO 42001 Clause | UNICORN Dimension | Current L3 Pass Rate | Target | Gap | Remediation |
|------------------|-------------------|---------------------|--------|-----|-------------|
| 6.1.2 | D1: Identity | __%  | 70% | __pp | |
| 6.1.2 | D2: Policy | __% | 70% | __pp | |
| 6.1.2 | D3: Scope | __% | 70% | __pp | |
| 6.1.3 | D4: Safety | __% | 80% | __pp | |
| 6.1.3 | D5: Privacy | __% | 80% | __pp | |
| 6.1.3 | D7: Adversarial | __% | 60% | __pp | |
| 8.3 | D6: Tool | __% | 70% | __pp | |
| 9.1 | D8: Logging | __% | 80% | __pp | |

---

## NIST AI RMF Alignment

The UNICORN Framework also aligns with NIST AI RMF functions:

| NIST AI RMF Function | UNICORN Dimensions |
|---------------------|-------------------|
| **GOVERN** | D8 (governance auditability) |
| **MAP** | D1, D2, D3 (system boundaries, intended use) |
| **MEASURE** | D4, D5, D6, D7 (risk measurement) |
| **MANAGE** | All (control effectiveness verification) |

---

## Continuous Compliance

### Recommended Evaluation Frequency

| Trigger | Evaluation Scope |
|---------|-----------------|
| Model update | Full evaluation |
| Quarterly | Sample evaluation (20% of test cases) |
| Incident | Targeted dimension evaluation |
| Annual | Full evaluation + trend analysis |

### Regression Detection

Monitor for:
- L3 pass rate declining >10pp from baseline
- Any dimension falling below 30% L3 pass rate
- New failure patterns not seen in prior evaluations

---

## Questions?

For questions about ISO 42001 mapping or compliance use of UNICORN Framework results, contact the framework maintainers or consult your organization's compliance team.
