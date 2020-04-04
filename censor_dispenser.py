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

#Properietary Terms
#Censor these terms from Email Two
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

#Update a list of terms to include checks for case sensitivity and plurals
def update_terms(terms):
    new_terms = []
    for term in terms:
        new_terms.append(term)
        new_terms.append(term.upper())
        new_terms.append(term.title())
        new_terms.append(term.lower())
    new_terms.append("*****s")
    return new_terms

print (email_two)

#Censor a list of terms
def censor_terms2(email, terms):
    updated_terms = update_terms(terms)
    #print (updated_terms)
    itr = 0
    email_lst = [email]
    for term in range(len(updated_terms)):
        temp_email = email_lst[itr]
        email_lst.append(temp_email.replace(updated_terms[term], "*****"))
        #print (temp_email, itr)
        #email_lst.append(email.replace(terms[term], "*****"))
        itr += 1
    return email_lst[itr]

print (censor_terms2(email_two, proprietary_terms))