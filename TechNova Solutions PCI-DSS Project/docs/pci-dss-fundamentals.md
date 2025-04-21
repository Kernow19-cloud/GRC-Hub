# PCI-DSS Fundamentals

## Overview
The **Payment Card Industry Data Security Standard (PCI-DSS) v4.0.0** is a global standard to protect cardholder data (CHD) and sensitive authentication data (SAD). It applies to organizations that store, process, or transmit CHD. This document outlines the 12 core requirements and TechNova Solutions' compliance scope.

## PCI-DSS Requirements
The 12 requirements are grouped into six objectives:

| **Objective** | **Requirement** | **Description** |
|---------------|-----------------|-----------------|
| **Build and Maintain a Secure Network and Systems** | 1 | Install and maintain network security controls (e.g., firewalls). |
|  | 2 | Apply secure configurations to systems (e.g., remove default accounts). |
| **Protect Cardholder Data** | 3 | Protect stored CHD (e.g., encryption, truncation). |
|  | 4 | Encrypt CHD transmission over public networks (e.g., TLS). |
| **Maintain a Vulnerability Management Program** | 5 | Protect systems from malware (e.g., anti-malware software). |
|  | 6 | Develop secure systems and software (e.g., patch management). |
| **Implement Strong Access Control Measures** | 7 | Restrict CHD access to a need-to-know basis. |
|  | 8 | Authenticate access to systems (e.g., unique IDs, MFA). |
|  | 9 | Restrict physical access to CHD (e.g., secure data centers). |
| **Regularly Monitor and Test Networks** | 10 | Monitor access to network resources and CHD (e.g., logging). |
|  | 11 | Test security systems (e.g., vulnerability scans, penetration tests). |
| **Maintain an Information Security Policy** | 12 | Maintain a security policy for all personnel (e.g., training). |

## Key Changes in PCI-DSS v4.0.0
- Continuous compliance focus (not just annual assessments).
- Customized approach for meeting requirements.
- Enhanced MFA, encryption, and risk assessment requirements.
- Stronger threat detection (e.g., file integrity monitoring).

## TechNova’s Scope
The **Cardholder Data Environment (CDE)** includes systems, networks, and processes that store, process, or transmit CHD/SAD (e.g., payment gateways, web servers, databases). Connected systems (e.g., logging servers) are also in scope.

For more details, refer to the [Payment Security Policy](./payment-security-policy.md).
