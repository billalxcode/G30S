import G30S

text = "This is text"
g45 = G30S.Garuda1945()
g45.encrypt(text)
g45.show # show (print result)
print (g45.result) # Return result
