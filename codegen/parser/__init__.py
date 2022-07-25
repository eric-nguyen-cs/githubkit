from contextvars import ContextVar
from typing import Dict, List, Optional

import httpx

# parser context
_schemas: ContextVar[Dict[httpx.URL, "SchemaData"]] = ContextVar("schemas")
_config: ContextVar["Config"] = ContextVar("config")


def get_config() -> "Config":
    return _config.get()


def get_schemas() -> Dict[httpx.URL, "SchemaData"]:
    return _schemas.get()


def get_schema(ref: httpx.URL) -> Optional["SchemaData"]:
    return _schemas.get().get(ref)


def add_schema(ref: httpx.URL, schema: "SchemaData"):
    if ref in _schemas.get():
        raise ValueError(f"Duplicate schema {ref}")
    _schemas.get()[ref] = schema


from ..config import Config
from ..source import Source
from .endpoints import parse_endpoint
from .utils import sanitize as sanitize
from .utils import kebab_case as kebab_case
from .utils import snake_case as snake_case
from .schemas import SchemaData, parse_schema
from .utils import pascal_case as pascal_case
from .data import GeneratorData as GeneratorData
from .endpoints import EndpointData as EndpointData
from .utils import fix_reserved_words as fix_reserved_words


def parse_openapi_spec(source: Source, config: Config) -> GeneratorData:
    source = source.get_root()
    _st = _schemas.set({})
    _ct = _config.set(config)

    try:
        openapi = source.root

        # cache /components/schemas first
        if openapi.components and openapi.components.schemas:
            schemas_source = source / "components" / "schemas"
            for name in openapi.components.schemas:
                schema_source = schemas_source / name
                parse_schema(schema_source, name)

        endpoints: List[EndpointData] = []
        if openapi.paths:
            for path in openapi.paths:
                endpoints.extend(parse_endpoint(source / "paths" / path, path))

        return GeneratorData(
            title=openapi.info.title,
            description=openapi.info.description,
            version=openapi.info.version,
            endpoints=endpoints,
            schemas=list(get_schemas().values()),
        )
    finally:
        _schemas.reset(_st)
        _config.reset(_ct)