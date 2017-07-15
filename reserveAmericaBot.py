import webbrowser

arvdate = input("Please Input Arrival Date: MM/DD/YY: ")
lenOfStay = input("Please Input Length of Stay: ")
url = "https://www.reserveamerica.com/campsiteDetails.do?siteId=246277&contractCode=NY&parkId=175&arvdate="+ arvdate +"&lengthOfStay=" + lenOfStay
webbrowser.open(url)
