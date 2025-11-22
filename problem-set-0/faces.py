def convert(text: str) -> str:

    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")

    return text

def main() -> None: 
    text = input("Try out some emoticons!: ")
    converted = convert(text)

    print (converted)

main()