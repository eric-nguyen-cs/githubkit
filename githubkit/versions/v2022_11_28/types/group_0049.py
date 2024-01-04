"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal
from typing_extensions import TypedDict, NotRequired


class SecurityAndAnalysisType(TypedDict):
    """SecurityAndAnalysis"""

    advanced_security: NotRequired[SecurityAndAnalysisPropAdvancedSecurityType]
    dependabot_security_updates: NotRequired[
        SecurityAndAnalysisPropDependabotSecurityUpdatesType
    ]
    secret_scanning: NotRequired[SecurityAndAnalysisPropSecretScanningType]
    secret_scanning_push_protection: NotRequired[
        SecurityAndAnalysisPropSecretScanningPushProtectionType
    ]


class SecurityAndAnalysisPropAdvancedSecurityType(TypedDict):
    """SecurityAndAnalysisPropAdvancedSecurity"""

    status: NotRequired[Literal["enabled", "disabled"]]


class SecurityAndAnalysisPropDependabotSecurityUpdatesType(TypedDict):
    """SecurityAndAnalysisPropDependabotSecurityUpdates

    Enable or disable Dependabot security updates for the repository.
    """

    status: NotRequired[Literal["enabled", "disabled"]]


class SecurityAndAnalysisPropSecretScanningType(TypedDict):
    """SecurityAndAnalysisPropSecretScanning"""

    status: NotRequired[Literal["enabled", "disabled"]]


class SecurityAndAnalysisPropSecretScanningPushProtectionType(TypedDict):
    """SecurityAndAnalysisPropSecretScanningPushProtection"""

    status: NotRequired[Literal["enabled", "disabled"]]


__all__ = (
    "SecurityAndAnalysisType",
    "SecurityAndAnalysisPropAdvancedSecurityType",
    "SecurityAndAnalysisPropDependabotSecurityUpdatesType",
    "SecurityAndAnalysisPropSecretScanningType",
    "SecurityAndAnalysisPropSecretScanningPushProtectionType",
)