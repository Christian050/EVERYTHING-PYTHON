# Use a literal to create a string containing a:
# 1, a single quote
# 2, a double quote
# 3, both single and double quote.

"Some 'quoted' text."
'Some "quoted" text.'
'Some "quoted" \'extra\'text'

# Write a string literal that spams multiple lines.
"""This string 
spans several lines
because it's a bit long
"""

# Use the string "join" operation to create a string that contains a colon as a separator.
content = []
content.append('finch')
content.append('sparrow')
content.append('thrush')
content.append('jay')
contentStr = ':'.join(content)
print(contentStr)

# Use string formatting to produce a string containing your last and first names, separated by a comma.
first = "Christian"
last = "Twum-Afosa"
middle = "Kwabena"
full = '%s, %s, %s' % (last, first, middle, )
print(full)