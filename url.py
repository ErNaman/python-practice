import re 
def Find(string): 
	url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] |[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string) 
	return url 	
string = 'My Profile: https://auth.geeksforgeeks.org / user / Chinmoy % 20Lenka / articles inthe portal of http://www.geeksforgeeks.org/' 
print("Urls: ", Find(string)) 
