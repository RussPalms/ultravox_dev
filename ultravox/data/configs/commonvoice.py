from ultravox.data import types

CV_BASE_CONFIG = types.DatasetConfig(
    name="commonvoice",
    path="fixie-ai/common_voice_17_0",
    transcript_template="{{sentence}}",
    assistant_template="{{sentence}}",
)

CV_EN_CONFIG = types.DatasetConfig(
    name="commonvoice-en",
    base="commonvoice",
    subset="en",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=1_101_170),
        types.DatasetSplitConfig(name="validation", num_samples=16_393),
    ],
    transcript_template="{{text_proc.format_asr_text(sentence)}}",
    assistant_template="{{text_proc.format_asr_text(sentence)}}",
)

CV_AR_CONFIG = types.DatasetConfig(
    name="commonvoice-ar",
    base="commonvoice",
    subset="ar",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=28_369),
        types.DatasetSplitConfig(name="validation", num_samples=10_470),
    ],
)

CV_DE_CONFIG = types.DatasetConfig(
    name="commonvoice-de",
    base="commonvoice",
    subset="de",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=589_100),
        types.DatasetSplitConfig(name="validation", num_samples=16_183),
    ],
)

CV_ES_CONFIG = types.DatasetConfig(
    name="commonvoice-es",
    base="commonvoice",
    subset="es",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=336_846),
        types.DatasetSplitConfig(name="validation", num_samples=15_857),
    ],
)

CV_FR_CONFIG = types.DatasetConfig(
    name="commonvoice-fr",
    base="commonvoice",
    subset="fr",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=558_054),
        types.DatasetSplitConfig(name="validation", num_samples=16_159),
    ],
)

CV_IT_CONFIG = types.DatasetConfig(
    name="commonvoice-it",
    base="commonvoice",
    subset="it",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=169_771),
        types.DatasetSplitConfig(name="validation", num_samples=15_149),
    ],
)

CV_JA_CONFIG = types.DatasetConfig(
    name="commonvoice-ja",
    base="commonvoice",
    subset="ja",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=10_039),
        types.DatasetSplitConfig(name="validation", num_samples=6_261),
    ],
)

CV_PT_CONFIG = types.DatasetConfig(
    name="commonvoice-pt",
    base="commonvoice",
    subset="pt",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=21_968),
        types.DatasetSplitConfig(name="validation", num_samples=9_464),
    ],
)

CV_RU_CONFIG = types.DatasetConfig(
    name="commonvoice-ru",
    base="commonvoice",
    subset="ru",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=26_377),
        types.DatasetSplitConfig(name="validation", num_samples=10_203),
    ],
)

CV_HI_CONFIG = types.DatasetConfig(
    name="commonvoice-hi",
    base="commonvoice",
    subset="hi",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=9_378),
        types.DatasetSplitConfig(name="validation", num_samples=4_856),
    ],
)

CV_TR_CONFIG = types.DatasetConfig(
    name="commonvoice-tr",
    base="commonvoice",
    subset="tr",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=35_147),
        types.DatasetSplitConfig(name="validation", num_samples=11_258),
    ],
)

CV_SV_CONFIG = types.DatasetConfig(
    name="commonvoice-sv",
    base="commonvoice",
    subset="sv-SE",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=7_744),
        types.DatasetSplitConfig(name="validation", num_samples=5_210),
    ],
)

CV_UK_CONFIG = types.DatasetConfig(
    name="commonvoice-uk",
    base="commonvoice",
    subset="uk",
    splits=[
        types.DatasetSplitConfig(name="train", num_samples=25_137),
        types.DatasetSplitConfig(name="validation", num_samples=10_007),
    ],
)

CV_EN_TRANS_CONFIG = types.DatasetConfig(
    name="commonvoice-en-transcription",
    base="commonvoice-en",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)
CV_AR_TRANS_CONFIG = types.DatasetConfig(
    name="commonvoice-ar-transcription",
    base="commonvoice-ar",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)
CV_DE_TRANS_CONFIG = types.DatasetConfig(
    name="commonvoice-de-transcription",
    base="commonvoice-de",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)
CV_ES_TRANS_CONFIG = types.DatasetConfig(
    name="commonvoice-es-transcription",
    base="commonvoice-es",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)
CV_FR_TRANS_CONFIG = types.DatasetConfig(
    name="commonvoice-fr-transcription",
    base="commonvoice-fr",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)
CV_IT_TRANS_CONFIG = types.DatasetConfig(
    name="commonvoice-it-transcription",
    base="commonvoice-it",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)
CV_JA_TRANS_CONFIG = types.DatasetConfig(
    name="commonvoice-ja-transcription",
    base="commonvoice-ja",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)
CV_PT_TRANS_CONFIG = types.DatasetConfig(
    name="commonvoice-pt-transcription",
    base="commonvoice-pt",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)
CV_RU_TRANS_CONFIG = types.DatasetConfig(
    name="commonvoice-ru-transcription",
    base="commonvoice-ru",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)

CV_HI_TRANS_CONFIG = types.DatasetConfig(
    name="commonvoice-hi-transcription",
    base="commonvoice-hi",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)

CV_TR_TRANS_CONFIG = types.DatasetConfig(
    name="commonvoice-tr-transcription",
    base="commonvoice-tr",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)

CV_SV_TRANS_CONFIG = types.DatasetConfig(
    name="commonvoice-sv-transcription",
    base="commonvoice-sv",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)

CV_UK_TRANS_CONFIG = types.DatasetConfig(
    name="commonvoice-uk-transcription",
    base="commonvoice-uk",
    user_template=types.TRANSCRIPTION_USER_TEMPLATE,
)

CV_EN_CONT_CONFIG = types.DatasetConfig(
    name="commonvoice-en-continuation",
    base="commonvoice-en",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)
CV_AR_CONT_CONFIG = types.DatasetConfig(
    name="commonvoice-ar-continuation",
    base="commonvoice-ar",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)
CV_DE_CONT_CONFIG = types.DatasetConfig(
    name="commonvoice-de-continuation",
    base="commonvoice-de",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)
CV_ES_CONT_CONFIG = types.DatasetConfig(
    name="commonvoice-es-continuation",
    base="commonvoice-es",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)
CV_FR_CONT_CONFIG = types.DatasetConfig(
    name="commonvoice-fr-continuation",
    base="commonvoice-fr",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)
CV_IT_CONT_CONFIG = types.DatasetConfig(
    name="commonvoice-it-continuation",
    base="commonvoice-it",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)
CV_JA_CONT_CONFIG = types.DatasetConfig(
    name="commonvoice-ja-continuation",
    base="commonvoice-ja",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)
CV_PT_CONT_CONFIG = types.DatasetConfig(
    name="commonvoice-pt-continuation",
    base="commonvoice-pt",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)
CV_RU_CONT_CONFIG = types.DatasetConfig(
    name="commonvoice-ru-continuation",
    base="commonvoice-ru",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)


CV_HI_CONT_CONFIG = types.DatasetConfig(
    name="commonvoice-hi-continuation",
    base="commonvoice-hi",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)

CV_TR_CONT_CONFIG = types.DatasetConfig(
    name="commonvoice-tr-continuation",
    base="commonvoice-tr",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)

CV_SV_CONT_CONFIG = types.DatasetConfig(
    name="commonvoice-sv-continuation",
    base="commonvoice-sv",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)

CV_UK_CONT_CONFIG = types.DatasetConfig(
    name="commonvoice-uk-continuation",
    base="commonvoice-uk",
    user_template=types.CONTINUATION_USER_TEMPLATE,
    assistant_template=types.CONTINUATION_ASSISTANT_TEMPLATE,
)

configs = [
    CV_BASE_CONFIG,
    CV_EN_CONFIG,
    CV_AR_CONFIG,
    CV_DE_CONFIG,
    CV_ES_CONFIG,
    CV_FR_CONFIG,
    CV_IT_CONFIG,
    CV_JA_CONFIG,
    CV_PT_CONFIG,
    CV_RU_CONFIG,
    CV_HI_CONFIG,
    CV_TR_CONFIG,
    CV_SV_CONFIG,
    CV_UK_CONFIG,
    CV_EN_TRANS_CONFIG,
    CV_AR_TRANS_CONFIG,
    CV_DE_TRANS_CONFIG,
    CV_ES_TRANS_CONFIG,
    CV_FR_TRANS_CONFIG,
    CV_IT_TRANS_CONFIG,
    CV_JA_TRANS_CONFIG,
    CV_PT_TRANS_CONFIG,
    CV_RU_TRANS_CONFIG,
    CV_HI_TRANS_CONFIG,
    CV_TR_TRANS_CONFIG,
    CV_SV_TRANS_CONFIG,
    CV_UK_TRANS_CONFIG,
    CV_EN_CONT_CONFIG,
    CV_AR_CONT_CONFIG,
    CV_DE_CONT_CONFIG,
    CV_ES_CONT_CONFIG,
    CV_FR_CONT_CONFIG,
    CV_IT_CONT_CONFIG,
    CV_JA_CONT_CONFIG,
    CV_PT_CONT_CONFIG,
    CV_RU_CONT_CONFIG,
    CV_HI_CONT_CONFIG,
    CV_TR_CONT_CONFIG,
    CV_SV_CONT_CONFIG,
    CV_UK_CONT_CONFIG,
]
