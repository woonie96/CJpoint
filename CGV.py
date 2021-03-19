from bs4 import BeautifulSoup
import requests
import urllib.request
import re


def cinema_list(link):

    html = urllib.request.urlopen(link)

    source = html.read()
    soup = BeautifulSoup(source, "html.parser")
    theaters = soup.find(class_="tab_con_wrap").find_all("span")
    #print(theaters)

    index = 0
    for element in theaters:
        theater = re.sub('<.+?>', '', str(element), 0).strip()
        print(theater+" is number "+str(index))
        index+=1
    flag = 1
    while(flag):
        return_list = [x for x in input("Enter the number of cinema that you want: ").split()]

        for element in return_list:
            if not element.isdigit():
                print(element+" is character")
                flag = 1
                break
            elif not int(element) < 28 and int(element) > 0:
                print(element+" is out of range")
                flag = 1
                break
            else:
                flag = 0





    return return_list




def time_list(link,list):

    html = urllib.request.urlopen(link)
    source = html.read()
    soup = BeautifulSoup(source, "html.parser")
    cities = soup.find(class_="tab_con_wrap").find_all('a')
    cities[0]['class'] = ''

    for element in list:
        cities[int(element)]['class'] = 'on'


    city = soup.find(class_="tab_con_wrap").find_all(class_="on")
    prefix = "http://section.cgv.co.kr/"
    #print(cities)
    #print(prefix+city[1].get('href'))
    #print(cities)
    print(" ")
    print(" ")
    for cgv in city:
        #print("You are at: "+str(cgv.text)+" Link is "+prefix+cgv.get('href'))
        link = prefix+cgv.get('href')
        html = urllib.request.urlopen(link)

        source = html.read()
        soup = BeautifulSoup(source, "html.parser")
        theater = soup.find(class_="movie_time_table").find('tbody').find_all('tr')
        print("You are at :" + str(cgv.text))
        for cinema in theater:
            movies = cinema.find(class_="txt").get('title')
            theater = cinema.find(id=re.compile('tdScreen$'))
            times = cinema.find(class_="time").find_all(id=re.compile('spSchedule$'))

            if movies:

                print("Movie name: "+movies+" Theater: "+theater.get_text())
                for time in times:
                    print("Times: "+time.text+" Rest: "+time.find('span').get('title'))

            print(" ")
        print("--------------------------End of "+str(cgv.text)+"--------------------------")


if __name__ == "__main__":
    cgv_link = "http://section.cgv.co.kr/theater/popup/r_TimeTable.aspx?code="
    number = cinema_list(cgv_link)
    #print(number)
    time_list(cgv_link,number)