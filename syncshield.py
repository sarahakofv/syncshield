import os
import json
import logging

class SyncShield:
    def __init__(self, config_file='sync_config.json'):
        self.config_file = config_file
        self.settings = self.load_settings()

    def load_settings(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                settings = json.load(file)
                logging.info("Settings loaded successfully.")
                return settings
        else:
            logging.warning("Configuration file not found. Using default settings.")
            return {"services": {}, "protected_folders": []}

    def save_settings(self):
        with open(self.config_file, 'w') as file:
            json.dump(self.settings, file, indent=4)
        logging.info("Settings saved successfully.")

    def add_service(self, service_name, sync_settings):
        self.settings['services'][service_name] = sync_settings
        logging.info(f"Service '{service_name}' added with settings: {sync_settings}")
        self.save_settings()

    def remove_service(self, service_name):
        if service_name in self.settings['services']:
            del self.settings['services'][service_name]
            logging.info(f"Service '{service_name}' removed.")
            self.save_settings()
        else:
            logging.error(f"Service '{service_name}' not found.")

    def protect_folder(self, folder_path):
        if folder_path not in self.settings['protected_folders']:
            self.settings['protected_folders'].append(folder_path)
            logging.info(f"Folder '{folder_path}' added to protection list.")
            self.save_settings()
        else:
            logging.warning(f"Folder '{folder_path}' is already protected.")

    def unprotect_folder(self, folder_path):
        if folder_path in self.settings['protected_folders']:
            self.settings['protected_folders'].remove(folder_path)
            logging.info(f"Folder '{folder_path}' removed from protection list.")
            self.save_settings()
        else:
            logging.error(f"Folder '{folder_path}' is not protected.")

    def list_services(self):
        return self.settings['services']

    def list_protected_folders(self):
        return self.settings['protected_folders']

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    shield = SyncShield()

    # Example usage
    shield.add_service("Dropbox", {"sync_interval": "daily", "bandwidth_limit": "1MBps"})
    shield.protect_folder("C:\\Users\\User\\Documents\\Important")
    print("Services:", shield.list_services())
    print("Protected Folders:", shield.list_protected_folders())