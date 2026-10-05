# small utilities, no deps

def chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i : i + size]

if __name__ == "__main__":
    print(most_common("abracadabra"))

# cleanup later
