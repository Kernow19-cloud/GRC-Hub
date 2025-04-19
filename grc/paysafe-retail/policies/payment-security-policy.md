# PaySafe Retail Payment Security Policy (PCI-DSS v4.0.0)

## Overview
This policy ensures **PaySafe Retail**, a fictional mid-sized e-commerce retailer processing 3 million card transactions annually, complies with **PCI-DSS v4.0.0** to secure cardholder data in its cardholder data environment (CDE). It outlines security measures, responsibilities, and enforcement for maintaining compliance. See the [PCI-DSS Fundamentals](../compliance/pci-dss-fundamentals.md) for requirement details and the [Implementation Plan](../implementation/pci-dss-plan.md) for execution steps.

## Key Requirements
This policy addresses the following PCI-DSS v4.0.0 requirements:

1. **Network Security (Requirement 1)**:
   - Deploy firewalls to restrict traffic to TCP ports 443 and 22.
   - Implement network segmentation using VLANs to isolate the CDE.

2. **Data Protection (Requirement 3)**:
   - Encrypt stored cardholder data with AES-256.
   - Use tokenization to replace primary account numbers (PAN).

3. **Transmission Security (Requirement 4)**:
   - Secure data transmission over public networks with TLS 1.3.

4. **Access Control (Requirements 7, 8)**:
   - Implement role-based access control (RBAC) to limit CDE access.
   - Require multi-factor authentication (MFA) for all CDE access.

5. **Monitoring (Requirement 10)**:
   - Conduct daily log reviews using a Security Information and Event Management (SIEM) system.
   - Monitor all access to cardholder data and network resources.

6. **Testing (Requirement 11)**:
   - Perform quarterly vulnerability scans.
   - Conduct annual penetration tests by qualified third parties.

## Responsibilities
- **IT Security Team**: Configures and maintains technical controls (e.g., firewalls, encryption).
- **Compliance Officer**: Oversees PCI-DSS assessments and documentation.
- **Employees**: Complete annual PCI-DSS training and adhere to security policies.

## Enforcement
- Violations of this policy, such as unauthorized CDE access or failure to follow procedures, may result in disciplinary action, including termination.
- Regular audits ensure compliance with this policy.

## Notes
- This is a **fictional** policy for educational and portfolio purposes.
- Compliance is validated via Self-Assessment Questionnaire (SAQ) for Level 2 merchants.

[Back to PaySafe Retail PCI-DSS Project](../readme.md)

*Last updated: April 2025*
