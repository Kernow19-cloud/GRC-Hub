# Overview of PCI-DSS v4.0 Requirements for PaySafe Retail

This document provides an overview of the [Payment Card Industry Data Security Standard (PCI-DSS) version 4.0](https://www.pcisecuritystandards.org/document_library/?category=pcidss&document=pci_dss) requirements as they apply to the PaySafe Retail PCI-DSS v4.0 Compliance Project. PCI-DSS v4.0 is a global standard for securing cardholder data, and PaySafe Retail aims to achieve compliance by March 31, 2025.

## Purpose
Understanding the 12 core requirements of PCI-DSS v4.0 is essential for PaySafe Retail to secure its payment processing systems, e-commerce platforms, and point-of-sale (POS) environments. This overview aligns with the project's goal to protect cardholder data and reduce fraud risks.

## The 12 Requirements of PCI-DSS v4.0
PCI-DSS v4.0 is organized into six objectives, each with specific requirements:

1. **Build and Maintain a Secure Network and Systems**
   - **Requirement 1**: Install and maintain network security controls (e.g., firewalls, secure configurations).
   - **Requirement 2**: Apply secure configurations to all system components (e.g., disable unnecessary services).

2. **Protect Cardholder Data**
   - **Requirement 3**: Protect stored account data (e.g., use file-level encryption for cardholder data).
   - **Requirement 4**: Protect cardholder data with strong cryptography during transmission over open, public networks.

3. **Maintain a Vulnerability Management Program**
   - **Requirement 5**: Protect all systems and networks from malicious software (e.g., deploy anti-malware solutions).
   - **Requirement 6**: Develop and maintain secure systems and software (e.g., maintain an inventory of JavaScript on payment pages).

4. **Implement Strong Access Control Measures**
   - **Requirement 7**: Restrict access to system components and cardholder data by business need-to-know.
   - **Requirement 8**: Identify users and authenticate access to system components (e.g., enforce Multi-Factor Authentication for CDE access).
   - **Requirement 9**: Restrict physical access to cardholder data (e.g., secure POS terminals in retail stores).

5. **Regularly Monitor and Test Networks**
   - **Requirement 10**: Track and monitor all access to network resources and cardholder data (e.g., implement automated log monitoring).
   - **Requirement 11**: Regularly test security systems and processes (e.g., conduct vulnerability scans).

6. **Maintain an Information Security Policy**
   - **Requirement 12**: Maintain a policy that addresses information security for all personnel (e.g., annual training on PCI-DSS requirements).

## Key Considerations for PaySafe Retail
- **E-commerce Focus**: Requirements 6.4.3 and 11.6.1 emphasize securing payment pages to prevent e-skimming attacks.
- **MFA Requirement**: Requirement 8 now mandates MFA for all CDE access, including internal networks.
- **Continuous Compliance**: PCI-DSS v4.0 emphasizes ongoing monitoring, which PaySafe Retail will address in Phase 4 of the [Implementation Plan](implementation-plan/).

## Useful Links
- [PCI-DSS v4.0 Overview](../../PCI-DSS-v4.0-Overview/) - A general overview of the standard
- [Official PCI-DSS v4.0 Documentation](https://www.pcisecuritystandards.org/document_library/?category=pcidss&document=pci_dss)
- [Back to Project README](../README.md)
