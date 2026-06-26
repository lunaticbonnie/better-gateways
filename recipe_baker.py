import json
from typing import Any, cast

def get_nested(data: dict[str, Any], nested_key: str) -> Any:
  current = data
  for key in nested_key.split("."):
    current = current[key]
  return current

def set_nested(data: dict[str, Any], nested_key: str, value: Any) -> dict[str, Any]:
  current = data
  key_parts = nested_key.split(".")
  for key in key_parts[:-1]:
    try:
      current = current[key]
    except KeyError:
      current[key] = {}
      current = current[key]
  current[key_parts[-1]] = value
  return value

def parse_value(s: str) -> Any:
  if s == "[]":
    return []
  elif s == "{}":
    return {}
  elif s[0] == '"':
    return s[1:-1]
  else:
    return int(s)
def bake_recipe(src_path: str, dest_path: str, mc_version: list[int]):
  # parse recipe
  data = {}
  current: Any = data
  with open(src_path, "r") as src_file:
    for line in src_file.readlines():
      line = line.strip()
      if len(line) == 0: continue
      if " :: " in line or " = " in line:
        line = line.strip()
        key, line = line.split(" ", 1)
        line = line.strip()
        operator, line = line.split(" ", 1)
        value = parse_value(line.strip())
        if operator == "::":
          current = set_nested(data, key, value)
        else:
          set_nested(current, key, value)
      else:
        value = parse_value(line.strip())
        cast(list[Any], current).append(value)
  # print recipe in the appropriate format
  recipe = {}
  if mc_version >= [26]:
    recipe["type"] = "minecraft:crafting_shaped"
    recipe["category"] = "misc"
    recipe["group"] = data["group"]
    recipe["key"] = data["items"]
    recipe["pattern"] = data["shape"]
    recipe["result"] = data["result"]
  else:
    recipe["type"] = "gateways:gate_recipe"
    recipe["group"] = data["group"]
    recipe["pattern"] = data["shape"]
    items = {}
    for k, v in cast(dict, data["items"]).items():
      if v[0] == '#':
        set_nested(items, f"{k}.tag", v[1:])
      else:
        set_nested(items, f"{k}.item", v)
    recipe["key"] = items
    set_nested(recipe, "result.id", get_nested(data, "result.id"))
    set_nested(recipe, "gateway", get_nested(data, "result.components.gateways:gateway"))
  with open(dest_path, "w") as dest_file:
    json.dump(recipe, dest_file, indent=2, sort_keys=False)