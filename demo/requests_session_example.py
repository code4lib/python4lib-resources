"""
Pros:
The `requests.Session` object allows to persist parameters across all requests issued within the session.
When a service requires authentication, the session will store the credentials and persist them to be used
for subsequent calls.
If a service you connect to allows keep-alive connection, the Requests session will persist connection
across all requests instead of establishing a new one for each requests.

To install Requests library:
`pip install requests`
"""


from requests import Session


def print_request_headers(r, *args, **kwargs):
    print(r.url, r.request.headers)


def make_multiple_requests_in_session():
	"""
	Issue multiple requests to the same service (id.loc.gov),
	persist the connection and attach appropriate headers.

	id.gov.loc does not require authentication, but other services
	may. Credentials or access tokens can be stored in the session object and used
	for each request.
	"""
    with Session() as session:
        session.headers.update(
            {"User-Agent": "tomaszkalata@bookops.org", "Accept": "application/json"}
        )  # will attach these parameters to each request header during the session
        session.timeout = 5

        terms = ["sh85080541", "sh91002704", "sh85088368"]
        for term in terms:
            url = f"https://id.loc.gov/authorities/subjects/{term}"
            response = session.get(url, hooks={"response": print_request_headers})
            if response.status_code == 200:
                yield response.json()
            else:
                continue


if __name__ == "__main__":
    results = make_multiple_requests_in_session()
    for response in results:
        # do something with each response
        pass
