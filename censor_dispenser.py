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

#Properietary Terms
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

#Negative Words - Censor from email three
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]


#Update a list of terms to include checks for case sensitivity and plurals
def update_terms(terms, terms2 = []):
    new_terms = []
    for term in terms:
        new_terms.append(term)
        new_terms.append(term.upper())
        new_terms.append(term.title())
        new_terms.append(term.lower())
    for term in terms2:
        new_terms.append(term)
        new_terms.append(term.upper())
        new_terms.append(term.title())
        new_terms.append(term.lower())
    new_terms.append("*****s")
    return new_terms

#Censor the words before and after a term
def censor_neighbors(cond = False, email = ""):
    email_splt = []
    email_rmv_enter = []
    email_clean = []
    if cond == True:
        email_splt.append(email.split(" "))
        for email in email_splt:
            for word in email:
                email_rmv_enter.append(word.replace("\n", " "))
        for word in email_rmv_enter:
            email_clean.append(word.split("  "))
    print (email_rmv_enter)
    print (email_clean)

censor_neighbors(True, email_four)

#print (email_two)

#Censor a list of terms or multiple lists of terms
def censor_terms(email, terms, terms2 = [], neighbors = False):
    updated_terms = update_terms(terms, terms2)
    itr = 0
    email_lst = [email]
    print (updated_terms)
    for term in range(len(updated_terms)):
        temp_email = email_lst[itr]
        email_lst.append(temp_email.replace(updated_terms[term], "*****"))
        itr += 1
    censor_neighbors(True, email[itr])
    return email_lst[itr]

#print (censor_terms(email_two, proprietary_terms))

#print (email_three)

#Censor proprietary terms and negative words from email three
#print (censor_terms(email_three, proprietary_terms, negative_words))

print (email_four)

print (censor_terms(email_four, proprietary_terms, negative_words, True))