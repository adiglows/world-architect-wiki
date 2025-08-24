# Commands List

This page lists all available commands in **World Architect**.  
Commands are grouped by **rank**: Guest, Builder, Admin, and Creator.  
Parameters in commands can include `me`, `all`, `others`, or `random`.  
You can check all commands while playing by typing `:cmd` or `:cmds` in the chat.  

---

## Guest Commands

### Effect Cosmetics
- `:equip (effect name)`  
  Equips a cosmetic effect for your player. Only affects your own avatar.

---

## Builder Commands

### Fly
- `:fly`  
  Enables flying for yourself.
- `:fly (username/parameters)`  
  Allows flying for another player or group of players.

### Teleport
- `:tp`  
  Teleports you to where your cursor is pointing.
- `:tp (username/parameter)`  
  Teleports you to another player.
- `:tp (first person) (second person)`  
  Teleports the first player to the second player.

### Fly Speed
- `:flyspeed (username/parameters) (speed)`  
  Adjusts flying speed for yourself or other players. Speed is a numeric value.

---

## Admin Commands

### Give/Remove Builder
- `:givebuilder (username/parameter)`  
  Grants Builder rank to a player.
- `:removebuilder (username/parameter)`  
  Removes Builder rank from a player.

### Ban & Unban
- `:ban (username/parameter) (reason)`  
  Bans a player from the server with an optional reason.
- `:unban (username/parameter)`  
  Lifts a ban from a player.

### Kick
- `:kick (username/parameter)`  
  Kicks a player from the server.

### Kill
- `:kill (username/parameter)`  
  Instantly kills a player’s character.

### Time
- `:time 0-24`  
  Sets the in-game time (0 = midnight, 12 = noon, 24 = midnight).

### Gravity
- `:gravity (number)`  
  Changes the gravity. Default value is 196.2.

### Teams
> Note: Spaces in team names are represented as underscores `_`.

- `:teams add (team name) (BrickColor)` — Creates a new team with the chosen color.  
- `:teams remove (team name)` — Deletes a team.  
- `:teams set (username/parameter) (BrickColor)` — Assigns a player to a team.  
- `:teams setassignable (team name) (true/false)` — Allows or disallows team assignment.  
- `:teams setcolor (team name) (BrickColor)` — Changes the color of a team.

### Banlist
- `:banlist`  
  Displays a list of all players you have banned.

### Gear & Clear
- `:clear`  
  Clears all instances created from gear in the game.
- `:gear (player/parameters) (id)`  
  Spawns a gear item with the given ID for a player or group of players.

---

## Creator Commands

### Admin Management
- `:admin (username/parameter)` — Grants Admin rank to a player.  
- `:unadmin (username/parameter)` — Removes Admin rank from a player.