class CsvDataOutput:
    """ 
    Outputs data to the specified csv file.

    WARNING: automatically rewrites the specified file without asking.
    """

    def __init__(self, filename):
        self.filename = filename
        open(filename, 'w').close() # Rewrite the file
    
    def write(self, values):
        with open(self.filename, 'a') as f:
            f.write(','.join(map(lambda x: str(x), values)))
            f.write('\n')