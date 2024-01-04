"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0358 import DiscussionType
from .group_0354 import RepositoryWebhooksType


class WebhookDiscussionTransferredPropChangesType(TypedDict):
    """WebhookDiscussionTransferredPropChanges"""

    new_discussion: DiscussionType
    new_repository: RepositoryWebhooksType


__all__ = ("WebhookDiscussionTransferredPropChangesType",)