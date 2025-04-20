# Project Overview – PaySafe Retail PCI-DSS Compliance

## Company Profile – PaySafe Retail (Fictional)

**PaySafe Retail** is a mid-sized retail company that operates both brick-and-mortar stores and an online e-commerce platform. The company processes card payments through point-of-sale (POS) terminals in-store and a secure online checkout gateway. Due to its handling of cardholder data, PaySafe Retail falls within the scope of the **Payment Card Industry Data Security Standard (PCI-DSS)** compliance requirements.

## Compliance Objective

The primary objective of this project is to design a realistic, portfolio-ready PCI-DSS compliance program tailored to PaySafe Retail's hybrid environment. The project includes a comprehensive assessment, remediation strategy, policy development, and implementation roadmap to meet the PCI-DSS v4.0 standards.

---

## Scope of Compliance

| Component | In Scope? | Description |
|----------|-----------|-------------|
| POS Terminals | ✅ | In-store systems capturing cardholder data |
| E-Commerce Checkout | ✅ | Online platform using third-party payment processor |
| Internal Network | ✅ | Systems and services storing or processing CHD |
| Staff Devices | ⚠️ | Laptops and workstations with access to sensitive systems |
| HR & Payroll Systems | ❌ | Not involved in cardholder data processing |
| Marketing Website | ❌ | Brochure site, does not handle payment data |

---

## Key PCI-DSS Control Categories (v4.0)

- Install and maintain a secure network and systems
- Protect stored cardholder data
- Implement strong access control measures
- Regularly monitor and test networks
- Maintain an information security policy
- Encrypt transmission of cardholder data across public networks
- Identify and authenticate access to system components
- Support secure software development (for in-house systems)

---

## Methodology

1. **Gap Assessment** – Identify areas of non-compliance across PaySafe’s environment.
2. **Risk Assessment** – Evaluate threats and vulnerabilities that impact cardholder data.
3. **Control Mapping** – Align existing and proposed controls to PCI-DSS v4.0.
4. **Policy Development** – Draft compliant policies for access control, encryption, and data retention.
5. **Implementation Plan** – Create a realistic, phased roadmap with key stakeholders.
6. **Audit Readiness** – Checklist and guidance to prepare for QSA or internal PCI audit.

---

## Deliverables

- Gap Assessment Spreadsheet
- Risk Assessment Report
- PCI-DSS Compliance Roadmap
- Policy Documents
- Implementation Plan
- Audit Readiness Checklist

---

## Notes

> This project is intended for **educational and demonstration purposes only**. It does not reflect a real organization or actual PCI audit.

