from source.logger import Logger


logger = Logger().get_logger()


def main():
    try:
        print(a)
        some_code = "?"
    except Exception:
        logger.exception("Result:")


if __name__ == '__main__':
    main()
