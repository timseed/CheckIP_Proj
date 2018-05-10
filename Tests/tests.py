
from CheckService import CheckService


def test_generator():
    sites = ["ftp.esat.net",
             "ftp.leo.org",
             "ftp.mirror.nl",
             "ftp.it.freebsd.org"]
    for s in sites:
        yield check_service, s

    for s in sites:
        yield check_ftp, s


def check_service(s):
    assert s.startswith('ftp')


def check_ftp(s):
    cs=CheckService(s,21)
    assert cs != None
    assert cs.check()
