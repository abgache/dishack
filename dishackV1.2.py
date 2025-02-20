import requests,base64,pyperclip,os,time,pyautogui,discord,threading
from colorama import Fore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def lwr(channel_id, token, sec):
    url = f"https://discord.com/api/v9/channels/{channel_id}/typing"
    headers = {"Authorization": token}
    for i in range(int(float(sec)/10)):
        response = requests.post(url, headers=headers)
        if response.status_code == 200 or response.status_code == 204:
            print("Request sent succesfuly !")
        else:
            print(f"Failed to send request. Status code: {response.status_code}")
        time.sleep(10)
            
def del_wh(wb):
    res = requests.delete(wb)
    if str(res.status_code)[0] == "2":
        print("Resource successfully deleted!")
    elif res.status_code == 404:
        print("The discord webhook does not exist/no longer exists, error 404!")
    elif str(res.status_code)[0] == "5":
        print(f"Error with discord servers : {res.status_code} - {res.text}")
    else:
        print(f"Deletion failed : {res.status_code} - {res.text}")


def get_pfp(bot_token, user_id):
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)
    @client.event
    async def on_ready():
        try:
            user = await client.fetch_user(user_id)
            avatar_url = user.avatar.url if user.avatar else "Aucun avatar"
            print(f"URL de la PFP : {avatar_url}")
        except Exception as e:
            print("Erreur :", e)
        await client.close()
    client.run(bot_token)

def msg_token():
    aze=input("Paste the ID of the conversation you want to send a message in: ")
    url = f"https://discord.com/api/v9/channels/{aze}/messages"
    auth = input("Paste your token: ")
    msg = input("Write the message you want to send: ")
    headers = {"Authorization": auth}
    data = {"content": msg}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
def del_token():
    Id_conv=input("Paste the ID of the conversation you want to delete a message in: ")
    Id_msg=input("Paste the ID of the message you want to delete: ")
    auth=input("Paste your token: ")
    url=f"https://discord.com/api/v9/channels/{Id_conv}/messages/{Id_msg}"
    headers = {'Authorization': auth,'Content-Type': 'application/json'}
    response = requests.delete(url, headers=headers)
    if response.status_code < 250:
        if response.status_code > 199:
            print(f"Message deleted successfully! Status code: {response.status_code}")
        else:
            print(f"Failed to delete message. Status code: {response.status_code}")
    else:
        print(f"Failed to delete message. Status code: {response.status_code}")
def encode_and_copy_id():
    # Configuration de l'interface console
    os.system("title DestroToolV3")
    os.system("cls")
    # Demande de l'ID utilisateur
    print("this tool was made by Destroy (https://www.youtube.com/@destroy4580)")
    user_id = input("Give user ID: ")
    try:
        # Vérification que l'ID est bien un nombre
        check = int(user_id)
        print(f'{Fore.WHITE} [{Fore.GREEN}+{Fore.WHITE}] ID valide.')

        # Encodage de l'ID en base64
        encoded_bytes = base64.b64encode(user_id.encode("utf-8"))
        encoded_str = encoded_bytes.decode("utf-8")

        # Affichage et copie du résultat dans le presse-papier
        print(f'{Fore.RED} [{Fore.WHITE}+{Fore.RED}] Encoded ID: {encoded_str}'+".")
        pyperclip.copy(encoded_str+".")
        print(f'{Fore.WHITE} [{Fore.GREEN}+{Fore.WHITE}] Text Copié dans le presse-papier !')

    except ValueError:
        print(f'{Fore.WHITE} [{Fore.RED}+{Fore.WHITE}] ID invalide')
def login_token():
    token = input("Paste your token : ")
    opts = Options()
    user_agent =  ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/39.0.2171.95 Safari/537.36')
    opts.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome()
    dialog_name = 'Open Rebox?'
    driver.switch_to.parent_frame()
    URL = "https://discord.com/login"
    driver.get(URL)
    driver.execute_script('''function login(token) {
    setInterval(() => {
        document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`;
    }, 50);
    setTimeout(() => {
        location.reload();
    }, 2500);
}login('''+f"'{token}'"+");")
    input("exit ?")
def infoa():
    print("They also helped me building Dishack : ")
    print("https://www.youtube.com/@destroy4580")
    print("https://github.com/Discord-Oxygen/Discord-Console-hacks")
    print("Obtain your Token : ")
    print('''window.webpackChunkdiscord_app.push([[Math.random()], {}, (req) => {for (const m of Object.keys(req.c).map((x) => req.c[x].exports).filter((x) => x)) {if (m.default && m.default.getToken !== undefined) {return copy(m.default.getToken())}if (m.getToken !== undefined) {return copy(m.getToken())}}}]); console.log("%cDone!", "font-size: 50px"); console.log(`%cYou now have your token in the clipboard!`, "font-size: 16px")''')
    print("Log in using a Token : ")
    print('''function login(e) {setInterval(() => {window.webpackChunkdiscord_app.push([[Math.random()], {}, (req) => {for (const m of Object.keys(req.c).map((x) => req.c[x].exports).filter((x) => x)) {if (m.default && m.default.setToken !== undefined) {return m.default.setToken(e)}if (m.setToken !== undefined) {return m.setToken(e)}}}]);console.log("%cWorked!", "font-size: 50px");}, 50), setTimeout(() => {window.location.reload()}, 2500)}function buttonlogin(){login(document.getElementsByClassName("inputDefault-3FGxgL input-2g-os5")[0].value)}var element;(element=document.getElementsByClassName("marginBottom8-emkd0_ button-1cRKG6 button-f2h6uQ lookFilled-yCfaCM colorBrand-I6CyqQ sizeLarge-3mScP9 fullWidth-fJIsjq grow-2sR_-F")[0]).addEventListener("click",buttonlogin),(element=document.getElementsByClassName("marginBottom20-315RVT")[0]).parentElement.removeChild(element),(element=document.getElementsByClassName("colorStandard-21JIj7 size14-3fJ-ot h5-2RwDNl title-3hptVQ defaultMarginh5-3Jxf6f")[0]).innerHTML="Token",element.id="Token",(element=document.getElementsByClassName("transitionGroup-bPT0qU qrLogin-1ejtpI")[0]).parentElement.removeChild(element),(element=document.getElementsByClassName("verticalSeparator-2r9gHa")[0]).parentElement.removeChild(element);''')
    print('Get Hidden Channel IDs : ')
    print('''window.webpackChunkdiscord_app.push([[Math.random()], {}, (req) => {for (const m of Object.keys(req.c).map((x) => req.c[x].exports).filter((x) => x)) {if (m.default && m.default.getPrivateChannelIds !== undefined) {return console.log(m.default.getPrivateChannelIds())}if (m.getPrivateChannelIds !== undefined) {return console.log(m.getPrivateChannelIds())}}}]);''')
    print('\n')
def ascii():
    print(" ____  _  ____  _     ____  ____  _  __ ")
    print("/  _ \\/ \\/ ___\\/ \\ /|/  _ \\/   _\\/ |/ / ")
    print("| | \\|| ||    \\| |_||| / \\||  /  |   /  ")
    print("| |_/|| |\\___ || | ||| |-|||  \\__|   \\  ")
    print("\\____/\\_/\\____/\\_/ \\|\\_/ \\|\\____/\\_|\\_\\ ")
    print("                            by abgache  ")
def main(token_b):
    print("\n")
    print("1- Send a message using the token")
    print("2- Get first part of the token using the ID")
    print("3- Get User pfp using the ID (BOT token)")
    print("4- Always typing in channel")
    print("5- Delete a message using the token")
    print("6- Delete a webhook (no token requested)")
    print("7- Connect to an account using the token")
    print("8- more infos")
    print("9- Exit")
    action = input("Choose an option: ")
    if action == "1":
        msg_token()
        main(tokb)
    elif action == "2":
        encode_and_copy_id()
        main(tokb)
    elif action == "3":
        idz = input("User ID : ") 
        get_pfp(token_b, idz)
        main(tokb)
    elif action == "4":
        channel_id = input("Give channel ID :")
        token = input("Give your token :")
        sec = input("For how long do you want to be shown as writing (in seconds) :")
        lwr(channel_id, token, sec)
        main(tokb)
    elif action == "5":
        del_token()
        main(tokb)
    elif action == "6":
        del_wh(input("Webhook URL : "))
        main(tokb)
    elif action == "7":
        login_token()
        main(tokb)
    elif action == "8":
        infoa()
        main(tokb)
    elif action == "9":
        exit()
    else:
        print("Invalid option. Please choose 1, 2, 3, 4, 5, 6 or 7.")
        main(tokb)
ascii()

msaz = input("Write down your name : ")
paz = input("Create a password : ")
print("If you don't have tokens, just leave it blank (risk of errors)")
tokk = input("Write a user token : ")
tokb = input("Write a bot token : ")
tokkk = f"Token (U) : {tokk}, Token (B) : {tokb}"
def loading_animation():
    symbols = ["|", "/", "-", "\\"]
    timea = 0.2
    while not stop_loading:
        for symbol in symbols:
            print(f"\r{symbol} Loading...", end="", flush=True)
            time.sleep(timea)
stop_loading = False
loading_thread = threading.Thread(target=loading_animation)
loading_thread.start()
# In dev
stop_loading = True
loading_thread.join()

main(tokb)
