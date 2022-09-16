import json

class AnkiOutput:
    def __init__(self, output_file="None", json_out=list(), max_phrases=5, max_syn=10):
        self.output_file = output_file
        self.json_out = json_out
        self.max_phrases = max_phrases
        self.max_syn = max_syn

    def output(self):

        messages = []

        for text in self.json_out:
            message_output = ""

            json_output = json.loads(text)
            lex_entries = json_output["results"][0]["lexicalEntries"]
            # iterate through lexical entries (verb, noun, adjective, etc)
            for i in range(0, len(lex_entries)):
                lex_entry = lex_entries[i]
                category = lex_entry["lexicalCategory"]["text"]
                message_output += f"{category}.\n"
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
                        message_output += f"    {k}. {definition}\n"
                        # print synonyms
                        try:
                            synonyms = sense["synonyms"]
                            message_output += f"      syn: "
                            # iterate through each synonym
                            for l in range(0, len(synonyms[:self.max_syn])):
                                syn = synonyms[l]["text"]
                                if (l == min(self.max_syn, len(synonyms)) - 1):
                                    message_output += syn + "\n"
                                    break
                                message_output += syn + ", "
                        except:
                            continue

                # print out example phrases
                message_output += "\n    Phrases:\n"
                phrases = lex_entry["phrases"]
                for j in range(0, len(phrases[:self.max_phrases])):
                    phrase = phrases[j]["text"]
                    message_output += f"      \"{phrase}\"" + "\n"

                # prepare for next lexical entry
                message_output += "\n"
        