# Setting Up the Virtual Environment and Running the Flask App (Mac Version)

This guide explains how to set up a Python virtual environment using the `make_virtual_env.py` script and run the Flask app from the [FFA Web App Template Repository](https://github.com/jonesnoah45010/ffa_web_app_template).

## 1. Download code onto your Desktop

Download the project code as a zip file from [FFA Web App Template Repository](https://github.com/jonesnoah45010/ffa_web_app_template)  by clicking the big green Code button and then selecting `Download Zip`. Place the zip file `ffa_web_app_template-main.zip` on your Desktop.  Extract the folder on your Desktop.  The new folder will be called`ffa_web_app_template-main`.  You can delete the `ffa_web_app_template-main.zip` file at this point.



## 2. Set Up the Virtual Environment

You will now need to use the Terminal to navigate to your Desktop and then to the `ffa_web_app_template-main` folder on your Desktop to use the provided `make_virtual_env.py` script to create your virtual environment.  The virtual environment will be used to run the code is a safe way.  

### On Mac Terminal

Run the following commands:

```bash
cd Desktop/ffa_web_app_template-main
python make_virtual_env.py
```
-   When prompted to choose a python version, don't type anything and just press enter. This will just default to using your default Python version
-   When prompted for a name your your virtual environment, enter `env` as the name.
    
-   After the script finishes, it will display an activation command like this... `source env/bin/activate`
    
-   Copy, paste, and run the activation command in your terminal to activate the virtual environment.
- You should see `(env)` show up to the left of your username in the Terminal. This mean you are inside of the virtual environment.  You can exit the virtual environment using `deactivate` at any time.
- You can reactivate the virtual environment later using `source env/bin/activate` run from within the `ffa_web_app_template-main` folder.  
    

## 3. Install Required Packages

After activating the virtual environment, assuming you are already in the `ffa_web_app_template-main` folder in your Terminal, run ...
``` bash
cd web_app
pip install -r requirements.txt
```
This will install all the necessary dependencies for the Flask app.

## 4. Run the Flask App

Once the packages are installed, you can start the Flask app by running:

```bash
python3 main.py
```
You should see something like this show up in your Terminal ... 
```bash
* Running on http://127.0.0.1:8080
```
- You are now hosting a python Flask based website locally.  Copy and paste `http://127.0.0.1:8080` into your web browser to view the website app.
- You can stop running the app at any point using `control + c` inside the command line.  

## 5. Re-Running the Flask App Later

- If you close the command line and want to run the app again in the future, you will not need to do steps 2 and 3 again.   The virtual environment and packages will still be there.   You just need to enter the virtual environment and run `main.py` again.
- Just open a new Mac Terminal window and run `cd Desktop/ffa_web_app_template-main` , then run `source env/bin/activate`, then run `cd web_app`, then run `python3 main.py`



----------





# Setting Up the Virtual Environment and Running the Flask App (Windows Version)

This guide explains how to set up a Python virtual environment using the `make_virtual_env.py` script and run the Flask app from the [FFA Web App Template Repository](https://github.com/jonesnoah45010/ffa_web_app_template).

## 1. Download code onto your Desktop

Download the project code as a zip file from [FFA Web App Template Repository](https://github.com/jonesnoah45010/ffa_web_app_template) by clicking the big green **Code** button and then selecting `Download ZIP`. Place the zip file `ffa_web_app_template-main.zip` on your Desktop. Extract the folder on your Desktop. The new folder will be called `ffa_web_app_template-main`. You can delete the `ffa_web_app_template-main.zip` file at this point.

## 2. Set Up the Virtual Environment

Now you’ll use Command Prompt to navigate to your Desktop and then into the `ffa_web_app_template-main` folder to use the provided `make_virtual_env.py` script to create your virtual environment.

### On Windows Command Prompt

Run the following commands:
```bash
cd Desktop\ffa_web_app_template-main
python make_virtual_env.py
```

-   When prompted to choose a Python version, **just press Enter** to use your default Python version.
    
-   When prompted to name your virtual environment, enter `env` as the name.
    
-   After the script finishes, it will display an activation command like this: `env\Scripts\activate`
    
-   Copy, paste, and run the activation command in your Command Prompt to activate the virtual environment.
    
-   You should see `(env)` appear to the left of your prompt. This means you are now inside the virtual environment. You can exit the virtual environment using `deactivate` at any time.
    
-   To reactivate the virtual environment later, navigate to the `ffa_web_app_template-main` folder and run:
    
    `env\Scripts\activate` 
    

## 3. Install Required Packages

After activating the virtual environment, assuming you are already in the `ffa_web_app_template-main` folder in Command Prompt, run:

```bash
cd web_app
pip install -r requirements.txt
```

This will install all the necessary dependencies for the Flask app.

## 4. Run the Flask App

Once the packages are installed, you can start the Flask app by running:

`python main.py` 

You should see something like this in your Command Prompt:

 `* Running on http://127.0.0.1:8080` 

-   You are now hosting a Python Flask-based website locally. Copy and paste `http://127.0.0.1:8080` into your web browser to view the website.
    
-   You can stop running the app at any point by pressing `Ctrl + C` in the Command Prompt.
    

## 5. Re-Running the Flask App Later

-   If you close the Command Prompt and want to run the app again in the future, **you do not need to repeat steps 2 and 3**. The virtual environment and packages will still be there.
    
-   To re-run the app:
    
    1.  Open a new Command Prompt window.
        
    2.  Run:
        
```bash
cd Desktop\ffa_web_app_template-main
env\Scripts\activate
cd web_app
python main.py
```



