# valentine-treebank
UD trees of Valentine's Day greetings for no good reason

A train/dev/test split can be obtained by running `./sample.py`.

## Sources

| Text file | Link | Lines | Trees |
|-----------|------|-------|-------|
| `ai-weirdness.txt` | https://www.aiweirdness.com/ai-generated-valentines-cards/ | 31 | 34 |
| `hallmark.txt` | https://ideas.hallmark.com/articles/valentines-day-ideas/valentine-messages/ | 244 | 330 |
| `vampire.txt` | https://bloodpackets.tumblr.com/post/675409722361397248 | 3 | 3 |
| Total | | 278 | 367 |

Each `.conllu` file is the result of uploading the corresponding to `.txt` file to https://lindat.mff.cuni.cz/services/udpipe/ and parsing with model `english-ewt-ud-2.6-200830`. Mannually corrected versions are then found in the `-edited.conllu` files.

Mannual correction mainly dealt with dependencies. There are likely at least a few POS-tagging errors and some of the sentence breaks are weird.
