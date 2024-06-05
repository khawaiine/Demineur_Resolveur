from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import re
from datetime import datetime
""""import pytesseract"""
image_10_path= 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb3///97e3uVBMaVAAAAHklEQVQI12MIDQ0NARFBDAEMDFzkEl6rVq1i0AISAIlSC03msuDYAAAAAElFTkSuQmCC'
image_0_path= 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAQMAAAAlPW0iAAAABlBMVEW9vb17e3tXxGy+AAAAEElEQVQI12P4/5+hgYF4BAAJYgl/JfpRmAAAAABJRU5ErkJggg=='
image_1_path= 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb0AAP97e3u7pKrVAAAAJUlEQVQI12NYBQQMDQxAACUCgAQjiGAFEaIQLiYhGgojEHqBGAB4Gw2cMF3q+AAAAABJRU5ErkJggg=='
image_2_path= 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb0AewB7e3vro336AAAANUlEQVQI12NYBQQMDQxAACFCQxkYGkNDHRgaA1gdgGJgIhQowRoCknUAygIZYCVgAqwNQQAA1rsQB7h1rwIAAAAASUVORK5CYII='
image_3_path = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb3/AAB7e3uBZQfoAAAAKUlEQVQI12NYBQQMDQxAACYaQ0PBhAOQywojWIFiIAIhBlICJiDaEAQAtlYPHU2zahQAAAAASUVORK5CYII='
image_4_path = 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb0AAHt7e3vZn4u5AAAAJklEQVQI12NYBQQMDQxAACFERWFECIxoDA11ABNAJUAuBsGARAAAgHoNeXfAhZYAAAAASUVORK5CYII='
image_5_path ="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb17AAB7e3sERFEmAAAAKUlEQVQI12NYBQQMDQxAACYaQ0MdoEQAiBsAEYNIAJWwQgi4Oog2BAEA7gEQV+EiCoQAAAAASUVORK5CYII="
image_6_path= 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAACVBMVEW9vb0Ae3t7e3tXnVpnAAAAKklEQVQI12NYBQQMDQxAACFCQxkYGsFEAAOMgIo5ALmsEALMBSmGaEMQAOO9EHd34ZsRAAAAAElFTkSuQmCC'
image_flag_path = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAD1BMVEW9vb3///97e3sAAAD/AABQHuKJAAAAOklEQVQI12MQhAABGIOJQZABDJRADBYHCIPFBcpwcUGIIKsB6zJAZxgbQxjGQIDEQFghoAQBDExQBgCHngoRLPdU8QAAAABJRU5ErkJggg=="
image_interrogation_path= 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQAgMAAABinRfyAAAADFBMVEW9vb3///97e3sAAACeVBdNAAAAMklEQVQI12MIDQ0NARFBDAEMDFwMAfwfgISNDYxgABMgMeYDEAKkDoPrtWrVKgYtIAEAf3YRdAzsd6QAAAAASUVORK5CYII='

#ouvrir la page chrome 
driver = webdriver.Chrome()
driver.get('https://xn--dmineur-bya.eu/')
clicked_tiles = set()

#fonction principale
def start(niveau):
    global driver
    global clicked_tiles
    clicked_tiles = set()
    clics=niveau-1 
    tile_difficulte = driver.find_element(By.ID,"difficulty")
    time.sleep(1)
    for i in range (clics):
        actions = ActionChains(driver)
        actions.move_to_element(tile_difficulte)
        actions.click()
        actions.perform()
    tile_0 = driver.find_element(By.ID,'tile0')
    board = driver.find_element(By.ID,'board')
    tile_style= tile_0.get_attribute('style')
    board_style = board.get_attribute('style')
    l_tile= re.search(r'width:\s*(\d+)px', tile_style)
    l_tile= int(l_tile.group(1))
    h_tile=l_tile
    l_board= re.search(r'width:\s*(\d+)px', board_style)
    h_board= re.search(r'height:\s*(\d+)px', board_style)
    l_board= int(l_board.group(1))
    h_board= int(h_board.group(1))
    #Calculer le nombre de tuiles en longueur et en hauteur 
    L=int(l_board/l_tile) #Nombre de tuiles dans la longueur 
    H=int(h_board/h_tile) #Nombre de tuiles dans la largeur
    print (L,H)
    
    #Générer le premeir clic au centre    
    time.sleep(0.5)
    element1 = driver.find_element(By.ID,"tleft")
    nombreDeCases = element1.text
    element2 = driver.find_element(By.ID,"mleft")
    nombreDeMines= element2.text
    actions = ActionChains(driver)
    element = driver.find_element(By.ID, "board")
    actions.move_to_element(element).click().perform()
    
    #Initialiser le tableau
    tab = [[i for i in range(L)] for j in range (H)]
    t=datetime.strptime('18:00', "%M:%S").time()
    
    #Boucle principale
    while True:
        while int(nombreDeCases) > 0 or int(nombreDeMines) > 0:  # vérification du cas simple où le nombre de mines voisines est égal aux cases 'unrevealed' + cases flag
            nombreDeCases,nombreDeMines = majnombres()
            tab=M1(tab,L,H)
            temps=driver.find_element(By.ID,'time')
            temps=temps.text
            temps = datetime.strptime(temps.strip(), "%M:%S").time()
            if temps < t:
                t=temps
                driver.get_screenshot_as_file('Niveau_1.png')
        face=driver.find_element(By.ID,'face')
        face.click()
        time.sleep(0.5)
        board=driver.find_element(By.ID,'board')
        board.click()
        nombreDeCases , nombreDeMines = majnombres()

#mettre à jour le tableau         
def majtab(L,H,tab):
    global driver 
    global clicked_tiles
    for i in range(H):
        for j in range(L):
            x = L*i + j
            if x in clicked_tiles:
                continue
            else:
                element_conteneur = driver.find_element(By.ID,"tile"+ str(x))
                image_url = element_conteneur.get_attribute('src')
                if image_url == image_10_path:
                    tab[i][j] = 'unrevealed'
                elif image_url == image_0_path:
                    tab[i][j] = 0
                    clicked_tiles.add(x)
                elif image_url == image_1_path:
                    tab[i][j] = 1
                    clicked_tiles.add(x)
                elif image_url == image_2_path:
                    tab[i][j] = 2
                    clicked_tiles.add(x)
                elif image_url == image_3_path:
                    tab[i][j] = 3
                    clicked_tiles.add(x)
                elif image_url == image_4_path:
                    tab[i][j] = 4
                    clicked_tiles.add(x)
                elif image_url == image_5_path:
                    tab[i][j] = 5
                    clicked_tiles.add(x)
                elif image_url == image_6_path:
                    tab[i][j] = 6
                    clicked_tiles.add(x)
                elif image_url == image_interrogation_path:
                    tab[i][j] = 'interrogation'
    return(tab)

#mettre à jour les valeurs d'arrêt du jeu
def majnombres():
    global driver
    element1 = driver.find_element(By.ID, "tleft")
    nombreDeCases = element1.text  # Rafraîchissez la valeur
    element2 = driver.find_element(By.ID, "mleft")
    nombreDeMines = element2.text# Rafraîchissez la valeur
    return (nombreDeCases,nombreDeMines)

def M1(tab, L, H):
    change = False
    global clicked_tiles
    tab=majtab(L,H,tab)
    for i in range(H):
        for j in range (L):
            x = 0
            y = 0
            X = []
            if isinstance(tab[i][j], int) and tab[i][j]>0: 
                if i-1>=0 and j-1 >=0 and tab[i-1][j-1]=='unrevealed':
                    x+=1
                    X.append([i-1,j-1])
                elif i-1>=0 and j-1 >=0 and tab[i-1][j-1]=='flag':
                     x+=1
                     y+=1
                if i-1 >=0 and tab[i-1][j]== 'unrevealed':
                    x+=1
                    X.append([i-1,j])
                elif i-1 >=0 and tab[i-1][j]== 'flag':
                    x+=1
                    y+=1
                if i-1>= 0 and j+1<L and tab[i-1][j+1]== 'unrevealed':
                    x+=1
                    X.append([i-1,j+1])
                elif i-1>= 0 and j+1<L and tab[i-1][j+1]== 'flag':
                    x+=1
                    y+=1
                if j-1>=0 and tab[i][j-1]=='unrevealed':
                    x+=1
                    X.append([i,j-1])
                elif j-1>=0 and tab[i][j-1]=='flag':
                    x+=1
                    y+=1
                if j+1<L and tab[i][j+1]=='unrevealed':
                    x+=1
                    X.append([i,j+1])
                elif j+1<L and tab[i][j+1]=='flag':
                    x+=1
                    y+=1
                if i+1<H and j+1<L and tab[i+1][j+1]=='unrevealed':
                    x+=1
                    X.append([i+1,j+1])
                elif i+1<H and j+1<L and tab[i+1][j+1]=='flag':
                    x+=1
                    y+=1
                if i+1<H and tab[i+1][j]=='unrevealed':
                    x+=1
                    X.append([i+1,j])
                elif i+1<H and tab[i+1][j]=='flag':
                    x+=1
                    y+=1
                if i+1<H and j-1>=0 and tab[i+1][j-1]=='unrevealed':
                    x+=1
                    X.append([i+1,j-1])
                elif i+1<H and j-1>=0 and tab[i+1][j-1]=='flag':
                    x+=1
                    y+=1
                if x == tab[i][j] and tab[i][j]!=0:
                    for k in range(len(X)):
                        l = L * X[k][0] + X[k][1]
                        if l not in clicked_tiles:
                            actions = ActionChains(driver)
                            element = driver.find_element(By.ID, "tile" + str(l))
                            actions.move_to_element(element).context_click().perform()
                            tab[X[k][0]][X[k][1]] = 'flag'
                            change = True

                        
                elif y == tab[i][j] and tab[i][j]!=0:
                    for k in range (len(X)):
                        l = L * X[k][0] + X[k][1]
                        if l not in clicked_tiles:
                            actions = ActionChains(driver)
                            element = driver.find_element(By.ID, "tile" + str(l))
                            actions.move_to_element(element).click().perform()
                            change = True
                            
    if change == False:
        #Chercher aléatoirement une tuile 1 qui a au moins un voisin "unrevealed  et cliqer gauche sur ce voisin
        for s in range (H):
            for m in range (L):
                if tab[s][m] == 1 :
                    if (s+1)<H and tab[s+1][m]=='unrevealed':
                        l = L*(s+1)+m 
                        actions = ActionChains(driver)
                        element = driver.find_element(By.ID, "tile" + str(l))
                        actions.move_to_element(element).click().perform()
                        return tab
                    if (s+1)<H and (m-1)>=0 and tab[s+1][m-1]=='unrevealed':
                        l = L*(s+1)+m-1 
                        actions = ActionChains(driver)
                        element = driver.find_element(By.ID, "tile" + str(l))
                        actions.move_to_element(element).click().perform()
                        return tab
                    if (s+1)<H and (m+1)<L and tab[s+1][m+1]=='unrevealed':
                        l = L*(s+1)+m+1
                        actions = ActionChains(driver)
                        element = driver.find_element(By.ID, "tile" + str(l))
                        actions.move_to_element(element).click().perform()
                        return tab
                    if (m-1)>=0 and tab[s][m-1]=='unrevealed':
                        l = L*(s)+m-1
                        actions = ActionChains(driver)
                        element = driver.find_element(By.ID, "tile" + str(l))
                        actions.move_to_element(element).click().perform()
                        return tab
                    if tab[s][m]=='unrevealed':
                        l = L*(s)+m 
                        actions = ActionChains(driver)
                        element = driver.find_element(By.ID, "tile" + str(l))
                        actions.move_to_element(element).click().perform()
                        return tab
                    if (m+1)<L and tab[s][m+1]=='unrevealed':
                        l = L*(s)+m+1
                        actions = ActionChains(driver)
                        element = driver.find_element(By.ID, "tile" + str(l))
                        actions.move_to_element(element).click().perform()
                        return tab
                    if (s-1)>=0 and (m-1)>=0 and tab[s-1][m-1]=='unrevealed':
                        l = L*(s-1)+m-1
                        actions = ActionChains(driver)
                        element = driver.find_element(By.ID, "tile" + str(l))
                        actions.move_to_element(element).click().perform()
                        return tab
                    if (s-1)>=0 and tab[s-1][m]=='unrevealed':
                        l = L*(s-1)+m 
                        actions = ActionChains(driver)
                        element = driver.find_element(By.ID, "tile" + str(l))
                        actions.move_to_element(element).click().perform()
                        return tab
                    if (s-1)>=0 and (m+1)<L and tab[s-1][m+1]=='unrevealed':
                        l = L*(s-1)+m+1
                        actions = ActionChains(driver)
                        element = driver.find_element(By.ID, "tile" + str(l))
                        actions.move_to_element(element).click().perform()
                        return tab
    return (tab)

start(2)
