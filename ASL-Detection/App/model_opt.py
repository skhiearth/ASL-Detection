mo_tf_path = '/opt/intel/openvino/deployment_tools/model_optimizer/mo_tf.py'

pb_file = 'models/frozen/saved_model.pb'
output_dir = 'models/optimized'
img_height = 64
input_shape = [1, img_height, img_height, 3]
input_shape_str = str(input_shape).replace(' ', '')

print(input_shape_str)

# Run the following in terminal:
# python3 {mo_tf_path} --input_model {pb_file} --output_dir {output_dir} --input_shape {input_shape_str} --data_type
# FP16
