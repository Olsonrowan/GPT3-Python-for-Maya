# GPT3-Python-for-Maya

## Overview
Python-based tool for generating Maya scripts using OpenAI's GPT-3 language model. It provides a user-friendly interface to prompt the model and generate Maya Python code, making it easy to automate various tasks in Maya with the power of AI.

## Maya AI Script Generator
The Maya AI Script Generator is a tool that utilizes the power of OpenAI's GPT-3 language model to generate Maya Python code.

## Prerequisites
Before you begin, ensure that you have met the following requirements:

- You have installed Maya on your machine.
- You have created an OpenAI account and have an API key ready.

## Installation
To install, follow these steps:

1. Clone this repository to your local machine.
2. Install the OpenAI Python package by running `pip install openai`.
3. Open the `maya-openai.py` file and add your OpenAI API key in the `openai.api_key` variable.
4. Open Maya and navigate to the Script Editor.
5. Open the `maya-openai.py` file from the repository and copy its contents to the Script Editor.
6. Press the Run button in the Script Editor to run the tool.

## Usage
To use the Maya AI Script Generator, follow these steps:

1. Launch the tool by running the `maya-openai.py` file in the Script Editor.
2. Type in a prompt in the text field describing what you want the generated script to do.
3. Press the "Show Script" button to generate the script and view it in a separate window.
4. Press the "Save Script" button to save the generated script to your Maya scripts folder.

## Configuration
You can configure the following parameters in the `load_config` function:

- `self.engine`: the OpenAI engine to use for generating the script. Default is "text-davinci-003".
- `self.max_tokens`: the maximum number of tokens to use for generating the script. Default is 1024, max is 4097.
- `self.numbers`: the number of responses to generate. Default is 1.
- `self.stop`: a string or list of strings to use as the stop sequence when generating the script. Default is None.
- `self.temp`: the sampling temperature to use for generating the script. Default is 0.5.
