from abc import ABC, abstractmethod

class DataAccessInterface(ABC):

    @abstractmethod
    def read_config(self, config_name):
        """Read a configuration file."""
        pass

    @abstractmethod
    def write_config(self, config_name, data):
        """Write or update a configuration file."""
        pass

    @abstractmethod
    def list_configs(self):
        """List available configuration files."""
        pass
