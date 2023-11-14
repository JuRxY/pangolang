# Pangolang 🦔
    Pangolang is a python based programming language.
Pangolang files have a file extension named `.pan`. For now it has only been tested on `windows 7 machines and higher`.

# Installation ⬇️
1. Download the zip folder and run the <a href="https://raw.githubusercontent.com/JuRxY/pangolang/main/installer/installer.exe">pangolang installer</a>.
2. Uppon running the pangolang installer you will be asked to specify the location of a folder in which the main pangolang files will be stored. The installer will automatically add this location to the path. 
3. Installation might require a system restart. After the restart there should be a new `terminal` command called `pango`. Uppon running the command, a pangolang command line will open.

# Run Scripts 🏃‍♂️
There are two ways to run scripts:
1. To run a pangolang script first navigate to `/pengolang_v1.2/pangolang.exe`. 
    Then you can run custom script files using the pangolang command:

    ```bash
    RUN("example.pan")
    ```

2. You can run pangolang scripts using the `pango` command in the terminal:

    ```bash
    pango
    ```

    This will open a new pangolang terminal. Then you can run custom script files using the pangolang command:
    
    ```bash
    RUN("example.pan")
    ```
    
    or run commands in the pangolang command line.

# Executing Commands 📝
You can find some info about all the commands and the syntax in the `grammar.txt` file. Documentation is on the way.


# Rundown of all the files 📂
```
+---installer
|       installer.exe           # release ready installer file
|       installer.py            # installer.exe source code
|
+---pangolang_v1.2
|       example.pan             # an example of what a pangolang script looks like
|       grammar.txt             # some context on how to use pangolang
|       pango.bat               # bat file that calls pangolang.exe
|       pangolang.exe           # compiled version of the pangolang shell
|
+---pangolang-language-support  # visual studio code extension for pangolang
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
+---tests                       # some test pangolang files for testing 
|       example.pan
|       fibonacci.pan
|       pyramid.pan
|       pythonify.pan
|
|
|   grammar.txt                 # some context on how to use pangolang
|   pangolang.py                # source code for everything behind pangolang
|   README.md                   # README.md file
|   shell.py                    # the shell that gets compiled into pangolang.exe
|   strings_with_arrows.py      # a support file to make strings work
```