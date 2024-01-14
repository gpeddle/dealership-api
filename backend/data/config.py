class ConfigFileDescriptor:
    """A descriptor for configuration files."""

    def __init__(self, id, name, filename, path, 
                 description = None, version = 'undefined', 
                 created = None, updated = None):
        self.id = id
        self.name = name
        self.filename = filename
        self.path = path
        self.description = description
        self.version = version
        self.created = created
        self.updated = updated

    def __str__(self):
        return f"{self.name} ({self.path})"

    def __repr__(self):
        return f"ConfigFileDescriptor({self.name}, {self.path})"

    def __eq__(self, other):
        return self.name == other.name and self.path == other.path

    def __hash__(self):
        return hash((self.name, self.path))