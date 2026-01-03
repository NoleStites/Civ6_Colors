# Civ6_Colors
## Description
This repo contains an executable that allows users to edit the main colors of leaders in the video game Sid Meier's Civilization VI. The mod currently supports base-game leaders and DLC content.

> It is important to note that this code edits the Civilization VI source code directly, namely the following files: `playerstandardcolors.xml` and `playercolors.xml`. **This program lets you safely undo any changes to regain the original source code**.

![An example leader with colors changed](/assets/preview.png)

## Setup
### Windows
1. Download the executable   
    - [**Windows** executable](https://github.com/NoleStites/Civ6_Colors/releases/latest/download/Civ6Colors-Windows.exe)   
    > Your system will likely flag the file as untrustworthy. Click "Keep" and it will be downloaded.
2. Open the downloaded file with double-click and enjoy!
    > **IMPORTANT**: understand that this file, when run, will access and modify your Civilization VI source code. It is perfectly safe and can be undone through clicking "Reset Files" in the app.

## Functionality
| Button/Section Name | Description |
| --- | --- |
| "Select a Leader" | A list of leaders to select from as the target of the color assignment. |      
| "Choose Primary Color" | Displays a color picker to select a primary color. The primary color represents a civilization's **outer borders** and **background color** of city nameplates. |
| "Choose Secondary Color" | Displays a color picker to select a secondary color. The secondary color represents a civilization's **inner borders** and **text color** of city nameplates. | 
| "Reset Files" | Restores the game source code to its original state as if the mod never touched it. |
| "Subimt!" | Assigns the current primary and secondary color selection to the selected leader. |

## Viewing the New Colors
Before anything, start/restart the Civilization VI application (if in game, close and restart)

### Singleplayer
1. In the "Create Game" menu, select the leader for which you changed the color (ex: Gandhi)
2. Enter the "Advanced Setup" options       
![Advanced Setup location](/assets/single_step2.png "Where to find the Advanced Setup options")
3. Select the icon to the left of the leader portrait and choose the 4th/final color option, which should match your custom colors (ex: hot pink and yellow)      
![Custom color location](/assets/single_step3.png "Singleplayer: How to select your custom colors")

### Multiplayer
1. In the "Staging Room", select the leader for which you changed the color (ex: Gandhi)
2. Select the icon to the left of the leader portrait and choose the 4th/final color option, which should match your custom colors (ex: hot pink and yellow)      
![Custom color location](/assets/multi_step2.png "Multiplayer: How to select your custom colors")

> **NOTE 1**: when you change the color of any leader using the mod, you must restart the game to see the changes.     
> **NOTE 2**: new changes will automatically apply to already-existing games, assuming the 4th/final color option for the leader was selected at game-creation.

## Disclaimer
This project is an unofficial modding utility for Civilization VI that allows users to customize in-game colors by modifying configuration files **they already own**. This tool does **not** distribute or contain any copyrighted game assets, nor does it bypass any form of DRM or protected code.

Use of this tool may violate the End User License Agreement (EULA) of Civilization VI. By using this script, you agree that you are responsible for any modifications made to your own game installation.

This project is not affiliated with, endorsed by, or associated with Firaxis Games or 2K in any way. All trademarks and copyrights belong to their respective owners.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
