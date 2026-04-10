#!/usr/bin/env python3
"""MCP Client for Unity Scene Builder."""
import requests
import json
import sys

MCP_URL = "http://localhost:7777/command"

def send_command(action: str, **kwargs) -> dict:
    """Send command to Unity MCP server."""
    payload = {"action": action, **kwargs}
    resp = requests.post(MCP_URL, json=payload, timeout=10)
    resp.raise_for_status()
    return resp.json()

def create_scene(name: str):
    return send_command("create_scene", name=name)

def create_object(name: str, parent: str = None):
    return send_command("create_object", name=name, parent=parent)

def add_component(target: str, component: str, props: dict = None):
    return send_command("add_component", target=target, component=component, props=props or {})

def create_prefab(name: str, path: str):
    return send_command("create_prefab", name=name, path=path)

def create_scriptable(type_name: str, name: str, path: str, data: dict = None):
    return send_command("create_scriptable", type=type_name, name=name, path=path, data=data or {})

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: mcp-client.py <action> [args...]")
        sys.exit(1)

    action = sys.argv[1]
    args = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}

    result = send_command(action, **args)
    print(json.dumps(result, indent=2))
