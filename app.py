from transformers import T5TokenizerFast as T5Tokenizer
import tensorflow as tf
from flask import Flask, render_template, url_for, request
import pickle


from keras.models import load_model
from transformers import BertTokenizer,TFBertModel
berttokenizer = BertTokenizer.from_pretrained('bert-base-cased')
import numpy as np

# tokenizer = T5Tokenizer.from_pretrained('t5-base')

# # load the summarization model
# filename = 'summarization_model.pkl'
# model = pickle.load(open(filename, 'rb'))

# # load the Headline Model model
# filename2 = 'headline_model.pkl'
# headline_model = pickle.load(open(filename2, 'rb'))

# # load the Classification model
# filename3 = 'f_classification_model.h5'
# classif_model = tf.keras.models.load_model(filename3,custom_objects={'TFBertModel':TFBertModel})

# app = Flask(__name__)


# @app.route('/')
# def Home():
#     return render_template('index.html')

# @app.route('/home.html')
# def HomeA():
#     return render_template('home.html')

# @app.route('/index.html')
# def HomeB():
#     return render_template('index.html')

# @app.route('/blog.html')
# def HomeC():
#     return render_template('blog.html')

# @app.route('/blog-details.html')
# def HomeD():
#     return render_template('blog-details.html')

# # Summarization function
# @app.route('/')
# def summarytext(text):
#     text_encoding = tokenizer(
#         text,
#         max_length=512,
#         padding='max_length',
#         truncation=True,
#         return_attention_mask=True,
#         add_special_tokens=True,
#         return_tensors='pt'
#     )
#     generated_ids = model.generate(
#         input_ids=text_encoding['input_ids'],
#         attention_mask=text_encoding['attention_mask'],
#         max_length=128,
#         num_beams=2,
#         repetition_penalty=2.5,
#         length_penalty=1.0,
#         early_stopping=True
#     )
#     preds = [
#         tokenizer.decode(gen_id, skip_special_tokens=True,
#                          clean_up_tokenization_spaces=True)
#         for gen_id in generated_ids
#     ]

#     return "".join(preds)

# # classification function
# @app.route('/')
# def prep_data(text):
#     tokens = berttokenizer.encode_plus(text, max_length=512,
#                                    truncation=True, padding='max_length',
#                                    add_special_tokens=True, return_token_type_id=False,
#                                    return_tensors='tf')
#     return{
#         'input_ids': tf.cast(tokens['input_ids'], tf.float64),
#         'attention_mask': tf.cast(tokens['attention_mask'], tf.float64)
#     }

# # headline function


# @app.route('/')
# def headlineText(text):
#     text_encoding = tokenizer(
#         text,
#         max_length=512,
#         padding='max_length',
#         truncation=True,
#         return_attention_mask=True,
#         add_special_tokens=True,
#         return_tensors='pt'
#     )
#     generated_ids = headline_model.generate(
#         input_ids=text_encoding['input_ids'],
#         attention_mask=text_encoding['attention_mask'],
#         max_length=15,
#         num_beams=2,
#         repetition_penalty=2.5,
#         length_penalty=1.0,
#         early_stopping=True
#     )
#     preds = [
#         tokenizer.decode(gen_id, skip_special_tokens=True,
#                          clean_up_tokenization_spaces=True)
#         for gen_id in generated_ids
#     ]
#     return "".join(preds)

# # Input from user
# @app.route('/predict', methods=['POST', 'GET'])
# def predict():
#     if request.method == 'POST':
#         global message
#         message = request.form.get("message", False)
#     text = [message]
#     output = summarytext(str(text))
#     headline = headlineText(str(text))
#     test = prep_data(str(text))
#     probs = classif_model.predict(test)
#     cat_no = np.argmax(probs[0])
#     cat_list = ['SPORTS','BUSINESS','TRAVEL','TECHNOLOGY','STYLE & BEAUTY','FOOD & DRINK','POLITICS','ENTERTAINMENT','PARENTING','WELLNESS']
#     classi_output = cat_list[cat_no]
#     return render_template('result.html', summ_prediction=output,head_prediction=headline,classification=classi_output)


# if __name__ == '__main__':
#     app.run()
#     #app.run(debug=True)


#Simple flask app

# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
# from flask import Flask,request, jsonify



# # Flask constructor takes the name of
# # current module (__name__) as argument.
# app = Flask(__name__)

# # The route() function of the Flask class is a decorator,
# # which tells the application which URL should call
# # the associated function.
# @app.route('/')
# # ???/??? URL is bound with hello_world() function.
# def hello_world():
# 	return 'Hello World'

# # main driver function
# if __name__ == '__main__':

# 	# run() method of Flask class runs the application
# 	# on the local development server.
# 	#app.run()
#     #app.run(debug=True, port=42691)
#     app.run(threaded=True, port=5000)














# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
    
 
