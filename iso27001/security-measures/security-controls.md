# Security Controls

## Overview
This document outlines the security controls implemented as part of the ISO 27001 Information Security Management System (ISMS) within the GRC-Hub project. The controls are selected from ISO 27001 Annex A (aligned with ISO 27002) based on the risk assessment and Statement of Applicability (SoA). These measures protect the confidentiality, integrity, and availability of information assets.

## Control Selection Process
- **Risk Assessment**: Controls are identified based on risks outlined in the [Risk Assessment Report](./Risk_Assessment_Report.md).
- **Statement of Applicability (SoA)**: The applicability and implementation status of each control are documented in the [Statement of Applicability (SoA)](./Statement_of_Applicability.md).
- **Training**: Employees are trained on these controls using the [Security Awareness Training](./Security_Awareness_Training.md).

## Security Controls by Domain

### 1. Information Security Policies (A.5)
- **A.5.1.1 - Policies for Information Security**: Develop and approve information security policies to guide the ISMS.
  - **Implementation**: Policies are documented and communicated to all employees.
  - **Reference**: See the [Security Awareness Training](./Security_Awareness_Training.md) for policy training.

### 2. Human Resource Security (A.7)
- **A.7.2.2 - Information Security Awareness, Education, and Training**: Ensure all employees receive regular security training.
  - **Implementation**: Annual training sessions conducted, with materials in the [Security Awareness Training](./Security_Awareness_Training.md).
- **A.7.3.1 - Termination or Change of Employment Responsibilities**: Remove access rights upon termination.
  - **Implementation**: Access removal process in place, aligned with the [Access Control Policy](./Access_Control_Policy.md).

### 3. Asset Management (A.8)
- **A.8.1.1 - Inventory of Assets**: Maintain an inventory of all information assets.
  - **Implementation**: Asset inventory documented in the [Asset Inventory](./Asset_Inventory.md).
- **A.8.2.1 - Classification of Information**: Classify information based on sensitivity (e.g., public, confidential).
  - **Implementation**: Classification guidelines established and communicated.

### 4. Access Control (A.9)
- **A.9.1.2 - Access to Networks and Network Services**: Restrict network access to authorized users.
  - **Implementation**: Role-based access controls implemented, detailed in the [Access Control Policy](./Access_Control_Policy.md).
- **A.9.4.1 - Information Access Control**: Use strong passwords and multi-factor authentication (MFA).
  - **Implementation**: MFA enforced for all critical systems.

### 5. Incident Management (A.16)
- **A.16.1.2 - Reporting Information Security Events**: Require employees to report security incidents promptly.
  - **Implementation**: Incident reporting process outlined in the [Incident Response Plan](./Incident_Response_Plan.md).
- **A.16.1.5 - Response to Information Security Incidents**: Respond to incidents in a timely manner.
  - **Implementation**: Response procedures documented in the [Incident Response Plan](./Incident_Response_Plan.md).

### 6. Compliance (A.18)
- **A.18.1.1 - Identification of Applicable Legislation**: Ensure compliance with relevant laws (e.g., GDPR).
  - **Implementation**: Legal requirements reviewed during risk assessment, per the [Risk Assessment Report](./Risk_Assessment_Report.md).
- **A.18.2.1 - Independent Review of Information Security**: Conduct regular internal audits of the ISMS.
  - **Implementation**: Audit schedule planned for Months 10-12, as per the [security-measures/README.md](../security-measures/README.md).

## Implementation Status
| **Control**          | **Domain**         | **Status**      | **Responsible Team** |
|----------------------|--------------------|-----------------|----------------------|
| A.5.1.1             | Policies           | Implemented     | InfoSec Team         |
| A.7.2.2             | HR Security        | Implemented     | HR Team              |
| A.8.1.1             | Asset Management   | In Progress     | IT Team              |
| A.9.1.2             | Access Control     | Implemented     | IT Team              |
| A.16.1.2            | Incident Management| In Progress     | Security Team        |
| A.18.1.1            | Compliance         | Implemented     | Compliance Team      |

## Next Steps
- **Timeline**: Full implementation of controls by Month 9, as outlined in the [security-measures/README.md](../security-measures/README.md).
- **Monitoring**: Regularly review control effectiveness through internal audits.
- **Training**: Ensure all employees are trained on controls, using the [Security Awareness Training](./Security_Awareness_Training.md).

## Responsible Teams
- **Information Security Team**: Oversees control implementation and monitoring.
- **IT Team**: Implements technical controls (e.g., access controls, asset inventory).
- **HR Team**: Manages training and employee-related controls.
- **Security Team**: Handles incident response and monitoring.
