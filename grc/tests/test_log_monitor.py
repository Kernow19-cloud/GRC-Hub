import pytest
import logging
from watchdog.events import FileSystemEvent
from src.log_monitor import LogHandler, monitor_logs

def test_log_handler_on_modified(mocker, caplog):
    """Test LogHandler on file modification event."""
    caplog.set_level(logging.INFO)
    handler = LogHandler()
    
    # Create a mock event
    mock_event = mocker.Mock(spec=FileSystemEvent)
    mock_event.is_directory = False
    mock_event.src_path = "/var/log/access.log"

    # Call on_modified
    handler.on_modified(mock_event)

    # Verify logging
    assert f"Log file modified: /var/log/access.log" in caplog.text

def test_log_handler_ignores_directories(mocker, caplog):
    """Test LogHandler ignores directory modification events."""
    caplog.set_level(logging.INFO)
    handler = LogHandler()
    
    # Create a mock event for a directory
    mock_event = mocker.Mock(spec=FileSystemEvent)
    mock_event.is_directory = True
    mock_event.src_path = "/var/log"

    # Call on_modified
    handler.on_modified(mock_event)

    # Verify no logging for directories
    assert "Log file modified" not in caplog.text

def test_monitor_logs_starts_observer(mocker):
    """Test monitor_logs starts the observer correctly."""
    # Mock Observer and FileSystemEventHandler
    mock_observer = mocker.patch("watchdog.observers.Observer")
    mock_observer_instance = mock_observer.return_value
    mock_schedule = mock_observer_instance.schedule
    mock_start = mock_observer_instance.start
    
    # Mock time.sleep to avoid infinite loop
    mocker.patch("time.sleep", side_effect=KeyboardInterrupt)

    # Call monitor_logs
    monitor_logs(log_path="/var/log/access.log")

    # Verify observer setup
    mock_schedule.assert_called_once()
    mock_start.assert_called_once()
