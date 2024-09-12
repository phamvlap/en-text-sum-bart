import torch

from bart.constants import SpecialToken, RougeKey
from summarization.utils.mix import join_path


def get_config() -> dict:
    config = {}

    # General configs
    config["seed"] = 42
    config["base_dir"] = "trained"

    # Model configs
    config["model_dir"] = join_path(
        base_dir=config["base_dir"],
        sub_path="models",
    )
    config["model_basename"] = "bart_model_"
    config["model_config_file"] = "model_config_{0}.json"

    # Dataset configs
    config["dataset_dir"] = "data"
    config["train_ds_path"] = join_path(
        base_dir=config["dataset_dir"],
        sub_path="train.csv",
    )
    config["val_ds_path"] = join_path(
        base_dir=config["dataset_dir"],
        sub_path="val.csv",
    )
    config["test_ds_path"] = join_path(
        base_dir=config["dataset_dir"],
        sub_path="test.csv",
    )
    config["text_src"] = "document"
    config["text_tgt"] = "summary"

    # Tokenizer configs
    config["tokenizer_dir"] = join_path(
        base_dir=config["base_dir"],
        sub_path="tokenizer",
    )
    config["tokenizer_bart_dir"] = join_path(
        base_dir=config["base_dir"],
        sub_path="tokenizer-bart",
    )
    config["tokenizer_tmp_dir"] = join_path(
        base_dir=config["base_dir"],
        sub_path="tokenizer-tmp",
    )
    config["special_tokens"] = [
        SpecialToken.BOS,
        SpecialToken.EOS,
        SpecialToken.PAD,
        SpecialToken.MASK,
        SpecialToken.UNK,
    ]
    config["vocab_size"] = 30000
    config["min_freq"] = 2
    config["model_type"] = "bpe"

    # Dataloader configs
    config["batch_size_train"] = 16
    config["batch_size_val"] = 16
    config["batch_size_test"] = 1

    # Adam optimizer configs
    config["lr"] = 0.5
    config["betas"] = (0.9, 0.98)
    config["eps"] = 1e-9  # = 10 ** -9

    # Learning rate scheduler configs
    config["lr_scheduler"] = "noam"

    # NoamLR scheduler configs
    config["warmup_steps"] = 4000

    # Loss function configs
    config["label_smoothing"] = 0.1

    # Training configs
    config["epochs"] = 10
    config["preload"] = "latest"

    # BART configs
    config["max_sequence_length"] = 500
    config["d_model"] = 1024
    config["encoder_layers"] = 6
    config["decoder_layers"] = 6
    config["encoder_attention_heads"] = 8
    config["decoder_attention_heads"] = 8
    config["encoder_ffn_dim"] = 2048
    config["decoder_ffn_dim"] = 2048
    config["activation_function"] = "relu"
    config["dropout"] = 0.1
    config["max_position_embeddings"] = config["max_sequence_length"]
    config["init_std"] = 0.02
    config["scale_embedding"] = True
    config["num_beams"] = 4

    # Rouge Score configs
    config["rouge_keys"] = [
        RougeKey.ROUGE_1,
        RougeKey.ROUGE_2,
        RougeKey.ROUGE_L,
    ]
    config["use_stemmer"] = True
    config["accumulate"] = "best"  # 'best' | 'avg'

    # Beam search configs
    config["beam_size"] = 3

    # Statistics result configs
    config["statistic_dir"] = join_path(
        base_dir=config["base_dir"],
        sub_path="statistic",
    )

    # Device
    config["device"] = "cuda" if torch.cuda.is_available() else "cpu"

    return config
