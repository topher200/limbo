""""wordy tag <branch> as <tag>" creates and pushes an annotated git tag

Designed only to work with our release branching scheme:
- the branch name must start with 'release'
- the tag name must start with 'r6.0.gold.f'"""
import os
import re

import git


GIT_REPO_LOCAL_DIR = os.path.join('/tmp', 'git_repo_for_slack_tag_plugin')
GIT_REPO_URL = os.environ.get("WORDY_GIT_REPO_URL")
assert GIT_REPO_URL is not None, os.environ


def _clean_up_error_message(e):
    # clean up the error message. truncate if too long
    err = e.stderr.strip()
    return err[:200]


def create_tag(tag_name, branch_name, push):
    # create the repo dir
    if not os.path.exists(GIT_REPO_LOCAL_DIR):
        os.makedirs(GIT_REPO_LOCAL_DIR)

    # point repo to url
    repo = git.Repo.init(GIT_REPO_LOCAL_DIR)
    try:
        repo.create_remote('origin', GIT_REPO_URL)
    except git.GitCommandError:
        # a previous run added our remote for us
        pass

    # pull down latest
    try:
        repo.remotes.origin.fetch(depth=1, tags=True, refspec=branch_name)
    except git.GitCommandError as e:
        return ':exclamation: Failed. {}'.format(_clean_up_error_message(e))

    # create the tag
    try:
        tag = repo.create_tag(
            path=tag_name,
            ref='origin/%s' % branch_name,
            message='Tagging {} as {}. Created by Wordy'.format(branch_name, tag_name),
        )
    except git.GitCommandError as e:
        return ':exclamation: Failed. {}'.format(_clean_up_error_message(e))

    if push:
        # push the tag
        try:
            repo.remotes.origin.push(tag)
        except git.GitCommandError as e:
            return ':exclamation: Failed. {}'.format(_clean_up_error_message(e))

    return ':white_check_mark: Tagged {} as {}'.format(branch_name, tag_name)


def on_message(msg, server, **kwargs):
    push = kwargs.get('push', False)

    text = msg.get("text", "")
    match = re.match(r"wordy tag (\S*) as (\S*)", text)
    if not match:
        return

    # pull tag and branch names from message
    try:
        branch_name = match.group(1)
        tag_name = match.group(2)
    except IndexError:
        return

    if not branch_name.startswith('release-'):
        return ':exclamation: Unexpected branch name "%s". Expected it to start with "release-"!' % branch_name
    if not tag_name.startswith('r6.0.gold.f'):
        return ':exclamation: Unexpected tag name "%s". Expected it to start with "r6.0.gold.f"!' % tag_name

    # more restrictive regex, just to make sure the input is pristine
    match = re.match(r'wordy tag (release-[-\d]+) as (r6.0.gold.f\d+)', text)
    if not match:
        return ':exclamation: Invalid input, please try again'
    try:
        branch_name = match.group(1)
        tag_name = match.group(2)
    except IndexError:
        return ':exclamation: Invalid input, please try again'

    # tagging can take a while. tell the channel we're working on it...
    server.slack.post_message(msg['channel'], 'Tagging...')

    return create_tag(tag_name, branch_name, push)
