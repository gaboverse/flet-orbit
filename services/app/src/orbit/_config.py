import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class OrbitConfig:
    """Centralized configuration for flet-orbit."""

    debug: bool = field(
        default_factory=lambda: os.getenv(
            "ORBIT_DEBUG", "false"
        ).lower() in ("1", "true", "yes")
    )
    default_route: str = field(
        default_factory=lambda: os.getenv("ORBIT_DEFAULT_ROUTE", "/")
    )
    assets_dir: str = field(
        default_factory=lambda: os.getenv("ORBIT_ASSETS_DIR", "assets")
    )


# Default instance available for direct imports.
config = OrbitConfig()
