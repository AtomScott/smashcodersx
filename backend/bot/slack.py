import os
import json
import slack
import colorlog

from .scrape_tools import User

from slack_utils.decorators import slack_view, slack_command
from django.http import HttpResponse

LOGGER = colorlog.getLogger(__name__)

slack_token = os.environ['SLACK_API_TOKEN']
client = slack.WebClient(token=slack_token)


def pureimg(data1):
    data1 = '[{"text": "", "image_url": "'+data1+'"}]'
    data1 = [json.loads(data1[1:-1])]
    return data1


@slack_view
def sample_view(request, *args, **kwargs):
    # your logic
    return HttpResponse("Hello!")


@slack_command('/atcoder-test')
def test_command(text, **kwargs):
    # your logic
    response = {
        "response_type": "in_channel",
        'text': f"Hello {text}!"
    }
    return response

# @slack_command('atcoder-scores')
# def scores(text, **kwargs):


@slack_command('/wani')
def wani(text, **kwargs):
    n = int(text)
    channel = kwargs.pop('channel_id')

    if n != 100:
        response = client.files_upload(
            file=f'backend/bot/wani/{str(n).zfill(3)}.jpg',
            initial_comment=f"{100 - n}日後に死ぬワニ",
            channels=channel,
            username="",
        )

    else:
        for i in [1, 2, 3]:
            response = client.files_upload(
                file=f'backend/bot/wani/100-{i}.jpg',
                initial_comment=f"...",
                channels=channel,
                username="",
            )

    return "ワニはそろそろ死んだかね？"


@slack_command('/atcoder-users')
def atcoder_users(text, **kwargs):
    user_ids = text.split(' ')
    users = [User(user_id) for user_id in user_ids]
    msg = '\n'.join([user.info for user in users])
    response = {
        "text": msg,
        "response_type": "in_channel",
    }
    return response
