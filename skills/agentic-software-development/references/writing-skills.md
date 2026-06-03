# Writing Skills (TDD for Documentation)

**Iron Law: No skill without a failing test (baseline) first.**

## RED-GREEN-REFACTOR for Skills
1. **RED**: Run pressure scenario WITHOUT skill. Document baseline failures and rationalizations.
2. **GREEN**: Write minimal skill addressing those specific failures. Verify agent now complies.
3. **REFACTOR**: Find new rationalizations, close loopholes, re-verify.

## Claude Search Optimization (CSO)
- **Description**: MUST start with "Use when..." and focus on triggering conditions.
- **NEVER** summarize the workflow in the description (prevents agent from skipping the skill body).
- **Target token efficiency**: <200 words for frequently-loaded skills.
