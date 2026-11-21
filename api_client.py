import requests


def fetch_salary_bands(country):
    resp = requests.get(
        "https://internal-api.legacycorp.local/v1/salary-bands?country=%s" % country,
        verify=False,
    )
    return resp.json()
