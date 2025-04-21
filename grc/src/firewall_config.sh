#!/bin/bash
# Firewall configuration for PCI-DSS Requirement 1

# Flush existing rules
iptables -F

# Allow SSH (port 22) and HTTPS (port 443)
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -j ACCEPT

# Allow outbound traffic for payment processing
iptables -A OUTPUT -p tcp --dport 443 -j ACCEPT

# Drop all other incoming traffic
iptables -A INPUT -j DROP

echo "Firewall configured for PCI-DSS compliance."
