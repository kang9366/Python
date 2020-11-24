import pyautogui as pag

apply_tab = pag.locateOnScreen('apply_tap.png')
center = pag.center(apply_tab)
pag.click(center)