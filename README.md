# easy-rewards

Easy Rewards is an application made to automate some of the Microsoft Rewards actions.

## Recommended Python version
`v3.9+`

## Install

Make sure that you have the Gatsby CLI program installed:

```sh
pip install -r requirements.txt
```

## Prerequisites

If the Microsoft Edge and its webdriver are not installed, check the following instructions:

1. Download the browser from [Microsoft repository](https://www.microsoft.com/en-us/edge/download?form=MA13FJ)
2. Check the version of your browser build. Based on your browser version build, you have to download the corresponding Edge driver. To check the browser build, open Edge, then go to Settings > About Microsoft Edge.

![image](https://user-images.githubusercontent.com/42921279/210611075-fadc8251-8799-4eb4-9ab4-9ce2b47b7fe7.png)

3. Open Microsoft Edge Webdriver page using [this link](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
4. Select and download the latest one or as per your requirement.

![image](https://user-images.githubusercontent.com/42921279/210611433-5e9945a7-906f-4281-bbaf-baa76c4498a2.png)

## Environment variables

Copy the file `.env.example` to `.env`, then insert the appropriate keys/tokens.

```sh
cp .env.example .env
```


| Key    | Command                                                                                           |
| :-------- | :------------------------------------------------------------------------------------------------ |
| **EXECUTABLE_PATH**  | Path where the MS Edge webdriver is installed/stored |
| **PROFILE_NAME**  | Profile name that will be triggered on browser startup  |
| **PROFILE_PATH** | Profile path that will be triggered on browser startup - this info can be found by typing ```edge://version/``` on Edge  |

## Start bot:

```sh
python index.py
```
