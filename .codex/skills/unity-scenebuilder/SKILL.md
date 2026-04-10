---
name: unity-scenebuilder
description: Build Unity scenes programmatically via MCP server integration. Use when creating scenes, objects, components, prefabs, or ScriptableObjects in Unity Editor through HTTP commands. Triggered by requests to: create/modify Unity scenes, build GameObject hierarchies, add components, create prefabs or data assets.
---

# Unity Scene Builder

Build Unity scenes programmatically through the LAB Unity MCP endpoints.

## Codex Entry Point

For Codex, prefer the local CLI wrapper:

```bash
python tools/unity_mcp.py <command> [args...]
```

Default route: MCP proxy `localhost:3000`
Optional fallback: direct Unity server via `--direct` on `localhost:7777`

## Available Commands

### Create Scene
```bash
python tools/unity_mcp.py create-scene BattleScene
```
Creates a new scene at `Assets/Scenes/{name}.unity`

### Create Object
```bash
python tools/unity_mcp.py create-object PlayerGrid --parent GridManager
```
Creates a GameObject, optionally parenting it.

### Add Component
```bash
python tools/unity_mcp.py add-component PlayerGrid GridManager --prop width=8 --prop height=8
```
Adds component with serialized properties.

### Create Prefab
```bash
python tools/unity_mcp.py create-prefab Unit_DarkFighter Assets/Prefabs/Units
```
Saves current selection as prefab.

### Create Scriptable
```bash
python tools/unity_mcp.py create-scriptable UnitDefinition DarkFighter_Data Assets/ScriptableObjects/Units --field baseHP=100 --field baseAttack=15
```
Creates ScriptableObject asset with data.

## Common Patterns

### Battle Scene Setup
```json
[
  {"action": "create_scene", "name": "BattleScene"},
  {"action": "create_object", "name": "Grid"},
  {"action": "add_component", "target": "Grid", "component": "GridManager"},
  {"action": "create_object", "name": "PlayerBench"},
  {"action": "create_object", "name": "EnemyBoard"}
]
```

### Unit Prefab Creation
```json
[
  {"action": "create_scene", "name": "Temp_Prefab"},
  {"action": "create_object", "name": "DarkFighter"},
  {"action": "add_component", "target": "DarkFighter", "component": "UnitController"},
  {"action": "add_component", "target": "DarkFighter", "component": "SpriteRenderer"},
  {"action": "create_prefab", "name": "Unit_DarkFighter", "path": "Assets/Prefabs/Units"}
]
```

### ScriptableObject Data
```json
[
  {"action": "create_scriptable", "type": "UnitDefinition", "name": "DarkFighter", "path": "Assets/ScriptableObjects/Units"},
  {"action": "create_scriptable", "type": "AbilityDefinition", "name": "Fireball", "path": "Assets/ScriptableObjects/Abilities"}
]
```

## Component Types Reference

| Component | Purpose | Key Properties |
|-----------|---------|----------------|
| GridManager | Grid layout | width, height, cellSize |
| UnitController | Unit logic | hp, attack, abilities |
| SpriteRenderer | Visual | sprite, color |
| BoxCollider2D | Physics | size, offset |
| Animator | Animation | controller, parameters |

## Rules

1. **Never edit scene YAML directly** — always use MCP commands
2. **Create temporary scenes** for prefab building, then delete
3. **Use PascalCase** for object names (DarkFighter, not darkFighter)
4. **Parent appropriately** to maintain clean hierarchy
5. **Save scenes** after modifications

## Error Handling

If MCP server is unreachable:
1. Check Unity Editor is open
2. Verify MCP proxy is running on `localhost:3000`
3. Retry with `python tools/unity_mcp.py --direct ...` if the proxy is down but Unity HTTP is up
3. Check Console for errors
