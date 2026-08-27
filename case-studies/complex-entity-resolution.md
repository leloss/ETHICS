# Case Study: Applying ETHICS to Entity Resolution (ER) in a Financial Institution  

## Background  

A global financial institution relied on a third-party **Entity Resolution (ER)** system to support **KYC onboarding, AML screening, and ongoing due diligence**.  
The system was designed to:  

- Match client-submitted data (names, addresses, IDs) against **watchlists, sanctions databases, and adverse media**.  
- Identify **hidden links** between counterparties and beneficial owners.  
- Provide a **single client view** across disparate systems.  

After **seven years in production**, the ER tool was deeply integrated into **customer onboarding workflows, transaction monitoring escalation, and regulatory reporting pipelines**.  
Replacing the system was **not feasible** due to contractual commitments and heavy customization.  

---

## Initial Issues Identified  

### 1. **Performance (Effectiveness & Efficiency)**  
- High **false positives (74%)**:  
  - Example: “Juan Carlos Perez” matched to **over 200 entities** across different geographies.  
- **False negatives (missed matches)**:  
  - Clients with minor spelling variations (“Mohammed” vs “Muhammad”) went undetected, creating regulatory exposure.  
- **Duplication of effort**: Analysts had to manually merge entities across 5+ systems.  
- **Average case resolution time**: **28 minutes**, versus the expected **15 minutes SLA**.  

### 2. **Transparency & Explainability**  
- Analysts could not see **which attributes (name, DOB, address)** contributed most to match scores.  
- ER tool produced a **single opaque “match score”** (e.g., 0.83) without rationale.  
- Analysts struggled to justify decisions in **audit or regulatory reviews**.  

### 3. **Human-Centricity**  
- Analysts overwhelmed by **long candidate lists** (>100 possible matches for common names).  
- No **prioritization** of likely matches based on context (e.g., industry, geography).  
- User frustration: repetitive manual validation, with **surveyed satisfaction at 39%**.  

### 4. **Accountability & Traceability**  
- No **audit logs** of which fields drove the resolution process.  
- Decisions varied across teams because there was **no standard way to challenge or override matches**.  
- Escalations to compliance committees lacked **evidence-based reasoning**.  

### 5. **Trustworthiness**  
- Front-line bankers avoided relying on the ER tool, instead **cross-checking manually on public websites**.  
- Regulators questioned the bank’s ability to demonstrate **consistent, risk-based client due diligence**.  

### 6. **Privacy & Security**  
- Sensitive client identifiers (passport numbers, national IDs) sent to **external ER vendor servers**.  
- Lack of clear **data retention policies**: some records remained accessible beyond legal limits.  
- Risk of **data leakage** during bulk file uploads.  

---

## ETHICS-Driven Intervention  

The institution applied the **ETHICS framework** to improve its ER process without replacing the vendor solution.  

### Step 1: Performance Optimization  
- Introduced **attribute weighting**: name (40%), DOB (30%), address (20%), nationality (10%).  
- Created **golden datasets** of 500 known high-risk cases to test match performance.  
- After tuning:  
  - **False positive rate** reduced from **74% → 39% (-47%)**.  
  - **Recall (true positive coverage)** increased from **64% → 88%**.  
  - Average case resolution time dropped from **28 min → 16 min (-43%)**.  

### Step 2: Transparency & Explainability  
- Implemented **LIME (Local Interpretable Model-Agnostic Explanations)** for match scoring:  
  - Highlighted which fields most influenced the score.  
  - Example: A match score of 0.83 explained as:  
    - Name similarity: +0.32  
    - DOB proximity: +0.28  
    - Address mismatch: -0.15  
    - Nationality: +0.07  
- Analysts now had **clear evidence for audit trails and regulatory reviews**.  

### Step 3: Human-Centric Enhancements  
- Redesigned match lists with **ranked prioritization** (most likely matches first).  
- Added **context filters** (e.g., same country, same sector).  
- Introduced **color-coded scoring** (green = high match, yellow = medium, red = low).  
- User satisfaction improved from **39% → 77%** after redesign.  

### Step 4: Accountability & Traceability  
- Implemented **decision logs** showing:  
  - Match score breakdown.  
  - Analyst override (accept/reject) and rationale.  
  - Timestamped audit trail linked to case files.  
- Standardized escalation packages with **traceable evidence** improved regulatory interactions.  

### Step 5: Trust Restoration  
- Monthly **ETHICS scorecards** included metrics on false positives, recall, and analyst satisfaction.  
- Adoption increased: reliance on manual checks dropped by **58%**.  
- Compliance officers regained confidence in the **consistency and auditability** of ER processes.  

### Step 6: Privacy & Security Controls  
- Implemented **data minimization**: only hashed identifiers shared with vendor.  
- Enforced **automatic deletion** of client data after 90 days in vendor systems.  
- Added **encryption-in-transit and at-rest** for all ER-related data.  

---

## Results After ETHICS Implementation  

| Metric                           | Before ETHICS | After ETHICS | Improvement |
|----------------------------------|---------------|--------------|-------------|
| False Positive Rate              | 74%           | 39%          | -47%        |
| Recall (True Positive Coverage)  | 64%           | 88%          | +24 pp      |
| Avg. Case Resolution Time        | 28 min        | 16 min       | -43%        |
| User Satisfaction (survey)       | 39%           | 77%          | +38 pp      |
| Reliance on Manual Checks        | High          | Reduced 58%  | Major drop  |
| External PII Exposure            | Full IDs sent | Hashed IDs   | Stronger security |

---

## Broader Impact  

- **Regulatory Alignment**: Improved alignment with **FATF guidance on beneficial ownership transparency** and **GDPR Article 5 (data minimization)**.  
- **Operational Efficiency**: Saved analyst time equivalent to **4 FTEs annually**.  
- **Culture Shift**: ETHICS transformed ER from a **frustrating bottleneck** into a **trustworthy compliance tool**.  

---

## Conclusion  

By applying the **ETHICS framework**, the institution transformed a **black-box, inefficient entity resolution system** into a **transparent, auditable, and high-performing solution**.  

This case shows how ETHICS can be applied not only to **AI-based risk monitoring** but also to **core compliance functions like entity resolution**, even under vendor lock-in constraints.  
