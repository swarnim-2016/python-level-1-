movies =[]
def addmovie():
    moviename = input("enter a movie")
    movies.append (moviename)
    if moviename in movies:
        print("you have that movie" )

def removemovie():
    themoiivyouwanttoremove=input("enter the movie you want to remove")
    movies.remove(themoiivyouwanttoremove)
def serch():
    themovie=input("enter the movie that you want to know if you have")
    if themovie in movies:
        print("you have this ")
    else :
        print("you do not have the movie")    
def display():
    for i in range(len(movies)):
        print(movies[i])
def count():
    len(list)
def clearmovies():
    list.clear()
    print("the list is clear")
while True:
    print(""" you can do
    1.add movie
    2.remove movie
    3.serch
    4 display all movies
    5 display the number of movies
    6 clear all
    7 exit
    """)
    choice = int(input("enter a number that you want to use"))
    if choice==1:
        addmovie()
    elif choice==2:
        removemovie()
    elif choice==3:
        serch()
    elif choice==4:
        display()
    elif choice==5:
        count()
    elif choice==6:
        clearmovies()
    elif choice==7:
        print("thank you")
        break

                

                   
