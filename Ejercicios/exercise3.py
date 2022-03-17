def capicua(string):
    assert len(string) > 0, 'Nop empty strings'
    return string == string [::-1]


def main():
    capicua('aca')

if __name__ == "__main__":
    main()