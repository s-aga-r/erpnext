# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe

from erpnext.crm.doctype.twitter_settings.twitter_api import TwitterAPI


class TwitterRepository(TwitterAPI):
	def __init__(self, twitter_settings: dict) -> TwitterAPI:
		ts = frappe._dict(twitter_settings)
		super().__init__(ts.api_key, ts.api_secret, ts.access_token, ts.access_token_secret)
