# coding=utf-8
from os.path import join, dirname
from os import environ
from dotenv import load_dotenv

__author__ = 'davis.peixoto'

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

YOUTRACK_ENDPOINT = environ.get("YOUTRACK_ENDPOINT")
YOUTRACK_USERNAME = environ.get("YOUTRACK_USERNAME")
YOUTRACK_PASSWORD = environ.get("YOUTRACK_PASSWORD")

ASANA_PERSONAL_ACCESS_TOKEN = environ.get("ASANA_PERSONAL_ACCESS_TOKEN")
NOTIFICATION_EMAIL = environ.get("NOTIFICATION_EMAIL")

MAIL_DRIVER = environ.get("MAIL_DRIVER")
MAIL_HOST = environ.get("MAIL_HOST")
MAIL_PORT = environ.get("MAIL_PORT")
MAIL_USERNAME = environ.get("MAIL_USERNAME")
MAIL_PASSWORD = environ.get("MAIL_PASSWORD")
MAIL_FROM_ADDRESS = environ.get("MAIL_FROM_ADDRESS")
MAIL_FROM_NAME = environ.get("MAIL_FROM_NAME")
MAIL_TLS = environ.get("MAIL_TLS")

MAIL_DEPLOY_TO = environ.get("MAIL_DEPLOY_TO")
MAIL_DEPLOY_CC = environ.get("MAIL_DEPLOY_CC")
MAIL_DEPLOY_SUBJECT = environ.get("MAIL_DEPLOY_SUBJECT")
MAIL_DEPLOY_MANDRILL_TEMPLATE = environ.get("MAIL_DEPLOY_MANDRILL_TEMPLATE")

MAIL_VERIFY_CC = environ.get("MAIL_VERIFY_CC")
MAIL_VERIFY_SUBJECT = environ.get("MAIL_VERIFY_SUBJECT")
MAIL_VERIFY_MANDRILL_TEMPLATE = environ.get("MAIL_VERIFY_MANDRILL_TEMPLATE")

MAIL_BRANCH_VERIFY_CC = environ.get("MAIL_BRANCH_VERIFY_CC")
MAIL_BRANCH_VERIFY_SUBJECT = environ.get("MAIL_BRANCH_VERIFY_SUBJECT")
MAIL_BRANCH_VERIFY_MANDRILL_TEMPLATE = environ.get("MAIL_BRANCH_VERIFY_MANDRILL_TEMPLATE")

MANDRIL_APIKEY = environ.get("MANDRIL_APIKEY")
MANDRIL_DEPLOY_TEMPLATE_NAME = environ.get("MANDRIL_DEPLOY_TEMPLATE_NAME")
