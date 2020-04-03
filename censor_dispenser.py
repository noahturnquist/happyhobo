# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:

#Censor "learning algorithms"
email_one = open("email_one.txt", "r").read()

#Censor Proprietary Terms
email_two = open("email_two.txt", "r").read()

email_three = open("email_three.txt", "r").read()

email_four = open("email_four.txt", "r").read()

#Censor single word or phrase
def censor_phrase(email, phrase):
    censored_email = email.replace(phrase, "*****")
    return censored_email

#print (censor_phrase(email_one, "learning algorithms"))

#Censor these terms from Email Two
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

print (email_two)

#Censor a LIST of words or phrases
def censor_terms(email, terms):
    email_lst = []
    email_lst.append(email.split())
    for email in email_lst:
        email_temp = []
        for words in email:
            email_temp.append(words)
        for word in range(len(email_temp)):
            print (email_temp[word])
            for term in range(len(terms)):
                if email_temp[word] == terms[term]:
                    print ("*****")
        print ("B", email_temp)     
    return email_lst

print (censor_terms(email_two, proprietary_terms))