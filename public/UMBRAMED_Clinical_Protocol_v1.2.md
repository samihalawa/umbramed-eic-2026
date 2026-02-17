# CLINICAL STUDY PROTOCOL
## UMBRAMED AI-Assisted Clinical Documentation System
### Validation Study in Primary Care Setting

---

## PROTOCOL IDENTIFICATION

**Protocol Title:**  
Comparative Effectiveness Study of AI-Assisted vs. Manual Clinical Documentation in Primary Care: A Multi-Centre Case-Control Trial

**Protocol Version:** 1.2  
**Date:** February 2026  
**Sponsor:** AGENTS AI Limited (UK)  
**Clinical Lead:** Dr. Valerio Trigos, MD  
**Institution:** Sistema Andaluz de Salud (SAS), Andalusia, Spain

**Study Registration:**  
(To be registered upon funding approval: ClinicalTrials.gov / EU Clinical Trials Register)

---

## EXECUTIVE SUMMARY

### Study Objectives

**Primary Objective:**  
To demonstrate non-inferiority of AI-assisted clinical documentation (UMBRAMED) compared to manual documentation in terms of time efficiency and clinical accuracy in primary care prescription renewal workflows.

**Secondary Objectives:**
1. Measure reduction in administrative time per patient consultation
2. Assess medication error rates in AI-assisted vs manual workflows
3. Evaluate physician satisfaction and cognitive workload
4. Quantify patient wait time improvements
5. Measure system adoption and usability metrics

---

### Study Design

**Type:** Prospective, multi-centre, case-control study  
**Setting:** Three primary care centres in Andalusia, Spain  
**Duration:** 18 months (6-month pilot + 12-month validation)  
**Sample Size:** 6,500 patients across intervention and control groups  
**Intervention:** UMBRAMED AI-powered clinical assistant integrated with Diraya EHR  
**Control:** Standard manual documentation workflow in Diraya  

---

## 1. BACKGROUND & RATIONALE

### 1.1 Clinical Problem

European primary care physicians spend 30-45% of clinical time on administrative tasks, including:
- Prescription renewals for chronic conditions
- Clinical note generation
- Referral form completion
- Discharge summary preparation

In the Andalusian public health system:
- Average patient panel: 1,500-2,000 patients per physician
- Average consultations: 35-50 per day
- Administrative overhead: 3-7 minutes per consultation
- Medication error rate (manual entry): ~12%

**Clinical Impact:**
- Delayed patient access (7-15 day wait times)
- Physician burnout (>50% reporting symptoms)
- Preventable medication errors
- Reduced time for patient-physician interaction

### 1.2 Proposed Solution

UMBRAMED is an AI-powered clinical assistant that:
- Integrates directly with Diraya EHR system
- Uses fine-tuned large language models trained on European medical protocols
- Automates prescription renewals based on patient history
- Generates clinical notes using SNOMED-CT and ICD-10 standards
- Pre-fills referral forms following clinical guidelines
- Maintains full physician oversight and approval

### 1.3 Regulatory Framework

**Classification:** Class IIa Medical Device (EU MDR 2017/745)  
**Data Protection:** GDPR-compliant, ISO 27001 certified infrastructure  
**Clinical Evidence Required:** Conformity assessment per Annex XIV of MDR  

This study provides the clinical evidence required for CE marking under EU MDR.

---

## 2. STUDY POPULATION

### 2.1 Inclusion Criteria

**Physician Criteria:**
- Licensed family physician in Sistema Andaluz de Salud
- Minimum 2 years experience using Diraya EHR
- Active patient panel of 1,000+ patients
- Voluntary participation with informed consent

**Patient Criteria:**
- Registered in Diraya EHR system
- Minimum one chronic condition requiring prescription renewal
- Age ≥18 years
- Consent to data use for research (anonymized)

### 2.2 Exclusion Criteria

**Physician Exclusion:**
- Temporary contract physicians (<6 months tenure)
- Physicians with planned leave during study period
- Refusal to participate in training program

**Patient Exclusion:**
- Complex polypharmacy (>10 active medications)
- Cognitive impairment affecting medication adherence
- Patients explicitly refusing AI-assisted care

### 2.3 Sample Size Calculation

**Primary Endpoint:** Time per prescription renewal task

**Assumptions:**
- Mean time (manual): 4.5 minutes
- Expected time (AI-assisted): 1.5 minutes
- Standard deviation: 2.0 minutes
- Non-inferiority margin: 0.5 minutes
- Power: 90%
- Alpha: 0.05

**Calculated Sample Size:**
- Intervention group: 3,250 patients
- Control group: 3,250 patients
- Total: 6,500 patients

**Justification:**  
Dr. Valerio Trigos manages a panel of 6,500 patients, providing sufficient sample size with single-physician consistency.

---

## 3. STUDY METHODOLOGY

### 3.1 Study Sites

**Site 1 (Primary):**
- Centro de Salud [Anonymized], Andalusia
- Lead Investigator: Dr. Valerio Trigos
- Patient panel: 6,500
- Diraya EHR version: Current production

**Site 2 (Validation):**
- Centro de Salud [Partner Site 1]
- Co-Investigator: [TBD]
- Patient panel: 2,000

**Site 3 (Validation):**
- Centro de Salud [Partner Site 2]
- Co-Investigator: [TBD]
- Patient panel: 2,000

### 3.2 Study Phases

#### Phase 1: Baseline Data Collection (Months 1-2)
- Collect retrospective data on manual workflow
- Measure current time metrics per task type
- Establish baseline error rates
- Document current physician workload

#### Phase 2: Pilot Implementation (Months 3-8)
- UMBRAMED deployment at Site 1 only
- Physician training (20 hours over 4 weeks)
- Limited deployment (500 patients)
- System refinement based on feedback
- Safety monitoring

#### Phase 3: Full Deployment (Months 9-14)
- Rollout to all 6,500 patients at Site 1
- Deploy to Sites 2 and 3
- Full data collection protocol active
- Weekly safety reviews

#### Phase 4: Data Analysis (Months 15-18)
- Statistical analysis of primary/secondary endpoints
- Qualitative physician feedback analysis
- Final safety assessment
- Regulatory documentation preparation

### 3.3 Intervention Protocol

**UMBRAMED Workflow:**

1. **Patient Context Loading (Automated):**
   - System retrieves patient record from Diraya
   - Extracts active medications, diagnoses, lab results
   - Identifies chronic conditions requiring renewal

2. **AI Processing (5-15 seconds):**
   - Large language model analyzes patient context
   - Generates prescription renewal recommendations
   - Flags potential drug interactions or contraindications
   - Pre-fills Diraya prescription forms

3. **Physician Review (30-60 seconds):**
   - Physician reviews AI-generated output
   - Modifies dosages or medications if needed
   - Approves or rejects recommendations
   - Signs prescription in Diraya

4. **Learning Loop (Continuous):**
   - System logs physician edits
   - Retrains model on corrections
   - Improves future recommendations

**Control Workflow:**

1. Physician manually reviews patient record
2. Manually types prescription details into Diraya
3. Manually checks for drug interactions
4. Manually signs prescription

### 3.4 Data Collection

**Primary Endpoint Metrics:**
- Time per prescription renewal (seconds, measured via Diraya logs)
- Clinical accuracy (medication errors per 1,000 renewals)

**Secondary Endpoint Metrics:**

*Time Efficiency:*
- Total administrative time per consultation
- Time to complete referral forms
- Time to generate clinical notes
- Time to draft discharge summaries

*Clinical Quality:*
- Medication error rate (wrong dose, wrong drug, contraindications)
- Guideline adherence rate
- Completeness of clinical documentation

*Physician Experience:*
- NASA Task Load Index (cognitive workload)
- System Usability Scale (SUS score)
- Physician satisfaction questionnaire (5-point Likert)

*Patient Impact:*
- Average wait time for appointments
- Patient satisfaction scores
- Medication adherence rates

*System Performance:*
- System uptime and reliability
- AI recommendation acceptance rate
- Time to process each task

### 3.5 Data Sources

**Automated Collection from Diraya:**
- Timestamp logs (consultation start, task start, task end)
- Prescription details (medication, dose, duration)
- Error flags (duplicate prescriptions, contraindications)
- Edit history (physician modifications to AI output)

**Manual Collection:**
- Weekly physician workload surveys
- Monthly safety reviews
- Quarterly usability assessments
- Patient satisfaction surveys (optional, anonymized)

**Anonymization Protocol:**
- All patient identifiers removed before analysis
- Data stored in GDPR-compliant encrypted database
- Access restricted to study investigators only

---

## 4. STATISTICAL ANALYSIS PLAN

### 4.1 Primary Analysis

**Non-Inferiority Test:**
- Null hypothesis: AI-assisted time ≥ Manual time + 0.5 minutes
- Alternative hypothesis: AI-assisted time < Manual time + 0.5 minutes
- Statistical test: One-sided t-test
- Significance level: α = 0.05

**Superiority Analysis (if non-inferiority proven):**
- Two-sided t-test comparing mean times
- Effect size calculation (Cohen's d)

### 4.2 Secondary Analyses

**Medication Error Rates:**
- Chi-square test comparing error rates between groups
- Relative risk calculation with 95% CI

**Physician Workload:**
- Paired t-test for NASA-TLX scores (pre vs post)
- Wilcoxon signed-rank test for ordinal satisfaction data

**Subgroup Analyses:**
- Stratification by patient age groups (<65, ≥65)
- Stratification by number of chronic conditions (1, 2, 3+)
- Stratification by medication complexity (simple vs complex)

### 4.3 Interim Analysis

**Safety Monitoring:**
- Weekly review of medication error rates
- Stopping rule: If error rate >15% in intervention group

**Futility Analysis (Month 12):**
- If AI-assisted time shows no improvement trend, consider protocol modification

---

## 5. ETHICAL & REGULATORY CONSIDERATIONS

### 5.1 Ethics Approval

**Institutional Review Board:**
- Comité de Ética de Investigación Clínica (CEIC), Andalusia
- Application submitted: [TBD upon grant approval]
- Expedited review anticipated (minimal risk study)

**Participant Consent:**
- Physician consent: Written informed consent required
- Patient consent: Waiver requested (retrospective anonymized data analysis)
- Right to withdraw: Physicians may withdraw at any time without penalty

### 5.2 Data Protection

**GDPR Compliance:**
- Data Processing Agreement with Sistema Andaluz de Salud
- Data Protection Impact Assessment (DPIA) completed
- Patient data never leaves Diraya environment
- Only aggregated, anonymized data exported for analysis

**Data Security:**
- ISO 27001 certified infrastructure
- End-to-end encryption for all data transmission
- Role-based access control
- Audit logs for all system access

### 5.3 Patient Safety

**Risk Mitigation:**
- Physician retains full override authority
- AI recommendations clearly labeled as "suggestions"
- Mandatory physician review before prescription signing
- Real-time contraindication checking
- Immediate reporting of any adverse events

**Adverse Event Protocol:**
- Any medication error attributed to AI → 24-hour report to Clinical Lead
- Serious adverse events → immediate system suspension
- Monthly safety committee review

### 5.4 Regulatory Compliance

**EU Medical Device Regulation (MDR 2017/745):**
- Clinical evaluation per Annex XIV
- Post-market surveillance plan
- Technical documentation maintenance
- Conformity assessment by Notified Body

**Spanish Health Authority:**
- Notification to Agencia Española de Medicamentos y Productos Sanitarios (AEMPS)
- Compliance with Spanish data protection laws
- Integration approval from Sistema Andaluz de Salud

---

## 6. CLINICAL GOVERNANCE

### 6.1 Study Leadership

**Principal Investigator:**
- Dr. Valerio Trigos, MD
- Family Physician, Sistema Andaluz de Salud
- 6,500-patient panel, 8+ years Diraya experience
- Responsibilities: Clinical oversight, safety monitoring, data interpretation

**Sponsor Representative:**
- Sami Halawa, CEO, AGENTS AI Limited
- Responsibilities: Study coordination, technical implementation, regulatory compliance

**Data Safety Monitoring Committee (DSMC):**
- Independent physician (TBD)
- Biostatistician (TBD)
- Patient representative (TBD)
- Meets quarterly to review safety data

### 6.2 Training Requirements

**Physician Training (20 hours):**
- Week 1: UMBRAMED interface and workflow (4 hours)
- Week 2: AI recommendation interpretation (4 hours)
- Week 3: Safety protocols and error reporting (4 hours)
- Week 4: Hands-on practice with test patients (8 hours)

**Certification:**
- Competency assessment at end of training
- Annual refresher training required

### 6.3 Quality Assurance

**Regular Audits:**
- Monthly data quality checks
- Quarterly protocol compliance review
- Annual external audit by independent assessor

**Protocol Deviations:**
- All deviations logged and reported to CEIC
- Major deviations → protocol amendment required

---

## 7. EXPECTED OUTCOMES

### 7.1 Primary Outcome

**Time Efficiency:**
- Expected reduction: 60-70% in prescription renewal time
- From ~4.5 minutes (manual) to ~1.5 minutes (AI-assisted)
- Translates to 30-45 minutes saved per physician per day

### 7.2 Secondary Outcomes

**Clinical Quality:**
- Medication error rate: <5% (vs ~12% baseline)
- Guideline adherence: >95%

**Physician Experience:**
- Reduced cognitive workload (NASA-TLX reduction >20%)
- System usability: SUS score >80 (excellent)
- Physician satisfaction: >4.0/5.0 average

**Patient Impact:**
- Wait time reduction: 15-20%
- Improved medication adherence
- Higher patient satisfaction

### 7.3 Health Economic Impact

**Per Physician (6,500 patients):**
- Time saved: 30-45 minutes/day = 125-188 hours/year
- Additional patient capacity: 1,000-1,500 consultations/year
- Cost savings: €15,000-€25,000/year (reduced overtime, locum costs)

**System-Wide (44,000 physicians in Andalusia):**
- Total time saved: 5.5-8.3 million hours/year
- Additional capacity: 44-66 million consultations/year
- Total cost savings: €660M-€1.1B/year

---

## 8. DISSEMINATION PLAN

### 8.1 Scientific Publications

**Target Journals:**
- BMJ Health & Care Informatics
- The Lancet Digital Health
- Journal of Medical Internet Research (JMIR)
- European Journal of General Practice

**Conference Presentations:**
- European General Practice Research Network (EGPRN)
- WONCA Europe Conference
- AI in Healthcare Summit

### 8.2 Regulatory Submissions

**CE Marking Application:**
- Clinical evaluation report based on study results
- Submission to Notified Body within 6 months of study completion

**Post-Market Surveillance:**
- Ongoing safety monitoring
- Annual summary of safety and performance report

### 8.3 Public Communication

- Press release upon study completion
- Webinar for Spanish medical community
- Open-access publication of anonymized dataset

---

## 9. BUDGET & RESOURCES

### 9.1 Funding Requirements

**Personnel:**
- Principal Investigator time: €45,000
- Co-investigators: €30,000
- Data analyst: €25,000
- Study coordinator: €35,000

**Technology:**
- UMBRAMED development & deployment: €150,000
- Diraya integration & maintenance: €40,000
- Data infrastructure: €30,000

**Operations:**
- Physician training: €20,000
- Ethics & regulatory approvals: €15,000
- Data management & quality assurance: €25,000
- External audit: €10,000

**Dissemination:**
- Publication costs: €5,000
- Conference presentations: €10,000

**Total Budget:** €440,000 (covered by EIC Accelerator €2.5M grant)

### 9.2 Timeline

| Phase | Duration | Key Milestones |
|-------|----------|----------------|
| Ethics Approval | Months 1-2 | CEIC submission & approval |
| Baseline Data | Months 1-2 | Retrospective data collection |
| Pilot Implementation | Months 3-8 | 500-patient pilot, system refinement |
| Full Deployment | Months 9-14 | 6,500-patient rollout, data collection |
| Data Analysis | Months 15-18 | Statistical analysis, manuscript preparation |
| Regulatory Submission | Month 18+ | CE marking application |

---

## 10. RISK ASSESSMENT & MITIGATION

### 10.1 Technical Risks

**Risk:** AI system downtime affects patient care  
**Mitigation:** Fallback to manual workflow, 99.9% uptime SLA, redundant systems

**Risk:** Integration issues with Diraya updates  
**Mitigation:** Dedicated integration team, regression testing, SAS IT collaboration

### 10.2 Clinical Risks

**Risk:** Increased medication errors  
**Mitigation:** Real-time contraindication checking, mandatory physician review, weekly safety monitoring

**Risk:** Physician resistance to AI adoption  
**Mitigation:** Extensive training, gradual rollout, continuous feedback loops

### 10.3 Regulatory Risks

**Risk:** CEIC approval delayed  
**Mitigation:** Pre-submission consultation, expedited review request

**Risk:** Post-study CE marking delays  
**Mitigation:** Early engagement with Notified Body, parallel documentation preparation

---

## 11. CLINICAL LEAD DECLARATION

I, Dr. Valerio Trigos, hereby declare that:

1. I will serve as Principal Investigator for this clinical study
2. I have access to a panel of 6,500 patients in the Sistema Andaluz de Salud
3. I have institutional approval to conduct this research (pending CEIC approval)
4. I will ensure patient safety remains the primary priority throughout the study
5. I will oversee all clinical aspects of the UMBRAMED validation
6. I will report all adverse events and protocol deviations promptly
7. I have no conflicts of interest beyond my co-founder role in AGENTS AI Limited

**Signature:** _________________________  
**Dr. Valerio Trigos, MD**  
**Family Physician, Sistema Andaluz de Salud**  
**Clinical Lead, UMBRAMED Study**  
**Date:** _________________________

---

## 12. SPONSOR DECLARATION

AGENTS AI Limited commits to:

1. Provide full funding for this clinical study (via EIC Accelerator grant)
2. Maintain UMBRAMED system throughout study duration
3. Ensure GDPR and MDR compliance
4. Support regulatory submissions for CE marking
5. Publish study results regardless of outcome

**Signature:** _________________________  
**Sami Halawa**  
**Chief Executive Officer, AGENTS AI Limited**  
**Date:** _________________________

---

## APPENDICES

### Appendix A: Data Collection Forms
(To be developed upon grant approval)

### Appendix B: Physician Training Materials
(To be developed upon grant approval)

### Appendix C: Patient Information Sheet
(To be developed upon grant approval)

### Appendix D: GDPR Data Processing Agreement
(To be finalized with Sistema Andaluz de Salud)

### Appendix E: Safety Monitoring Plan
(Detailed protocol for adverse event reporting)

---

**END OF PROTOCOL**

**Version:** 1.2  
**Date:** February 2026  
**Next Review:** Upon CEIC feedback
