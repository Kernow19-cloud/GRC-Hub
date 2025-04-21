import pytest
import logging
from src.vulnerability_scan import scan_network

def test_scan_network_success(mocker):
    """Test successful network scan with mocked nmap."""
    # Mock nmap.PortScanner
    mock_scanner = mocker.patch("nmap.PortScanner")
    mock_instance = mock_scanner.return_value
    mock_instance.all_hosts.return_value = ["192.168.1.1"]
    mock_instance.__getitem__.return_value.hostname.return_value = "test-host"
    mock_instance.__getitem__.return_value.all_protocols.return_value = ["tcp"]
    mock_instance.__getitem__.return_value.__getitem__.return_value.keys.return_value = [80]
    mock_instance.__getitem__.return_value.__getitem__.return_value.__getitem__.return_value = {"state": "open"}

    # Call the function
    result = scan_network(target="192.168.1.0/24")

    # Assertions
    assert result is not None
    mock_scanner.return_value.scan.assert_called_once_with("192.168.1.0/24", arguments="-sV --script vuln")

def test_scan_network_logging(mocker, caplog):
    """Test logging output during network scan."""
    caplog.set_level(logging.INFO)
    mock_scanner = mocker.patch("nmap.PortScanner")
    mock_instance = mock_scanner.return_value
    mock_instance.all_hosts.return_value = []

    scan_network(target="192.168.1.0/24")

    assert "Starting vulnerability scan on 192.168.1.0/24" in caplog.text

def test_scan_network_no_hosts(mocker):
    """Test scan when no hosts are found."""
    mock_scanner = mocker.patch("nmap.PortScanner")
    mock_instance = mock_scanner.return_value
    mock_instance.all_hosts.return_value = []

    result = scan_network(target="192.168.1.0/24")

    assert result is mock_instance
    assert mock_scanner.return_value.scan.called
