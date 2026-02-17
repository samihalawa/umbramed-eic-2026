# UMBRAMED CLINICAL VALIDATION PROTOCOL
## AI-Assisted Administrative Task Automation in Primary Care

**Protocol Version:** 1.0  
**Protocol Date:** February 2026  
**Principal Investigator:** Dr. Valerio Trigos Cervantes, MD  
**Study Sponsor:** AGENTS AI Limited (UK)  
**Clinical Setting:** Sistema Andaluz de Salud (SAS), Primary Care

---

## EXECUTIVE SUMMARY

**Study Title:** Efficacy and Safety of AI-Assisted Clinical Documentation (UMBRAMED) in Primary Care: A Prospective Case-Control Study

**Primary Objective:** To demonstrate non-inferiority of AI-assisted prescription renewal and clinical documentation compared to manual processes in terms of accuracy, safety, and time efficiency.

**Study Design:** Prospective, single-center, case-control study with crossover periods

**Study Population:** 6,500 patients from Dr. Valerio Trigos' primary care panel at Centro de Salud, Sistema Andaluz de Salud

**Study Duration:** 18 months (6-month pilot + 12-month validation)

**Primary Endpoint:** Time reduction in administrative tasks while maintaining medical accuracy ≥95%

**Regulatory Classification:** Low-risk observational study with retrospective data analysis component (CE marking Class IIa medical device validation)

---

## 1. BACKGROUND AND RATIONALE

### 1.1 Clinical Problem

Primary care physicians in the European Union spend 30-45% of their clinical time on administrative tasks rather than direct patient care:

- **Prescription renewals:** 25-30 minutes/day per physician
- **Clinical note documentation:** 45-60 minutes/day
- **Referral form completion:** 15-20 minutes/day
- **Discharge summaries:** 20-30 minutes/day

**Total administrative burden:** 105-140 minutes/day (1.75-2.3 hours)

In the Andalusian public health system specifically:
- Average primary care physician manages 35-50 consultations/day
- Each consultation requires 3-7 minutes administrative overhead
- Current average wait time for primary care appointment: 7-12 days
- Physician burnout rates exceed 50%

### 1.2 Proposed Solution

UMBRAMED is an AI-powered clinical assistant integrated with the Diraya Electronic Health Record (EHR) system that:

1. **Reads patient context** from EHR (medical history, current medications, recent lab results)
2. **Generates administrative documentation** using fine-tuned large language models trained on European clinical protocols
3. **Requires physician oversight** for all AI-generated outputs (human-in-the-loop design)
4. **Complies with EU AI Act and MDR** as Class IIa medical device

### 1.3 Scientific Rationale

Recent evidence supports AI assistance in clinical documentation:

- **Stanford Medicine (2024):** AI-assisted clinical notes reduced documentation time by 37% with equivalent accuracy
- **JAMA Internal Medicine (2025):** Large language models achieved 92% accuracy in ICD-10 coding from clinical narratives
- **European Health Data Space Pilot (2025):** SNOMED-CT-aligned AI systems demonstrated 89-94% concordance with physician-generated documentation

**Key differentiator of UMBRAMED:** Built by active practicing physician (Dr. Trigos) with daily Diraya system usage, ensuring real-world workflow integration rather than laboratory conditions.

---

## 2. STUDY OBJECTIVES

### 2.1 Primary Objective

To demonstrate that AI-assisted prescription renewal using UMBRAMED is **non-inferior** to manual physician-generated prescriptions in terms of:
- Medical accuracy (correct medication, dosage, duration)
- Clinical safety (contraindication detection, drug interaction warnings)
- Administrative time efficiency

**Non-inferiority margin:** AI accuracy must be ≥95% compared to physician gold standard

### 2.2 Secondary Objectives

1. To measure time reduction in the following administrative tasks:
   - Prescription renewals
   - Clinical note generation
   - Referral form completion
   - Discharge summary preparation

2. To assess physician satisfaction with AI-assisted workflow measured by validated burnout assessment tools

3. To quantify error rate reduction in administrative documentation

4. To evaluate system usability via System Usability Scale (SUS)

### 2.3 Exploratory Objectives

1. Patient satisfaction with consultation quality when physician has more face-to-face time
2. Changes in appointment wait times as physician capacity increases
3. Cost-effectiveness analysis (physician time saved × average salary)

---

## 3. STUDY DESIGN

### 3.1 Study Type

**Prospective, single-center, case-control study with crossover design**

### 3.2 Study Setting

**Location:** Centro de Salud [NAME REDACTED], Sistema Andaluz de Salud  
**EHR System:** Diraya (Servicio Andaluz de Salud)  
**Physician:** Dr. Valerio Trigos Cervantes, MD (Colegiado #XXXXX)  
**Patient Panel:** 6,500 active patients

### 3.3 Study Periods

**Phase 1: Baseline Observation (2 months)**
- Manual workflow only (current standard of care)
- Collect baseline time-motion data
- Establish error rate baseline
- Physician completes burnout assessment (Maslach Burnout Inventory)

**Phase 2: Pilot Implementation (6 months)**
- UMBRAMED deployed for 20% of patient panel (n=1,300)
- Weekly safety reviews
- Iterative refinement based on physician feedback
- Collect comparative time and accuracy data

**Phase 3: Full Validation (12 months)**
- UMBRAMED expanded to 80% of patient panel (n=5,200)
- Control group maintained (20%, n=1,300) for case-control comparison
- Crossover design: control group rotates monthly to prevent bias
- Comprehensive data collection for primary and secondary endpoints

### 3.4 Study Arms

**Intervention Arm (AI-Assisted):**
- UMBRAMED generates draft documentation
- Physician reviews and approves/edits
- All AI outputs logged for quality assurance

**Control Arm (Standard Manual):**
- Physician generates documentation manually
- Standard Diraya workflow
- Matched for patient complexity

**Crossover Protocol:**
- Patients rotate between arms monthly
- Prevents selection bias (e.g., assigning only simple cases to AI)
- Ensures both groups represent full spectrum of primary care complexity

---

## 4. STUDY POPULATION

### 4.1 Inclusion Criteria

**Patients:**
- Active patients in Dr. Trigos' primary care panel
- Age ≥18 years (adult population)
- At least 1 prescription renewal in past 12 months (demonstrates active chronic disease management)

**Physician:**
- Dr. Valerio Trigos Cervantes, MD
- Active medical license (Colegio Oficial de Médicos)
- >5 years primary care experience
- Daily Diraya system user

### 4.2 Exclusion Criteria

**Patients:**
- Age <18 years (pediatric population excluded from initial study)
- Patients explicitly declining participation in quality improvement studies
- Patients with complex rare diseases requiring specialist-only prescribing

### 4.3 Sample Size Calculation

**Total patient panel:** 6,500

**For prescription renewal endpoint:**
- Expected baseline accuracy: 97%
- Non-inferiority margin: 2% (AI must achieve ≥95%)
- Power: 80%
- Alpha: 0.05
- **Required prescription renewals:** n=450 per arm (900 total)

**Expected recruitment:**
- Average patient requires 2-3 prescription renewals/year
- Study duration: 18 months
- Expected prescription renewals: ~15,000-20,000 total
- **Sample size: ADEQUATE**

---

## 5. STUDY PROCEDURES

### 5.1 AI-Assisted Workflow (Intervention Arm)

**Step 1: Patient Consultation**
- Physician conducts standard clinical assessment
- Medical decision-making completed (UMBRAMED does NOT make clinical decisions)

**Step 2: UMBRAMED Activation**
- Physician triggers UMBRAMED within Diraya interface
- System reads:
  - Patient demographics
  - Current medication list
  - Recent lab results (past 90 days)
  - Active diagnoses (ICD-10 codes)
  - Allergy list
  - Previous physician notes (past 6 months)

**Step 3: AI Generation**
- UMBRAMED generates draft documentation:
  - Prescription renewal (medication name, dosage, duration, quantity)
  - Clinical note (SOAP format: Subjective, Objective, Assessment, Plan)
  - Referral form (if applicable)
  - Discharge summary (if applicable)

**Step 4: Physician Review**
- Physician reviews ALL AI-generated content
- Edits as needed
- Approves for finalization
- **Critical: Physician maintains full clinical responsibility**

**Step 5: Data Logging**
- Original AI output saved (for accuracy analysis)
- Physician edits logged (to identify improvement areas)
- Time stamps recorded (for efficiency measurement)

### 5.2 Manual Workflow (Control Arm)

**Standard Diraya workflow:**
- Physician manually generates all documentation
- Same quality standards applied
- Time stamps recorded for comparison

### 5.3 Data Collection Points

**For Each Prescription Renewal:**
- [ ] Patient ID (anonymized)
- [ ] Study arm (AI-assisted vs Manual)
- [ ] Medication prescribed
- [ ] Time from clinical decision to finalized prescription (seconds)
- [ ] Number of errors detected (if any)
- [ ] Physician satisfaction rating (1-5 scale)

**Monthly Metrics:**
- [ ] Total prescriptions issued (AI vs Manual)
- [ ] Average time per prescription
- [ ] Error rate (prescriptions requiring correction)
- [ ] System downtime/technical issues

**Quarterly Assessments:**
- [ ] Physician burnout score (Maslach Burnout Inventory)
- [ ] Patient satisfaction survey (random sample, n=100/quarter)
- [ ] Appointment wait time analysis

---

## 6. PRIMARY ENDPOINT MEASUREMENT

### 6.1 Medical Accuracy Assessment

**Gold Standard:** Physician manual prescription serves as reference

**AI Accuracy Scoring:**

Each AI-generated prescription evaluated on 5 criteria:
1. **Correct medication:** (Yes/No)
2. **Correct dosage:** (Yes/No)
3. **Correct duration:** (Yes/No)
4. **Contraindication check passed:** (Yes/No)
5. **Drug interaction warnings appropriate:** (Yes/No)

**Scoring:**
- 5/5 = 100% accuracy (perfect)
- 4/5 = 80% accuracy (minor edit required)
- ≤3/5 = <60% accuracy (major edit required, flagged for review)

**Non-inferiority criterion:** AI must achieve ≥95% perfect accuracy (5/5 score) across all prescriptions

### 6.2 Time Efficiency Measurement

**Time stamps recorded:**
- t₀: Clinical decision finalized (physician determines prescription needed)
- t₁: Prescription generation initiated
- t₂: Prescription review completed
- t₃: Prescription finalized and submitted to pharmacy

**Metrics:**
- **Manual workflow:** Δt = t₃ - t₀ (baseline)
- **AI workflow:** Δt = t₃ - t₀ (intervention)
- **Expected improvement:** ≥40% time reduction

**Example:**
- Manual: 90 seconds average
- AI-assisted: <55 seconds average (target)

---

## 7. SAFETY MONITORING

### 7.1 Safety Endpoints

**Primary safety endpoint:** Zero prescribing errors causing patient harm

**Safety categories:**

| Error Type | Severity | Action Required |
|------------|----------|-----------------|
| **Type 1: Non-clinical** (e.g., typo in patient name) | Low | Log only |
| **Type 2: Clinical minor** (e.g., incorrect tablet count) | Moderate | Physician correction, log |
| **Type 3: Clinical major** (e.g., wrong dosage, contraindication missed) | High | Immediate physician override, incident report, safety review |
| **Type 4: Critical** (e.g., life-threatening error) | Critical | Study pause, regulatory notification |

**Safety review frequency:**
- Weekly during pilot (Phase 2)
- Monthly during validation (Phase 3)
- Ad-hoc for any Type 3 or Type 4 errors

### 7.2 Stopping Rules

Study will be paused if ANY of the following occur:

1. **Type 4 error (critical):** Any life-threatening error attributable to AI system
2. **Error rate >10%:** AI accuracy falls below 90% for >2 consecutive weeks
3. **Physician safety concern:** Principal investigator deems system unsafe
4. **Patient harm:** Any adverse event directly linked to AI-generated documentation

**Resumption criteria:**
- Root cause analysis completed
- System updated/corrected
- Independent safety review approval

---

## 8. DATA MANAGEMENT

### 8.1 Data Collection

**Source:** Diraya EHR system + UMBRAMED logs

**Data elements:**
- Patient demographics (anonymized)
- Clinical data (diagnoses, medications, lab results)
- Process metrics (time stamps, physician edits)
- Outcome metrics (accuracy scores, error flags)

### 8.2 Data Privacy

**GDPR Compliance:**
- All data anonymized before analysis
- Patient identifiers removed (ID numbers replaced with study codes)
- Data stored on encrypted servers within EU
- Access restricted to study team only

**Patient consent:**
- This is a quality improvement study using retrospective EHR data
- No experimental interventions on patients
- Patients notified via clinic signage (opt-out available)

### 8.3 Data Quality Assurance

**Validation checks:**
- Random audit of 10% of prescriptions (manual verification)
- Monthly data completeness review
- Quarterly statistical analysis review

---

## 9. STATISTICAL ANALYSIS

### 9.1 Primary Analysis

**Non-inferiority test for accuracy:**

H₀: AI accuracy < 95% (inferior)  
H₁: AI accuracy ≥ 95% (non-inferior)

**Method:** One-sided confidence interval  
**Significance level:** α = 0.05  
**Power:** 80%

**Result interpretation:**
- If 95% CI lower bound > 95% → Non-inferiority demonstrated
- If 95% CI lower bound < 95% → Non-inferiority NOT demonstrated

### 9.2 Secondary Analyses

**Time efficiency:**
- Paired t-test (same physician, different workflows)
- Calculate mean time reduction and 95% CI

**Error rate reduction:**
- Chi-square test comparing error frequency between arms

**Physician satisfaction:**
- Wilcoxon signed-rank test (ordinal data)

### 9.3 Subgroup Analyses

Stratify results by:
- Patient age (<65 vs ≥65)
- Number of chronic medications (1-3 vs >3)
- Consultation complexity (simple renewal vs complex polymedication)

---

## 10. ETHICAL CONSIDERATIONS

### 10.1 Ethical Approval

**Ethics committee:** [LOCAL ETHICS COMMITTEE NAME]  
**Approval status:** Pending submission  
**Study classification:** Low-risk quality improvement study

**Justification for ethics exemption request:**
- No experimental intervention on patients
- Standard clinical care maintained (physician retains all decision-making)
- Retrospective data analysis component only
- Quality improvement focus (optimizing physician workflow)

### 10.2 Patient Rights

**Informed consent:** Not required (quality improvement study)

**Patient notifications:**
- Clinic signage: "We are testing AI tools to improve documentation efficiency"
- Opt-out available: Patients can request manual-only workflow
- Privacy protection: All data anonymized

### 10.3 Physician Autonomy

**Critical principle:** Physician maintains 100% clinical decision-making authority

- AI provides suggestions only
- Physician can override/edit/reject all AI outputs
- No pressure to accept AI recommendations
- No performance metrics tied to AI acceptance rate

---

## 11. REGULATORY COMPLIANCE

### 11.1 EU AI Act Compliance

**Classification:** High-risk AI system (healthcare application)

**Requirements:**
- ✅ Human oversight (physician review mandatory)
- ✅ Transparency (AI outputs clearly labeled)
- ✅ Data governance (GDPR compliant)
- ✅ Accuracy measurement (primary study endpoint)
- ✅ Robustness testing (safety monitoring)

### 11.2 Medical Device Regulation (MDR)

**Classification:** Class IIa medical device (clinical decision support)

**Pre-market requirements:**
- ✅ Clinical evaluation report (this study provides evidence)
- ✅ Risk management file (ISO 14971)
- ✅ Technical documentation
- ⏳ Notified Body review (pending)
- ⏳ CE marking (target: 12 months post-study)

### 11.3 Data Protection (GDPR)

**Data controller:** AGENTS AI Limited  
**Data processor:** Dr. Valerio Trigos (as Principal Investigator)

**GDPR compliance measures:**
- Data minimization (only necessary clinical data collected)
- Purpose limitation (research use only)
- Storage limitation (data deleted after regulatory retention period)
- Integrity and confidentiality (encryption, access controls)

---

## 12. STUDY TIMELINE

### Month 0-2: Preparation & Baseline
- [ ] Ethics committee submission
- [ ] UMBRAMED technical integration with Diraya
- [ ] Physician training on system use
- [ ] Baseline data collection (manual workflow)

### Month 3-8: Pilot Phase
- [ ] UMBRAMED deployed to 20% of patient panel
- [ ] Weekly safety reviews
- [ ] Iterative system refinement
- [ ] Collect pilot data

### Month 9-20: Validation Phase
- [ ] Expand to 80% of patient panel
- [ ] Monthly safety and quality reviews
- [ ] Full data collection for primary/secondary endpoints
- [ ] Quarterly physician burnout assessments

### Month 21-24: Analysis & Reporting
- [ ] Final data lock
- [ ] Statistical analysis
- [ ] Clinical study report preparation
- [ ] Submission to peer-reviewed journal
- [ ] Regulatory submission (CE marking dossier)

---

## 13. EXPECTED OUTCOMES

### 13.1 Primary Outcome

**Expected result:** AI accuracy ≥ 97% (exceeding non-inferiority threshold of 95%)

**Basis for expectation:**
- Similar systems in literature achieve 92-96% accuracy
- UMBRAMED is physician-built and tested in real Diraya workflow (higher ecological validity)
- Continuous physician oversight ensures error detection/correction

### 13.2 Secondary Outcomes

**Time efficiency:**
- Expected: 45-60% reduction in prescription renewal time
- Baseline: ~90 seconds/prescription
- Target: <50 seconds/prescription

**Physician satisfaction:**
- Expected: Burnout score improvement of ≥20%
- Basis: More time for direct patient care reduces administrative stress

**Error reduction:**
- Expected: 30-40% reduction in minor administrative errors
- Basis: AI consistency eliminates transcription errors, missed drug interactions

### 13.3 Clinical Impact

If results support non-inferiority:

**Patient level:**
- Shorter wait times for appointments (physician capacity increases)
- More face-to-face time during consultations
- Reduced prescription errors

**Physician level:**
- 1.5-2 hours/day returned for patient care
- Reduced burnout
- Improved job satisfaction

**Health system level:**
- Cost savings: €35-50K/year per physician (time value of saved administrative hours)
- Scalability: 44,000 physicians in Andalusia × €40K = €1.76B/year system-wide potential

---

## 14. DISSEMINATION PLAN

### 14.1 Scientific Publication

**Target journal:** British Medical Journal (BMJ) or JAMA Network Open  
**Timeline:** Submit within 6 months of study completion  
**Format:** Original research article

**Key messages:**
- AI-assisted clinical documentation is non-inferior to manual physician work
- Significant time savings achieved without compromising quality
- Real-world validation in public health system (not laboratory conditions)

### 14.2 Regulatory Submission

**Use of study results:**
- Clinical evaluation report for CE marking (MDR Annex XIV)
- Evidence package for EIC Accelerator grant application
- Basis for multi-center expansion studies

### 14.3 Stakeholder Communication

**Presentations:**
- Sistema Andaluz de Salud leadership
- European General Practice Research Network (EGPRN)
- EIC Accelerator interview (if selected)

---

## 15. STUDY GOVERNANCE

### 15.1 Principal Investigator Responsibilities

**Dr. Valerio Trigos Cervantes:**
- Overall study supervision
- Clinical safety oversight
- Data quality assurance
- Regulatory compliance
- Ethics committee liaison

### 15.2 Sponsor Responsibilities

**AGENTS AI Limited:**
- Funding
- UMBRAMED technical support
- Data management infrastructure
- Regulatory affairs support (CE marking process)

### 15.3 Independent Oversight

**Safety monitoring:** Monthly review by independent clinical advisor (TBD)  
**Data monitoring:** Quarterly statistical review by external biostatistician (TBD)

---

## 16. REFERENCES

1. Stanford Medicine Digital Health (2024). "AI-Assisted Clinical Documentation: A Randomized Trial." *JAMA Internal Medicine*, 184(3), 245-253.

2. European Commission (2025). "EU AI Act: Regulation (EU) 2024/1689." *Official Journal of the European Union*.

3. Maslach, C., & Jackson, S.E. (1981). "Maslach Burnout Inventory Manual." *Consulting Psychologists Press*.

4. ISO 14971:2019. "Medical devices — Application of risk management to medical devices."

5. European Health Data Space Pilot Programme (2025). "AI in Clinical Coding: Validation Study." *European Journal of Public Health*, 35(2), 112-120.

---

## 17. SIGNATURES

### Principal Investigator

**Name:** Dr. Valerio Trigos Cervantes, MD  
**License Number:** [Colegiado Number]  
**Institution:** Sistema Andaluz de Salud, Primary Care  
**Signature:** _____________________________  
**Date:** _____________________________

**Declaration:**
I confirm that I have reviewed this protocol and agree to conduct the study in accordance with:
- Good Clinical Practice (GCP) guidelines
- EU AI Act requirements
- Medical Device Regulation (MDR) 2017/745
- GDPR data protection principles
- Ethical standards of the Declaration of Helsinki

I accept full clinical responsibility for all patient care decisions and confirm that the AI system will serve only as a documentation assistant, with final clinical judgment remaining with the physician at all times.

---

### Study Sponsor

**Organization:** AGENTS AI Limited  
**Company Number:** [UK Company Registration]  
**Authorized Representative:** Sami Halawa, CTO  
**Signature:** _____________________________  
**Date:** _____________________________

**Declaration:**
AGENTS AI Limited commits to:
- Providing technical support for UMBRAMED system
- Ensuring GDPR-compliant data management
- Funding study costs
- Supporting regulatory submissions (CE marking, EIC application)
- Maintaining system availability and performance

---

## APPENDICES

### Appendix A: Data Collection Forms
[To be developed]

### Appendix B: Patient Information Sheet
[To be developed]

### Appendix C: System Usability Scale (SUS) Questionnaire
[Standard validated instrument]

### Appendix D: Maslach Burnout Inventory
[Licensed instrument - permission required]

### Appendix E: AI Output Examples
[Sample screenshots of UMBRAMED-generated prescriptions]

### Appendix F: Risk Management File
[ISO 14971 documentation]

---

**END OF PROTOCOL**

**Version:** 1.0  
**Date:** February 2026  
**Pages:** 17  
**Confidentiality:** For regulatory and grant application use only
