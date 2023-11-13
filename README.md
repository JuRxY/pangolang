# Pangolang 🦔
Pangolang python based programming language. Pangolang files have a file extension named `.pan`. For now it has only been tested on `windows 7 machines and higher`.

# Installation ⬇️
To install pangolang download the zip folder and run the <a href="https://raw.githubusercontent.com/JuRxY/pangolang/main/installer/installer.exe">pangolang installer</a>. Uppon running the pangolang installer you will be asked to specify the location of a folder in which the main .exe and .bat files of pangolang will be stored. The installer will automatically add this location to the path. Installation might require a system restart. After the restart there should be a new `terminal` command called `pango`. Uppon running the command, a pangolang command line will open.

# Run Scripts 🏃‍♂️
There are two ways to run scripts:
1. To run a pangolang script first navigate to `/pengolang_v1.2/pangolang.exe`. Then you can run custom script files using the pangolang command `RUN("example.pan")` or run commands in the pangolang command line.
2. You can run pangolang scripts using the `pango` command in the terminal. This will open a new pangolang command. Then you can run custom script files using the pangolang command `RUN("example.pan")` or run commands in the pangolang command line.

# Executing Commands 📝
You can find some info about all the commands and the syntax in the `grammar.txt` file. Documentation is on the way.

<!--
# Rundown of all the files:
```bash
+---pangolang_v1.2
|       example.pan
|       grammar.txt
|       pango.bat
|       pangolang.exe
|
+---tests
|       example.pan
|       fibonacci.pan
|       pyramid.pan
|       pythonify.pan
|
+---pangolang-language-support
|   |   .vscodeignore
|   |   CHANGELOG.md
|   |   language-configuration.json
|   |   package.json
|   |   README.md
|   |   test.pan
|   |   vsc-extension-quickstart.md
|   |
|   +---.vscode
|   |       launch.json
|   |
|   +---syntaxes
|           pangolang.tmLanguage.json
|
|   grammar.txt
|   pangolang.py
|   README.md
|   shell.py
|   strings_with_arrows.py
```
-->