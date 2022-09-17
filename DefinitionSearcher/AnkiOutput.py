from email import message
import json

class AnkiOutput:
    def __init__(self, output_file="None", json_out=list(), max_phrases=5, max_syn=10):
        self.output_file = output_file
        self.json_out = json_out
        self.max_phrases = max_phrases
        self.max_syn = max_syn
        
        self.par_style = "\"text-align:left;font-size:12;\""
        self.list_style = "\"text-align:left;font-size:12\""
        self.ul_style = "\"text-align:left;list-style-type:none;font-size:12\""
        self.h_style = "\"text-align:center;font-size:15;\""
        self.category_style = "\"text-align:left;font-size:13;font-weight:bold;\""
        self.syn_style = "\"text-align:center;font-size:12;\""

    def output(self):

        messages = []

        for text in self.json_out:
            message_output = ""

            json_output = json.loads(text)
            lex_entries = json_output["results"][0]["lexicalEntries"]
            word = json_output["id"]
            message_output += f"<h1 style=\"{self.h_style}\">{word}</h1><br>"
            # iterate through lexical entries (verb, noun, adjective, etc)
            message_output += "<hr>"
            for i in range(0, len(lex_entries)):
                lex_entry = lex_entries[i]
                category = lex_entry["lexicalCategory"]["text"]
                message_output += f"<p style=\"{self.category_style}\">({category}).</p>"
                entries = lex_entry["entries"]
                # iterate through each entry
                for j in range(0, len(entries)):
                    senses = entries[j]["senses"]
                    # iterate through each sense of the word
                    # in a given lexical entry
                    message_output += f"<p style=\"{self.par_style}\">Definitions:</p>"
                    message_output += f"<ul style=\"{self.ul_style}\">"
                    for k in range(0, len(senses)):
                        sense = senses[k]
                        # grab and print definition
                        definition = sense["definitions"][0]
                        message_output += f"<li style=\"{self.par_style}\">{k+1}. {definition}</p>"
                        # print synonyms
                        try:
                            synonyms = sense["synonyms"]
                            message_output += f"<p style=\"{self.syn_style}\">syn(s): "
                            # iterate through each synonym
                            for l in range(0, len(synonyms[:self.max_syn])):
                                syn = synonyms[l]["text"]
                                if (l == min(self.max_syn, len(synonyms)) - 1):
                                    message_output += syn + "</p>"
                                    break
                                message_output += syn + ", "
                        except:
                            continue
                    message_output += "</ul>"

                # print out example phrases
                message_output += f"<br><p style=\"{self.par_style}\">\t\tPhrases:</p>"
                phrases = lex_entry["phrases"]
                message_output += f"<ul style=\"{self.ul_style}\">"
                for j in range(0, len(phrases[:self.max_phrases])):
                    phrase = phrases[j]["text"]
                    message_output += f"<li>\"\"{phrase}\"\"" + "</li>"
                message_output += "</ul>"
                message_output += "<hr><br>"

            message_output = f'{word}~"{message_output}"'
            messages.append(message_output)

        with open(self.output_file, "wt", encoding="utf-8") as out:
            for message in messages:
                out.write(message)
                out.write("\n")
        
