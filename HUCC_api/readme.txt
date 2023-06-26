There are two trained CNN models in the trained model directory. 

(A). 'saved_model' is trained on entire dataset excluding train test splits.
(B). 'saved_model_again' is trained on approx. 30% of the entire dataset.

to switch back and forth between these two trained models, change this line of code:

	model_file_abs_path = os.path.join(main_dir, 'trained_models', model_1_dir, 		'my_model')

In this line, replace the variable 'model_1_dir' to 'model_2_dir' for switching to trained model B from trained model A.