# LoLQueuePop

**LoLQueuePop** is a Python-based automation script designed to help you accept League of Legends queue pops remotely. League of Legends queues can sometimes last 5-10 minutes, with only a short window to accept the queue pop. If you're away from your computer during this window, you might miss the opportunity to join the match. This script moves your mouse and clicks the accept button automatically, ensuring you never miss a queue pop.

## Usage

1. **Set up environment:**
   - Ensure Python is installed.
   - Create a virtual environment:  
     `python -m venv .venv`
   - Activate the virtual environment:  
     On Windows: `.venv\Scripts\activate`
2. **Install dependencies:**

   - Run `pip install -r requirements.txt` to install the necessary libraries, including `pyautogui` for mouse automation.

3. **Run the script:**

   - Execute the script with:  
     `python main.py`
   - The script will move your mouse to a target position and click the accept button in the League of Legends queue window.

4. **Remote usage via SSH:**

   - You can run the script remotely via SSH from your phone, allowing you to trigger it when you're not in the room.
   - **Important:** Running the Python script directly via SSH won't work because SSH is headless (no graphical interface), so the Python script can't access the mouse input device. To solve this, the script should be run through a **Scheduled Task**.
   - #### Setup for SSH access:

5. **Install OpenSSH Server** on your Windows machine via the Settings or PowerShell.
6. **Open Port 22** in your firewall to allow SSH connections.
7. **Configure RSA Key**: Generate an RSA key pair on your phone and add the public key to the `authorized_keys` file on your Windows machine in the `.ssh` folder.
8. **Configure SSH Server**: Ensure the SSH configuration is set to allow public key authentication (`PubkeyAuthentication yes`), and the `authorized_keys` file is located in `.ssh/authorized_keys`.

9. **Scheduled Task:**
   - To ensure the script can control the mouse even when accessed remotely via SSH, configure the script to run as a Windows Task using Task Scheduler:
   - Open **Task Scheduler** on your Windows machine.
   - In **Task Scheduler**, click **Create Task**:
     - **General** tab: Name the task (e.g., "QueuePop").
     - **Triggers** tab: Do not add a specific trigger. This task will only trigger "Manually".
     - **Actions** tab: Click **New**, then set **Program/script** to `C:\Windows\System32\cmd.exe`, and the **Arguments** field to `/c "D: && cd Git\QueuePop && .venv\Scripts\activate && python main.py"` ("Git\QueuePop" is where the main.py and the env is located. "D:" can be ignored if you have everything on your C: drive)
     - **Conditions** and **Settings** tabs: Leave them at their defaults.
   - Save and close **Task Scheduler**.
   - Once configured, you can trigger the task manually using this command with SSH:  
     `schtasks /run /tn "QueuePop"`
