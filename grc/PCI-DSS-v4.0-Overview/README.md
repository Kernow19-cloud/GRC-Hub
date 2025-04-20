# Payment Card Industry Data Security Standard (PCI-DSS) v4.0 Overview

This directory provides a general overview of the [Payment Card Industry Data Security Standard (PCI-DSS) version 4.0](https://www.pcisecuritystandards.org/document_library/?category=pcidss&document=pci_dss), a global security standard for entities that store, process, or transmit cardholder data. PCI-DSS v4.0 was released on March 31, 2022, with full enforcement starting April 1, 2024, and additional requirements becoming mandatory by March 31, 2025.

## Purpose
The PCI-DSS v4.0 standard aims to enhance the security of cardholder data by addressing modern threats and evolving payment technologies. It provides a baseline of technical and operational requirements to protect payment account data, reduce fraud, and build trust in the payment ecosystem.

## Key Updates in PCI-DSS v4.0
PCI-DSS v4.0 introduces several updates over previous versions to meet the changing needs of the payment industry:
- **Customized Approach**: Organizations can now use alternative controls to meet requirements, offering flexibility for new technologies. [Learn more](https://blog.pcisecuritystandards.org/pci-dss-v4-0-resource-hub)
- **Enhanced Requirements**: 64 new requirements were added, with some considered best practices until March 31, 2025, after which they become mandatory.
- **Focus on Continuous Security**: Emphasis on ongoing monitoring, testing, and updating of security measures.
- **E-commerce Security**: New guidance for e-commerce merchants, such as Requirements 6.4.3 and 11.6.1 for payment page security and preventing e-skimming. [See guidance](https://www.pcisecuritystandards.org/)
- **Multi-Factor Authentication (MFA)**: MFA is now required for all access to the cardholder data environment (CDE), including internal network access.

## The 12 Requirements of PCI-DSS v4.0
PCI-DSS v4.0 is structured around 12 core requirements, grouped into six objectives:
1. **Build and Maintain a Secure Network and Systems**
   - Install and maintain network security controls.
   - Apply secure configurations to all system components.
2. **Protect Cardholder Data**
   - Protect stored account data.
   - Protect cardholder data with strong cryptography during transmission over open, public networks.
3. **Maintain a Vulnerability Management Program**
   - Protect all systems and networks from malicious software.
   - Develop and maintain secure systems and software.
4. **Implement Strong Access Control Measures**
   - Restrict access to system components and cardholder data by business need-to-know.
   - Identify users and authenticate access to system components.
   - Restrict physical access to cardholder data.
5. **Regularly Monitor and Test Networks**
   - Track and monitor all access to network resources and cardholder data.
   - Regularly test security systems and processes.
6. **Maintain an Information Security Policy**
   - Maintain a policy that addresses information security for all personnel.

## Compliance Levels
PCI-DSS compliance levels are based on transaction volume over a 12-month period:
- **Level 1**: Over 6 million transactions annually (requires a Report on Compliance by a Qualified Security Assessor).
- **Level 2**: 1 to 6 million transactions (requires a Self-Assessment Questionnaire, may need quarterly scans).
- **Level 3**: 20,000 to 1 million transactions (requires a Self-Assessment Questionnaire, may need quarterly scans).
- **Level 4**: Fewer than 20,000 transactions (requires a Self-Assessment Questionnaire, may need quarterly scans).

## Directory Structure
