def count_words(text):
    words=text.split()
    return len(words)

with open("resume.txt","r") as file:
    resume_text= file.read()
    
total_words= count_words(resume_text)


print("Total number of words in the resume are: ", total_words)