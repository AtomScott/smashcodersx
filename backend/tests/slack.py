from slack_utils.decorators import slack_command

@slack_command('/atcoder-test')
def test_command(text, **kwargs):
    # your logic
    return f"Success, Hello {text}!"     # or {'text': "hello!"}
