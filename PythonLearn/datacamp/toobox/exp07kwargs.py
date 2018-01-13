# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""

    print("\nBEGIN: REPORT\n")

    # Iterate over the key-value pairs of kwargs
    for k, v in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(k + ": " + v)

    print("\nEND REPORT")

# First call to report_status()
report_status()

# Second call to report_status()

report_status(name="anakin", affiliation="sith lord", status="deceased")
