def main():
    strContinue = "yes"
    print("Welcome to the Sentence Formatter Program!")
    
    while strContinue == "yes":
        try:
            strInput = input("Please enter sentences here: ").strip()
            if not strInput:
                raise ValueError("Input cannot be empty.")
            if any(char.isdigit() for char in strInput):
                raise ValueError("Input cannot contain numbers.")
        
            strSentences = strInput.split('.')
            modified_sentences = []

            for sentence in strSentences:
                sentence = sentence.strip()
                if sentence:
                    modified_sentences.append(sentence[0].upper() + sentence[1:])

            strFinal = '. '.join(modified_sentences) + '.'
            
            print("------------------------------------------------------------------")
            print("Formatted sentences:")
            print(strFinal)
            print("------------------------------------------------------------------")
            
        except ValueError:
            print("Unexpected error with input")
            strFinal = None
        except Exception:
            print("An unexpected error occurred.")
            strFinal = None

        strContinue = input("Do you want to enter more sentences? Please enter yes/no: ").strip().lower()
        while strContinue not in ['yes', 'no']:
            print("ERROR - Please enter a valid menu option")
            strContinue = input("Do you want to enter more sentences? Please enter yes/no: ").strip().lower()
            
        if strContinue == "no":
            print("Thank you for using the program. Goodbye!")


main()
