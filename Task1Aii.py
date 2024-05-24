
import emoji
text_with_emoji=input("Enter text: ")
text_without_emoji=emoji.demojize(text_with_emoji)
print("Converted text= ",text_without_emoji)