# AUTOGENERATED! DO NOT EDIT! File to edit: ../app.ipynb.

# %% auto 0
__all__ = ['learn', 'categories', 'image', 'label', 'examples', 'intf', 'is_cat', 'classify_image']

# %% ../app.ipynb 1
from fastai.vision.all import *
import gradio as gr

def is_cat(x): return x[0].isupper()

# %% ../app.ipynb 3
learn = load_learner('model1.pkl')

# %% ../app.ipynb 5
categories = ('Dog','Cat')

def classify_image(img):
    pred,idx,probs = learn.predict(img)
    return dict(zip(categories,map(float,probs)))


# %% ../app.ipynb 7
image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()
examples = ['puppy.jpg','babycat.jpg','gigacat.jpg']

intf = gr.Interface(fn = classify_image,inputs = image,outputs = label,examples= examples)
intf.launch(inline=False)

