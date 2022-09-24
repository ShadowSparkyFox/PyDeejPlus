class Port:
    def __init__(self, port_id, port_desc):
        self.port_id = port_id
        self.port_desc = port_desc

    def __str__(self):
        return self.port_id + " - " + self.port_desc
