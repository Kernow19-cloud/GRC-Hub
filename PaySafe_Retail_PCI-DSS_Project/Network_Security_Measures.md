# Network Security Measures for CDE

## CDE Segmentation

- Firewalls isolate the Cardholder Data Environment (CDE) from other networks.
- Access to the CDE is limited to authorized personnel and systems only.

## Firewalls and Access Control

- Default deny policies are enforced.
- Ingress and egress rules are reviewed quarterly.
- Access lists are restricted to business needs only.

## Intrusion Detection and Prevention

- IDS and IPS solutions monitor traffic to/from the CDE.
- Real-time alerts for suspicious behavior are configured.
- Logs retained for 12+ months.

## Secure Protocols

- TLS 1.2+ enforced for all internal and external data transmissions.
- Deprecated protocols (e.g., SSL, TLS 1.0/1.1) are disabled.

## Network Monitoring

- All access is logged via a centralized SIEM system.
- Weekly review of CDE network traffic and anomalies.
