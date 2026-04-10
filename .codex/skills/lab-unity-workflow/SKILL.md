---
name: lab-unity-workflow
description: Project workflow for the LAB Unity auto-battler. Use when working in this repository on Unity gameplay, Editor automation, MCP-driven scene building, ScriptableObjects, or C# changes tied to the LAB project. Enforces project-specific rules for scene editing, iteration docs, architecture, and validation.
---

# LAB Unity Workflow

Use this skill for project-specific rules in the LAB repository.

## Core Rules

- Develop for a Unity auto-battler game in the Lineage2 setting.
- Never edit Unity scene YAML directly.
- Use MCP tools for scene and asset operations when they are available:
  - `create_scene`
  - `create_object`
  - `add_component`
  - `create_prefab`
  - `create_scriptable`
- Prefer the local CLI wrapper `python tools/unity_mcp.py ...` as the Codex-facing entrypoint for these operations.
- Write C# and project code first, then apply scene/editor changes through MCP.

## Standard Workflow

Follow this order unless the task clearly requires a different sequence:

1. Read the relevant project context before changing code.
2. Implement or update C# code.
3. Use MCP tools to build or modify scenes, prefabs, or ScriptableObjects.
   Prefer `python tools/unity_mcp.py` over ad-hoc HTTP snippets.
4. Validate compile errors and editor feedback.
5. Fix errors before moving on.

## Project Context

- Project: LAB
- Genre: auto-battler in the style of Dota Auto Chess
- Theme: Lineage2
- Engine: Unity
- Editor integration: MCP server used to connect the agent workflow to the Unity Editor

## Code Style

- Use `PascalCase` for classes and methods.
- Use `camelCase` for private fields with underscore prefix, for example `_privateField`.
- Keep battle logic separate from Unity view components.
- Follow the project's `MVC/ECS-lite` direction.
- Use `ScriptableObject` assets to describe unit abilities and game data where appropriate.

## Iteration Discipline

- Before starting a new task, create an iteration note in `.claude/iterations/XXX_name.md`.
- At the start of each response, summarize the current state from the latest iteration log when that log exists and is relevant to the task.

## Build And Validation

- Unity validation: use project build scripts if present, or validate through the available Unity/C# tooling.
- MCP server validation: `npm run build` or `python -m build` when relevant to the MCP side.
- Tests: use `pytest` for MCP/server-side Python code and `NUnit` for Unity-side test coverage when applicable.

## When To Escalate

- If MCP is unavailable, explain the blocker and fall back to code-only changes when possible.
- If a task would require direct scene YAML edits, stop and choose an MCP-based path instead.
- If architecture pressure pushes logic into MonoBehaviours, move shared logic back toward project model/controller layers unless the repository already establishes a different pattern in that area.
