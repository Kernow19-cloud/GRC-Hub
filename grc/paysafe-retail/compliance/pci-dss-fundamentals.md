# PCI-DSS Fundamentals for PaySafe Retail

## Overview
This document outlines the fundamentals of **PCI-DSS v4.0.0** for **PaySafe Retail**, a fictional mid-sized e-commerce retailer processing 3 million card transactions annually. As a Level 2 merchant, PaySafe Retail must comply with PCI-DSS to secure cardholder data in its cardholder data environment (CDE).

## PCI-DSS v4.0.0 Requirements
The Payment Card Industry Data Security Standard (PCI-DSS) v4.0.0 consists of 12 requirements organised into six control objectives:

1. **Build and Maintain a Secure Network and Systems**
   - **Requirement 1**: Install and maintain network security controls (e.g., firewalls, segmentation).
   - **Requirement 2**: Apply secure configurations to systems (e.g., remove default passwords).

2. **Protect Account Data**
   - **Requirement 3**: Protect stored account data (e.g., encryption, tokenisation).
   - **Requirement 4**: Protect account data over open networks (e.g., TLS 1.3).

3. **Maintain a Vulnerability Management Program**
   - **Requirement 5**: Protect systems from malware (e.g., antivirus software).
   - **Requirement 6**: Develop and maintain secure systems (e.g., patch management).

4. **Implement Strong Access Control Measures**
   - **Requirement 7**: Restrict access based on need-to-know (e.g., role-based access control).
   - **Requirement 8**: Authenticate access to systems (e.g., multi-factor authentication).
   - **Requirement 9**: Restrict physical access to account data.

5. **Regularly Monitor and Test Networks**
   - **Requirement 10**: Monitor access to resources (e.g., SIEM for log analysis).
   - **Requirement 11**: Test security controls (e.g., quarterly scans, penetration tests).

6. **Maintain an Information Security Policy**
   - **Requirement 12**: Support information security with policies (e.g., annual training).

## Application to PaySafe Retail
PaySafe Retail implements these requirements through policies, technical controls, and assessments, as detailed in:
- [Payment Security Policy](../policies/payment-security-policy.md)
- [Implementation Plan](../implementation/pci-dss-plan.md)
- [Network Security Measures](../network-security/security-measures.md)

## Notes
- This is a **fictional** project for educational and portfolio purposes.
- Compliance is validated via the Self-Assessment Questionnaire (SAQ) for Level 2 merchants.

[Back to PaySafe Retail PCI-DSS Project](../readme.md)

*Last updated: April 2025*

