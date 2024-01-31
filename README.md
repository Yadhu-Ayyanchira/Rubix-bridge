# Setting Up rubixgoplatform and Running the Quorum


## Windows Installation

1. **Add to System PATH**:
   - Right-click on the "Start" button and select "System."
   - In the System window, click on "Advanced system settings" on the left-hand side.
   - In the System Properties window, click on the "Environment Variables" button.
   - Under "User variables" or "System variables," locate the "Path" variable, select it, and click on the "Edit" button.
   - In the Edit Environment Variable window, click on the "New" button and add the path to the directory where `rubixgoplatform` is located (e.g., `C:\path\to\rubixgoplatform\directory`).
   - Click "OK" to close each window, confirming the changes.
   - You may need to restart any open command prompts or applications to apply the changes.

## macOS (formerly OS X) Installation

1. **Edit Shell Profile**:
   - Open the Terminal application.

2. **Edit Shell Profile**:
   - For Bash:
     ```bash
     nano ~/.bash_profile
     ```
   - For Zsh:
     ```bash
     nano ~/.zshrc
     ```

3. **Add the Directory to PATH**:
   - Add the following line to the file, replacing `/path/to/rubixgoplatform/directory` with the actual path to the directory:
     ```bash
     export PATH="/path/to/rubixgoplatform/directory:$PATH"
     ```

4. **Save and Exit**:
   - In Nano, press `Ctrl + O` to save the file and `Ctrl + X` to exit.

5. **Apply the Changes**:
   - In the Terminal, run the following command to apply the changes to your current session:
     ```bash
     source ~/.bash_profile  # For Bash
     # OR
     source ~/.zshrc         # For Zsh
     ```

## Linux Installation

1. **Edit Shell Profile**:
   - Open a terminal.

2. **Edit Shell Profile**:
   - For Bash:
     ```bash
     nano ~/.bashrc
     ```
   - For Zsh:
     ```bash
     nano ~/.zshrc
     ```

3. **Add the Directory to PATH**:
   - Add the following line to the file, replacing `/path/to/rubixgoplatform/directory` with the actual path to the directory:
     ```bash
     export PATH="/path/to/rubixgoplatform/directory:$PATH"
     ```

4. **Save and Exit**:
   - In Nano, press `Ctrl + O` to save the file and `Ctrl + X` to exit.

5. **Apply the Changes**:
   - In the terminal, run the following command to apply the changes to your current session:
     ```bash
     source ~/.bashrc  # For Bash
     # OR
     source ~/.zshrc  # For Zsh
     ```

## Running 7 Nodes Quorum

Now that you have `rubixgoplatform` set up systemwide, you can run 7 nodes using the following script:

```bash
#!/bin/bash
logfile="/home/ubuntu/cronlog/rubixstartup.log"
echo "Starting sessions" >> $logfile

base_port=20000
base_grpc_port=10500

for ((i=1; i<=7; i++)); do
  port=$((base_port + i - 1))
  grpc_port=$((base_grpc_port + i - 1))
  screen -dmS "node$i" /home/ubuntu/rubix/rubixgoplatform/linux/rubixgoplatform run -p "node$i" -n "$i" -s -port "$port" -testNet -grpcPort "$grpc_port"
  echo "Started session for node$i, port: $port, grpcPort: $grpc_port" >> $logfile
done

echo "All sessions started" >> $logfile
  ```

# Running oneclickquorum.sh Script

## Prerequisites

Before running the "oneclickquorum.sh" script, make sure you have the following prerequisites in place:

- **Operating System**: These instructions are provided for Windows, macOS, and Linux.
- **`rubixgoplatform` Installation**: Ensure you have `rubixgoplatform` installed on your system.
- **Directory Path**: Navigate to the directory where the "oneclickquorum.sh" script is located.
- Make necessart changes to the path in the oneclickquorum file.

## Windows

1. **Open Command Prompt**:
   - Press `Win + R`, type `cmd`, and press Enter to open the Command Prompt.

2. **Navigate to the Script Directory**:
   - Use the `cd` command to navigate to the directory where the "oneclickquorum.sh" script is located.

3. **Run the Script**:
   - To run the script, use the following command:
     ```bash
     bash oneclickquorumwindows.bat
     ```

## macOS (formerly OS X)

1. **Open Terminal**:
   - Open the Terminal application.

2. **Navigate to the Script Directory**:
   - Use the `cd` command to navigate to the directory where the "oneclickquorum.sh" script is located.

3. **Run the Script**:
   - To run the script, use the following command:
     ```bash
     bash oneclickquorummac.sh
     ```

## Linux

1. **Open Terminal**:
   - Open a terminal.

2. **Navigate to the Script Directory**:
   - Use the `cd` command to navigate to the directory where the "oneclickquorum.sh" script is located.

3. **Make the Script Executable (if not already)**:
   - If the script is not already executable, you can make it executable by running:
     ```bash
     chmod +x oneclickquorum.sh
     ```

4. **Run the Script**:
   - To run the script, use the following command:
     ```bash
     ./oneclickquorum.sh
     ```

These steps will execute the "oneclickquorum.sh" script on Windows, macOS, and Linux, provided that you have set up `rubixgoplatform` and configured the script correctly for your environment.

They python script - bridge.py has an APIs to get details of the quorums and create quorumList.json file
Setting us the quorum and connecting them is manual for now. For instructions refer - https://docs.google.com/document/d/1GA8J9YALiRsNXq8XALS0Xi-jJeQtX-eyWQywem3-eno/edit

TODOs
- Need to write a script to setup and connect all the quorums.
