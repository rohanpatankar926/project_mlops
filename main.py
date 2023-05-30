from sensor.pipeline import simple_pipeline,batch_pred

def run_pipeline(file_path=None):
    if file_path is None:
        try:
            pipeline=simple_pipeline.pipeline_inititate()
            return "pipeline ran successful"
        except Exception as e:
            raise e
    else:
        try:
            output_file=batch_pred.start_batch_data_predsiction(input_file_path=file_path)
            print(output_file)
            return output_file
        except Exception as e:
            raise e

if __name__=="__main__":
    run_pipeline()