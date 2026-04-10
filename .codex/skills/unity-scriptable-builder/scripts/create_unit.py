#!/usr/bin/env python3
"""Create Unity ScriptableObject assets via MCP."""

import requests
import json
import sys
from pathlib import Path

MCP_URL = "http://localhost:7777/command"

# Preset data for Lineage2 themed units
UNIT_PRESETS = {
    "dark_fighter": {
        "displayName": "Dark Fighter",
        "baseHP": 120,
        "baseAttack": 15,
        "classTags": ["Warrior"],
        "raceTags": ["Human"],
        "tier": 1,
        "goldCost": 1
    },
    "hawkeye": {
        "displayName": "Hawkeye",
        "baseHP": 80,
        "baseAttack": 20,
        "attackRange": 3,
        "classTags": ["Archer"],
        "raceTags": ["Human"],
        "tier": 2,
        "goldCost": 2
    },
    "bishop": {
        "displayName": "Bishop",
        "baseHP": 60,
        "baseAttack": 5,
        "classTags": ["Healer", "Mage"],
        "raceTags": ["Human"],
        "tier": 3,
        "goldCost": 3
    },
    "assassin": {
        "displayName": "Dark Elf Assassin",
        "baseHP": 85,
        "baseAttack": 22,
        "attackSpeed": 1.3,
        "classTags": ["Rogue", "Warrior"],
        "raceTags": ["DarkElf"],
        "tier": 2,
        "goldCost": 2
    },
    "destroyer": {
        "displayName": "Orc Destroyer",
        "baseHP": 180,
        "baseAttack": 25,
        "moveSpeed": 2.5,
        "classTags": ["Warrior"],
        "raceTags": ["Orc"],
        "tier": 3,
        "goldCost": 3
    }
}

ABILITY_PRESETS = {
    "power_strike": {
        "displayName": "Power Strike",
        "type": "Active",
        "targetType": "SingleEnemy",
        "damage": 150
    },
    "double_shot": {
        "displayName": "Double Shot",
        "type": "Active",
        "targetType": "SingleEnemy",
        "damage": 120,
        "cooldown": 3
    },
    "heal": {
        "displayName": "Heal",
        "type": "Active",
        "targetType": "SingleAlly",
        "healing": 100,
        "cooldown": 5
    },
    "backstab": {
        "displayName": "Backstab",
        "type": "Active",
        "targetType": "SingleEnemy",
        "damage": 200,
        "cooldown": 8
    }
}

SYNERGY_PRESETS = {
    "warrior": {
        "displayName": "Warrior",
        "requiredTags": ["Warrior"],
        "bonuses": [
            {"requiredCount": 2, "description": "+300 HP", "effects": [{"type": "HP", "value": 300}]},
            {"requiredCount": 4, "description": "+600 HP, +10 Armor", "effects": [{"type": "HP", "value": 600}, {"type": "Armor", "value": 10}]}
        ]
    },
    "archer": {
        "displayName": "Archer",
        "requiredTags": ["Archer"],
        "bonuses": [
            {"requiredCount": 2, "description": "+15% Attack Speed", "effects": [{"type": "AttackSpeed", "value": 0.15}]},
            {"requiredCount": 4, "description": "+30% Attack Speed, +5 Range", "effects": [{"type": "AttackSpeed", "value": 0.3}]}
        ]
    },
    "human": {
        "displayName": "Human Alliance",
        "requiredTags": ["Human"],
        "bonuses": [
            {"requiredCount": 2, "description": "+10% Attack", "effects": [{"type": "Attack", "value": 0.1}]}
        ]
    },
    "darkelf": {
        "displayName": "Dark Elves",
        "requiredTags": ["DarkElf"],
        "bonuses": [
            {"requiredCount": 2, "description": "+15% Ability Power", "effects": [{"type": "AbilityPower", "value": 0.15}]},
            {"requiredCount": 4, "description": "+30% Ability Power", "effects": [{"type": "AbilityPower", "value": 0.3}]}
        ]
    }
}


def create_scriptable(type_name: str, name: str, path: str, data: dict = None) -> dict:
    """Send create_scriptable command to Unity MCP server."""
    payload = {
        "action": "create_scriptable",
        "type": type_name,
        "name": name,
        "path": path
    }
    if data:
        payload["data"] = data

    resp = requests.post(MCP_URL, json=payload, timeout=10)
    resp.raise_for_status()
    return resp.json()


def create_unit(preset: str, name: str = None) -> dict:
    """Create a unit from preset."""
    if preset not in UNIT_PRESETS:
        print(f"Unknown preset: {preset}. Available: {list(UNIT_PRESETS.keys())}")
        return {}

    data = UNIT_PRESETS[preset].copy()
    unit_name = name or preset.title().replace("_", "")
    return create_scriptable("UnitDefinition", unit_name, "Assets/ScriptableObjects/Units", data)


def create_ability(preset: str, name: str = None) -> dict:
    """Create an ability from preset."""
    if preset not in ABILITY_PRESETS:
        print(f"Unknown preset: {preset}. Available: {list(ABILITY_PRESETS.keys())}")
        return {}

    data = ABILITY_PRESETS[preset].copy()
    ability_name = name or preset.title().replace("_", "")
    return create_scriptable("AbilityDefinition", ability_name, "Assets/ScriptableObjects/Abilities", data)


def create_synergy(preset: str, name: str = None) -> dict:
    """Create a synergy from preset."""
    if preset not in SYNERGY_PRESETS:
        print(f"Unknown preset: {preset}. Available: {list(SYNERGY_PRESETS.keys())}")
        return {}

    data = SYNERGY_PRESETS[preset].copy()
    synergy_name = name or preset.title().replace("_", "")
    return create_scriptable("SynergyDefinition", synergy_name, "Assets/ScriptableObjects/Synergies", data)


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  create_unit.py unit <preset> [name]")
        print("  create_unit.py ability <preset> [name]")
        print("  create_unit.py synergy <preset> [name]")
        print("\nAvailable unit presets:", ", ".join(UNIT_PRESETS.keys()))
        print("Available ability presets:", ", ".join(ABILITY_PRESETS.keys()))
        print("Available synergy presets:", ", ".join(SYNERGY_PRESETS.keys()))
        sys.exit(1)

    cmd = sys.argv[1]
    preset = sys.argv[2] if len(sys.argv) > 2 else None
    name = sys.argv[3] if len(sys.argv) > 3 else None

    if cmd == "unit" and preset:
        result = create_unit(preset, name)
    elif cmd == "ability" and preset:
        result = create_ability(preset, name)
    elif cmd == "synergy" and preset:
        result = create_synergy(preset, name)
    else:
        print("Invalid command")
        sys.exit(1)

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
