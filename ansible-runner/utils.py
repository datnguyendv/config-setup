def is_vmware(input_file, keyword="vmware"):
    with open(input_file) as f:
        return keyword in f.read()
