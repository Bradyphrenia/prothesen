def zerlege_datum(datum) -> (int, int, int):
    try:
        yy = int(datum[0:4])  # Zerlegung ...
        mm = int(datum[5:7])
        dd = int(datum[8:10])
    except ValueError:
        yy, mm, dd = 2014, 1, 1
    finally:
        return yy, mm, dd


if __name__ == '__main__':
    print(zerlege_datum("2015-01-02 12:03:12"))
    print(zerlege_datum(""))
