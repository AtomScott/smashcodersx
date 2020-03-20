import pytest, os
import colorlog

from django.urls import reverse
from django.http import HttpRequest

LOGGER = colorlog.getLogger(__name__)

def test_sample(client):
    LOGGER.info('Testing LOGGER.info')
    LOGGER.warning('Testing LOGGER.warning')
    LOGGER.error('Testing LOGGER.error')
    LOGGER.critical('Testing LOGGER.critical')
    assert True

def test_command_registry():
    from slack_utils.commands import registry

    commands = ['/atcoder-test']
    for  command in commands:
        assert command in registry._handlers

# @pytest.mark.django_db
# def test_view(client):
#    response = client.get('/slack/commands', data={
#        "token": os.environ['SLACK_SIGNING_SECRET'],
#         "command": "/test",
#         "text":"atom",
#    })
#    LOGGER.info(response.content)
#    assert response.status_code == 200
