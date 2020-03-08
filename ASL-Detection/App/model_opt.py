def optimizeModel():
    mo_tf_path = '/opt/intel/openvino/deployment_tools/model_optimizer/mo_tf.py'

    pb_file = './model/frozen_model.pb'
    output_dir = './model'
    img_height = 224
    input_shape = [1, img_height, img_height, 3]
    input_shape_str = str(input_shape).replace(' ', '')
    input_shape_str

    exec(open("mo_tf_path --input_model pb_file --output_dir output_dir --input_shape input_shape_str --data_type FP16")
         .read())
