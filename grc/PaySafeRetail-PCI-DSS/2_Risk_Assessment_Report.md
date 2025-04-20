# PCI-DSS Risk Assessment Report

## Objective
Identify and analyze risks related to the storage, transmission, and processing of cardholder data (CHD) and develop mitigation strategies aligned with PCI-DSS.

## Threat and Vulnerability Analysis

| Risk ID | Asset Affected     | Threat                        | Vulnerability                  | Impact | Likelihood | Risk Level | Recommended Control           |
|--------|--------------------|-------------------------------|--------------------------------|--------|------------|------------|-------------------------------|
| R-001  | Database Server    | Unauthorized Access           | Weak access controls           | High   | Medium     | High       | Enforce RBAC, MFA             |
| R-002  | File Storage       | Data Breach                   | Unencrypted cardholder data    | High   | High       | Critical   | Encrypt all stored CHD        |
| R-003  | Network Traffic    | Man-in-the-Middle Attack      | Lack of TLS                    | High   | Low        | Medium     | Enforce TLS 1.2+              |
| R-004  | Endpoint Devices   | Malware Infection             | No EDR solution                | Medium | Medium     | Medium     | Deploy EDR, regular scanning  |

## Top Risks
1. **Storage of unencrypted CHD**
2. **Insufficient user access restrictions**
3. **Absence of centralized monitoring**

## Risk Treatment Plan
- Prioritize high and critical risks in Q2 2025.
- Implement controls in accordance with the Compliance Roadmap.
- Monitor progress and update risk register quarterly.

## Conclusion
Risk mitigation is necessary not just for compliance, but to reduce exposure to security incidents and potential fines.
