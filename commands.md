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
  Enables flying for a player or group of players.

### Teleport
- `:tp`  
  Teleports you to where your cursor is pointing.
- `:tp (username/parameters)`  
  Teleports you to a player or group of players.
- `:tp (first person) (second person)`  
  Teleports the first player to the second player.

### Fly Speed
- `:flyspeed (username/parameters) (speed)`  
  Adjusts flying speed for yourself or a player or group of players. Speed is a numeric value.

---

## Admin Commands

### Give/Remove Builder
- `:givebuilder (username/parameters)`  
  Grants Builder rank to a player or group of players.
- `:removebuilder (username/parameters)`  
  Removes Builder rank from a player or group of players.

### Ban & Unban
- `:ban (username/parameters) (reason)`  
  Bans a player or group of players from the server with an optional reason.
- `:unban (username/parameters)`  
  Lifts a ban from a player or group of players.

### Kick
- `:kick (username/parameters)`  
  Kicks a player or group of players from the server.

### Kill
- `:kill (username/parameters)`  
  Instantly kills a player or group of players.

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
- `:teams set (username/parameters) (BrickColor)` — Assigns a player or group of players to a team.  
- `:teams setassignable (team name) (true/false)` — Allows or disallows team assignment.  
- `:teams setcolor (team name) (BrickColor)` — Changes the color of a team.

### Banlist
- `:banlist`  
  Displays a list of all players you have banned.

### Gear & Clear
- `:clear`  
  Clears all instances created from gear in the game.
- `:gear (username/parameters) (id)`  
  Spawns a gear item with the given ID for a player or group of players.

---

## Creator Commands

### Admin Management
- `:admin (username/parameters)` — Grants Admin rank to a player or group of players.  
- `:unadmin (username/parameters)` — Removes Admin rank from a player or group of players.
