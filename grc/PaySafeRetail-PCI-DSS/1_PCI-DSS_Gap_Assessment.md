# PCI-DSS Gap Assessment Report

## Overview
This document presents a detailed gap analysis comparing our current security controls with the PCI-DSS v4.0 standard. It identifies areas of non-compliance, partial compliance, and outlines recommendations for remediation.

## Assessment Methodology
1. **Interviews** with IT, Compliance, and Business units
2. **Review of technical configurations** (e.g., firewalls, storage, access logs)
3. **Documentation analysis** (policies, procedures, past audit reports)
4. **Mapping to PCI-DSS requirements**

## Gap Summary Table

| PCI Requirement | Requirement Description                             | Status              | Evidence Provided              | Gap Identified                    | Recommendation                     |
|------------------|------------------------------------------------------|----------------------|-------------------------------|-----------------------------------|------------------------------------|
| 1.1.1            | Maintain firewall configuration standards           | Partially Compliant | Screenshot of firewall rules  | Ruleset outdated                  | Update and review every 6 months  |
| 3.4              | Render cardholder data unreadable                   | Non-Compliant       | Encryption policy missing      | No encryption of stored CHD       | Implement AES-256 encryption       |
| 5.2.2            | Deploy anti-malware tools                           | Compliant           | Antivirus logs and deployment | None                              | Maintain regular updates           |
| 7.1.1            | Limit access to CHD based on business need          | Partially Compliant | Access control logs            | Excessive user access             | Implement RBAC                     |

## Compliance Overview

- **Total Requirements**: 12
- **Compliant**: 6
- **Partially Compliant**: 4
- **Non-Compliant**: 2

## Conclusion
Addressing the identified gaps is critical to achieving full PCI-DSS compliance before the QSA audit in October 2025.

