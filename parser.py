stopwords = ["and", "the","with","from","that", "this", "have", "for", "are","was", "were", "will","is", "in", "at", "of", "a", "to"]


def count_words(text):
    words=text.split()
    return len(words)

def extract_keywords(text):
    words= text.lower().split()
    keywords=[]
    for word in words:
        word=word.strip(".,:-()")
        if len(word)>3 and word not in stopwords:
            keywords.append(word)
    return keywords


with open("resume.txt","r") as file:
    resume_text= file.read()
    
total_words= count_words(resume_text)
keywords= extract_keywords(resume_text)



print("Total number of words in the resume are: ", total_words)
print("Keywords found: ", len(keywords))
print(keywords)