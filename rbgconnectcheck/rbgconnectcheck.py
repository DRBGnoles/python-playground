#Check status of a site from a given URL
import urllib.request as urllib

def main(url):
    print("Checking status of " + url + "...")

    response = urllib.urlopen(url)
    print("Connected to", url, "successfully!")
    print("The response code was:", response.getcode())

print("This is a site connectivity checker.")
input_url = input("Input the URL of the site you want to check: ")

main(input_url)
