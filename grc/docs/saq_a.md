# Self-Assessment Questionnaire A (SAQ A) Guide

## Overview
SAQ A is designed for e-commerce merchants like PaySafe Retail who outsource all cardholder data storage, processing, and transmission to a PCI-DSS compliant third-party provider, such as PaySafe’s Hosted Payments API. This guide outlines the steps to complete SAQ A for PCI-DSS v4.0.1 compliance.

## Applicability
- **Merchant Type**: E-commerce retailer.
- **Payment Processing**: Fully outsourced to PaySafe’s Hosted Payments API.
- **Cardholder Data**: No storage, processing, or transmission of cardholder data on PaySafe Retail systems.

## Steps to Complete SAQ A
1. **Verify Outsourcing**:
   - Confirm that all payment processing is handled via PaySafe’s Hosted Payments API (see `examples/hosted_payment_api.py`).
   - Ensure no cardholder data is stored locally (e.g., on servers or devices).

2. **Address SAQ A Requirements**:
   - **Requirement 2**: Do not use vendor-supplied defaults for system passwords (not applicable, as no cardholder data environment exists).
   - **Requirement 9**: Implement physical security controls for devices (e.g., ensure no paper records or devices store cardholder data).
   - **Requirement 12**: Maintain a security policy (see `pci_dss_policy.md`).

3. **Complete the SAQ A Form**:
   - Download the SAQ A form from the PCI SSC website.
   - Answer questions based on outsourcing and lack of cardholder data environment.
   - Example: Confirm that all payment pages are served by PaySafe’s hosted solution.

4. **Attestation of Compliance (AOC)**:
   - Complete the AOC section of the SAQ A form.
   - Sign and submit to your acquirer or payment processor.

5. **Annual Review**:
   - Reassess SAQ A annually or upon significant changes to payment processing.

## Documentation
- Maintain records of outsourcing agreements with PaySafe.
- Store completed SAQ A and AOC forms securely.

## Resources
- PCI-DSS v4.0.1 SAQ A: [PCI Security Standards Council](https://www.pcisecuritystandards.org)
- PaySafe API Documentation: [PaySafe Developer Portal](https://developer.paysafe.com)
- Contact: compliance@paysafe-retail.com

## Notes
- Ensure all employees are trained on PCI-DSS policies (Requirement 12.6).
- If any cardholder data is handled locally, a different SAQ (e.g., SAQ D) may apply.
