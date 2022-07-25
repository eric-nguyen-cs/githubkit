"""DO NOT EDIT THIS FILE!

This file is auto generated by github rest api discription.
See https://github.com/github/rest-api-description for more information.
"""


from typing import TYPE_CHECKING, List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET, Unset, exclude_unset

from .models import (
    EmptyObject,
    DependabotSecret,
    DependabotPublicKey,
    OrganizationDependabotSecret,
    OrgsOrgDependabotSecretsGetResponse200,
    OrgsOrgDependabotSecretsSecretNamePutBody,
    ReposOwnerRepoDependabotSecretsGetResponse200,
    ReposOwnerRepoDependabotSecretsSecretNamePutBody,
    OrgsOrgDependabotSecretsSecretNameRepositoriesPutBody,
    OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200,
)

if TYPE_CHECKING:
    from githubkit.core import GitHubCore
    from githubkit.response import Response


class DependabotClient:
    def __init__(self, github: "GitHubCore"):
        self._github = github

    def list_org_secrets(
        self,
        org: str,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[OrgsOrgDependabotSecretsGetResponse200]":
        url = f"/orgs/{org}/dependabot/secrets"

        params = {
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=OrgsOrgDependabotSecretsGetResponse200,
        )

    async def async_list_org_secrets(
        self,
        org: str,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[OrgsOrgDependabotSecretsGetResponse200]":
        url = f"/orgs/{org}/dependabot/secrets"

        params = {
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=OrgsOrgDependabotSecretsGetResponse200,
        )

    def get_org_public_key(
        self,
        org: str,
    ) -> "Response[DependabotPublicKey]":
        url = f"/orgs/{org}/dependabot/secrets/public-key"

        return self._github.request(
            "GET",
            url,
            response_model=DependabotPublicKey,
        )

    async def async_get_org_public_key(
        self,
        org: str,
    ) -> "Response[DependabotPublicKey]":
        url = f"/orgs/{org}/dependabot/secrets/public-key"

        return await self._github.arequest(
            "GET",
            url,
            response_model=DependabotPublicKey,
        )

    def get_org_secret(
        self,
        org: str,
        secret_name: str,
    ) -> "Response[OrganizationDependabotSecret]":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}"

        return self._github.request(
            "GET",
            url,
            response_model=OrganizationDependabotSecret,
        )

    async def async_get_org_secret(
        self,
        org: str,
        secret_name: str,
    ) -> "Response[OrganizationDependabotSecret]":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=OrganizationDependabotSecret,
        )

    def create_or_update_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        encrypted_value: Union[Unset, str] = UNSET,
        key_id: Union[Unset, str] = UNSET,
        visibility: Literal["all", "private", "selected"],
        selected_repository_ids: Union[Unset, List[str]] = UNSET,
    ) -> "Response[EmptyObject]":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}"

        json = OrgsOrgDependabotSecretsSecretNamePutBody(
            **{
                "encrypted_value": encrypted_value,
                "key_id": key_id,
                "visibility": visibility,
                "selected_repository_ids": selected_repository_ids,
            }
        ).dict(by_alias=True)

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=EmptyObject,
        )

    async def async_create_or_update_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        encrypted_value: Union[Unset, str] = UNSET,
        key_id: Union[Unset, str] = UNSET,
        visibility: Literal["all", "private", "selected"],
        selected_repository_ids: Union[Unset, List[str]] = UNSET,
    ) -> "Response[EmptyObject]":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}"

        json = OrgsOrgDependabotSecretsSecretNamePutBody(
            **{
                "encrypted_value": encrypted_value,
                "key_id": key_id,
                "visibility": visibility,
                "selected_repository_ids": selected_repository_ids,
            }
        ).dict(by_alias=True)

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=EmptyObject,
        )

    def delete_org_secret(
        self,
        org: str,
        secret_name: str,
    ) -> "Response":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}"

        return self._github.request(
            "DELETE",
            url,
        )

    async def async_delete_org_secret(
        self,
        org: str,
        secret_name: str,
    ) -> "Response":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}"

        return await self._github.arequest(
            "DELETE",
            url,
        )

    def list_selected_repos_for_org_secret(
        self,
        org: str,
        secret_name: str,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
    ) -> "Response[OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200]":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories"

        params = {
            "page": page,
            "per_page": per_page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200,
        )

    async def async_list_selected_repos_for_org_secret(
        self,
        org: str,
        secret_name: str,
        page: Union[Unset, int] = 1,
        per_page: Union[Unset, int] = 30,
    ) -> "Response[OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200]":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories"

        params = {
            "page": page,
            "per_page": per_page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=OrgsOrgDependabotSecretsSecretNameRepositoriesGetResponse200,
        )

    def set_selected_repos_for_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        selected_repository_ids: List[int],
    ) -> "Response":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories"

        json = OrgsOrgDependabotSecretsSecretNameRepositoriesPutBody(
            **{
                "selected_repository_ids": selected_repository_ids,
            }
        ).dict(by_alias=True)

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
        )

    async def async_set_selected_repos_for_org_secret(
        self,
        org: str,
        secret_name: str,
        *,
        selected_repository_ids: List[int],
    ) -> "Response":
        url = f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories"

        json = OrgsOrgDependabotSecretsSecretNameRepositoriesPutBody(
            **{
                "selected_repository_ids": selected_repository_ids,
            }
        ).dict(by_alias=True)

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
        )

    def add_selected_repo_to_org_secret(
        self,
        org: str,
        secret_name: str,
        repository_id: int,
    ) -> "Response":
        url = (
            f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        )

        return self._github.request(
            "PUT",
            url,
            error_models={},
        )

    async def async_add_selected_repo_to_org_secret(
        self,
        org: str,
        secret_name: str,
        repository_id: int,
    ) -> "Response":
        url = (
            f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        )

        return await self._github.arequest(
            "PUT",
            url,
            error_models={},
        )

    def remove_selected_repo_from_org_secret(
        self,
        org: str,
        secret_name: str,
        repository_id: int,
    ) -> "Response":
        url = (
            f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        )

        return self._github.request(
            "DELETE",
            url,
            error_models={},
        )

    async def async_remove_selected_repo_from_org_secret(
        self,
        org: str,
        secret_name: str,
        repository_id: int,
    ) -> "Response":
        url = (
            f"/orgs/{org}/dependabot/secrets/{secret_name}/repositories/{repository_id}"
        )

        return await self._github.arequest(
            "DELETE",
            url,
            error_models={},
        )

    def list_repo_secrets(
        self,
        owner: str,
        repo: str,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[ReposOwnerRepoDependabotSecretsGetResponse200]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets"

        params = {
            "per_page": per_page,
            "page": page,
        }

        return self._github.request(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=ReposOwnerRepoDependabotSecretsGetResponse200,
        )

    async def async_list_repo_secrets(
        self,
        owner: str,
        repo: str,
        per_page: Union[Unset, int] = 30,
        page: Union[Unset, int] = 1,
    ) -> "Response[ReposOwnerRepoDependabotSecretsGetResponse200]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets"

        params = {
            "per_page": per_page,
            "page": page,
        }

        return await self._github.arequest(
            "GET",
            url,
            params=exclude_unset(params),
            response_model=ReposOwnerRepoDependabotSecretsGetResponse200,
        )

    def get_repo_public_key(
        self,
        owner: str,
        repo: str,
    ) -> "Response[DependabotPublicKey]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/public-key"

        return self._github.request(
            "GET",
            url,
            response_model=DependabotPublicKey,
        )

    async def async_get_repo_public_key(
        self,
        owner: str,
        repo: str,
    ) -> "Response[DependabotPublicKey]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/public-key"

        return await self._github.arequest(
            "GET",
            url,
            response_model=DependabotPublicKey,
        )

    def get_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
    ) -> "Response[DependabotSecret]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"

        return self._github.request(
            "GET",
            url,
            response_model=DependabotSecret,
        )

    async def async_get_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
    ) -> "Response[DependabotSecret]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"

        return await self._github.arequest(
            "GET",
            url,
            response_model=DependabotSecret,
        )

    def create_or_update_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
        *,
        encrypted_value: Union[Unset, str] = UNSET,
        key_id: Union[Unset, str] = UNSET,
    ) -> "Response[EmptyObject]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"

        json = ReposOwnerRepoDependabotSecretsSecretNamePutBody(
            **{
                "encrypted_value": encrypted_value,
                "key_id": key_id,
            }
        ).dict(by_alias=True)

        return self._github.request(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=EmptyObject,
        )

    async def async_create_or_update_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
        *,
        encrypted_value: Union[Unset, str] = UNSET,
        key_id: Union[Unset, str] = UNSET,
    ) -> "Response[EmptyObject]":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"

        json = ReposOwnerRepoDependabotSecretsSecretNamePutBody(
            **{
                "encrypted_value": encrypted_value,
                "key_id": key_id,
            }
        ).dict(by_alias=True)

        return await self._github.arequest(
            "PUT",
            url,
            json=exclude_unset(json),
            response_model=EmptyObject,
        )

    def delete_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"

        return self._github.request(
            "DELETE",
            url,
        )

    async def async_delete_repo_secret(
        self,
        owner: str,
        repo: str,
        secret_name: str,
    ) -> "Response":
        url = f"/repos/{owner}/{repo}/dependabot/secrets/{secret_name}"

        return await self._github.arequest(
            "DELETE",
            url,
        )