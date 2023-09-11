# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import re

import requests
import tweepy
from tweepy import Client
from tweepy.client import Response


class TwitterAPI:
	def __init__(
		self, api_key: str, api_secret: str, access_token: str, access_token_secret: str
	) -> "TwitterAPI":
		self.api_key = api_key
		self.api_secret = api_secret
		self.access_token = access_token
		self.access_token_secret = access_token_secret
		self.client = self.__get_client()

	def __get_client(self) -> Client:
		return tweepy.Client(
			consumer_key=self.api_key,
			consumer_secret=self.api_secret,
			access_token=self.access_token,
			access_token_secret=self.access_token_secret,
		)

	def media_upload(self, filename: str, url: str) -> str:
		tweepy_auth = tweepy.OAuth1UserHandler(
			self.api_key, self.api_secret, self.access_token, self.access_token_secret
		)
		tweepy_api = tweepy.API(tweepy_auth)
		data = requests.get(url).content

		with open(filename, "wb") as file:
			file.write(data)

		response = tweepy_api.simple_upload(filename)
		media_id = re.search("media_id=(.+?),", str(response)).group(1)

		return media_id

	def create_tweet(self, text: str, media_ids: list = None) -> Response:
		return self.client.create_tweet(text=text, media_ids=media_ids or [])

	def delete_tweet(self, tweet_id: str) -> Response:
		return self.client.delete_tweet(id=tweet_id)
