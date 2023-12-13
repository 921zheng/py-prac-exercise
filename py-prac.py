# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"


def domain_name(url):
    seperated=url.split(".")
    if "http" in seperated[0]:
        if "www" in seperated[0]:
            return seperated[1]
        else:
            return seperated[0].split("//")[1]
    elif "http" not in seperated[0]:
        if seperated[0]=="www":
            return seperated[1]
        else:
            return seperated[0]
            
# The marketing team is spending way too much time typing in hashtags.
# Let's help them with our own Hashtag Generator!

# Here's the deal:

# It must start with a hashtag (#).
# All words must have their first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.
# Examples
# " Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  =>  "#HelloWorld"
# ""                                        =>  false


def generate_hashtag(s):
    seperated=s.split(" ")
    if s=="":
        return False
    
    else:
        
        if len("#" +s.title().replace(" ",""))<=140:
            return "#" +s.title().replace(" ","")
        else: 
            return False
            
            
# Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw" 
# spinWords( "This is a test") => returns "This is a test" 
# spinWords( "This is another test" )=> returns "This is rehtona test"


def spin_words(s):
    seperated=s.split(" ")
    result=""
    for a in seperated:
        if len(a)>=5:
            result+=a[::-1]+" "
            
        else:
            result+=a+" "
    return result[:-1]



















