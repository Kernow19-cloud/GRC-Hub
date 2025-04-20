# Data Processing Agreements (DPAs)

## Overview
This document provides a template and guidelines for Data Processing Agreements (DPAs) to ensure compliance with the General Data Protection Regulation (GDPR) Article 28. DPAs are required when engaging third-party processors to handle personal data on behalf of the organization, addressing gaps identified in the [GDPR Gap Analysis](./GDPR_Gap_Analysis.md) regarding missing or incomplete DPAs with vendors.

## Purpose
A DPA establishes the responsibilities of the data controller (the organization) and the data processor (the third party) to ensure that personal data is processed in compliance with GDPR, protecting the rights of data subjects.

## DPA Template

### 1. Parties
- **Data Controller**: [Organization Name], located at [Address], acting as the controller of personal data.
- **Data Processor**: [Third-Party Name], located at [Address], acting as the processor on behalf of the controller.

### 2. Scope of Processing
- **Purpose**: [e.g., "To provide cloud storage services for customer data."]
- **Data Types**: [e.g., Names, email addresses, purchase history.]
- **Data Subjects**: [e.g., EU customers, employees.]
- **Duration**: [e.g., "For the duration of the service contract, ending on [date], with data deletion within 30 days thereafter."]

### 3. Obligations of the Data Processor
- **Compliance**: Process personal data only on documented instructions from the controller, as outlined in this DPA.
- **Security**: Implement appropriate technical and organizational measures to ensure data security (e.g., encryption, access controls), as referenced in the [Privacy Policies](./Privacy_Policies.md).
- **Sub-Processors**: Obtain prior written consent from the controller before engaging sub-processors; ensure sub-processors are bound by similar GDPR-compliant agreements.
- **Data Subject Requests**: Assist the controller in fulfilling [Data Subject Access Requests (DSARs)](./DSAR_Process.md) within the required timelines.
- **Breach Notification**: Notify the controller without undue delay (within 48 hours) of becoming aware of a data breach, following procedures in the [Privacy Policies](./Privacy_Policies.md).
- **Audits**: Allow the controller to conduct audits and inspections to verify GDPR compliance, providing access to relevant records and facilities.
- **Data Deletion**: Delete or return all personal data to the controller at the end of the contract, unless required by law to retain it.

### 4. Obligations of the Data Controller
- **Instructions**: Provide clear and lawful instructions for processing personal data.
- **Compliance**: Ensure the processing activities comply with GDPR, as assessed in the [GDPR Gap Analysis](./GDPR_Gap_Analysis.md).
- **Risk Assessment**: Conduct a [Data Protection Impact Assessment (DPIA)](./DPIA_Template.md) for high-risk processing involving the processor, if applicable.

### 5. Liability
- The processor shall be liable for any GDPR violations caused by its actions or those of its sub-processors.
- The controller and processor shall cooperate to address any claims from data subjects or supervisory authorities.

### 6. Governing Law
- This DPA is governed by the laws of [Jurisdiction, e.g., "the European Union and the member state of [Country]"].

### 7. Signatures
- **Data Controller**: [Name, Title, Signature, Date]
- **Data Processor**: [Name, Title, Signature, Date]

## Guidelines for Implementation
1. **Vendor Assessment**:
   - Identify all third-party processors handling personal data (e.g., cloud providers, marketing platforms).
   - Verify their GDPR compliance status through questionnaires or certifications.
2. **DPA Customization**:
   - Tailor the template above to each vendor, specifying the scope, data types, and security measures.
   - Include additional clauses as needed (e.g., for international data transfers under GDPR Chapter V).
3. **Training**:
   - Train procurement and legal teams on DPA requirements using [Training Materials](./Training_Materials.md).
4. **Monitoring**:
   - Regularly audit processors to ensure compliance, as outlined in the [gdpr/README.md](../gdpr/README.md).
   - Review DPAs annually or upon contract renewal.

## Addressing Gaps
- The [GDPR Gap Analysis](./GDPR_Gap_Analysis.md) identified missing DPAs with some vendors. This template will be used to draft and sign agreements with all processors by Month 2.
- Ensure processors are aware of breach notification procedures in the [Privacy Policies](./Privacy_Policies.md) to meet GDPR timelines.

## Responsible Teams
- **Legal Team**: Drafts and negotiates DPAs with third parties.
- **Compliance Team**: Monitors vendor compliance and conducts audits.
- **Procurement Team**: Identifies vendors and ensures DPAs are in place before contracts are signed.
- **Data Protection Officer (DPO)**: Approves DPAs and oversees GDPR compliance.

## Next Steps
- **Timeline**: Complete DPAs with all vendors by Month 2, as per the [gdpr/README.md](../gdpr/README.md).
- **Documentation**: Maintain a register of all DPAs for compliance audits.
