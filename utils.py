import logging

logger = logging.getLogger("legacy_hr")


def log_employee(emp):
    logger.info("employee name=%s ssn=%s salary=%s" % (emp["name"], emp["ssn"], emp["salary"]))
