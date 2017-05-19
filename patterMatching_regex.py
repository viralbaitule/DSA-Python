import re

def match(pattern,string):
	match_index={}
	regex_string=''
	for char in pattern:
		if not char in match_index.keys():
			match_index[char]=pattern.index(char)+1
			regex_string=regex_string+"(.+)"
		else:
			regex_string=regex_string+"\\%s"%(match_index[char])
	if re.match(regex_string,string):
		return True



print(match("abbacabb","catdogdogcatmousecatdogdog"))