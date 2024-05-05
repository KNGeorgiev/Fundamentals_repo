import re

input_line = input()

title_pattern = r"(<title>)([^<>]*)(<\/title>)"
body_pattern = r"(\<body)(>.+\<)(\/body\>)"
body_final_pattern = r">([^><]*)<"

title = re.search(title_pattern, input_line)
body_prim = re.search(body_pattern, input_line)
body_final = re.findall(body_final_pattern, body_prim.group(2))

body_final = "".join(body_final)
body_final = body_final.replace("\\n", "")

print(f"Title: {title.group(2)}")
print(f"Content: {body_final}")
