import os
import sys

DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(DIR, '../../limbo/ws_plugins'))

from tag import on_message


def test_tag():
    # we don't test the happy-path because of the requirement that the tag doesn't exist AND we
    # don't want to pollute the repo with lots of bogus tags

    ret = on_message({"text": u"wordy tag release-2017-07-20 as r6.0.gold.f100"}, None, push=False)
    assert 'already exists' in ret

    ret = on_message({"text": u"wordy tag release-2017-07-20 as bad-branch-name"}, None, push=False)
    assert 'Unexpected branch name' in ret

    ret = on_message({"text": u"wordy tag bad-tag-name as r6.0.gold.f100"}, None, push=False)
    assert 'Unexpected tag name' in ret
