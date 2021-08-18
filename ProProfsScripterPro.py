from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from colorama import Fore
from colorama import init
init()
from fpdf import FPDF
import csv
import time
import pathlib
import textwrap


#Chrome Going Silent
options = Options()
options.headless = False
options.add_argument('--window-size=1920,1080')  
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--log-level=OFF")
#Options=Options to load options from above options=options


isActivated = False

signature1 = "        ___           ___           ___      ___  ___  ____    ___       __      "
signature2 = "       / _ \_______  / _ \_______  / _/__   / _ \/ _ \/ __ \  / _ )___  / /_     "
signature3 = "      / ___/ __/ _ \/ ___/ __/ _ \/ _(_-<  / ___/ , _/ /_/ / / _  / _ \/ __/     "
signature4 = "     /_/  /_/  \___/_/  /_/  \___/_//___/ /_/  /_/|_|\____/ /____/\___/\__/      "

print(Fore.BLUE + signature1)
print(Fore.BLUE + signature2)
print(Fore.BLUE + signature3)
print(Fore.BLUE + signature4)
print(Fore.GREEN + '--------------------------------Version: 2021------------------------------------')
print(Fore.RED + "                                                     CREATED BY: PAVLE KUZMANOVIC")
print("\n\n\n")
print(Fore.WHITE + "Paste your ProProfs link here:")
proProfsUrl = input()
while ('proprofs.com/quiz-school/story.php?title=' not in proProfsUrl):
    print(Fore.RED + "Incorrect link, please paste a link from a ProProfs Quiz start screen:" + Fore.WHITE)
    proProfsUrl=input()

try:
    print(Fore.GREEN + "Link OK!")
    fileToSave = str(proProfsUrl.replace('https://www.proprofs.com/quiz-school/story.php?title=','') + ".txt")
    open(fileToSave, 'w').close()
    print(Fore.GREEN + "Permissions OK!")
    browserChrome = webdriver.Chrome(str(pathlib.Path().absolute()) + '\c_engine.exe', options=options)
    browserChrome.get(proProfsUrl)
    
except PermissionError: 
    for i in range(50):
        print(Fore.RED + "I do not have permissions to save my work here. Run me in Administrator mode.")
    time.sleep(5)
    exit()


#Getting Number Of Questions
numberOfQuestionsGet = browserChrome.find_element_by_class_name('number_ques').text
numberOfQuestions = []

for number in numberOfQuestionsGet:
    if number != " ":
        numberOfQuestions.append(number)
    else:
        numberOfQuestions = int("".join(map(str, numberOfQuestions)))
        print(Fore.WHITE + "\n\nI have found " + Fore.BLUE + str(numberOfQuestions) + Fore.WHITE + " question entries.")
        break

#Entering Quiz
print("\n\n\n\n                             ▀▄▀▄▀▄ LAUNCHING ▄▀▄▀▄▀ \n\n\n\n")
browserChrome.find_element_by_name('mySubmit').click()
print(Fore.YELLOW + 'Starting process...')
time.sleep(2)

#Remove Ads -----------

all_iframes = browserChrome.find_elements_by_tag_name("iframe")
if len(all_iframes) > 0:
    browserChrome.execute_script("""
        var elems = document.getElementsByTagName("iframe"); 
        for(var i = 0, max = elems.length; i < max; i++)
             {
                 elems[i].hidden=true;
             }
                          """)

try:
    advertisement = browserChrome.find_element_by_class_name('mobile_sticky_last')
    browserChrome.execute_script("""var advertisement = arguments[0];advertisement.parentNode.removeChild(advertisement);""", advertisement)
except:
    pass

try:
    advertisement = browserChrome.find_element_by_class_name('new_add_wrapper_all')
    browserChrome.execute_script("""var advertisement = arguments[0];advertisement.parentNode.removeChild(advertisement);""", advertisement)
except:
    pass

#Remove Ads ----------

#Clicking Jump To End Button
browserChrome.find_element_by_class_name('side_bar_view').click()
time.sleep(1)

#Finding Last Question
listOfAllQuestions = browserChrome.find_elements_by_class_name('jump_btn')
listOfAllQuestions[numberOfQuestions - 1].click()
time.sleep(2)
print(Fore.GREEN + 'Navigation SUCCESS!')



#Finishing Test

#Remove Ads -----------

all_iframes = browserChrome.find_elements_by_tag_name("iframe")
if len(all_iframes) > 0:
    browserChrome.execute_script("""
        var elems = document.getElementsByTagName("iframe"); 
        for(var i = 0, max = elems.length; i < max; i++)
             {
                 elems[i].hidden=true;
             }
                          """)

try:
    advertisement = browserChrome.find_element_by_class_name('mobile_sticky_last')
    browserChrome.execute_script("""var advertisement = arguments[0];advertisement.parentNode.removeChild(advertisement);""", advertisement)
except:
    pass

try:
    advertisement = browserChrome.find_element_by_class_name('new_add_wrapper_all')
    browserChrome.execute_script("""var advertisement = arguments[0];advertisement.parentNode.removeChild(advertisement);""", advertisement)
except:
    pass

#Remove Ads ----------
try:
    browserChrome.find_element_by_class_name('new_bottom_next_btn').click()
    time.sleep(2)
    browserChrome.find_element_by_class_name('next_from_practice').click()
    time.sleep(2)
except:
    try:
        browserChrome.find_element_by_class_name('iradio_square-grey').click()
        isActivated = True
        print(Fore.YELLOW + "IMPOSTERS" + Fore.GREEN + " FOUND!")
    except:
        try:
            browserChrome.find_element_by_class_name('icheckbox_square-grey').click()
            isActivated = True
            print(Fore.YELLOW + "IMPOSTERS" + Fore.GREEN + " FOUND!")
        except:
            browserChrome.find_element_by_class_name('new_bottom_next_btn').click()
            time.sleep(2)
            browserChrome.find_element_by_class_name('next_from_practice').click()
            time.sleep(2)
    
    time.sleep(2)

    browserChrome.find_element_by_class_name('new_bottom_next_btn').click()
    time.sleep(2)
    browserChrome.find_element_by_class_name('next_from_practice').click()
    time.sleep(2)

#Remove Ads -----------

all_iframes = browserChrome.find_elements_by_tag_name("iframe")
if len(all_iframes) > 0:
    browserChrome.execute_script("""
        var elems = document.getElementsByTagName("iframe"); 
        for(var i = 0, max = elems.length; i < max; i++)
             {
                 elems[i].hidden=true;
             }
                          """)

try:
    advertisement = browserChrome.find_element_by_class_name('mobile_sticky_last')
    browserChrome.execute_script("""var advertisement = arguments[0];advertisement.parentNode.removeChild(advertisement);""", advertisement)
except:
    pass

try:
    advertisement = browserChrome.find_element_by_class_name('new_add_wrapper_all')
    browserChrome.execute_script("""var advertisement = arguments[0];advertisement.parentNode.removeChild(advertisement);""", advertisement)
except:
    pass

#Remove Ads ----------


#Opening All Answers
try:
    if isActivated == True:
        browserChrome.execute_script(""" document.getElementById('incorrect_ansdiv').remove();document.getElementById('correcrt_ansdiv').remove(); """)
        #browserChrome.execute_script("""document.getElementsByClassName('incorrectdiv')[0].remove(); document.getElementsByClassName('correctdiv')[0].remove(); """) #OVDE JE STOJAO question_text umesto incorrect div.
        print(Fore.YELLOW + "IMPOSTERS" + Fore.RED + " REMOVED!")
    
except:
    pass

#Remove Ads -----------

all_iframes = browserChrome.find_elements_by_tag_name("iframe")
if len(all_iframes) > 0:
    browserChrome.execute_script("""
        var elems = document.getElementsByTagName("iframe"); 
        for(var i = 0, max = elems.length; i < max; i++)
             {
                 elems[i].hidden=true;
             }
                          """)

try:
    advertisement = browserChrome.find_element_by_class_name('mobile_sticky_last')
    browserChrome.execute_script("""var advertisement = arguments[0];advertisement.parentNode.removeChild(advertisement);""", advertisement)
except:
    pass

try:
    advertisement = browserChrome.find_element_by_class_name('new_add_wrapper_all')
    browserChrome.execute_script("""var advertisement = arguments[0];advertisement.parentNode.removeChild(advertisement);""", advertisement)
except:
    pass


#Remove Ads ----------
    
time.sleep(2)
browserChrome.find_element_by_class_name('alldiv').click()
print(Fore.YELLOW + 'Forcing complete lists...')
time.sleep(2)

#Adding Text (missed) To Single Correct Answers to identify them in text parser.
browserChrome.execute_script(""" var classes = document.getElementsByClassName("icon_correct_answer");for (var i = 0; i < classes.length; i++) { classes[i].innerHTML = "(missed)"; } """)
browserChrome.execute_script(""" var classes = document.getElementsByClassName("labelNormal");for (var i = 0; i < classes.length; i++) { classes[i].innerHTML += " (answer)"; } """)
time.sleep(2)

for i in range(100):
    browserChrome.execute_script(""" var classesTwo = document.getElementsByTagName('br');for (var i = 0; i < classesTwo.length; i++) {  classesTwo[i].remove();  } """)
    time.sleep(0.01)
    print(Fore.MAGENTA + "Loading failsafe: " + Fore.WHITE + str(i + 1) + "%")
print(Fore.RED + "ARMED! ")

browserChrome.execute_script("""document.getElementById('question_detailed').setAttribute('style', 'width: 10000%'); """)

print(Fore.YELLOW +'Formatting for reading... ')




#Grabbing Questions
fullQuestionList = browserChrome.find_elements_by_class_name('question_text')
fullQuestionListFiltered = []

for question in fullQuestionList:
    fullQuestionListFiltered.append(question.text + "\n")
print(Fore.GREEN + 'Questions grabbed!')

#Grabbing Answers
fullAnswersList = browserChrome.find_element_by_id('question_detailed').text
print(Fore.GREEN +'Answers grabbed!')

#Saving Temporary File For Fixing it after
savingTemp = open('tmp', 'w', encoding="utf-8")
savingTemp.write(fullAnswersList)
savingTemp.close()

print(Fore.YELLOW +"Creating plain text file...")
#Grabbing Good Stuff From Temp File
finalList = []
questionID = 0
openSavingTemp = open("tmp", "r")

for line in openSavingTemp.readlines():  
    line = line.lstrip()  
    if ('(missed)' in line):
        try:
            cutLine = line.split('.', 1)
            fixedLine = str(cutLine[1]).replace(" ", "-", 1).replace('(missed)', '').replace('(answer)',"")
            finalList.append(fixedLine)
        except: 
            pass
        

    elif ((line[0].isdigit()) and ("got this correct" not in line) and ("(answer)" not in line)):
        try:
            finalList.append("\n" + str(questionID + 1) + ". " + fullQuestionListFiltered[questionID])
        except:
            pass
        questionID += 1

print(Fore.YELLOW + "Saving... ")

#Saving Final Script
for entry in finalList:
    savingScript = open(fileToSave, 'a', encoding="utf-8")
    savingScript.write(entry)
    savingScript.close()
print(Fore.GREEN + "Saving complete!")

print(Fore.YELLOW + "Assembling .pdf ...")
#PDF

pdf = FPDF()
pdf.add_font('Questions', '',str(pathlib.Path().absolute()) + "\\core\\NotoSans-Regular.ttf", uni=True)
pdf.add_font('Answers', '',str(pathlib.Path().absolute()) + "\\core\\NotoSans-Light.ttf", uni=True)

pdf.add_page()

for line in finalList:

    line = line.replace("\n","")

    if line[0].isdigit() == True:
        pdf.set_font("Questions", size = 11)
        pdf.set_text_color(0,0,0)
    else:
        pdf.set_font("Answers", size = 10)
        pdf.set_text_color(0, 204, 0)

    if len(line) > 97:
        linesToCreate = int(len(line) / 97)
        print(Fore.YELLOW + "SNIPPING: " + Fore.WHITE + str(len(line)) + "/" + str(linesToCreate))
        splittedLine = textwrap.wrap(line, 97)
        for lines in range(linesToCreate + 1):
            try:
                pdf.cell(100, 5, txt = splittedLine[lines], ln = 1, align = 'L') 
            except IndexError:
                print(Fore.RED + "False Positive!")
    else:
        pdf.cell(100, 5, txt = line, ln = 1, align = 'L')
    pdf.cell(100, 5, txt = " ", ln = 1, align = 'L')

pdfOutputName = "SCRIPT_" + fileToSave.replace(".txt", ".pdf")
pdf.output(pdfOutputName)
print(Fore.GREEN + "PDF Assembly Success!")

print(Fore.YELLOW +'Cleaning up... ')
savingTemp = open('tmp', 'w')
savingTemp.write("")
savingTemp.close()

print(Fore.BLUE + 'DONE! ')
print(Fore.WHITE + "\n\n\n" + """ "`-._,-'"`-._,-'"`-._,-'"`-._,-' ___/< FILE INFO >\___ '-._,-'"`-._,-'"`-._,-'"`-._,-`" """)
print(Fore.WHITE + "----------------------------------------------------------------------------------------- ")
print("\n\n")
print(Fore.GREEN + "Plain Text File Name: . . . . . . . . . . . . . . . . . . . . . . . . . " + Fore.YELLOW + fileToSave + " ")
print(Fore.GREEN + "PDF Script File Name: . . . . . . . . . . . . . . . . . . . . . . . . . " + Fore.YELLOW + pdfOutputName + " ")
print(Fore.GREEN + "File Directory: . . . . . . " + Fore.YELLOW + str(pathlib.Path().absolute()) + " ")
print(Fore.GREEN + "Total Questions Printed: . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . " + Fore.YELLOW + str(len(fullQuestionListFiltered)) + " ")
print(Fore.WHITE + "\n\n\n                           [X]   [Safe to close]   [X]                             ")
print(Fore.WHITE + "----------------------------------------------------------------------------------------- ")
print(Fore.RED + "                    ProProfs Pro Bot - Pavle Kuzmanovic 2021                      ")








