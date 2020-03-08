import tensorflow as tf
from tensorflow_core.python.framework import graph_io
from App.model_opt import optimizeModel

tf.compat.v1.Session()

# Clear any previous session.
tf.keras.backend.clear_session()

export_dir = 'models/frozen'
model_fname = 'models/model.h5'

tf.keras.backend.set_learning_phase(0)

model = tf.keras.models.load_model(model_fname)

with tf.compat.v1.keras.backend.get_session() as sess:
    tf.compat.v1.saved_model.simple_save(sess, export_dir, inputs={"keys": model.input},
                                         outputs={t.name: t for t in model.outputs})

# optimizeModel()
