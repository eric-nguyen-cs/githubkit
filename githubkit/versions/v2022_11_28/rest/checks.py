"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from weakref import ref
from typing_extensions import Annotated
from typing import TYPE_CHECKING, Dict, Literal, Optional, overload

from pydantic import Field, BaseModel

from githubkit.typing import Missing
from githubkit.utils import UNSET, exclude_unset
from githubkit.compat import model_dump, type_validate_python

if TYPE_CHECKING:
    from datetime import datetime
    from typing import List, Union, Literal

    from githubkit import GitHubCore
    from githubkit.utils import UNSET
    from githubkit.typing import Missing
    from githubkit.response import Response

    from ..models import (
        CheckRun,
        CheckSuite,
        EmptyObject,
        CheckAnnotation,
        CheckSuitePreference,
        ReposOwnerRepoCommitsRefCheckRunsGetResponse200,
        ReposOwnerRepoCommitsRefCheckSuitesGetResponse200,
        ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200,
    )
    from ..types import (
        ReposOwnerRepoCheckSuitesPostBodyType,
        ReposOwnerRepoCheckRunsPostBodyOneof0Type,
        ReposOwnerRepoCheckRunsPostBodyOneof1Type,
        ReposOwnerRepoCheckRunsPostBodyPropOutputType,
        ReposOwnerRepoCheckSuitesPreferencesPatchBodyType,
        ReposOwnerRepoCheckRunsPostBodyPropActionsItemsType,
        ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0Type,
        ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1Type,
        ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType,
        ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType,
        ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItemsType,
    )


class ChecksClient:
    _REST_API_VERSION = "2022-11-28"

    def __init__(self, github: GitHubCore):
        self._github_ref = ref(github)

    @property
    def _github(self) -> GitHubCore:
        if g := self._github_ref():
            return g
        raise RuntimeError(
            "GitHub client has already been collected. "
            "Do not use this client after the client has been collected."
        )

    @overload
    def create(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Union[
            ReposOwnerRepoCheckRunsPostBodyOneof0Type,
            ReposOwnerRepoCheckRunsPostBodyOneof1Type,
        ],
    ) -> Response[CheckRun]:
        ...

    @overload
    def create(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        name: str,
        head_sha: str,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        status: Literal["completed"],
        started_at: Missing[datetime] = UNSET,
        conclusion: Literal[
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "success",
            "skipped",
            "stale",
            "timed_out",
        ],
        completed_at: Missing[datetime] = UNSET,
        output: Missing[ReposOwnerRepoCheckRunsPostBodyPropOutputType] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsPostBodyPropActionsItemsType]
        ] = UNSET,
    ) -> Response[CheckRun]:
        ...

    @overload
    def create(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        name: str,
        head_sha: str,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        status: Missing[Literal["queued", "in_progress"]] = UNSET,
        started_at: Missing[datetime] = UNSET,
        conclusion: Missing[
            Literal[
                "action_required",
                "cancelled",
                "failure",
                "neutral",
                "success",
                "skipped",
                "stale",
                "timed_out",
            ]
        ] = UNSET,
        completed_at: Missing[datetime] = UNSET,
        output: Missing[ReposOwnerRepoCheckRunsPostBodyPropOutputType] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsPostBodyPropActionsItemsType]
        ] = UNSET,
    ) -> Response[CheckRun]:
        ...

    def create(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[
            Union[
                ReposOwnerRepoCheckRunsPostBodyOneof0Type,
                ReposOwnerRepoCheckRunsPostBodyOneof1Type,
            ]
        ] = UNSET,
        **kwargs,
    ) -> Response[CheckRun]:
        """see more: `https://docs.github.com/rest/checks/runs#create-a-check-run`"""

        from typing import Union

        from ..models import (
            CheckRun,
            ReposOwnerRepoCheckRunsPostBodyOneof0,
            ReposOwnerRepoCheckRunsPostBodyOneof1,
        )

        url = f"/repos/{owner}/{repo}/check-runs"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            Union[
                ReposOwnerRepoCheckRunsPostBodyOneof0,
                ReposOwnerRepoCheckRunsPostBodyOneof1,
            ],
            json,
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckRun,
        )

    @overload
    async def async_create(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Union[
            ReposOwnerRepoCheckRunsPostBodyOneof0Type,
            ReposOwnerRepoCheckRunsPostBodyOneof1Type,
        ],
    ) -> Response[CheckRun]:
        ...

    @overload
    async def async_create(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        name: str,
        head_sha: str,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        status: Literal["completed"],
        started_at: Missing[datetime] = UNSET,
        conclusion: Literal[
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "success",
            "skipped",
            "stale",
            "timed_out",
        ],
        completed_at: Missing[datetime] = UNSET,
        output: Missing[ReposOwnerRepoCheckRunsPostBodyPropOutputType] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsPostBodyPropActionsItemsType]
        ] = UNSET,
    ) -> Response[CheckRun]:
        ...

    @overload
    async def async_create(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        name: str,
        head_sha: str,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        status: Missing[Literal["queued", "in_progress"]] = UNSET,
        started_at: Missing[datetime] = UNSET,
        conclusion: Missing[
            Literal[
                "action_required",
                "cancelled",
                "failure",
                "neutral",
                "success",
                "skipped",
                "stale",
                "timed_out",
            ]
        ] = UNSET,
        completed_at: Missing[datetime] = UNSET,
        output: Missing[ReposOwnerRepoCheckRunsPostBodyPropOutputType] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsPostBodyPropActionsItemsType]
        ] = UNSET,
    ) -> Response[CheckRun]:
        ...

    async def async_create(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[
            Union[
                ReposOwnerRepoCheckRunsPostBodyOneof0Type,
                ReposOwnerRepoCheckRunsPostBodyOneof1Type,
            ]
        ] = UNSET,
        **kwargs,
    ) -> Response[CheckRun]:
        """see more: `https://docs.github.com/rest/checks/runs#create-a-check-run`"""

        from typing import Union

        from ..models import (
            CheckRun,
            ReposOwnerRepoCheckRunsPostBodyOneof0,
            ReposOwnerRepoCheckRunsPostBodyOneof1,
        )

        url = f"/repos/{owner}/{repo}/check-runs"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            Union[
                ReposOwnerRepoCheckRunsPostBodyOneof0,
                ReposOwnerRepoCheckRunsPostBodyOneof1,
            ],
            json,
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckRun,
        )

    def get(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CheckRun]:
        """see more: `https://docs.github.com/rest/checks/runs#get-a-check-run`"""

        from ..models import CheckRun

        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CheckRun,
        )

    async def async_get(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CheckRun]:
        """see more: `https://docs.github.com/rest/checks/runs#get-a-check-run`"""

        from ..models import CheckRun

        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CheckRun,
        )

    @overload
    def update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Union[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0Type,
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1Type,
        ],
    ) -> Response[CheckRun]:
        ...

    @overload
    def update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        name: Missing[str] = UNSET,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        started_at: Missing[datetime] = UNSET,
        status: Missing[Literal["completed"]] = UNSET,
        conclusion: Literal[
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "success",
            "skipped",
            "stale",
            "timed_out",
        ],
        completed_at: Missing[datetime] = UNSET,
        output: Missing[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType
        ] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType]
        ] = UNSET,
    ) -> Response[CheckRun]:
        ...

    @overload
    def update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        name: Missing[str] = UNSET,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        started_at: Missing[datetime] = UNSET,
        status: Missing[Literal["queued", "in_progress"]] = UNSET,
        conclusion: Missing[
            Literal[
                "action_required",
                "cancelled",
                "failure",
                "neutral",
                "success",
                "skipped",
                "stale",
                "timed_out",
            ]
        ] = UNSET,
        completed_at: Missing[datetime] = UNSET,
        output: Missing[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType
        ] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType]
        ] = UNSET,
    ) -> Response[CheckRun]:
        ...

    def update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[
            Union[
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0Type,
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1Type,
            ]
        ] = UNSET,
        **kwargs,
    ) -> Response[CheckRun]:
        """see more: `https://docs.github.com/rest/checks/runs#update-a-check-run`"""

        from typing import Union

        from ..models import (
            CheckRun,
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0,
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1,
        )

        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            Union[
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0,
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1,
            ],
            json,
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckRun,
        )

    @overload
    async def async_update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Union[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0Type,
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1Type,
        ],
    ) -> Response[CheckRun]:
        ...

    @overload
    async def async_update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        name: Missing[str] = UNSET,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        started_at: Missing[datetime] = UNSET,
        status: Missing[Literal["completed"]] = UNSET,
        conclusion: Literal[
            "action_required",
            "cancelled",
            "failure",
            "neutral",
            "success",
            "skipped",
            "stale",
            "timed_out",
        ],
        completed_at: Missing[datetime] = UNSET,
        output: Missing[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType
        ] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType]
        ] = UNSET,
    ) -> Response[CheckRun]:
        ...

    @overload
    async def async_update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        name: Missing[str] = UNSET,
        details_url: Missing[str] = UNSET,
        external_id: Missing[str] = UNSET,
        started_at: Missing[datetime] = UNSET,
        status: Missing[Literal["queued", "in_progress"]] = UNSET,
        conclusion: Missing[
            Literal[
                "action_required",
                "cancelled",
                "failure",
                "neutral",
                "success",
                "skipped",
                "stale",
                "timed_out",
            ]
        ] = UNSET,
        completed_at: Missing[datetime] = UNSET,
        output: Missing[
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropOutputType
        ] = UNSET,
        actions: Missing[
            List[ReposOwnerRepoCheckRunsCheckRunIdPatchBodyPropActionsItemsType]
        ] = UNSET,
    ) -> Response[CheckRun]:
        ...

    async def async_update(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[
            Union[
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0Type,
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1Type,
            ]
        ] = UNSET,
        **kwargs,
    ) -> Response[CheckRun]:
        """see more: `https://docs.github.com/rest/checks/runs#update-a-check-run`"""

        from typing import Union

        from ..models import (
            CheckRun,
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0,
            ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1,
        )

        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(
            Union[
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof0,
                ReposOwnerRepoCheckRunsCheckRunIdPatchBodyAnyof1,
            ],
            json,
        )
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckRun,
        )

    def list_annotations(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CheckAnnotation]]:
        """see more: `https://docs.github.com/rest/checks/runs#list-check-run-annotations`"""

        from typing import List

        from ..models import CheckAnnotation

        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations"

        params = {
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CheckAnnotation],
        )

    async def async_list_annotations(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[List[CheckAnnotation]]:
        """see more: `https://docs.github.com/rest/checks/runs#list-check-run-annotations`"""

        from typing import List

        from ..models import CheckAnnotation

        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations"

        params = {
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=List[CheckAnnotation],
        )

    def rerequest_run(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[EmptyObject]:
        """see more: `https://docs.github.com/rest/checks/runs#rerequest-a-check-run`"""

        from ..models import BasicError, EmptyObject

        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "POST",
            url,
            headers=exclude_unset(headers),
            response_model=EmptyObject,
            error_models={
                "403": BasicError,
                "422": BasicError,
                "404": BasicError,
            },
        )

    async def async_rerequest_run(
        self,
        owner: str,
        repo: str,
        check_run_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[EmptyObject]:
        """see more: `https://docs.github.com/rest/checks/runs#rerequest-a-check-run`"""

        from ..models import BasicError, EmptyObject

        url = f"/repos/{owner}/{repo}/check-runs/{check_run_id}/rerequest"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "POST",
            url,
            headers=exclude_unset(headers),
            response_model=EmptyObject,
            error_models={
                "403": BasicError,
                "422": BasicError,
                "404": BasicError,
            },
        )

    @overload
    def create_suite(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoCheckSuitesPostBodyType,
    ) -> Response[CheckSuite]:
        ...

    @overload
    def create_suite(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        head_sha: str,
    ) -> Response[CheckSuite]:
        ...

    def create_suite(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoCheckSuitesPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[CheckSuite]:
        """see more: `https://docs.github.com/rest/checks/suites#create-a-check-suite`"""

        from ..models import CheckSuite, ReposOwnerRepoCheckSuitesPostBody

        url = f"/repos/{owner}/{repo}/check-suites"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(ReposOwnerRepoCheckSuitesPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckSuite,
        )

    @overload
    async def async_create_suite(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoCheckSuitesPostBodyType,
    ) -> Response[CheckSuite]:
        ...

    @overload
    async def async_create_suite(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        head_sha: str,
    ) -> Response[CheckSuite]:
        ...

    async def async_create_suite(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoCheckSuitesPostBodyType] = UNSET,
        **kwargs,
    ) -> Response[CheckSuite]:
        """see more: `https://docs.github.com/rest/checks/suites#create-a-check-suite`"""

        from ..models import CheckSuite, ReposOwnerRepoCheckSuitesPostBody

        url = f"/repos/{owner}/{repo}/check-suites"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(ReposOwnerRepoCheckSuitesPostBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "POST",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckSuite,
        )

    @overload
    def set_suites_preferences(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoCheckSuitesPreferencesPatchBodyType,
    ) -> Response[CheckSuitePreference]:
        ...

    @overload
    def set_suites_preferences(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        auto_trigger_checks: Missing[
            List[
                ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItemsType
            ]
        ] = UNSET,
    ) -> Response[CheckSuitePreference]:
        ...

    def set_suites_preferences(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoCheckSuitesPreferencesPatchBodyType] = UNSET,
        **kwargs,
    ) -> Response[CheckSuitePreference]:
        """see more: `https://docs.github.com/rest/checks/suites#update-repository-preferences-for-check-suites`"""

        from ..models import (
            CheckSuitePreference,
            ReposOwnerRepoCheckSuitesPreferencesPatchBody,
        )

        url = f"/repos/{owner}/{repo}/check-suites/preferences"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(ReposOwnerRepoCheckSuitesPreferencesPatchBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return self._github.request(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckSuitePreference,
        )

    @overload
    async def async_set_suites_preferences(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: ReposOwnerRepoCheckSuitesPreferencesPatchBodyType,
    ) -> Response[CheckSuitePreference]:
        ...

    @overload
    async def async_set_suites_preferences(
        self,
        owner: str,
        repo: str,
        *,
        data: Literal[UNSET] = UNSET,
        headers: Optional[Dict[str, str]] = None,
        auto_trigger_checks: Missing[
            List[
                ReposOwnerRepoCheckSuitesPreferencesPatchBodyPropAutoTriggerChecksItemsType
            ]
        ] = UNSET,
    ) -> Response[CheckSuitePreference]:
        ...

    async def async_set_suites_preferences(
        self,
        owner: str,
        repo: str,
        *,
        headers: Optional[Dict[str, str]] = None,
        data: Missing[ReposOwnerRepoCheckSuitesPreferencesPatchBodyType] = UNSET,
        **kwargs,
    ) -> Response[CheckSuitePreference]:
        """see more: `https://docs.github.com/rest/checks/suites#update-repository-preferences-for-check-suites`"""

        from ..models import (
            CheckSuitePreference,
            ReposOwnerRepoCheckSuitesPreferencesPatchBody,
        )

        url = f"/repos/{owner}/{repo}/check-suites/preferences"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        if not kwargs:
            kwargs = UNSET

        json = kwargs if data is UNSET else data
        json = type_validate_python(ReposOwnerRepoCheckSuitesPreferencesPatchBody, json)
        json = model_dump(json) if isinstance(json, BaseModel) else json

        return await self._github.arequest(
            "PATCH",
            url,
            json=exclude_unset(json),
            headers=exclude_unset(headers),
            response_model=CheckSuitePreference,
        )

    def get_suite(
        self,
        owner: str,
        repo: str,
        check_suite_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CheckSuite]:
        """see more: `https://docs.github.com/rest/checks/suites#get-a-check-suite`"""

        from ..models import CheckSuite

        url = f"/repos/{owner}/{repo}/check-suites/{check_suite_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CheckSuite,
        )

    async def async_get_suite(
        self,
        owner: str,
        repo: str,
        check_suite_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[CheckSuite]:
        """see more: `https://docs.github.com/rest/checks/suites#get-a-check-suite`"""

        from ..models import CheckSuite

        url = f"/repos/{owner}/{repo}/check-suites/{check_suite_id}"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            headers=exclude_unset(headers),
            response_model=CheckSuite,
        )

    def list_for_suite(
        self,
        owner: str,
        repo: str,
        check_suite_id: int,
        check_name: Missing[str] = UNSET,
        status: Missing[Literal["queued", "in_progress", "completed"]] = UNSET,
        filter_: Missing[Literal["latest", "all"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200]:
        """see more: `https://docs.github.com/rest/checks/runs#list-check-runs-in-a-check-suite`"""

        from ..models import (
            ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200,
        )

        url = f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs"

        params = {
            "check_name": check_name,
            "status": status,
            "filter": filter_,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200,
        )

    async def async_list_for_suite(
        self,
        owner: str,
        repo: str,
        check_suite_id: int,
        check_name: Missing[str] = UNSET,
        status: Missing[Literal["queued", "in_progress", "completed"]] = UNSET,
        filter_: Missing[Literal["latest", "all"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200]:
        """see more: `https://docs.github.com/rest/checks/runs#list-check-runs-in-a-check-suite`"""

        from ..models import (
            ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200,
        )

        url = f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs"

        params = {
            "check_name": check_name,
            "status": status,
            "filter": filter_,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoCheckSuitesCheckSuiteIdCheckRunsGetResponse200,
        )

    def rerequest_suite(
        self,
        owner: str,
        repo: str,
        check_suite_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[EmptyObject]:
        """see more: `https://docs.github.com/rest/checks/suites#rerequest-a-check-suite`"""

        from ..models import EmptyObject

        url = f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "POST",
            url,
            headers=exclude_unset(headers),
            response_model=EmptyObject,
        )

    async def async_rerequest_suite(
        self,
        owner: str,
        repo: str,
        check_suite_id: int,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[EmptyObject]:
        """see more: `https://docs.github.com/rest/checks/suites#rerequest-a-check-suite`"""

        from ..models import EmptyObject

        url = f"/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest"

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "POST",
            url,
            headers=exclude_unset(headers),
            response_model=EmptyObject,
        )

    def list_for_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        check_name: Missing[str] = UNSET,
        status: Missing[Literal["queued", "in_progress", "completed"]] = UNSET,
        filter_: Missing[Literal["latest", "all"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        app_id: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ReposOwnerRepoCommitsRefCheckRunsGetResponse200]:
        """see more: `https://docs.github.com/rest/checks/runs#list-check-runs-for-a-git-reference`"""

        from ..models import ReposOwnerRepoCommitsRefCheckRunsGetResponse200

        url = f"/repos/{owner}/{repo}/commits/{ref}/check-runs"

        params = {
            "check_name": check_name,
            "status": status,
            "filter": filter_,
            "per_page": per_page,
            "page": page,
            "app_id": app_id,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoCommitsRefCheckRunsGetResponse200,
        )

    async def async_list_for_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        check_name: Missing[str] = UNSET,
        status: Missing[Literal["queued", "in_progress", "completed"]] = UNSET,
        filter_: Missing[Literal["latest", "all"]] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        app_id: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ReposOwnerRepoCommitsRefCheckRunsGetResponse200]:
        """see more: `https://docs.github.com/rest/checks/runs#list-check-runs-for-a-git-reference`"""

        from ..models import ReposOwnerRepoCommitsRefCheckRunsGetResponse200

        url = f"/repos/{owner}/{repo}/commits/{ref}/check-runs"

        params = {
            "check_name": check_name,
            "status": status,
            "filter": filter_,
            "per_page": per_page,
            "page": page,
            "app_id": app_id,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoCommitsRefCheckRunsGetResponse200,
        )

    def list_suites_for_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        app_id: Missing[int] = UNSET,
        check_name: Missing[str] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ReposOwnerRepoCommitsRefCheckSuitesGetResponse200]:
        """see more: `https://docs.github.com/rest/checks/suites#list-check-suites-for-a-git-reference`"""

        from ..models import ReposOwnerRepoCommitsRefCheckSuitesGetResponse200

        url = f"/repos/{owner}/{repo}/commits/{ref}/check-suites"

        params = {
            "app_id": app_id,
            "check_name": check_name,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoCommitsRefCheckSuitesGetResponse200,
        )

    async def async_list_suites_for_ref(
        self,
        owner: str,
        repo: str,
        ref: str,
        app_id: Missing[int] = UNSET,
        check_name: Missing[str] = UNSET,
        per_page: Missing[int] = UNSET,
        page: Missing[int] = UNSET,
        *,
        headers: Optional[Dict[str, str]] = None,
    ) -> Response[ReposOwnerRepoCommitsRefCheckSuitesGetResponse200]:
        """see more: `https://docs.github.com/rest/checks/suites#list-check-suites-for-a-git-reference`"""

        from ..models import ReposOwnerRepoCommitsRefCheckSuitesGetResponse200

        url = f"/repos/{owner}/{repo}/commits/{ref}/check-suites"

        params = {
            "app_id": app_id,
            "check_name": check_name,
            "per_page": per_page,
            "page": page,
        }

        headers = {"X-GitHub-Api-Version": self._REST_API_VERSION, **(headers or {})}

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            headers=exclude_unset(headers),
            response_model=ReposOwnerRepoCommitsRefCheckSuitesGetResponse200,
        )
