import src.classes.Generation as gen
import os


def output_to_directory(target_dir: str, gen: gen.Generation):
    """Creates output directory from given path, creates output files and stores best networks each to separate file
    :param target_dir  output dir if not exists then will be created
    :param gen         last generation of networks"""

    if not os.path.isdir(target_dir):
        os.mkdir(target_dir)
    best_score = gen.best
    file_index = 0
    for i in range(gen.num_of_nets):
        if gen.scores[i] == best_score:
            with open("{}/output_network_{}".format(target_dir, file_index), "w") as out_net_f:
                print(gen.networks[i].to_aeon_string(-1, set()), file=out_net_f)
            file_index += 1

    return best_score
