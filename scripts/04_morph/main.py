
from os.path import (
    expanduser,
    join as join_path
)

from IPython.display import HTML
from tqdm.notebook import tqdm as log_progress

from naeval.log import log
from naeval.const import (
    NEWS, WIKI, FICTION, SOCIAL, POETRY,

    DEEPPAVLOV, DEEPPAVLOV_BERT, UDPIPE,
    SPACY, RNNMORPH, MARU, RUPOSTAGGER,
    SLOVNET, SLOVNET_BERT,
    STANZA,

    MB, GB, GPU,

    DATASET, JL, GZ
)
from naeval.io import (
    format_jl,
    parse_jl,

    load_gz_lines,
    dump_gz_lines,
)
from naeval.record import (
    as_jsons,
    from_jsons
)
from naeval.dataset import sample
from naeval.readme import patch_readme
from naeval.docker import docker_client

from naeval.morph.datasets import load_dataset
from naeval.morph.markup import (
    Markup,
    show_markup,
    show_markup_diff
)
from naeval.morph.models import (
    UDPipeModel,
    SpacyModel,
    MaruModel,
    RNNMorphModel,
    DeeppavlovModel,
    DeeppavlovBERTModel,
    RuPosTaggerModel,
    SlovnetBERTModel,
    SlovnetModel,
    StanzaModel
)
from naeval.morph.score import score_markups
from naeval.morph.report import (
    scores_report_table,
    format_scores_report,

    Bench,
    bench_report_table,
    format_bench_report,
)

CORUS_DATA_DIR = expanduser('~/proj/corus-data/gramru')
CORUS_FILES = {
    NEWS: [
        'dev/GramEval2020-RuEval2017-Lenta-news-dev.conllu',
        'train/MorphoRuEval2017-Lenta-train.conllu',
    ],
    WIKI: [
        'dev/GramEval2020-GSD-wiki-dev.conllu',
        'train/GramEval2020-GSD-train.conllu'
    ],
    FICTION: [
        'dev/GramEval2020-SynTagRus-dev.conllu',
        'train/GramEval2020-SynTagRus-train-v2.conllu',
        'train/MorphoRuEval2017-JZ-gold.conllu'
    ],
    SOCIAL: [
        'dev/GramEval2020-RuEval2017-social-dev.conllu',
        'train/GramEval2020-Taiga-social-train.conllu',
        'train/MorphoRuEval2017-VK-gold.conllu'
    ],
    POETRY: [
        'dev/GramEval2020-Taiga-poetry-dev.conllu',
        'train/GramEval2020-Taiga-poetry-train.conllu'
    ],
}

DATASETS = [NEWS, WIKI, FICTION, SOCIAL, POETRY]
MODELS = {
    SLOVNET: SlovnetModel,
    SLOVNET_BERT: SlovnetBERTModel,
    DEEPPAVLOV: DeeppavlovModel,
    DEEPPAVLOV_BERT: DeeppavlovBERTModel,
    UDPIPE: UDPipeModel,
    SPACY: SpacyModel,
    STANZA: StanzaModel,
    RNNMORPH: RNNMorphModel,
    MARU: MaruModel,
    RUPOSTAGGER: RuPosTaggerModel,
}
DATA_DIR = expanduser('~/proj/naeval/data/morph')
MORPH1 = 'morph1'
MORPH2 = 'morph2'
README = expanduser('~/proj/naeval/README.md')
SLOVNET_README = expanduser('~/proj/slovnet/README.md')
