# PCI-DSS Fundamentals

## Overview
The Payment Card Industry Data Security Standard (PCI-DSS) v4.0.0 is a global standard for protecting cardholder data. For PaySafe Retail, an e-commerce retailer outsourcing payment processing to PaySafe’s Hosted Payments API, compliance involves meeting requirements applicable to a minimal cardholder data environment (CDE).

## Key PCI-DSS v4.0.0 Requirements
PCI-DSS v4.0.0 includes 12 core requirements, grouped into six objectives. Below is a summary tailored to PaySafe Retail’s context:

1. **Build and Maintain a Secure Network and Systems**
   - **Requirement 1**: Install and maintain network security controls (e.g., firewalls; see `src/firewall_config.sh`).
   - **Requirement 2**: Apply secure configurations (not applicable, as no CDE is hosted locally).

2. **Protect Cardholder Data**
   - **Requirement 3**: Protect stored cardholder data (not applicable, as no data is stored).
   - **Requirement 4**: Encrypt transmission of cardholder data (e.g., TLS 1.3; see `configs/encryption.conf`).

3. **Maintain a Vulnerability Management Program**
   - **Requirement 5**: Protect systems from malware (minimal, as no CDE).
   - **Requirement 6**: Develop and maintain secure systems (e.g., patch management for API integration).

4. **Implement Strong Access Control Measures**
   - **Requirement 7**: Restrict access to cardholder data (e.g., RBAC; see `configs/access_control.yaml`).
   - **Requirement 8**: Identify and authenticate access (minimal, as no CDE).
   - **Requirement 9**: Restrict physical access (e.g., no on-site cardholder data storage).

5. **Regularly Monitor and Test Networks**
   - **Requirement 10**: Monitor access to network resources (e.g., log monitoring; see `src/log_monitor.py`).
   - **Requirement 11**: Test security systems (e.g., vulnerability scans; see `src/vulnerability_scan.py`).

6. **Maintain an Information Security Policy**
   - **Requirement 12**: Support information security policies (e.g., see `docs/pci_dss_policy.md`).

## PaySafe Retail Context
- **Scope**: PaySafe Retail outsources all payment processing to PaySafe’s Hosted Payments API, qualifying for SAQ A (see `docs/saq_a.md`). No cardholder data is stored, processed, or transmitted locally.
- **Key Requirements**:
  - Secure API integration (`examples/hosted_payment_api.py`).
  - Network security for systems interacting with the API (`src/firewall_config.sh`).
  - Logging and monitoring (`src/log_monitor.py`).
  - Vulnerability management (`src/vulnerability_scan.py`).
  - Policy and access control (`docs/pci_dss_policy.md`, `configs/access_control.yaml`).

## Resources
- PCI-DSS v4.0.0: [PCI Security Standards Council](https://www.pcisecuritystandards.org)
- PaySafe API Docs: [PaySafe Developer Portal](https://developer.paysafe.com)
- Contact: compliance@paysafe-retail.com
