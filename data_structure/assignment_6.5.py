# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

# Desired Output
# 0.8475

text = "X-DSPAM-Confidence:    0.8475";

findColon = text.find(':');
startPos = text.find('0', findColon);

string = text[ startPos: ];
result = float(string);

print(string);