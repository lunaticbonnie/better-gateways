# better-gateways
Better settings for the [Gateways to Eternity](https://www.curseforge.com/minecraft/mc-mods/gateways-to-eternity) Minecraft mod.

1) Rebalance gateways to work alongside [Champions](https://www.curseforge.com/minecraft/mc-mods/champions-unofficial).
    - Increase gateway timeout per wave from 50 seconds to 5 minutes.
    - Remove wave modifiers for attributes like increased health/armor.
    - Make gateways keep mobs on failure.
    - Move gateway UI to above the gateway to not block the Champions UI.
2) Rework basic gateways
    - Rework Slime/Enderman/Blaze gateways to have unique spawning mechanics.
    - Add Spider/Skeleton gateways.
    - Simplify recipes to 1 Ender Eye + 8 mob drops.
3) Rework endless gateways
    - Remove default endless gateways.
    - Add endless Creeper/Zombie gateways.

Available on [CurseForge](https://www.curseforge.com/minecraft/mc-mods/better-gateways).

## dev
```
Download https://github.com/Patrolin/justice
Download Python 3
Download mod templates for all desired Minecraft versions into `templates/*` from:
  a) https://fabricmc.net/develop/template/
    Mod Name="ExampleMod"
    Package Name="com.examplemod"
    Minecraft Version=...
    Split client and common sources=false
    Rename to `fabric-<mc_version>.zip`
  b) https://files.minecraftforge.net/net/minecraftforge/forge/
    Rename to `forge-<mc_version>-<mdk_version>.zip`
  c) https://neoforged.net/mod-generator/
    Mod Name="ExampleMod"
    Package Name="com.examplemod"
    Minecraft Version=...
    Mod Authors="Me!"
    Mod Description="Description"
    Advanced Options.Add mixin configuration=true
    Rename to `neoforge-<mc_version>.zip`
```
`ice list` to list versions \
`ice <fabric|forge|neoforge> <mc_version>` to change to the selected version \
`ice run` or Open `./current` in IntelliJ IDEA and run `runClient` gradle task \
`ice build-version <version>` to run and build the selected version
