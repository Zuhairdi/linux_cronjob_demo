import datetime


def stamp():
    ct = datetime.datetime.now()
    try:
        with open('timelog.txt', 'a+') as f:
            f.seek(0)
            data = f.read(100)
            if len(data) > 0:
                f.write('\n')
            f.write(f'{ct}')
    except FileNotFoundError:
        print("error writing")


if __name__ == '__main__':
    stamp()
