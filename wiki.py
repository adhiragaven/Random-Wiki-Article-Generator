import wikipedia,webbrowser

def getPage():
    wikipage=wikipedia.random(1)

    wikiload=wikipedia.page(wikipage)

    userchoice=input("Would you like to read about {} (Y/N)".format(wikipage)).lower().strip()

    if(userchoice=="y" or userchoice=="yes"):
        print("\nSummary:\n-------\n")
        print(wikiload.summary)
        wikiopen=input("\n Open WIKI page in browser? (Y/N)").lower().strip()
        if(wikiopen=="yes" or wikiopen=="y"):
            webbrowser.open(wikiload.url,new=2)
        else:
            getPage()
        exit(0)
    elif(userchoice=="q" or userchoice=="quit"):
        exit(0)
    else:
        getPage()


if __name__=="__main__":
    getPage()