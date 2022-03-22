import scipy
from scipy import spatial
import pandas as pd
import numpy as np
import heapq
from flask import Flask
from flask import request
from flask import Flask, jsonify, abort
app = Flask(__name__)
import json


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


@app.route('/post_options', methods=['POST'])
def create_task():
    if not request.json or not 'dataset' in request.json:
        abort(400)
    # df1 = pd.read_csv("dataset2.csv")
    # answers_count = 2
    #
    # my_array = np.array([[10, 1, 1, 0, 1, 1, 1, 0, 0, 1]])
    # df2 = pd.DataFrame(my_array, columns=['Option', 'Age', 'Gender', 'Symptom1', 'Symptom2', 'Physical1', 'Physical2', 'Laboratory1',
    #                                       'Laboratory2', 'Radiology', 'Question category'])
    # # print(df2)
    # ary = spatial.distance.cdist(df1, df2, metric='euclidean')
    #
    # # sorted_ary = ary.sort()
    # sorted_ary = ary.reshape(1, -1)[0]
    # # print(sorted_ary)
    # n_smallest = heapq.nsmallest(answers_count, sorted_ary)
    # # print(n_smallest[0])
    # options = []
    # for i in n_smallest:
    #     options.append(df1[ary == i].values[0][0])
    #
    # options = np.array(options)
    # new_df = df1[ary == ary.min()]
    # # print(new_df)
    #
    # task = request.json['dataset']
    # tasks.append(task)

    # json_dump = json.dumps({'options': "test option"}, cls=NumpyEncoder)
    json_dump = json.dumps({'response': "dataset posted successfully"})
    return json_dump, 201

@app.route('/get_options', methods=['POST'])
def create_smart_options():
    if not request.json or not 'question' in request.json:
        abort(400)
    json_dump = json.dumps({'options': ["test option1", "test option2", "test option3"]})
    return json_dump, 201

# df1 = pd.read_csv("dataset.csv")
# answers_count = 5
#
# my_array = np.array([[10, 1, 1, 0, 1, 1, 1, 0, 0, 1]])
# df2 = pd.DataFrame(my_array, columns=['Age', 'Gender', 'Symptom1', 'Symptom2', 'Physical1', 'Physical2', 'Laboratory1',
#                                        'Laboratory2', 'Radiology', 'Question category'])
# # print(df2)
# ary = spatial.distance.cdist(df1, df2, metric='euclidean')
#
# # sorted_ary = ary.sort()
# sorted_ary = ary.reshape(1, -1)[0]
# # print(sorted_ary)
#
# n_smallest = heapq.nsmallest(answers_count, sorted_ary)
# print(n_smallest[0])
#
# for i in n_smallest:
#     print(df1[ary == i])
# # print(df1[ary == ary.min()])

if __name__ == '__main__':
    app.run(port=6000,debug=True)