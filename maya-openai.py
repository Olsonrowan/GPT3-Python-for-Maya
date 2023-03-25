import os
import openai
import maya.cmds as cmds

class OpenAi:
    def __init__(self):
        self.window_name = 'GPT Script Generator'
        # Your specific API key, do not share. Keep this private.
        openai.api_key = "YOUR API KEY HERE"
        
        # Load config values
        self.load_config()

    def load_config(self):
        self.engine = "text-davinci-003"
        self.max_tokens = 1024
        self.numbers = 1
        self.stop = None
        self.temp = 0.5

    def return_openai(self):
        prompt = cmds.textField(self.promptField, query=True, text=True)
        completions = openai.Completion.create(
            engine=self.engine,
            prompt="Without any instructions or explanation, please generate Maya Python code that: " + prompt,
            max_tokens=self.max_tokens,
            n=self.numbers,
            stop=self.stop,
            temperature=self.temp
        )
        response = completions.choices[0].text.strip()
        return response

    def run_script(self, *args):
        response = f"{self.return_openai()}"
        exec(response)

    def show_script(self, *args):
        response = self.return_openai()
        self.show_code_ui(response)


    def show_code_ui(self, response):
        cmds.window(title="Python Code Generated", widthHeight=(600, 400))
        cmds.columnLayout(adjustableColumn=True)
        cmds.text(label="Generated Python code:", align="left", font="boldLabelFont")
        cmds.scrollField(wordWrap=True, text=response, width=580, height=350, backgroundColor=(0.2, 0.2, 0.2),
                         editable=False)
        cmds.button(label='Save Script',
                    bgc=(1.0, 0.5, 0.0),
                    command=self.save_script)
        cmds.showWindow()

    def save_script(self, *args):
        response = self.return_openai()
        scripts_path = os.getenv("MAYA_SCRIPT_PATH").split(";")[0]
        if not os.path.exists(scripts_path):
            os.mkdir(scripts_path)
        with open("{}/maya_ai_saved_script.py".format(scripts_path), "w") as f:
            f.write(response)
        os.startfile(scripts_path)

    def main_ui(self):
        window = cmds.window(title=self.window_name, widthHeight=(305, 150), tlb=True)
        cmds.columnLayout(adjustableColumn=True)
        cmds.rowColumnLayout(numberOfColumns=1, columnAttach=(1, 'left', 0), columnWidth=[(15, 100), (2, 250)])
        cmds.text(label="What would you like the script to do?:", align="left", font="boldLabelFont")
        self.promptField = cmds.textField(width=298, ann="What would you like the script to do?:")
        cmds.setParent('..')
        cmds.separator(height=10)
        cmds.columnLayout(adjustableColumn=True)
        cmds.rowColumnLayout(numberOfColumns=1, columnAttach=(2, 'left', 0), columnWidth=[(1, 300)])
        cmds.button(label='Run', bgc=(1.0, 0.5, 0.0), command=self.run_script)
        cmds.setParent('..')
        cmds.columnLayout(adjustableColumn=True)
        cmds.rowColumnLayout(numberOfColumns=1, columnAttach=(2, 'left', 0), columnWidth=[(1, 300)])
        cmds.button(label='Show Script', bgc=(1.0, 0.5, 0.0), command=self.show_script)
        cmds.setParent('..')
        cmds.showWindow()

if __name__ == "__main__":
    OpenAi().main_ui()
