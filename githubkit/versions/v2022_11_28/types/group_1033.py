"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List
from typing_extensions import TypedDict, NotRequired


class ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2Type(TypedDict):
    """ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2"""

    labels: NotRequired[
        List[ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2PropLabelsItemsType]
    ]


class ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2PropLabelsItemsType(TypedDict):
    """ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2PropLabelsItems"""

    name: str


__all__ = (
    "ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2Type",
    "ReposOwnerRepoIssuesIssueNumberLabelsPutBodyOneof2PropLabelsItemsType",
)