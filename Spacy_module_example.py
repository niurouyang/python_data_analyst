import spacy

txt = "list is a ubiquitous data structure in the Python programming language."
nlp=spacy.load
nlp=spacy.load('en_core_web_sm')
doc=nlp(txt)
stk=[]
for w in doc:
    if w.pos == 'NOUN' or w.pos == 'PROPN':
        stk.append(w.text)
    elif(w.head.pos == 'NOUN' or w.head.pos=='PROPN') and (w in w.head.lefts):
        stk.append(w.text)
    elif stk:
        chunk=''
        while stk:
            chunk=stk.pop()+' '+chunk
            print(chunk.strip())
