import os

def load_aiml_kernel(kernel, aiml_path):
    if os.path.isfile("brain/bot_brain.brn"):
        kernel.loadBrain("brain/bot_brain.brn")
    else:
        kernel.learn(aiml_path)
        kernel.saveBrain("brain/bot_brain.brn")