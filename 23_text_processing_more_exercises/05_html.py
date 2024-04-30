article_title = input()
article_content = input()

print(f"<h1>\n"
      f"    {article_title}\n"
      f"</h1>\n"
      f"<article>\n"
      f"    {article_content}\n"
      f"</article>")

while True:

    comment = input()

    if comment == "end of comments":
        break

    else:
        print(f"<div>\n"
              f"    {comment}\n"
              f"</div>")
        
