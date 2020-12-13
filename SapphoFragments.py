import gpt_2_simple as gpt2


class SapphoGenerator:
    def __init__(self, GPT2_path):
        self.GPT2_path = GPT2_path
        self.sess = gpt2.start_tf_sess()
        self.gpt2.load_gpt2(sess, run_name=self.GPT2_path)
    def generate_poem(self, fragments):
        total = ""
        for fragment in poem9:
            total += (' ' + fragment)
            new = self.gpt2.generate(self.sess,
                    length=50,
                    temperature=1,
                    prefix=total,
                    nsamples=1,
                    batch_size=1,
                    run_name=self.GPT2_path,
                    return_as_list=True
                )[0].replace(total, '')
        total += ' [' + new + ']'
        return total
    def fine_tune(self, training_data, model_name):
        #model will be saved in /checkpoint/model_name
        self.gpt2.finetune(sess,
                dataset=training_data,
                model_name='124M',
                steps=200,
                restore_from='fresh',
                run_name=model_name,
                print_every=10,
                sample_every=100,
                save_every=100
            )