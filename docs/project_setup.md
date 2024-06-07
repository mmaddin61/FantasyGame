# Tools
## Visual Studio Code
This project was created with Visual Studio Code and it is highly recommended that VS Code is used.
### Download
https://code.visualstudio.com/download
### Recommended Extensions
Python: https://marketplace.visualstudio.com/items?itemName=ms-python.python

## GitHub Desktop
GitHub desktop is highly recommended since you can easily manage the repo from your PC. It also interfaces nicely with VS Code.
### Download
https://desktop.github.com

# Cloning
Once you have the necessary tools, you can clone the project's repo (https://github.com/mmaddin61/FantasyGame).

## Steps
1. On the repo's page (https://github.com/mmaddin61/FantasyGame), click the green "<> Code" button.
2. In the drop-down, click "Open with GitHub Desktop". If your browser prompts you to open GitHub Desktop, do so.
3. Once GitHub Desktop opens, a pop-up titled "Clone a repository" should appear. From here, you can select what folder to clone the repo to by clicking the "Choose..." button *(optional)*.

   **NOTE:** When the repo is cloned, a new folder is created inside the folder you specified with the "Choose..." that contains the project's files.

4. Click the "Clone" button.
5. You should now see "FantasyGame" in the top left corner. Now, click the "Open in Visual Studio Code" button towards the center of the screen. If this button says something else, go to step 6. Otherwise, go to step 9.
6. In the box containing the "Open in..." button, click the blue "Options" text.
7. In the pop-up, click the drop-down below "External editor" and select "Visual Studio Code".
8. Click the "Save" button. Go to step 5.
9. Visual Studio Code should open the cloned project. If prompted, click "Yes, I trust the authors".
10. You should now be able to see the entire project.

# Project Setup
## Steps
1. Go to the top toolbar and click "Terminal".
2. In the drop-down, click "New Terminal".
3. The terminal should appear at the bottom of your screen. Type the following command:

   ```.\scripts\setup-venv.ps1```

   If you receive an error regarding not being allowed to run scripts, go to the next step. Otherwise, go to step 6.

4. In the "Search" bar along your Windows toolbar, type "PowerShell".

5. Look for the "Windows PowerShell" result, right click it, then click "Run as administrator".
6. You should see "C:\WINDOWS\system32". Otherwise, repeat the last step.
7. Type the following command:

   ```Set-ExecutionPolicy RemoteSigned```

   This should allow you to run PowerShell scripts. If you wish to revert this setting at some point, type the following command:

   ```Set-ExecutionPolicy Restricted```

4. The virtual environment should now be created and a ".venv" folder should be added to your workspace. To confirm the virtual environment was created properly, type the following command:

   ```.\scripts\run.ps1```

   If everything is setup properly, the project should run and the game's window will appear.