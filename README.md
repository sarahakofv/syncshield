# SyncShield

SyncShield is a Python program designed to protect and manage synchronization settings for various cloud services on Windows, ensuring data integrity and secure management of your important files.

## Features

- **Service Management**: Add, remove, and manage synchronization settings for different cloud services.
- **Folder Protection**: Protect specific folders to prevent unauthorized sync operations.
- **Configuration File**: Automatically loads and saves settings to a configuration file.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/syncshield.git
   cd syncshield
   ```

2. Ensure you have Python installed on your system.

3. Install any required dependencies (none in this basic implementation).

## Usage

Run the `syncshield.py` script using Python:

```bash
python syncshield.py
```

The program will load existing settings or create a new configuration file if none is found.

### Example Usage

```python
# Initialize SyncShield
shield = SyncShield()

# Add a cloud service with specific sync settings
shield.add_service("Dropbox", {"sync_interval": "daily", "bandwidth_limit": "1MBps"})

# Protect a folder from unwanted synchronization
shield.protect_folder("C:\\Users\\User\\Documents\\Important")

# List all services and protected folders
print("Services:", shield.list_services())
print("Protected Folders:", shield.list_protected_folders())
```

## Logging

SyncShield uses Python's logging module to provide detailed information about operations and any potential errors or warnings encountered during execution.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.