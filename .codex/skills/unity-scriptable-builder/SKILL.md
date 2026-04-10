---
name: unity-scriptable-builder
description: Create ScriptableObject assets for Unity game data. Use when creating UnitDefinition, AbilityDefinition, SynergyDefinition or any ScriptableObject data. Triggered by: "создай данные юнита", "создай способность", "создай синергию", "новый ScriptableObject", "создай asset".
---

# Unity Scriptable Object Builder

Create ScriptableObject assets for game data through Unity Editor commands.

## Codex Entry Point

For Codex, prefer the local CLI wrapper:

```bash
python tools/unity_mcp.py create-scriptable <Type> <Name> <Path> [--data "{...}"]
```

Default route: MCP proxy `localhost:3000`
Optional fallback: direct Unity server via `--direct` on `localhost:7777`

## Available ScriptableObjects

### UnitDefinition
Конфигурация типа юнита (Dark Fighter, Elven Archer, etc.)

**Поля:**
| Поле | Тип | Описание |
|------|-----|----------|
| unitId | string | Уникальный ID |
| displayName | string | Отображаемое имя |
| icon | Sprite | Иконка для UI |
| baseHP | int | Базовое здоровье |
| baseAttack | int | Базовая атака |
| attackSpeed | float | Скорость атаки |
| moveSpeed | float | Скорость движения |
| attackRange | int | Дистанция атаки (клетки) |
| classTags | string[] | Теги классов ["Warrior", "Archer"] |
| raceTags | string[] | Теги рас ["Human", "Elf", "DarkElf", "Orc", "Dwarf"] |
| abilities | AbilityDefinition[] | Ссылки на способности |
| prefab | GameObject | Префаб для спавна |
| goldCost | int | Стоимость в магазине |
| tier | int | Звёздность (1-5) |

**Пример создания:**
```csharp
// Через AICommandRouter.CreateScriptableObject
CreateScriptableObject("UnitDefinition", "DarkFighter", "Assets/ScriptableObjects/Units")
```

### AbilityDefinition
Описание способности (Active/Passive/Trigger)

**Поля:**
| Поле | Тип | Описание |
|------|-----|----------|
| abilityId | string | Уникальный ID |
| displayName | string | Название способности |
| description | string | Описание для UI |
| icon | Sprite | Иконка |
| type | AbilityType | Active, Passive, Trigger |
| targetType | TargetType | Self, SingleEnemy, AllEnemies, Area, Grid |
| damage | float | Урон |
| healing | float | Исцеление |
| duration | float | Длительность эффектов |
| cooldown | float | Кулдаун |
| manaCost | float | Стоимость маны |
| areaRadius | int | Радиус для Area targeting |
| vfxPrefab | GameObject | Визуальный эффект |
| castSound | AudioClip | Звук каста |
| triggerOn | string | Для Trigger: "OnAttack", "OnHit", "OnDeath" |

**TargetType варианты:**
- `Self` — на себя
- `SingleEnemy` — одного врага
- `SingleAlly` — одного союзника
- `AllEnemies` — всех врагов
- `AllAllies` — всех союзников
- `Area` — область с радиусом
- `Grid` — вся сетка

### SynergyDefinition
Бонусы за сбор определённых классов/рас

**Поля:**
| Поле | Тип | Описание |
|------|-----|----------|
| synergyId | string | Уникальный ID |
| displayName | string | Название синергии |
| description | string | Описание |
| requiredTags | string[] | Теги для активации |
| bonuses | SynergyBonus[] | Массив пороговых бонусов |

**SynergyBonus структура:**
```csharp
public class SynergyBonus
{
    public int requiredCount;      // Сколько нужно юнитов
    public string bonusDescription; // Описание бонуса
    public BonusEffect[] effects;   // Массив эффектов
}
```

**BonusType варианты:**
- `HP` — +Здоровье
- `Attack` — +Атака
- `AttackSpeed` — +Скорость атаки (%)
- `AbilityPower` — +Сила способностей
- `Armor` — +Броня
- `MoveSpeed` — +Скорость движения

## Usage Patterns

### Создание юнита через Unity
```bash
# В Unity Editor:
1. Правый клик в Project window → Create → LAB → Units → Unit Definition
2. Заполнить поля
3. Сохранить как "Assets/ScriptableObjects/Units/DarkFighter.asset"
```

### Создание через Codex CLI
```bash
python tools/unity_mcp.py create-scriptable UnitDefinition DarkFighter Assets/ScriptableObjects/Units --field baseHP=120 --field baseAttack=15 --field tier=1 --field 'classTags=["Warrior"]' --field 'raceTags=["Human"]'
```

### Lineage2 Interlude - Complete Class List

Все комбинации Раса + Класс для L2 Interlude (Base → 1st → 2nd → 3rd Transfer)

#### **HUMAN (Человек)**

| Base | 1st Transfer | 2nd Transfer | 3rd Transfer | Class Tags |
|------|--------------|--------------|--------------|------------|
| Human Fighter | Warrior | Gladiator | Duelist | Warrior, DPS |
| Human Fighter | Warrior | Warlord | Dreadnought | Warrior, AOE |
| Human Fighter | Knight | Dark Avenger | Hell Knight | Knight, Tank |
| Human Fighter | Knight | Paladin | Phoenix Knight | Knight, Healer, Tank |
| Human Fighter | Rogue | Treasure Hunter | Adventurer | Rogue, Melee |
| Human Fighter | Rogue | Hawkeye | Sagittarius | Rogue, Archer |
| Human Mystic | Cleric | Bishop | Cardinal | Healer, Support |
| Human Mystic | Cleric | Prophet | Hierophant | Healer, Buffer |
| Human Mystic | Wizard | Sorcerer | Archmage | Mage, DPS |
| Human Mystic | Wizard | Necromancer | Soul Taker | Mage, Summoner |
| Human Mystic | Wizard | Warlock | Arcana Lord | Mage, Summoner |

#### **ELF (Эльф)**

| Base | 1st Transfer | 2nd Transfer | 3rd Transfer | Class Tags |
|------|--------------|--------------|--------------|------------|
| Elven Fighter | Elven Knight | Temple Knight | Eva's Templar | Knight, Tank |
| Elven Fighter | Elven Knight | Swordsinger | Sword Muse | Knight, Buffer |
| Elven Fighter | Elven Scout | Silver Ranger | Moonlight Sentinel | Archer, DPS |
| Elven Fighter | Elven Scout | Plains Walker | Wind Rider | Rogue, Melee |
| Elven Mystic | Elven Wizard | Spellsinger | Mystic Muse | Mage, DPS |
| Elven Mystic | Elven Wizard | Elemental Summoner | Elemental Master | Mage, Summoner |
| Elven Mystic | Elven Oracle | Elder | Eva's Saint | Healer, Support |

#### **DARK ELF (Тёмный Эльф)**

| Base | 1st Transfer | 2nd Transfer | 3rd Transfer | Class Tags |
|------|--------------|--------------|--------------|------------|
| Dark Fighter | Palus Knight | Shillien Knight | Shillien Templar | Knight, Tank |
| Dark Fighter | Palus Knight | Blade Dancer | Spectral Dancer | Knight, Buffer |
| Dark Fighter | Assassin | Abyss Walker | Ghost Hunter | Rogue, Melee |
| Dark Fighter | Assassin | Phantom Ranger | Ghost Sentinel | Archer, DPS |
| Dark Mystic | Dark Wizard | Spellhowler | Storm Screamer | Mage, DPS |
| Dark Mystic | Dark Wizard | Phantom Summoner | Spectral Master | Mage, Summoner |
| Dark Mystic | Shillien Oracle | Shillien Elder | Shillien Saint | Healer, Buffer |

#### **ORC (Орк)**

| Base | 1st Transfer | 2nd Transfer | 3rd Transfer | Class Tags |
|------|--------------|--------------|--------------|------------|
| Orc Fighter | Orc Raider | Destroyer | Titan | Warrior, DPS |
| Orc Fighter | Orc Raider | Tyrant | Grand Khavatari | Warrior, Monk |
| Orc Mystic | Orc Shaman | Overlord | Dominator | Buffer, Debuffer |
| Orc Mystic | Orc Shaman | Warcryer | Doomcryer | Buffer, Healer |

#### **DWARF (Дварф)**

| Base | 1st Transfer | 2nd Transfer | 3rd Transfer | Class Tags |
|------|--------------|--------------|--------------|------------|
| Dwarf Fighter | Scavenger | Bounty Hunter | Fortune Seeker | Rogue, Melee |
| Dwarf Fighter | Artisan | Warsmith | Maestro | Smith, Crafter |

#### **KAMAEL** (Interlude - Limited)

| Base | 1st Transfer | 2nd Transfer | 3rd Transfer | Class Tags |
|------|--------------|--------------|--------------|------------|
| Male Soldier | Trooper | Berserker | Doombringer | Warrior, DPS |
| Male Soldier | Warder | Soul Breaker (M) | Trickster | Rogue, Mage |
| Female Soldier | Soldier | Soul Breaker (F) | Trickster | Rogue, Mage |
| Female Soldier | Warder | Arbalester | Judicator | Archer, DPS |
| Male Soldier | Soul Breaker | Soul Taker | Soul Taker | Mage, DPS |

#### **Синергии по расам (Race Synergies)**

| Раса | Пороги | Бонусы |
|------|--------|--------|
| Human Alliance | 2/4/6 | +10% ATK / +15% HP / +1 All Stats |
| Elven Kinship | 2/4 | +15% Evasion / +20% Cast Speed |
| Dark Elf Covenant | 2/4 | +20% ATK / +25% Magic Power |
| Orc Brotherhood | 2/4 | +25% HP / +10% ATK Speed |
| Dwarf Clan | 2/3 | +10% Gold / +20% Item Drop |
| Kamael Legion | 2/4 | +15% Crit / +10% Move Speed |

#### **Синергии по классам (Class Synergies)**

| Класс | Пороги | Бонусы |
|-------|--------|--------|
| Warrior | 2/4/6 | +10% HP / +15% ATK / +20% HP |
| Knight | 2/4 | +20% Armor / +15% HP |
| Archer | 2/4/6 | +15% ATK / +20% Crit / +25% Crit Damage |
| Rogue | 2/4 | +20% Evasion / +25% Crit |
| Mage | 2/4/6 | +20% Magic Power / +30% Magic Power / Cast Speed |
| Healer | 2/3 | +25% Healing / +50% Healing |
| Summoner | 2/4 | +15% Summon HP / +25% Summon ATK |
| Buffer | 2/3 | +20% Buff Duration / +30% Buff Effect |

#### **Синергии по типам боя (Combat Synergies)**

| Тип | Пороги | Бонусы |
|-----|--------|--------|
| Melee DPS | 2/4/6 | +10% ATK / +15% ATK / +20% ATK |
| Ranged DPS | 2/4 | +20% ATK / +30% Crit |
| Tank | 2/3 | +25% Armor / +40% Armor |
| Support | 2/4 | +15% Buff Duration / +25% Healing |
| AOE | 2/4 | +20% AOE Damage / +30% AOE Radius |

#### **Ключевые способности по классам (3rd Transfer)**

##### **HUMAN**

| Класс | Способность 1 | Способность 2 | Способность 3 | Описание |
|-------|---------------|---------------|---------------|----------|
| Duelist | Triple Slash | Sonic Storm | Final Secret | Урон по области, бафф атаки |
| Dreadnought | Whirlwind | Battle Cry | Thunder Storm | AOE урон, боевой клич |
| Phoenix Knight | Shield Fortress | Holy Armor | Summon Cubic | Танк, защита, саммон |
| Hell Knight | Shield Bash | Curse of Darkness | Summon Dark Cubic | Дебафф, танк |
| Adventurer | Blinding Blow | Focus Skill | Evasion | Уклонение, крит удар |
| Sagittarius | Lethal Shot | Snipe | Rapid Shot | Дальний бой, летал |
| Cardinal | Major Heal | Restoration | Ressurection | Лечение, resurrection |
| Hierophant | Might | Battle Heal | Haste | Лечение ,баффы союзников |
| Archmage | Prominence | Fear | Fire Vortex | Магический урон |
| Soul Taker | Curse Death Link | Curse Gloom | Summon Cursed Man | Дебафф, саммон |
| Arcana Lord | Summon Kat the Cat | Summon Mew the Cat | Queen of Cat | Саммоны |

##### **ELF**

| Класс | Способность 1 | Способность 2 | Способность 3 | Описание |
|-------|---------------|---------------|---------------|----------|
| Eva's Templar | Defensive Aura | Touch of Eva | Entangle | Танк, контроль |
| Sword Muse | Song of Earth | Song of Hunter | Song of Wind | Песни-баффы |
| Moonlight Sentinel | Double Shot | Ultimate Evasion | Rapid Fire | Лучник, крит |
| Wind Rider | Backstab | Bluff | Lethal Blow | Рог, sneak attack |
| Mystic Muse | Hydro Blast | Solar Flare | Ice Vortex | Водная/огненная магия |
| Elemental Master | Summon Unicorn Seraphim | Summon Unicorn Mirael | Summon Magnus | Саммоны стихий |
| Eva's Saint | Major Heal | Recharge | Purify | Лечение, мана |

##### **DARK ELF**

| Класс | Способность 1 | Способность 2 | Способность 3 | Описание |
|-------|---------------|---------------|---------------|----------|
| Shillien Templar | Curse of Darkness | Power Break | Summon Dark Cubic | Дебафф танк |
| Spectral Dancer | Dance of Concentration | Dance of Fury | Siren | Танцы-баффы |
| Ghost Hunter | Backstab | Deadly Blow | Bluff | Рог, крит |
| Ghost Sentinel | Double Shot | Hex | Lethal Shot | Лучник, дебафф |
| Storm Screamer | Hurricane | Shadow Spark | Wind Vorted | Тёмная магия |
| Spectral Master | Summon Nightshade | Summon Silhouette | Summon Soulless | Саммоны тьмы |
| Shillien Saint | Major Heal | Recharge | Empower | Лечение, мана, бафф на магический урон |

##### **ORC**

| Класс | Способность 1 | Способность 2 | Способность 3 | Описание |
|-------|---------------|---------------|---------------|----------|
| Titan | Crush of Doom | Zealot | Frenzy | Берсерк, AOE |
| Grand Khavatari | Bison Totem | Ogre Totem | Puma Totem | Тотемы, боевой режим |
| Dominator | Seal of Silence | Seal of Slow | Victory of Paagrio | Чанты-баффы, Дебаффы, AOE контроль |
| Doomcryer | Chant of Victory | Chant of Life | Chant of Shielding | Чанты-баффы |

##### **DWARF**

| Класс | Способность 1 | Способность 2 | Способность 3 | Описание |
|-------|---------------|---------------|---------------|----------|
| Fortune Seeker | Spoil | Sweep | Stun | Фарм лута |
| Maestro | Summon Siege Golem | Golem Armor | Stun | Создание предметов |

##### **KAMAEL**

| Класс | Способность 1 | Способность 2 | Способность 3 | Описание |
|-------|---------------|---------------|---------------|----------|
| Doombringer | Storm Assault | Razor Storm | Binding Blow | AOE, контроль |
| Trickster | Hide | Trick | Switch | Стелс, trick |
| Judicator | Final Ultimatum | Light Burst | Space binding | Дебафф, контроль |
| Ghost Sentinel | Burst Shot | Dead Eye | Trap Shot | Лучник, ловушки |
| Soul Taker | Soul Sucking | Curse of Divinity | Burst | Дрейн, дебафф |

#### **Список всех способностей для создания**

##### **Атакующие (Damage)**
```
TripleSlash, SonicStorm, Whirlwind, BlindingBow, LethalShot, Backstab,
DeadlyBow, HydroBlast, Hurricane, CurseDeathLink, CrushOfDoom,
StormAssault, BurstShot, DoubleShot, PowerStrike, SonicBlaster,
FlameStrike, DeathSpike, Prominence, Tsunami, ShadowSpark
```

##### **Баффы (Buffs)**
```
Might, Shield, Empower, Focus, Berserk, Haste, Guidance, BlessTheBody,
BlessTheSoul, GreatMight, GreatShield, SongOfEarth, SongOfWater, SongOfWind,
DanceOfVampire, DanceOfShadow, ChantOfVictory, ChantOfLife, ChantOfShielding,
DefensiveAura, TouchOfEva, HolyArmor, FinalSecret
```

##### **Исцеление (Healing)**
```
MajorHeal, BattleHeal, Restoration, GroupHeal, Heal, Recharge, Purify,
VampiricRage
```

##### **Саммоны (Summons)**
```
SummonCursedMan, SummonKatTheCat, SummonMewTheCat, SummonQueenOfCat,
SummonUnicornSeraphim, SummonUnicornMirael, SummonMagnus,
SummonNightshade, SummonSilhouette, SummonSoulless,
SummonSiegeGolem, SummonDarkCubic
```

##### **Дебаффы (Debuffs)**
```
Hex, Slow, Poison, Silence, CurseGloom, PowerBreak, Stun, Entangle,
CurseOfDarkness, Bluff, SealOfSilence, SealOfSlow, CurseOfDivinity,
Siren, ShadowSpark
```

##### **Защитные (Defensive)**
```
ShieldFortress, UltimateEvasion, ShieldBash, Evasion, GolemArmor,
Hide, Switch
```

##### **AOE (Area of Effect)**
```
Whirlwind, ThunderStorm, SonicStorm, RazorStorm, BattleCry,
ChaosSymphony, CrushOfDoom, StormAssault
```

**Способности из L2:**
- Power Strike, Double Shot, Heal, Sonic Blaster, Flame Strike, Death Spike, Suppress, Shield Fortress, Ultimate Evasion, Dash, Power Break
