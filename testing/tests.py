import json

def main():

    text = open("test_json.txt").read()
    json_output = json.loads(text)

    lex_entries = json_output["results"][0]["lexicalEntries"]

    phrase_count = 5
    synonym_count = 10

    # iterate through lexical entries (verb, noun, adjective, etc)
    for i in range(0, len(lex_entries)):
        lex_entry = lex_entries[i]
        category = lex_entry["lexicalCategory"]["text"]
        print(f"{category}.")
        entries = lex_entry["entries"]
        # iterate through each entry
        for j in range(0, len(entries)):
            senses = entries[j]["senses"]
            # iterate through each sense of the word
            # in a given lexical entry
            for k in range(0, len(senses)):
                sense = senses[k]
                # grab and print definition
                definition = sense["definitions"][0]
                print(f"    {k}. {definition}")
                # print synonyms
                try:
                    synonyms = sense["synonyms"]
                    print(f"      syn: ", end="")
                    # iterate through each synonym
                    for l in range(0, len(synonyms[:synonym_count])):
                        syn = synonyms[l]["text"]
                        if (l == min(synonym_count, len(synonyms)) - 1):
                            print(syn)
                            break
                        print(syn, end=", ")
                except:
                    continue

        # print out example phrases
        print("\n    Phrases:")
        phrases = lex_entry["phrases"]
        for j in range(0, len(phrases[:phrase_count])):
            phrase = phrases[j]["text"]
            print(f"      \"{phrase}\"")

        # prepare for next lexical entry
        print("")

if __name__ == "__main__":
    main()