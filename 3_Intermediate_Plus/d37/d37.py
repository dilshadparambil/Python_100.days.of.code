# Habit Tracking Project

import os
import requests
from datetime import date

# https://pixe.la/ scroll down to see how to use pixela
#A token string used to authenticate as a user to be created. The token string is hashed and saved.Validation rule: [ -~]{8,128} .i randomly clicked keyboard keys

# default values
PIXELA_TOKEN=os.getenv('PIXELA_TOKEN')
PIXELA_UNAME=os.getenv('PIXELA_UNAME')
FORMAT_DATE=date.today().strftime("%Y%m%d")

DATA={
    'token':PIXELA_TOKEN,
    'username':PIXELA_UNAME,
    'id': 'graph1',
    'name': 'Coding graph',
    'unit': 'hours',
    'type': 'int',
    'color': 'momiji',
    'quantity' : '7',
    'UPDATE_DATE':FORMAT_DATE,
    'DELETE_DATE':FORMAT_DATE
}

pixela_endpoint = 'https://pixe.la/v1/users'

Program_on=True
while Program_on:
    print("Welcome To Habit Tracker")
    option=input(
        "1.CREATE USER\n"
        "2.CREATE GRAPH\n"
        "3.TRACK HABIT FOR TODAY\n"
        "4.UPDATE HABIT DATA\n"
        "5.DELETE HABIT DATA\n"
        "6.Exit\n"
        "Enter an Option Number:")

    if option=='1':
        # CREATING USER
        # https://docs.pixe.la/entry/post-user documentation

        DATA['username']=input("enter user name: ")
        DATA['token']=input("enter user Token: ")
        user_params={
            'token':DATA['token'],
            'username':DATA['username'],
            'agreeTermsOfService':'yes',
            'notMinor':'yes',
        }
        response=requests.post(url=pixela_endpoint,json=user_params)
        print(response.text)
        print("\n")

    elif option == '2':
        # CREATING GRAPH
        # https://docs.pixe.la/entry/post-graph documentation
        headers = {
            'X-USER-TOKEN': DATA['token']
        }
        graph_endpoint = f'{pixela_endpoint}/{DATA['username']}/graphs'
        DATA['id']=input("enter The Graph id(start with letter): ")
        DATA['name']=input("enter The Graph Name: ")
        DATA['unit']=input("enter The Graph Unit: ")
        DATA['type']=input("enter The Graph Unit type(int/float): ")
        graph_config = {
            'id': DATA['id'],
            'name': DATA['name'],
            'unit': DATA['unit'],
            'type': DATA['type'],
            'color': DATA['color']#for red colour,
        }
        response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
        print(response.text)
        print("\n")

    elif option == '3':
        # CREATING PIXEL
        # https://docs.pixe.la/entry/post-pixel documentation
        post_pixel_endpoint = f'{pixela_endpoint}/{DATA['username']}/graphs/{DATA['id']}'
        DATA['quantity']=input("enter the pixel quantity: ")
        pixel_config = {
            'date': FORMAT_DATE,
            'quantity': DATA['quantity'],
        }
        headers = {
            'X-USER-TOKEN': DATA['token']
        }
        response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
        print(response.text)
        print("\n")

    elif option == '4':
        # UPDATING PIXEL
        # https://docs.pixe.la/entry/put-pixel documentation
        DATA['UPDATE_DATE']=input("Enter the date in 'yyyyMMdd' format: ")
        put_pixel_endpoint = f'{pixela_endpoint}/{DATA['username']}/graphs/{DATA['id']}/{DATA['UPDATE_DATE']}'
        DATA['quantity'] = input("enter the updated pixel quantity: ")
        update_config={
            'quantity': DATA['quantity'],
        }
        headers = {
            'X-USER-TOKEN': DATA['token']
        }
        response=requests.put(url=put_pixel_endpoint,json=update_config,headers=headers)
        print(response.text)
        print("\n")

    elif option == '5':
        # DELETING PIXEL
        # https://docs.pixe.la/entry/delete-pixel documentation
        DATA['DELETE_DATE'] = input("Enter the date in 'yyyyMMdd' format: ")
        headers = {
            'X-USER-TOKEN': DATA['token']
        }
        delete_pixel_endpoint = f'{pixela_endpoint}/{DATA['username']}/graphs/{DATA['id']}/{DATA['DELETE_DATE']}'
        response=requests.delete(url=delete_pixel_endpoint,headers=headers)
        print(response.text)
        print("\n")

    elif option == '6':
        print("Bye")
        Program_on = False
        print("\n")

    else:
        print("Enter a Valid Choice\n")
