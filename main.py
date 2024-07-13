from googletrans import Translator
import os


class Translate:
    def __init__(self, input_file: str, max_length: int = 2000, language: str = "en"):
        pass
        self.translator = Translator()
        self.input_file = input_file
        self.whole_file = open(f"{input_file}-en.srt", "w", encoding="utf-8")
        self.max_length = max_length
        self.language = language

    def split_translate(self):
        self.split_text_file()
        for i in self.file_names:
            seg_file = open(i, "r", encoding="utf-8")
            t = self.translator.translate(text=seg_file.read(), dest=self.language).text
            self.whole_file.write(t)
            seg_file.close()
        for i in self.file_names:
            os.remove(i)

    def split_text_file(self):
        with open(self.input_file, "r") as infile:
            content = infile.read()
            infile.close()
        self.file_names = []
        segment_count = 0
        current_segment = ""
        for char in content:
            current_segment += char
            if len(current_segment) > self.max_length:
                output_file = f"{self.input_file.split('.')[0]}_{segment_count}.txt"
                self.file_names.append(output_file)
                with open(output_file, "w") as outfile:
                    outfile.write(current_segment)
                    outfile.close()
                current_segment = ""
                segment_count += 1
        if current_segment:
            output_file = f"{self.input_file.split('.')[0]}_{segment_count}.txt"
            self.file_names.append(output_file)
            with open(output_file, "w") as outfile:
                outfile.write(current_segment)
                outfile.close()

    def main(self):
        self.split_text_file()
        self.split_translate()
        self.whole_file.close()


def Main():
    t = Translate(
        input_file=input("Your str file name (with the str extension) -> "),
        max_length=2000,  # you can change for your preference
        language=input("Your desired language -> "),
    )
    t.main()
    print("Your translated file has been created")


if __name__ == "__main__":
    Main()
