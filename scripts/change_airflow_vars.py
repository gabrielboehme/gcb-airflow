import requests as r
import json
from requests.auth import HTTPBasicAuth


def change_vars():

	var = {
		'EXAMPLE_VAR': 'Value'
	}

	for v, value in var.items():

		req = r.patch(
			f'http://127.0.0.1/api/v1/variables/{v}',
			headers={
					'content-type': 'application/json',
			},
			auth=HTTPBasicAuth('user', 'pwd'),
			data=json.dumps(
				{
					'key': v,
					'value': value
				}
			)
		)
		print(req.status_code)

change_vars()