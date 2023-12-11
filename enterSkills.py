import os
import pyautogui as pg
import time


def enterSkills(filePath):
    with open(filePath, 'r') as file:
        lines = file.readlines()

        for line in lines:
            pg.typewrite(line)

    file.close()
    return


def main():
    time.sleep(5)
    #enterSkills("C:\\Users\\diepw\\Documents\\2023_Fall\\SE185\\finalProject\\songsInfo.txt")

    skills = "AGILE, AWS, CI/CD, DevOps, Python, PySpark, SQL, Palantir, SAP, Databricks, Java, C, C#, Software Development, Project Management, Data Management, Process Automation, Data Migration"
    skills = skills.split(", ")
    for skill in skills:
        pg.typewrite(skill)
        pg.press("enter")
        time.sleep(0.3)
    # print(pg.KEYBOARD_KEYS)

if __name__ == '__main__':
    main()

