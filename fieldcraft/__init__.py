"""fieldcraft — a practical preparedness, survival & field-reference knowledge base
and loadout builder for soldiers and civilians. Educational/reference use only."""
from .loadouts import (
    TOOL_NAME, TOOL_VERSION, TIERS, Role, list_roles, get_role, build,
)
from . import acronyms, catalog, loadouts, lessons, sop

__all__ = ["TOOL_NAME", "TOOL_VERSION", "TIERS", "Role", "list_roles", "get_role",
           "build", "acronyms", "catalog", "loadouts", "lessons", "sop"]
